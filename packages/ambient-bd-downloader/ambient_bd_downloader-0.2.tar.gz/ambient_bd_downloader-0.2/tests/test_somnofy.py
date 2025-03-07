import pytest
from unittest.mock import patch, MagicMock, mock_open
from ambient_bd_downloader.sf_api.somnofy import Somnofy
from os.path import join


class Properties:
    def __init__(self, client_id, client_id_file, zone_name):
        self.client_id = client_id
        self.client_id_file = client_id_file
        self.zone_name = zone_name


class TestSomnofy:
    @patch('ambient_bd_downloader.sf_api.somnofy.Somnofy.set_auth', return_value=MagicMock())
    @patch('ambient_bd_downloader.sf_api.somnofy.Somnofy.get_zone_id', return_value=1)
    def test_init(self, mock_get_zone_id, mock_set_auth):
        properties = Properties(client_id='test_client_id',
                                client_id_file='/path/to/client_id_file',
                                zone_name='test_zone')
        somnofy = Somnofy(properties)

        assert somnofy.client_id == 'test_client_id'
        assert somnofy.zone_name == 'test_zone'
        assert somnofy.token_file == join('/path/to', 'token.txt')
        assert somnofy.subjects_url == 'https://api.health.somnofy.com/api/v1/subjects'
        assert somnofy.sessions_url == 'https://api.health.somnofy.com/api/v1/sessions'
        assert somnofy.reports_url == 'https://api.health.somnofy.com/api/v1/reports'
        assert somnofy.zones_url == 'https://api.health.somnofy.com/api/v1/zones'
        assert somnofy.date_start == '2023-08-01T00:00:00Z'
        assert somnofy.date_end is not None
        assert somnofy.LIMIT == 300
        mock_set_auth.assert_called_once_with('test_client_id')
        mock_get_zone_id.assert_called_once()

    def test_init_no_client_id(self):
        properties = Properties(client_id=None, client_id_file='/path/to/client_id_file', zone_name='test_zone')
        with pytest.raises(ValueError, match='Client ID must be provided'):
            Somnofy(properties)

    @patch('ambient_bd_downloader.sf_api.somnofy.exists', return_value=True)
    @patch('ambient_bd_downloader.sf_api.somnofy.open', new_callable=mock_open, read_data='test_token')
    @patch('ambient_bd_downloader.sf_api.somnofy.OAuth2Session')
    @patch('ambient_bd_downloader.sf_api.somnofy.Somnofy.get_zone_id', return_value=1)
    def test_set_auth_with_valid_token(self, mock_get_zone_id, mock_oauth2session, mock_open, mock_exists):
        properties = Properties(client_id='test_client_id',
                                client_id_file='/path/to/client_id_file',
                                zone_name='test_zone')
        mock_oauth2session.return_value.get.return_value.status_code = 200
        somnofy = Somnofy(properties)
        oauth = somnofy.set_auth('test_client_id')

        mock_open.assert_called_with(join('/path/to', 'token.txt'), 'r')
        mock_oauth2session.assert_called_with('test_client_id', token={'access_token': 'test_token',
                                                                       'token_type': 'Bearer'})
        assert oauth is not None

    @patch('ambient_bd_downloader.sf_api.somnofy.webbrowser.open')
    @patch('ambient_bd_downloader.sf_api.somnofy.input', return_value='https://example.com/callback?code=test_code')
    @patch('ambient_bd_downloader.sf_api.somnofy.OAuth2Session')
    @patch('ambient_bd_downloader.sf_api.somnofy.open', new_callable=mock_open)
    @patch('ambient_bd_downloader.sf_api.somnofy.Somnofy.get_zone_id', return_value=1)
    def test_set_auth_new_authorization(self, mock_get_zone_id, mock_open,
                                        mock_oauth2session, mock_input, mock_webbrowser):
        properties = Properties(client_id='test_client_id',
                                client_id_file='/path/to/client_id_file',
                                zone_name='test_zone')
        mock_oauth2session.return_value.authorization_url.return_value = ('https://auth.somnofy.com/oauth2/authorize',
                                                                          'test_state')
        mock_oauth2session.return_value.fetch_token.return_value = {'access_token': 'new_test_token'}
        somnofy = Somnofy(properties)
        oauth = somnofy.set_auth('test_client_id')

        mock_webbrowser.assert_called_with('https://auth.somnofy.com/oauth2/authorize')
        mock_input.assert_called_with('Enter the full URL: ')
        mock_open.assert_called_with(join('/path/to', 'token.txt'), 'w')
        mock_open().write.assert_called_with('new_test_token')
        assert oauth is not None
