#coding: utf-8
"""Facebook wrapper tests"""

import datetime
import httplib
import unittest

import tweepy

import mockito
import mock

from wrap2 import twitter


class TwitterTestCase(unittest.TestCase):
    """TestCase for Twitter wrapper"""

    get_data = """
    {"statuses" :[
    {
      "coordinates": null,
      "favorited": false,
      "truncated": false,
      "created_at": "Mon Sep 24 03:35:21 +0000 2012",
      "id_str": "250075927172759552",
      "entities": {
        "urls": [

        ],
        "hashtags": [
          {
            "text": "freebandnames",
            "indices": [
              20,
              34
            ]
          }
        ],
        "user_mentions": [

        ]
      },
      "in_reply_to_user_id_str": null,
      "contributors": null,
      "text": "Aggressive Ponytail #freebandnames",
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      },
      "retweet_count": 0,
      "in_reply_to_status_id_str": null,
      "id": 250075927172759552,
      "geo": null,
      "retweeted": false,
      "in_reply_to_user_id": null,
      "place": null,
      "user": {
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_sidebar_border_color": "C0DEED",
        "profile_background_tile": false,
        "name": "Sean Cummings",
        "profile_image_url": "http://a0.twimg.com/profile_images/2359746665/1v6zfgqo8g0d3mk7ii5s_normal.jpeg",
        "created_at": "Mon Apr 26 06:01:55 +0000 2010",
        "location": "LA, CA",
        "follow_request_sent": null,
        "profile_link_color": "0084B4",
        "is_translator": false,
        "id_str": "137238150",
        "entities": {
          "url": {
            "urls": [
              {
                "expanded_url": null,
                "url": "",
                "indices": [
                  0,
                  0
                ]
              }
            ]
          },
          "description": {
            "urls": [

            ]
          }
        },
        "default_profile": true,
        "contributors_enabled": false,
        "favourites_count": 0,
        "url": null,
        "profile_image_url_https": "https://si0.twimg.com/profile_images/2359746665/1v6zfgqo8g0d3mk7ii5s_normal.jpeg",
        "utc_offset": -28800,
        "id": 137238150,
        "profile_use_background_image": true,
        "listed_count": 2,
        "profile_text_color": "333333",
        "lang": "en",
        "followers_count": 70,
        "protected": false,
        "notifications": null,
        "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
        "profile_background_color": "C0DEED",
        "verified": false,
        "geo_enabled": true,
        "time_zone": "Pacific Time (US & Canada)",
        "description": "Born 330 Live 310",
        "default_profile_image": false,
        "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
        "statuses_count": 579,
        "friends_count": 110,
        "following": null,
        "show_all_inline_media": false,
        "screen_name": "sean_cummings"
      },
      "in_reply_to_screen_name": null,
      "source": "Twitter for Mac",
      "in_reply_to_status_id": null
    }],
        "search_metadata": {
        "max_id": 250126199840518145,
        "since_id": 24012619984051000,
        "refresh_url": "?since_id=250126199840518145&q=%23freebandnames&result_type=mixed&include_entities=1",
        "next_results": "?max_id=249279667666817023&q=%23freebandnames&count=4&include_entities=1&result_type=mixed",
        "count": 4,
        "completed_in": 0.035,
        "since_id_str": "24012619984051000",
        "query": "%23freebandnames",
        "max_id_str": "250126199840518145"
      }
    }
    """

    get_data_expected = [{
        'author': {
            'contributors_enabled': False,
            'created_at': datetime.datetime(2010, 4, 26, 6, 1, 55),
            'default_profile': True,
            'default_profile_image': False,
            'description': u'Born 330 Live 310',
            'entities': {
                u'description': {u'urls': []},
                u'url': {u'urls': [{
                    u'expanded_url': None,
                    u'indices': [0, 0],
                    u'url': u''}]}},
            'favourites_count': 0,
            'follow_request_sent': None,
            'followers_count': 70,
            'following': False,
            'friends_count': 110,
            'geo_enabled': True,
            'id': 137238150,
            'id_str': u'137238150',
            'is_translator': False,
            'lang': u'en',
            'listed_count': 2,
            'location': u'LA, CA',
            'name': u'Sean Cummings',
            'notifications': None,
            'profile_background_color': u'C0DEED',
            'profile_background_image_url': u'http://a0.twimg.com/images/themes/theme1/bg.png',
            'profile_background_image_url_https': u'https://si0.twimg.com/images/themes/theme1/bg.png',
            'profile_background_tile': False,
            'profile_image_url': u'http://a0.twimg.com/profile_images/2359746665/1v6zfgqo8g0d3mk7ii5s_normal.jpeg',
            'profile_image_url_https':
                u'https://si0.twimg.com/profile_images/2359746665/1v6zfgqo8g0d3mk7ii5s_normal.jpeg',
            'profile_link_color': u'0084B4',
            'profile_sidebar_border_color': u'C0DEED',
            'profile_sidebar_fill_color': u'DDEEF6',
            'profile_text_color': u'333333',
            'profile_use_background_image': True,
            'protected': False,
            'screen_name': u'sean_cummings',
            'show_all_inline_media': False,
            'statuses_count': 579,
            'time_zone': u'Pacific Time (US & Canada)',
            'url': None,
            'utc_offset': -28800,
            'verified': False},
        'contributors': None,
        'coordinates': None,
        'created_at': datetime.datetime(2012, 9, 24, 3, 35, 21),
        'entities': {u'hashtags': [{u'indices': [20, 34],
                                    u'text': u'freebandnames'}],
                     u'urls': [],
                     u'user_mentions': []},
        'favorited': False,
        'from_user': u'sean_cummings',
        'from_user_name': u'Sean Cummings',
        'from_user_id': 137238150,
        'from_user_id_str': u'137238150',
        'geo': None,
        'id': 250075927172759552,
        'id_str': u'250075927172759552',
        'in_reply_to_screen_name': None,
        'in_reply_to_status_id': None,
        'in_reply_to_status_id_str': None,
        'in_reply_to_user_id': None,
        'in_reply_to_user_id_str': None,
        'metadata': {u'iso_language_code': u'en', u'result_type': u'recent'},
        'place': None,
        'profile_image_url': u'http://a0.twimg.com/profile_images/2359746665/1v6zfgqo8g0d3mk7ii5s_normal.jpeg',
        'retweet_count': 0,
        'retweeted': False,
        'source': u'Twitter for Mac',
        'source_url': None,
        'text': u'Aggressive Ponytail #freebandnames',
        'truncated': False,
        'user': {
            'contributors_enabled': False,
            'created_at': datetime.datetime(2010, 4, 26, 6, 1, 55),
            'default_profile': True,
            'default_profile_image': False,
            'description': u'Born 330 Live 310',
            'entities': {
                u'description': {u'urls': []},
                u'url': {u'urls': [{
                    u'expanded_url': None,
                    u'indices': [0, 0],
                    u'url': u''}]}},
            'favourites_count': 0,
            'follow_request_sent': None,
            'followers_count': 70,
            'following': False,
            'friends_count': 110,
            'geo_enabled': True,
            'id': 137238150,
            'id_str': u'137238150',
            'is_translator': False,
            'lang': u'en',
            'listed_count': 2,
            'location': u'LA, CA',
            'name': u'Sean Cummings',
            'notifications': None,
            'profile_background_color': u'C0DEED',
            'profile_background_image_url': u'http://a0.twimg.com/images/themes/theme1/bg.png',
            'profile_background_image_url_https': u'https://si0.twimg.com/images/themes/theme1/bg.png',
            'profile_background_tile': False,
            'profile_image_url': u'http://a0.twimg.com/profile_images/2359746665/1v6zfgqo8g0d3mk7ii5s_normal.jpeg',
            'profile_image_url_https':
                u'https://si0.twimg.com/profile_images/2359746665/1v6zfgqo8g0d3mk7ii5s_normal.jpeg',
            'profile_link_color': u'0084B4',
            'profile_sidebar_border_color': u'C0DEED',
            'profile_sidebar_fill_color': u'DDEEF6',
            'profile_text_color': u'333333',
            'profile_use_background_image': True,
            'protected': False,
            'screen_name': u'sean_cummings',
            'show_all_inline_media': False,
            'statuses_count': 579,
            'time_zone': u'Pacific Time (US & Canada)',
            'url': None,
            'utc_offset': -28800,
            'verified': False}}]

    def tearDown(self):
        """Test cleanup routine"""
        mockito.unstub()

    def test_get_authorization_url(self):
        """test .get_authorization_url method of the Twitter wrapper."""

        tw = twitter.Twitter('token', 'secret')
        callback_url = 'http://some.com'
        test_auth_url = 'http://twitter.com/auth_url'

        auth_handler = mockito.mock()
        auth_handler.request_token = tweepy.oauth.OAuthToken.from_string('oauth_token_secret=test_secret'
                                                                         '&oauth_token=test_token')
        mockito.when(tweepy).OAuthHandler(tw.id, tw.secret, callback_url).thenReturn(auth_handler)
        mockito.when(auth_handler).get_authorization_url(signin_with_twitter=True).thenReturn(test_auth_url)

        url, opts = tw.get_authorization_url(callback_url)
        self.assertEqual(url, test_auth_url)
        self.assertEqual(opts, ('test_token', 'test_secret'))

    def test_get(self):
        """test .get method of the Twitter wrapper"""
        self.maxDiff = None

        (mockito.when(httplib.HTTPSConnection).request(mockito.any(), mockito.any(), mockito.any(), mockito.any())
            .thenReturn(None))
        response = mock.MagicMock()
        response.status = 200
        response.read = lambda: self.get_data
        (mockito.when(httplib.HTTPSConnection).getresponse()
            .thenReturn(response))

        tw = twitter.Twitter(1, 2)
        results = tw.get(dict(ids=[123123123, 234234234]), 'sometesttoken')

        self.assertEqual(list(results), self.get_data_expected)
