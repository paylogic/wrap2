"""Twitter wrapper tests."""

import tweepy

import mock

from wrap2 import twitter


def test_get_authorization_url():
    """test .get_authorization_url method of the Twitter wrapper."""

    tw = twitter.Twitter('token', 'secret')
    callback_url = 'http://example.com'
    test_auth_url = 'http://twitter.com/auth_url'

    auth_handler = mock.MagicMock()
    auth_handler.request_token = tweepy.oauth.OAuthToken.from_string('oauth_token_secret=test_secret'
                                                                     '&oauth_token=test_token')
    auth_handler.get_authorization_url.return_value = test_auth_url

    with mock.patch('tweepy.OAuthHandler') as mocked:
        mocked.return_value = auth_handler

        url, opts = tw.get_authorization_url(callback_url)
        assert url == test_auth_url
        assert opts == ('test_token', 'test_secret')
