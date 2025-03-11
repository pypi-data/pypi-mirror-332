import json
import os
from types import SimpleNamespace
from unittest.mock import patch

import ckan.tests.factories as factories
import pytest
from ckan import model
from ckan.common import config
from ckan.plugins import toolkit

from ckanext.feedback.command import feedback
from ckanext.feedback.plugin import FeedbackPlugin
from ckanext.feedback.services.common.config import (
    CONFIG_HANDLER_PATH,
    FeedbackConfig,
    download_handler,
    get_organization,
)

engine = model.repo.session.get_bind()


@pytest.mark.usefixtures('clean_db', 'with_plugins', 'with_request_context')
class TestCheck:
    @classmethod
    def setup_class(cls):
        model.repo.init_db()

    def test_check_administrator(self):
        enable_org = factories.Organization(
            is_organization=True,
            name='enable_org',
            type='organization',
            title='enable_org',
        )

        result = get_organization(enable_org['id'])
        assert result.name == enable_org['name']

    @patch('ckanext.feedback.services.common.config.import_string')
    def test_seted_download_handler(self, mock_import_string):
        toolkit.config['ckan.feedback.download_handler'] = CONFIG_HANDLER_PATH
        download_handler()
        mock_import_string.assert_called_once_with(CONFIG_HANDLER_PATH, silent=True)

    def test_not_seted_download_handler(self):
        toolkit.config.pop('ckan.feedback.download_handler', '')
        assert download_handler() is None

    @patch('ckanext.feedback.services.common.config.DownloadsConfig.load_config')
    @patch('ckanext.feedback.services.common.config.ResourceCommentConfig.load_config')
    @patch('ckanext.feedback.services.common.config.UtilizationConfig.load_config')
    @patch('ckanext.feedback.services.common.config.ReCaptchaConfig.load_config')
    @patch('ckanext.feedback.services.common.config.NoticeEmailConfig.load_config')
    def test_load_feedback_config_with_feedback_config_file(
        self,
        mock_DownloadsConfig_load_config,
        mock_ResourceCommentConfig_load_config,
        mock_UtilizationConfig_load_config,
        mock_ReCaptchaConfig_load_config,
        mock_NoticeEmailConfig_load_config,
    ):
        # without feedback_config_file and .ini file
        try:
            os.remove('/srv/app/feedback_config.json')
        except FileNotFoundError:
            pass

        FeedbackConfig().load_feedback_config()
        assert FeedbackConfig().is_feedback_config_file is False

        # without .ini file
        feedback_config = {'modules': {}}
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()
        assert FeedbackConfig().is_feedback_config_file is True
        mock_DownloadsConfig_load_config.assert_called_once()
        mock_ResourceCommentConfig_load_config.assert_called_once()
        mock_UtilizationConfig_load_config.assert_called_once()
        mock_ReCaptchaConfig_load_config.assert_called_once()
        mock_NoticeEmailConfig_load_config.assert_called_once()
        os.remove('/srv/app/feedback_config.json')

    @patch('ckanext.feedback.plugin.toolkit')
    def test_update_config_attribute_error(self, mock_toolkit):
        feedback_config = {'modules': {}}
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()
        mock_toolkit.error_shout.call_count == 4
        os.remove('/srv/app/feedback_config.json')

    @patch('ckanext.feedback.services.common.config.toolkit')
    def test_update_config_json_decode_error(self, mock_toolkit):
        with open('/srv/app/feedback_config.json', 'w') as f:
            f.write('{"modules":')

        FeedbackConfig().load_feedback_config()
        mock_toolkit.error_shout.assert_called_once_with(
            'The feedback config file not decoded correctly'
        )
        os.remove('/srv/app/feedback_config.json')

    def test_get_commands(self):
        result = FeedbackPlugin.get_commands(self)
        assert result == [feedback.feedback]

    @patch('ckanext.feedback.services.common.config.get_organization')
    def test_download_is_enable(self, mock_get_organization):
        org_name1 = 'enable_org'
        org_name2 = 'disable_org'
        org_name3 = 'nonexistent_org'

        # without feedback_config_file and .ini file
        config.pop('ckan.feedback.downloads.enable', None)
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') == 'None'
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().download.is_enable() is True
        assert FeedbackConfig().download.is_enable(org_name1) is True
        assert FeedbackConfig().download.is_enable(org_name2) is True
        assert FeedbackConfig().download.is_enable(org_name3) is True

        # without feedback_config_file, .ini file enable is True
        config['ckan.feedback.downloads.enable'] = True
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') is True
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().download.is_enable() is True
        assert FeedbackConfig().download.is_enable(org_name1) is True
        assert FeedbackConfig().download.is_enable(org_name2) is True
        assert FeedbackConfig().download.is_enable(org_name3) is True

        # without feedback_config_file, .ini file enable is False
        config['ckan.feedback.downloads.enable'] = False
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') is False
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().download.is_enable() is False
        assert FeedbackConfig().download.is_enable(org_name1) is False
        assert FeedbackConfig().download.is_enable(org_name2) is False
        assert FeedbackConfig().download.is_enable(org_name3) is False

        # with feedback_config_file enable is False and org_name1 is in enable_orgs
        config.pop('ckan.feedback.downloads.enable', None)
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        feedback_config = {
            'modules': {
                'downloads': {
                    'enable': False,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') is False
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == [org_name1]
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().download.is_enable() is False
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().download.is_enable(org_name1) is False
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().download.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().download.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is False and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.downloads.enable', None)
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        feedback_config = {
            'modules': {
                'downloads': {
                    'enable': False,
                    'enable_orgs': [],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') is False
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == []
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().download.is_enable() is False
        assert FeedbackConfig().download.is_enable(org_name1) is False
        assert FeedbackConfig().download.is_enable(org_name2) is False
        assert FeedbackConfig().download.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.downloads.enable', None)
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        feedback_config = {
            'modules': {
                'downloads': {
                    'enable': True,
                    'enable_orgs': [],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') is True
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == []
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().download.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().download.is_enable(org_name1) is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().download.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().download.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name1 is in enable_orgs
        config['ckan.feedback.downloads.enable'] = False
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        feedback_config = {
            'modules': {
                'downloads': {
                    'enable': True,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') is True
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == [org_name1]
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().download.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().download.is_enable(org_name1) is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().download.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().download.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # If enable in feedback_config_file is True
        # and org_name1 is in enable_orgs and disable_orgs
        config.pop('ckan.feedback.downloads.enable', None)
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        feedback_config = {
            'modules': {
                'downloads': {
                    'enable': True,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name1, org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') is True
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == [org_name1]
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == [
            org_name1,
            org_name2,
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().download.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().download.is_enable(org_name1) is False
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().download.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().download.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # When the "enable" in ckan.ini is a string
        # Execute only in the download module
        # as it does not vary across other modules or functionalities.
        config['ckan.feedback.downloads.enable'] = "enable"
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') == "enable"
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().download.is_enable() is False
        assert FeedbackConfig().download.is_enable(org_name1) is False
        assert FeedbackConfig().download.is_enable(org_name2) is False
        assert FeedbackConfig().download.is_enable(org_name3) is False

        # When the "enable" in the feedback_config_file is a string
        # Execute only in the download module
        # as it does not vary across other modules or functionalities.
        config.pop('ckan.feedback.downloads.enable', None)
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        feedback_config = {
            'modules': {
                'downloads': {
                    'enable': "enable",
                    'enable_orgs': [org_name1, org_name2],
                    'disable_orgs': [org_name3],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') == "enable"
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == [
            org_name1,
            org_name2,
        ]
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == [org_name3]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().download.is_enable() is False
        assert FeedbackConfig().download.is_enable(org_name1) is False
        assert FeedbackConfig().download.is_enable(org_name2) is False
        assert FeedbackConfig().download.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # When the "enable_orgs" in feedback_config_file is not a list
        # Execute only in the download module
        # as it does not vary across other modules or functionalities.
        config.pop('ckan.feedback.downloads.enable', None)
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        feedback_config = {
            'modules': {
                'downloads': {
                    'enable': True,
                    'enable_orgs': org_name1,
                    'disable_orgs': [],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') is True
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == org_name1
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == []
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().download.is_enable() is False
        assert FeedbackConfig().download.is_enable(org_name1) is False
        assert FeedbackConfig().download.is_enable(org_name2) is False
        assert FeedbackConfig().download.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # When the contents of the "disable_orgs" list
        # in feedback_config_file are not strings
        # Execute only in the download module
        # as it does not vary across other modules or functionalities.
        config.pop('ckan.feedback.downloads.enable', None)
        config.pop('ckan.feedback.downloads.enable_orgs', None)
        config.pop('ckan.feedback.downloads.disable_orgs', None)

        feedback_config = {
            'modules': {
                'downloads': {
                    'enable': True,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [{"name": org_name3}],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.downloads.enable', 'None') is True
        assert config.get('ckan.feedback.downloads.enable_orgs', 'None') == [org_name1]
        assert config.get('ckan.feedback.downloads.disable_orgs', 'None') == [
            {"name": org_name3}
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().download.is_enable() is False
        assert FeedbackConfig().download.is_enable(org_name1) is False
        assert FeedbackConfig().download.is_enable(org_name2) is False
        assert FeedbackConfig().download.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

    @patch('ckanext.feedback.services.common.config.get_organization')
    def test_utilization_is_enable(self, mock_get_organization):
        org_name1 = 'enable_org'
        org_name2 = 'disable_org'
        org_name3 = 'nonexistent_org'

        # without feedback_config_file and .ini file
        config.pop('ckan.feedback.utilizations.enable', None)
        config.pop('ckan.feedback.utilizations.enable_orgs', None)
        config.pop('ckan.feedback.utilizations.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.utilizations.enable', 'None') == 'None'
        assert config.get('ckan.feedback.utilizations.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.utilizations.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().utilization.is_enable() is True
        assert FeedbackConfig().utilization.is_enable(org_name1) is True
        assert FeedbackConfig().utilization.is_enable(org_name2) is True
        assert FeedbackConfig().utilization.is_enable(org_name3) is True

        # without feedback_config_file, .ini file enable is True
        config['ckan.feedback.utilizations.enable'] = True
        config.pop('ckan.feedback.utilizations.enable_orgs', None)
        config.pop('ckan.feedback.utilizations.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.utilizations.enable', 'None') is True
        assert config.get('ckan.feedback.utilizations.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.utilizations.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().utilization.is_enable() is True
        assert FeedbackConfig().utilization.is_enable(org_name1) is True
        assert FeedbackConfig().utilization.is_enable(org_name2) is True
        assert FeedbackConfig().utilization.is_enable(org_name3) is True

        # without feedback_config_file, .ini file enable is False
        config['ckan.feedback.utilizations.enable'] = False
        config.pop('ckan.feedback.utilizations.enable_orgs', None)
        config.pop('ckan.feedback.utilizations.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.utilizations.enable', 'None') is False
        assert config.get('ckan.feedback.utilizations.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.utilizations.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().utilization.is_enable() is False
        assert FeedbackConfig().utilization.is_enable(org_name1) is False
        assert FeedbackConfig().utilization.is_enable(org_name2) is False
        assert FeedbackConfig().utilization.is_enable(org_name3) is False

        # with feedback_config_file enable is False and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.utilizations.enable', None)
        config.pop('ckan.feedback.utilizations.enable_orgs', None)
        config.pop('ckan.feedback.utilizations.disable_orgs', None)

        feedback_config = {
            'modules': {
                'utilizations': {
                    'enable': False,
                    'enable_orgs': [],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.utilizations.enable', 'None') is False
        assert config.get('ckan.feedback.utilizations.enable_orgs', 'None') == []
        assert config.get('ckan.feedback.utilizations.disable_orgs', 'None') == [
            org_name2
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().utilization.is_enable() is False
        assert FeedbackConfig().utilization.is_enable(org_name1) is False
        assert FeedbackConfig().utilization.is_enable(org_name2) is False
        assert FeedbackConfig().utilization.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is False and org_name1 is in enable_orgs
        config.pop('ckan.feedback.utilizations.enable', None)
        config.pop('ckan.feedback.utilizations.enable_orgs', None)
        config.pop('ckan.feedback.utilizations.disable_orgs', None)

        feedback_config = {
            'modules': {
                'utilizations': {
                    'enable': False,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.utilizations.enable', 'None') is False
        assert config.get('ckan.feedback.utilizations.enable_orgs', 'None') == [
            org_name1
        ]
        assert config.get('ckan.feedback.utilizations.disable_orgs', 'None') == [
            org_name2
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().utilization.is_enable() is False
        assert FeedbackConfig().utilization.is_enable(org_name1) is False
        assert FeedbackConfig().utilization.is_enable(org_name2) is False
        assert FeedbackConfig().utilization.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.utilizations.enable', None)
        config.pop('ckan.feedback.utilizations.enable_orgs', None)
        config.pop('ckan.feedback.utilizations.disable_orgs', None)

        feedback_config = {
            'modules': {
                'utilizations': {
                    'enable': True,
                    'enable_orgs': [],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.utilizations.enable', 'None') is True
        assert config.get('ckan.feedback.utilizations.enable_orgs', 'None') == []
        assert config.get('ckan.feedback.utilizations.disable_orgs', 'None') == [
            org_name2
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().utilization.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().utilization.is_enable(org_name1) is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().utilization.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().utilization.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name1 is in enable_orgs
        config['ckan.feedback.utilizations.enable'] = False
        config.pop('ckan.feedback.utilizations.enable_orgs', None)
        config.pop('ckan.feedback.utilizations.disable_orgs', None)

        feedback_config = {
            'modules': {
                'utilizations': {
                    'enable': True,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.utilizations.enable', 'None') is True
        assert config.get('ckan.feedback.utilizations.enable_orgs', 'None') == [
            org_name1
        ]
        assert config.get('ckan.feedback.utilizations.disable_orgs', 'None') == [
            org_name2
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().utilization.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().utilization.is_enable(org_name1) is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().utilization.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().utilization.is_enable(org_name3) is False

        os.remove('/srv/app/feedback_config.json')

        # If enable in feedback_config_file is True
        # and org_name1 is in enable_orgs and disable_orgs
        config.pop('ckan.feedback.utilizations.enable', None)
        config.pop('ckan.feedback.utilizations.enable_orgs', None)
        config.pop('ckan.feedback.utilizations.disable_orgs', None)

        feedback_config = {
            'modules': {
                'utilizations': {
                    'enable': True,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name1, org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.utilizations.enable', 'None') is True
        assert config.get('ckan.feedback.utilizations.enable_orgs', 'None') == [
            org_name1
        ]
        assert config.get('ckan.feedback.utilizations.disable_orgs', 'None') == [
            org_name1,
            org_name2,
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().utilization.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().utilization.is_enable(org_name1) is False
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().utilization.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().utilization.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

    @patch('ckanext.feedback.services.common.config.get_organization')
    def test_resource_comment_is_enable(self, mock_get_organization):
        org_name1 = 'enable_org'
        org_name2 = 'disable_org'
        org_name3 = 'nonexistent_org'

        # without feedback_config_file and .ini file
        config.pop('ckan.feedback.resources.enable', None)
        config.pop('ckan.feedback.resources.enable_orgs', None)
        config.pop('ckan.feedback.resources.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.resources.enable', 'None') == 'None'
        assert config.get('ckan.feedback.resources.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.resources.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().resource_comment.is_enable() is True
        assert FeedbackConfig().resource_comment.is_enable(org_name1) is True
        assert FeedbackConfig().resource_comment.is_enable(org_name2) is True
        assert FeedbackConfig().resource_comment.is_enable(org_name3) is True

        # without feedback_config_file, .ini file enable is True
        config['ckan.feedback.resources.enable'] = True
        config.pop('ckan.feedback.resources.enable_orgs', None)
        config.pop('ckan.feedback.resources.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.resources.enable', 'None') is True
        assert config.get('ckan.feedback.resources.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.resources.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().resource_comment.is_enable() is True
        assert FeedbackConfig().resource_comment.is_enable(org_name1) is True
        assert FeedbackConfig().resource_comment.is_enable(org_name2) is True
        assert FeedbackConfig().resource_comment.is_enable(org_name3) is True

        # without feedback_config_file, .ini file enable is False
        config['ckan.feedback.resources.enable'] = False
        config.pop('ckan.feedback.resources.enable_orgs', None)
        config.pop('ckan.feedback.resources.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.resources.enable', 'None') is False
        assert config.get('ckan.feedback.resources.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.resources.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().resource_comment.is_enable() is False
        assert FeedbackConfig().resource_comment.is_enable(org_name1) is False
        assert FeedbackConfig().resource_comment.is_enable(org_name2) is False
        assert FeedbackConfig().resource_comment.is_enable(org_name3) is False

        # with feedback_config_file enable is False and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.resources.enable', None)
        config.pop('ckan.feedback.resources.enable_orgs', None)
        config.pop('ckan.feedback.resources.disable_orgs', None)

        feedback_config = {
            'modules': {
                'resources': {
                    'enable': False,
                    'enable_orgs': [],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.resources.enable', 'None') is False
        assert config.get('ckan.feedback.resources.enable_orgs', 'None') == []
        assert config.get('ckan.feedback.resources.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.is_enable() is False
        assert FeedbackConfig().resource_comment.is_enable(org_name1) is False
        assert FeedbackConfig().resource_comment.is_enable(org_name2) is False
        assert FeedbackConfig().resource_comment.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is False and org_name1 is in enable_orgs
        config.pop('ckan.feedback.resources.enable', None)
        config.pop('ckan.feedback.resources.enable_orgs', None)
        config.pop('ckan.feedback.resources.disable_orgs', None)

        feedback_config = {
            'modules': {
                'resources': {
                    'enable': False,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.resources.enable', 'None') is False
        assert config.get('ckan.feedback.resources.enable_orgs', 'None') == [org_name1]
        assert config.get('ckan.feedback.resources.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.is_enable() is False
        assert FeedbackConfig().resource_comment.is_enable(org_name1) is False
        assert FeedbackConfig().resource_comment.is_enable(org_name2) is False
        assert FeedbackConfig().resource_comment.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.resources.enable', None)
        config.pop('ckan.feedback.resources.enable_orgs', None)
        config.pop('ckan.feedback.resources.disable_orgs', None)

        feedback_config = {
            'modules': {
                'resources': {
                    'enable': True,
                    'enable_orgs': [],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.resources.enable', 'None') is True
        assert config.get('ckan.feedback.resources.enable_orgs', 'None') == []
        assert config.get('ckan.feedback.resources.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().resource_comment.is_enable(org_name1) is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().resource_comment.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().resource_comment.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org
        config.pop('ckan.feedback.resources.enable', None)
        config.pop('ckan.feedback.resources.enable_orgs', None)
        config.pop('ckan.feedback.resources.disable_orgs', None)

        feedback_config = {
            'modules': {
                'resources': {
                    'enable': True,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.resources.enable', 'None') is True
        assert config.get('ckan.feedback.resources.enable_orgs', 'None') == [org_name1]
        assert config.get('ckan.feedback.resources.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().resource_comment.is_enable(org_name1) is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().resource_comment.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().resource_comment.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # If enable in feedback_config_file is True
        # and org_name1 is in enable_orgs and disable_orgs
        config.pop('ckan.feedback.resources.enable', None)
        config.pop('ckan.feedback.resources.enable_orgs', None)
        config.pop('ckan.feedback.resources.disable_orgs', None)

        feedback_config = {
            'modules': {
                'resources': {
                    'enable': True,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name1, org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.resources.enable', 'None') is True
        assert config.get('ckan.feedback.resources.enable_orgs', 'None') == [org_name1]
        assert config.get('ckan.feedback.resources.disable_orgs', 'None') == [
            org_name1,
            org_name2,
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().resource_comment.is_enable(org_name1) is False
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().resource_comment.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().resource_comment.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

    @patch('ckanext.feedback.services.common.config.get_organization')
    def test_like_is_enable(self, mock_get_organization):
        org_name1 = 'enable_org'
        org_name2 = 'disable_org'
        org_name3 = 'nonexistent_org'

        # without feedback_config_file and .ini file
        config.pop('ckan.feedback.likes.enable', None)
        config.pop('ckan.feedback.likes.enable_orgs', None)
        config.pop('ckan.feedback.likes.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.likes.enable', 'None') == 'None'
        assert config.get('ckan.feedback.likes.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.likes.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().like.is_enable() is True
        assert FeedbackConfig().like.is_enable(org_name1) is True
        assert FeedbackConfig().like.is_enable(org_name2) is True
        assert FeedbackConfig().like.is_enable(org_name3) is True

        # without feedback_config_file, .ini file enable is True
        config['ckan.feedback.likes.enable'] = True
        config.pop('ckan.feedback.likes.enable_orgs', None)
        config.pop('ckan.feedback.likes.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.likes.enable', 'None') is True
        assert config.get('ckan.feedback.likes.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.likes.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().like.is_enable() is True
        assert FeedbackConfig().like.is_enable(org_name1) is True
        assert FeedbackConfig().like.is_enable(org_name2) is True
        assert FeedbackConfig().like.is_enable(org_name3) is True

        # without feedback_config_file, .ini file enable is False
        config['ckan.feedback.likes.enable'] = False
        config.pop('ckan.feedback.likes.enable_orgs', None)
        config.pop('ckan.feedback.likes.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.likes.enable', 'None') is False
        assert config.get('ckan.feedback.likes.enable_orgs', 'None') == 'None'
        assert config.get('ckan.feedback.likes.disable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().like.is_enable() is False
        assert FeedbackConfig().like.is_enable(org_name1) is False
        assert FeedbackConfig().like.is_enable(org_name2) is False
        assert FeedbackConfig().like.is_enable(org_name3) is False

        # with feedback_config_file enable is False and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.likes.enable', None)
        config.pop('ckan.feedback.likes.enable_orgs', None)
        config.pop('ckan.feedback.likes.disable_orgs', None)

        feedback_config = {
            'modules': {
                'likes': {
                    'enable': False,
                    'enable_orgs': [],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        mock_get_organization.return_value = None
        assert config.get('ckan.feedback.likes.enable', 'None') is False
        assert config.get('ckan.feedback.likes.enable_orgs', 'None') == []
        assert config.get('ckan.feedback.likes.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().like.is_enable() is False
        assert FeedbackConfig().like.is_enable(org_name1) is False
        assert FeedbackConfig().like.is_enable(org_name2) is False
        assert FeedbackConfig().like.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is False and org_name1 is in enable_orgs
        config.pop('ckan.feedback.likes.enable', None)
        config.pop('ckan.feedback.likes.enable_orgs', None)
        config.pop('ckan.feedback.likes.disable_orgs', None)

        feedback_config = {
            'modules': {
                'likes': {
                    'enable': False,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.likes.enable', 'None') is False
        assert config.get('ckan.feedback.likes.enable_orgs', 'None') == [org_name1]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().like.is_enable() is False
        assert FeedbackConfig().like.is_enable(org_name1) is False
        assert FeedbackConfig().like.is_enable(org_name2) is False
        assert FeedbackConfig().like.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name is not in enable_orgs
        config.pop('ckan.feedback.likes.enable', None)
        config.pop('ckan.feedback.likes.enable_orgs', None)
        config.pop('ckan.feedback.likes.disable_orgs', None)

        feedback_config = {
            'modules': {
                'likes': {
                    'enable': True,
                    'enable_orgs': [],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.likes.enable', 'None') is True
        assert config.get('ckan.feedback.likes.enable_orgs', 'None') == []
        assert config.get('ckan.feedback.likes.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().like.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().like.is_enable(org_name1) is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().like.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().like.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name is in enable_orgs
        config.pop('ckan.feedback.likes.enable', None)
        config.pop('ckan.feedback.likes.enable_orgs', None)
        config.pop('ckan.feedback.likes.disable_orgs', None)

        feedback_config = {
            'modules': {
                'likes': {
                    'enable': True,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.likes.enable', 'None') is True
        assert config.get('ckan.feedback.likes.enable_orgs', 'None') == [org_name1]
        assert config.get('ckan.feedback.likes.disable_orgs', 'None') == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().like.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().like.is_enable(org_name1) is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().like.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().like.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # If enable in feedback_config_file is True
        # and org_name1 is in enable_orgs and disable_orgs
        config.pop('ckan.feedback.likes.enable', None)
        config.pop('ckan.feedback.likes.enable_orgs', None)
        config.pop('ckan.feedback.likes.disable_orgs', None)

        feedback_config = {
            'modules': {
                'likes': {
                    'enable': True,
                    'enable_orgs': [org_name1],
                    'disable_orgs': [org_name1, org_name2],
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.likes.enable', 'None') is True
        assert config.get('ckan.feedback.likes.enable_orgs', 'None') == [org_name1]
        assert config.get('ckan.feedback.likes.disable_orgs', 'None') == [
            org_name1,
            org_name2,
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().like.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().like.is_enable(org_name1) is False
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().like.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().like.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

    @patch('ckanext.feedback.services.common.config.get_organization')
    def test_repeat_post_on_resource_is_enable(self, mock_get_organization):
        org_name1 = 'enable_org'
        org_name2 = 'disable_org'
        org_name3 = 'nonexistent_org'

        # without feedback_config_file and .ini file
        config.pop('ckan.feedback.resources.comment.repeated_post_limit.enable', None)
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', None
        )
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', None
        )

        FeedbackConfig().load_feedback_config()

        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable', 'None'
            )
            == 'None'
        )
        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs',
                'None',
            )
            == 'None'
        )
        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs',
                'None',
            )
            == 'None'
        )
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().resource_comment.repeat_post_limit.is_enable() is False
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name1)
            is False
        )
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name2)
            is False
        )
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name3)
            is False
        )

        # without feedback_config_file, .ini file enable is True
        config['ckan.feedback.resources.comment.repeated_post_limit.enable'] = True
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', None
        )
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', None
        )

        FeedbackConfig().load_feedback_config()

        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable', 'None'
            )
            is True
        )
        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs',
                'None',
            )
            == 'None'
        )
        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs',
                'None',
            )
            == 'None'
        )
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().resource_comment.repeat_post_limit.is_enable() is True
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name1)
            is True
        )
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name2)
            is True
        )
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name3)
            is True
        )

        # without feedback_config_file, .ini file enable is False
        config['ckan.feedback.resources.comment.repeated_post_limit.enable'] = False
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', None
        )
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', None
        )

        FeedbackConfig().load_feedback_config()

        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable', 'None'
            )
            is False
        )
        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs',
                'None',
            )
            == 'None'
        )
        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs',
                'None',
            )
            == 'None'
        )
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().resource_comment.repeat_post_limit.is_enable() is False
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name1)
            is False
        )
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name2)
            is False
        )
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name3)
            is False
        )

        # with feedback_config_file enable is False and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.resources.comment.repeated_post_limit.enable', None)
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', None
        )
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', None
        )

        feedback_config = {
            'modules': {
                'resources': {
                    'comments': {
                        'repeat_post_limit': {
                            'enable': False,
                            'enable_orgs': [],
                            'disable_orgs': [org_name2],
                        }
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable', 'None'
            )
            is False
        )
        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs',
                'None',
            )
            == []
        )
        assert config.get(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', 'None'
        ) == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.repeat_post_limit.is_enable() is False
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name1)
            is False
        )
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name2)
            is False
        )
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name3)
            is False
        )
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is False and org_name1 is in enable_orgs
        config.pop('ckan.feedback.resources.comment.repeated_post_limit.enable', None)
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', None
        )
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', None
        )

        feedback_config = {
            'modules': {
                'resources': {
                    'comments': {
                        'repeat_post_limit': {
                            'enable': False,
                            'enable_orgs': [org_name1],
                            'disable_orgs': [org_name2],
                        }
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable', 'None'
            )
            is False
        )
        assert config.get(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', 'None'
        ) == [org_name1]
        assert config.get(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', 'None'
        ) == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.repeat_post_limit.is_enable() is False
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name1)
            is False
        )
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name2)
            is False
        )
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name3)
            is False
        )
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.resources.comment.repeated_post_limit.enable', None)
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', None
        )
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', None
        )

        feedback_config = {
            'modules': {
                'resources': {
                    'comments': {
                        'repeat_post_limit': {
                            'enable': True,
                            'enable_orgs': [],
                            'disable_orgs': [org_name2],
                        }
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable', 'None'
            )
            is True
        )
        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs',
                'None',
            )
            == []
        )
        assert config.get(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', 'None'
        ) == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.repeat_post_limit.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name1)
            is True
        )
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name2)
            is False
        )
        mock_get_organization.return_value = None
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name3)
            is False
        )
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name1 is in enable_orgs
        config['ckan.feedback.resources.comment.repeated_post_limit.enable'] = False
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', None
        )
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', None
        )

        feedback_config = {
            'modules': {
                'resources': {
                    'comments': {
                        'repeat_post_limit': {
                            'enable': True,
                            'enable_orgs': [org_name1],
                            'disable_orgs': [org_name2],
                        }
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable', 'None'
            )
            is True
        )
        assert config.get(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', 'None'
        ) == [org_name1]
        assert config.get(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', 'None'
        ) == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.repeat_post_limit.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name1)
            is True
        )
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name2)
            is False
        )
        mock_get_organization.return_value = None
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name3)
            is False
        )
        os.remove('/srv/app/feedback_config.json')

        # If enable in feedback_config_file is True
        # and org_name1 is in enable_orgs and disable_orgs
        config.pop('ckan.feedback.resources.comment.repeated_post_limit.enable', None)
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', None
        )
        config.pop(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', None
        )

        feedback_config = {
            'modules': {
                'resources': {
                    'comments': {
                        'repeat_post_limit': {
                            'enable': True,
                            'enable_orgs': [org_name1],
                            'disable_orgs': [org_name1, org_name2],
                        }
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get(
                'ckan.feedback.resources.comment.repeated_post_limit.enable', 'None'
            )
            is True
        )
        assert config.get(
            'ckan.feedback.resources.comment.repeated_post_limit.enable_orgs', 'None'
        ) == [org_name1]
        assert config.get(
            'ckan.feedback.resources.comment.repeated_post_limit.disable_orgs', 'None'
        ) == [org_name1, org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.repeat_post_limit.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name1)
            is False
        )
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name2)
            is False
        )
        mock_get_organization.return_value = None
        assert (
            FeedbackConfig().resource_comment.repeat_post_limit.is_enable(org_name3)
            is False
        )
        os.remove('/srv/app/feedback_config.json')

    @patch('ckanext.feedback.services.common.config.get_organization')
    def test_rating_is_enable(self, mock_get_organization):
        org_name1 = 'enable_org'
        org_name2 = 'disable_org'
        org_name3 = 'nonexistent_org'

        # without feedback_config_file and .ini file
        config.pop('ckan.feedback.resources.comment.rating.enable', None)
        config.pop('ckan.feedback.resources.comment.rating.enable_orgs', None)
        config.pop('ckan.feedback.resources.comment.rating.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get('ckan.feedback.resources.comment.rating.enable', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.resources.comment.rating.enable_orgs', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.resources.comment.rating.disable_orgs', 'None')
            == 'None'
        )
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().resource_comment.rating.is_enable() is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name1) is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name2) is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name3) is False

        # without feedback_config_file, .ini file enable is True
        config['ckan.feedback.resources.comment.rating.enable'] = True
        config.pop('ckan.feedback.resources.comment.rating.enable_orgs', None)
        config.pop('ckan.feedback.resources.comment.rating.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get('ckan.feedback.resources.comment.rating.enable', 'None') is True
        )
        assert (
            config.get('ckan.feedback.resources.comment.rating.enable_orgs', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.resources.comment.rating.disable_orgs', 'None')
            == 'None'
        )
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().resource_comment.rating.is_enable() is True
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name1) is True
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name2) is True
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name3) is True

        # without feedback_config_file, .ini file enable is False
        config['ckan.feedback.resources.comment.rating.enable'] = False
        config.pop('ckan.feedback.resources.comment.rating.enable_orgs', None)
        config.pop('ckan.feedback.resources.comment.rating.disable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get('ckan.feedback.resources.comment.rating.enable', 'None') is False
        )
        assert (
            config.get('ckan.feedback.resources.comment.rating.enable_orgs', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.resources.comment.rating.disable_orgs', 'None')
            == 'None'
        )
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().resource_comment.rating.is_enable() is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name1) is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name2) is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name3) is False

        # with feedback_config_file enable is False and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.resources.comment.rating.enable', None)
        config.pop('ckan.feedback.resources.comment.rating.enable_orgs', None)
        config.pop('ckan.feedback.resources.comment.rating.disable_orgs', None)

        feedback_config = {
            'modules': {
                'resources': {
                    'comments': {
                        'rating': {
                            'enable': False,
                            'enable_orgs': [],
                            'disable_orgs': [org_name2],
                        }
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        mock_get_organization.return_value = None
        assert (
            config.get('ckan.feedback.resources.comment.rating.enable', 'None') is False
        )
        assert (
            config.get('ckan.feedback.resources.comment.rating.enable_orgs', 'None')
            == []
        )
        assert config.get(
            'ckan.feedback.resources.comment.rating.disable_orgs', 'None'
        ) == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.rating.is_enable() is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name1) is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name2) is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is False and org_name1 is in enable_orgs
        config.pop('ckan.feedback.resources.comment.rating.enable', None)
        config.pop('ckan.feedback.resources.comment.rating.enable_orgs', None)
        config.pop('ckan.feedback.resources.comment.rating.disable_orgs', None)

        feedback_config = {
            'modules': {
                'resources': {
                    'comments': {
                        'rating': {
                            'enable': False,
                            'enable_orgs': [org_name1],
                            'disable_orgs': [org_name2],
                        }
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get('ckan.feedback.resources.comment.rating.enable', 'None') is False
        )
        assert config.get(
            'ckan.feedback.resources.comment.rating.enable_orgs', 'None'
        ) == [org_name1]
        assert config.get(
            'ckan.feedback.resources.comment.rating.disable_orgs', 'None'
        ) == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.rating.is_enable() is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name1) is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name2) is False
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name1 is not in enable_orgs
        config.pop('ckan.feedback.resources.comment.rating.enable', None)
        config.pop('ckan.feedback.resources.comment.rating.enable_orgs', None)
        config.pop('ckan.feedback.resources.comment.rating.disable_orgs', None)

        feedback_config = {
            'modules': {
                'resources': {
                    'comments': {
                        'rating': {
                            'enable': True,
                            'enable_orgs': [],
                            'disable_orgs': [org_name2],
                        }
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get('ckan.feedback.resources.comment.rating.enable', 'None') is True
        )
        assert (
            config.get('ckan.feedback.resources.comment.rating.enable_orgs', 'None')
            == []
        )
        assert config.get(
            'ckan.feedback.resources.comment.rating.disable_orgs', 'None'
        ) == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.rating.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name1) is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name1 is in enable_orgs
        config['ckan.feedback.resources.comment.rating.enable'] = False
        config.pop('ckan.feedback.resources.comment.rating.enable_orgs', None)
        config.pop('ckan.feedback.resources.comment.rating.disable_orgs', None)

        feedback_config = {
            'modules': {
                'resources': {
                    'comments': {
                        'rating': {
                            'enable': True,
                            'enable_orgs': [org_name1],
                            'disable_orgs': [org_name2],
                        }
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get('ckan.feedback.resources.comment.rating.enable', 'None') is True
        )
        assert config.get(
            'ckan.feedback.resources.comment.rating.enable_orgs', 'None'
        ) == [org_name1]
        assert config.get(
            'ckan.feedback.resources.comment.rating.disable_orgs', 'None'
        ) == [org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.rating.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name1) is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

        # If enable in feedback_config_file is True
        # and org_name1 is in enable_orgs and disable_orgs
        config.pop('ckan.feedback.resources.comment.rating.enable', None)
        config.pop('ckan.feedback.resources.comment.rating.enable_orgs', None)
        config.pop('ckan.feedback.resources.comment.rating.disable_orgs', None)

        feedback_config = {
            'modules': {
                'resources': {
                    'comments': {
                        'rating': {
                            'enable': True,
                            'enable_orgs': [org_name1],
                            'disable_orgs': [org_name1, org_name2],
                        }
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert (
            config.get('ckan.feedback.resources.comment.rating.enable', 'None') is True
        )
        assert config.get(
            'ckan.feedback.resources.comment.rating.enable_orgs', 'None'
        ) == [org_name1]
        assert config.get(
            'ckan.feedback.resources.comment.rating.disable_orgs', 'None'
        ) == [org_name1, org_name2]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().resource_comment.rating.is_enable() is True
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name1})
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name1) is False
        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name2})
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name2) is False
        mock_get_organization.return_value = None
        assert FeedbackConfig().resource_comment.rating.is_enable(org_name3) is False
        os.remove('/srv/app/feedback_config.json')

    def test_recaptcha_config(self):
        # without feedback_config_file and .ini file
        config.pop('ckan.feedback.recaptcha.enable', None)
        config.pop('ckan.feedback.recaptcha.publickey', None)
        config.pop('ckan.feedback.recaptcha.privatekey', None)
        config.pop('ckan.feedback.recaptcha.score_threshold', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.recaptcha.enable', 'None') == 'None'
        assert config.get('ckan.feedback.recaptcha.publickey', 'None') == 'None'
        assert config.get('ckan.feedback.recaptcha.privatekey', 'None') == 'None'
        assert config.get('ckan.feedback.recaptcha.score_threshold', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert (
            FeedbackConfig().recaptcha.is_enable() is FeedbackConfig().recaptcha.default
        )
        assert (
            FeedbackConfig().recaptcha.publickey.get()
            is FeedbackConfig().recaptcha.publickey.default
        )
        assert (
            FeedbackConfig().recaptcha.privatekey.get()
            is FeedbackConfig().recaptcha.privatekey.default
        )
        assert (
            FeedbackConfig().recaptcha.score_threshold.get()
            is FeedbackConfig().recaptcha.score_threshold.default
        )

        # without feedback_config_file, .ini file enable is True
        config['ckan.feedback.recaptcha.enable'] = True
        config.pop('ckan.feedback.recaptcha.publickey', None)
        config.pop('ckan.feedback.recaptcha.privatekey', None)
        config.pop('ckan.feedback.recaptcha.score_threshold', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.recaptcha.enable', 'None') is True
        assert config.get('ckan.feedback.recaptcha.publickey', 'None') == 'None'
        assert config.get('ckan.feedback.recaptcha.privatekey', 'None') == 'None'
        assert config.get('ckan.feedback.recaptcha.score_threshold', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().recaptcha.is_enable() is True
        assert (
            FeedbackConfig().recaptcha.publickey.get()
            is FeedbackConfig().recaptcha.publickey.default
        )
        assert (
            FeedbackConfig().recaptcha.privatekey.get()
            is FeedbackConfig().recaptcha.privatekey.default
        )
        assert (
            FeedbackConfig().recaptcha.score_threshold.get()
            is FeedbackConfig().recaptcha.score_threshold.default
        )

        # without feedback_config_file, .ini file enable is False
        config['ckan.feedback.recaptcha.enable'] = False
        config.pop('ckan.feedback.recaptcha.publickey', None)
        config.pop('ckan.feedback.recaptcha.privatekey', None)
        config.pop('ckan.feedback.recaptcha.score_threshold', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.recaptcha.enable', 'None') is False
        assert config.get('ckan.feedback.recaptcha.publickey', 'None') == 'None'
        assert config.get('ckan.feedback.recaptcha.privatekey', 'None') == 'None'
        assert config.get('ckan.feedback.recaptcha.score_threshold', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().recaptcha.is_enable() is False
        assert (
            FeedbackConfig().recaptcha.publickey.get()
            is FeedbackConfig().recaptcha.publickey.default
        )
        assert (
            FeedbackConfig().recaptcha.privatekey.get()
            is FeedbackConfig().recaptcha.privatekey.default
        )
        assert (
            FeedbackConfig().recaptcha.score_threshold.get()
            is FeedbackConfig().recaptcha.score_threshold.default
        )

        # with feedback_config_file enable is False
        config['ckan.feedback.recaptcha.enable'] = True
        config.pop('ckan.feedback.recaptcha.publickey', None)
        config.pop('ckan.feedback.recaptcha.privatekey', None)
        config.pop('ckan.feedback.recaptcha.score_threshold', None)

        feedback_config = {
            'modules': {
                "recaptcha": {
                    "enable": False,
                },
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.recaptcha.enable', 'None') is False
        assert config.get('ckan.feedback.recaptcha.publickey', 'None') == 'None'
        assert config.get('ckan.feedback.recaptcha.privatekey', 'None') == 'None'
        assert config.get('ckan.feedback.recaptcha.score_threshold', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().recaptcha.is_enable() is False
        assert (
            FeedbackConfig().recaptcha.publickey.get()
            is FeedbackConfig().recaptcha.publickey.default
        )
        assert (
            FeedbackConfig().recaptcha.privatekey.get()
            is FeedbackConfig().recaptcha.privatekey.default
        )
        assert (
            FeedbackConfig().recaptcha.score_threshold.get()
            is FeedbackConfig().recaptcha.score_threshold.default
        )
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True
        config['ckan.feedback.notice.email.enable'] = False
        config.pop('ckan.feedback.notice.email.template_directory', None)
        config.pop('ckan.feedback.notice.email.template_utilization', None)
        config.pop('ckan.feedback.notice.email.template_utilization_comment', None)
        config.pop('ckan.feedback.notice.email.template_resource_comment', None)
        config.pop('ckan.feedback.notice.email.subject_utilization', None)
        config.pop('ckan.feedback.notice.email.subject_utilization_comment', None)
        config.pop('ckan.feedback.notice.email.subject_resource_comment', None)

        feedback_config = {
            'modules': {
                "recaptcha": {
                    "enable": True,
                    "publickey": "xxxxxxxxx",
                    "privatekey": "yyyyyyyy",
                    "score_threshold": 0.3,
                },
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.recaptcha.enable', 'None') is True
        assert config.get('ckan.feedback.recaptcha.publickey', 'None') == "xxxxxxxxx"
        assert config.get('ckan.feedback.recaptcha.privatekey', 'None') == "yyyyyyyy"
        assert config.get('ckan.feedback.recaptcha.score_threshold', 'None') == 0.3
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().recaptcha.is_enable() is True
        assert FeedbackConfig().recaptcha.publickey.get() == "xxxxxxxxx"
        assert FeedbackConfig().recaptcha.privatekey.get() == "yyyyyyyy"
        assert FeedbackConfig().recaptcha.score_threshold.get() == 0.3
        os.remove('/srv/app/feedback_config.json')

    def test_notice_email_config(self):
        # without feedback_config_file and .ini file
        config.pop('ckan.feedback.notice.email.enable', None)
        config.pop('ckan.feedback.notice.email.template_directory', None)
        config.pop('ckan.feedback.notice.email.template_utilization', None)
        config.pop('ckan.feedback.notice.email.template_utilization_comment', None)
        config.pop('ckan.feedback.notice.email.template_resource_comment', None)
        config.pop('ckan.feedback.notice.email.subject_utilization', None)
        config.pop('ckan.feedback.notice.email.subject_utilization_comment', None)
        config.pop('ckan.feedback.notice.email.subject_resource_comment', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.notice.email.enable', 'None') == 'None'
        assert (
            config.get('ckan.feedback.notice.email.template_directory', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.notice.email.template_utilization', 'None')
            == 'None'
        )
        assert (
            config.get(
                'ckan.feedback.notice.email.template_utilization_comment', 'None'
            )
            == 'None'
        )
        assert (
            config.get('ckan.feedback.notice.email.template_resource_comment', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_utilization', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_utilization_comment', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_resource_comment', 'None')
            == 'None'
        )
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().notice_email.is_enable() is False
        assert (
            FeedbackConfig().notice_email.template_directory.get()
            == FeedbackConfig().notice_email.template_directory.default
        )
        assert (
            FeedbackConfig().notice_email.template_utilization.get()
            == FeedbackConfig().notice_email.template_utilization.default
        )
        assert (
            FeedbackConfig().notice_email.template_utilization_comment.get()
            == FeedbackConfig().notice_email.template_utilization_comment.default
        )
        assert (
            FeedbackConfig().notice_email.template_resource_comment.get()
            == FeedbackConfig().notice_email.template_resource_comment.default
        )
        assert (
            FeedbackConfig().notice_email.subject_utilization.get()
            == FeedbackConfig().notice_email.subject_utilization.default
        )
        assert (
            FeedbackConfig().notice_email.subject_utilization_comment.get()
            == FeedbackConfig().notice_email.subject_utilization_comment.default
        )
        assert (
            FeedbackConfig().notice_email.subject_resource_comment.get()
            == FeedbackConfig().notice_email.subject_resource_comment.default
        )

        # without feedback_config_file, .ini file enable is True
        config['ckan.feedback.notice.email.enable'] = True
        config['ckan.feedback.notice.email.template_directory'] = (
            'test_template_directory'
        )
        config['ckan.feedback.notice.email.template_utilization'] = (
            'test_template_utilization'
        )
        config['ckan.feedback.notice.email.template_utilization_comment'] = (
            'test_template_utilization_comment'
        )
        config['ckan.feedback.notice.email.template_resource_comment'] = (
            'test_template_resource_comment'
        )
        config['ckan.feedback.notice.email.subject_utilization'] = (
            'test_subject_utilization'
        )
        config['ckan.feedback.notice.email.subject_utilization_comment'] = (
            'test_subject_utilization_comment'
        )
        config['ckan.feedback.notice.email.subject_resource_comment'] = (
            'test_subject_resource_comment'
        )

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.notice.email.enable', 'None') is True
        assert (
            config.get('ckan.feedback.notice.email.template_directory', 'None')
            == 'test_template_directory'
        )
        assert (
            config.get('ckan.feedback.notice.email.template_utilization', 'None')
            == 'test_template_utilization'
        )
        assert (
            config.get(
                'ckan.feedback.notice.email.template_utilization_comment', 'None'
            )
            == 'test_template_utilization_comment'
        )
        assert (
            config.get('ckan.feedback.notice.email.template_resource_comment', 'None')
            == 'test_template_resource_comment'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_utilization', 'None')
            == 'test_subject_utilization'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_utilization_comment', 'None')
            == 'test_subject_utilization_comment'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_resource_comment', 'None')
            == 'test_subject_resource_comment'
        )
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().notice_email.is_enable() is True
        assert (
            FeedbackConfig().notice_email.template_directory.get()
            == 'test_template_directory'
        )
        assert (
            FeedbackConfig().notice_email.template_utilization.get()
            == 'test_template_utilization'
        )
        assert (
            FeedbackConfig().notice_email.template_utilization_comment.get()
            == 'test_template_utilization_comment'
        )
        assert (
            FeedbackConfig().notice_email.template_resource_comment.get()
            == 'test_template_resource_comment'
        )
        assert (
            FeedbackConfig().notice_email.subject_utilization.get()
            == 'test_subject_utilization'
        )
        assert (
            FeedbackConfig().notice_email.subject_utilization_comment.get()
            == 'test_subject_utilization_comment'
        )
        assert (
            FeedbackConfig().notice_email.subject_resource_comment.get()
            == 'test_subject_resource_comment'
        )

        # without feedback_config_file, .ini file enable is False
        config['ckan.feedback.notice.email.enable'] = False
        config.pop('ckan.feedback.notice.email.template_directory', None)
        config.pop('ckan.feedback.notice.email.template_utilization', None)
        config.pop('ckan.feedback.notice.email.template_utilization_comment', None)
        config.pop('ckan.feedback.notice.email.template_resource_comment', None)
        config.pop('ckan.feedback.notice.email.subject_utilization', None)
        config.pop('ckan.feedback.notice.email.subject_utilization_comment', None)
        config.pop('ckan.feedback.notice.email.subject_resource_comment', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.notice.email.enable', 'None') is False
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().notice_email.is_enable() is False

        # with feedback_config_file enable is False
        config['ckan.feedback.notice.email.enable'] = True
        config.pop('ckan.feedback.notice.email.template_directory', None)
        config.pop('ckan.feedback.notice.email.template_utilization', None)
        config.pop('ckan.feedback.notice.email.template_utilization_comment', None)
        config.pop('ckan.feedback.notice.email.template_resource_comment', None)
        config.pop('ckan.feedback.notice.email.subject_utilization', None)
        config.pop('ckan.feedback.notice.email.subject_utilization_comment', None)
        config.pop('ckan.feedback.notice.email.subject_resource_comment', None)

        feedback_config = {
            'modules': {
                'notice': {
                    'email': {
                        'enable': False,
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.notice.email.enable', 'None') is False
        assert (
            config.get('ckan.feedback.notice.email.template_directory', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.notice.email.template_utilization', 'None')
            == 'None'
        )
        assert (
            config.get(
                'ckan.feedback.notice.email.template_utilization_comment', 'None'
            )
            == 'None'
        )
        assert (
            config.get('ckan.feedback.notice.email.template_resource_comment', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_utilization', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_utilization_comment', 'None')
            == 'None'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_resource_comment', 'None')
            == 'None'
        )
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().notice_email.is_enable() is False
        assert (
            FeedbackConfig().notice_email.template_directory.get()
            == FeedbackConfig().notice_email.template_directory.default
        )
        assert (
            FeedbackConfig().notice_email.template_utilization.get()
            == FeedbackConfig().notice_email.template_utilization.default
        )
        assert (
            FeedbackConfig().notice_email.template_utilization_comment.get()
            == FeedbackConfig().notice_email.template_utilization_comment.default
        )
        assert (
            FeedbackConfig().notice_email.template_resource_comment.get()
            == FeedbackConfig().notice_email.template_resource_comment.default
        )
        assert (
            FeedbackConfig().notice_email.subject_utilization.get()
            == FeedbackConfig().notice_email.subject_utilization.default
        )
        assert (
            FeedbackConfig().notice_email.subject_utilization_comment.get()
            == FeedbackConfig().notice_email.subject_utilization_comment.default
        )
        assert (
            FeedbackConfig().notice_email.subject_resource_comment.get()
            == FeedbackConfig().notice_email.subject_resource_comment.default
        )
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True
        config['ckan.feedback.notice.email.enable'] = False
        config.pop('ckan.feedback.notice.email.template_directory', None)
        config.pop('ckan.feedback.notice.email.template_utilization', None)
        config.pop('ckan.feedback.notice.email.template_utilization_comment', None)
        config.pop('ckan.feedback.notice.email.template_resource_comment', None)
        config.pop('ckan.feedback.notice.email.subject_utilization', None)
        config.pop('ckan.feedback.notice.email.subject_utilization_comment', None)
        config.pop('ckan.feedback.notice.email.subject_resource_comment', None)

        feedback_config = {
            'modules': {
                'notice': {
                    'email': {
                        'enable': True,
                        'template_directory': 'test_template_directory',
                        'template_utilization': 'test_template_utilization',
                        'template_utilization_comment': (
                            'test_template_utilization_comment'
                        ),
                        'template_resource_comment': 'test_template_resource_comment',
                        'subject_utilization': 'test_subject_utilization',
                        'subject_utilization_comment': (
                            'test_subject_utilization_comment'
                        ),
                        'subject_resource_comment': 'test_subject_resource_comment',
                    }
                }
            }
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.notice.email.enable', 'None') is True
        assert (
            config.get('ckan.feedback.notice.email.template_directory', 'None')
            == 'test_template_directory'
        )
        assert (
            config.get('ckan.feedback.notice.email.template_utilization', 'None')
            == 'test_template_utilization'
        )
        assert (
            config.get(
                'ckan.feedback.notice.email.template_utilization_comment', 'None'
            )
            == 'test_template_utilization_comment'
        )
        assert (
            config.get('ckan.feedback.notice.email.template_resource_comment', 'None')
            == 'test_template_resource_comment'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_utilization', 'None')
            == 'test_subject_utilization'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_utilization_comment', 'None')
            == 'test_subject_utilization_comment'
        )
        assert (
            config.get('ckan.feedback.notice.email.subject_resource_comment', 'None')
            == 'test_subject_resource_comment'
        )
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().notice_email.is_enable() is True
        assert (
            FeedbackConfig().notice_email.template_directory.get()
            == 'test_template_directory'
        )
        assert (
            FeedbackConfig().notice_email.template_utilization.get()
            == 'test_template_utilization'
        )
        assert (
            FeedbackConfig().notice_email.template_utilization_comment.get()
            == 'test_template_utilization_comment'
        )
        assert (
            FeedbackConfig().notice_email.template_resource_comment.get()
            == 'test_template_resource_comment'
        )
        assert (
            FeedbackConfig().notice_email.subject_utilization.get()
            == 'test_subject_utilization'
        )
        assert (
            FeedbackConfig().notice_email.subject_utilization_comment.get()
            == 'test_subject_utilization_comment'
        )
        assert (
            FeedbackConfig().notice_email.subject_resource_comment.get()
            == 'test_subject_resource_comment'
        )
        os.remove('/srv/app/feedback_config.json')

    @patch('ckanext.feedback.services.common.config.get_organization')
    def test_moral_keeper_ai_is_enable(self, mock_get_organization):
        org_name = 'example_org_name'

        # without feedback_config_file and .ini file
        config.pop('ckan.feedback.moral_keeper_ai.enable', None)
        config.pop('ckan.feedback.moral_keeper_ai.enable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.moral_keeper_ai.enable', 'None') == 'None'
        assert config.get('ckan.feedback.moral_keeper_ai.enable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().moral_keeper_ai.is_enable() is False
        assert FeedbackConfig().moral_keeper_ai.is_enable(org_name) is False

        # without feedback_config_file, .ini file enable is True
        config['ckan.feedback.moral_keeper_ai.enable'] = True
        config.pop('ckan.feedback.moral_keeper_ai.enable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.moral_keeper_ai.enable', 'None') is True
        assert config.get('ckan.feedback.moral_keeper_ai.enable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().moral_keeper_ai.is_enable() is True
        assert FeedbackConfig().moral_keeper_ai.is_enable(org_name) is True

        # without feedback_config_file, .ini file enable is False
        config['ckan.feedback.moral_keeper_ai.enable'] = False
        config.pop('ckan.feedback.moral_keeper_ai.enable_orgs', None)

        FeedbackConfig().load_feedback_config()

        assert config.get('ckan.feedback.moral_keeper_ai.enable', 'None') is False
        assert config.get('ckan.feedback.moral_keeper_ai.enable_orgs', 'None') == 'None'
        assert FeedbackConfig().is_feedback_config_file is False
        assert FeedbackConfig().moral_keeper_ai.is_enable() is False
        assert FeedbackConfig().moral_keeper_ai.is_enable(org_name) is False

        # with feedback_config_file enable is False and org_name is not in enable_orgs
        config.pop('ckan.feedback.moral_keeper_ai.enable', None)
        config.pop('ckan.feedback.moral_keeper_ai.enable_orgs', None)

        feedback_config = {
            'modules': {'moral_keeper_ai': {'enable': False, 'enable_orgs': []}}
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        mock_get_organization.return_value = None
        assert config.get('ckan.feedback.moral_keeper_ai.enable', 'None') is False
        assert config.get('ckan.feedback.moral_keeper_ai.enable_orgs', 'None') == []
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().moral_keeper_ai.is_enable() is False
        assert FeedbackConfig().moral_keeper_ai.is_enable(org_name) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is False and org_name is in enable_orgs
        config.pop('ckan.feedback.moral_keeper_ai.enable', None)
        config.pop('ckan.feedback.moral_keeper_ai.enable_orgs', None)

        feedback_config = {
            'modules': {'moral_keeper_ai': {'enable': False, 'enable_orgs': [org_name]}}
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name})
        assert config.get('ckan.feedback.moral_keeper_ai.enable', 'None') is False
        assert config.get('ckan.feedback.moral_keeper_ai.enable_orgs', 'None') == [
            org_name
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().moral_keeper_ai.is_enable() is False
        assert FeedbackConfig().moral_keeper_ai.is_enable(org_name) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name is not in enable_orgs
        config.pop('ckan.feedback.moral_keeper_ai.enable', None)
        config.pop('ckan.feedback.moral_keeper_ai.enable_orgs', None)

        feedback_config = {
            'modules': {'moral_keeper_ai': {'enable': True, 'enable_orgs': []}}
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        mock_get_organization.return_value = None
        assert config.get('ckan.feedback.moral_keeper_ai.enable', 'None') is True
        assert config.get('ckan.feedback.moral_keeper_ai.enable_orgs', 'None') == []
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().moral_keeper_ai.is_enable() is True
        assert FeedbackConfig().moral_keeper_ai.is_enable(org_name) is False
        os.remove('/srv/app/feedback_config.json')

        # with feedback_config_file enable is True and org_name is in enable_orgs
        config['ckan.feedback.moral_keeper_ai.enable'] = False
        config.pop('ckan.feedback.moral_keeper_ai.enable_orgs', None)

        feedback_config = {
            'modules': {'moral_keeper_ai': {'enable': True, 'enable_orgs': [org_name]}}
        }
        with open('/srv/app/feedback_config.json', 'w') as f:
            json.dump(feedback_config, f, indent=2)

        FeedbackConfig().load_feedback_config()

        mock_get_organization.return_value = SimpleNamespace(**{'name': org_name})
        assert config.get('ckan.feedback.moral_keeper_ai.enable', 'None') is True
        assert config.get('ckan.feedback.moral_keeper_ai.enable_orgs', 'None') == [
            org_name
        ]
        assert FeedbackConfig().is_feedback_config_file is True
        assert FeedbackConfig().moral_keeper_ai.is_enable() is True
        assert FeedbackConfig().moral_keeper_ai.is_enable(org_name) is True
        os.remove('/srv/app/feedback_config.json')

    @patch('ckanext.feedback.services.common.config.config.get')
    def test_get_enable_orgs(self, mock_config_get):
        mock_config_get.side_effect = [True, ['org1', 'org2']]

        result = FeedbackConfig().download.get_enable_orgs()

        assert result == ['org1', 'org2']

    @patch('ckanext.feedback.services.common.config.config.get')
    def test_get_enable_orgs_false(self, mock_config_get):
        mock_config_get.return_value = False

        result = FeedbackConfig().download.get_enable_orgs()

        assert result is False
