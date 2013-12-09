"""Facebook wrapper tests."""

import datetime

import anyjson
import urlparse
import facebook as facebook_api

import mock
import testfixtures

from wrap2 import facebook


# mocking data returned by Facebook
DATA_GET = r"""{"data":[{"name":"posts","fql_result_set":[{"post_id":"302590276513997_316451585127866",
"actor_id":100000103765943,"attachment":{"description":""},"comments":{"count":3},"created_time":1355781979,
"likes":{"href":"http:\/\/www.facebook.com\/browse\/likes\/?id=316451585127866","count":1,
"sample":[100003032215825],"friends":[],"user_likes":false,"can_like":false},"message":"i couldn't sleep...",
"message_tags":[],"parent_post_id":null,
"permalink":"http:\/\/www.facebook.com\/groups\/302590276513997\/permalink\/316451585127866\/",
"place":null,"privacy":{"value":""},"share_count":0,"source_id":302590276513997,"type":308,
"updated_time":1355782393,"target_id":302590276513997},{"post_id":"302590276513997_316411988465159",
"actor_id":100001964824717,"attachment":{"description":""},"comments":{"count":0},"created_time":1355773807,
"likes":{"href":"http:\/\/www.facebook.com\/browse\/likes\/?id=316411988465159","count":1,
"sample":[100000103765943],"friends":[],"user_likes":false,"can_like":false},
"message":"I \u003C3 fatal frame \uff3c(^o^)\uff0f","message_tags":[],"parent_post_id":null,
"permalink":"http:\/\/www.facebook.com\/groups\/302590276513997\/permalink\/316411988465159\/","place":null,
"privacy":{"value":""},"share_count":0,"source_id":302590276513997,"type":308,"updated_time":1355773807,
"target_id":302590276513997}]},{"name":"comments",
"fql_result_set":[{"id":"302590276513997_316451585127866_316451715127853","likes":0,
"text":"let me sleep with u hahaha...","text_tags":[],"time":1355782020,"post_id":"302590276513997_316451585127866",
"fromid":100000103765943},{"id":"302590276513997_316451585127866_316452618461096","likes":1,
"text":"poor miku....","text_tags":[],"time":1355782262,"post_id":"302590276513997_316451585127866",
"fromid":100003032215825}]},{"name":"post_actor_info","fql_result_set":[{"uid":100000103765943,
"name":"Yami Malik Ishtar"},{"uid":100001964824717,"name":"Kitana Rayna Webb"}]},{"name":"comment_actor_info",
"fql_result_set":[{"uid":100000103765943,"name":"Yami Malik Ishtar"},
{"uid":100003032215825,"name":"Kairis Namine"}]}]}"""

EXPECTED_DATA_GET = [{'created_at': datetime.datetime(2012, 12, 17, 20, 50, 7),
                      'entities': {'urls': [{
                                            'display_url': 'http://www.facebook.com/groups/302590276513997/'
                                                           'permalink/316411988465159/',
                                            'expanded_url': 'http://www.facebook.com/groups/302590276513997/'
                                                            'permalink/316411988465159/',
                                            'indices': [],
                                            'url': 'http://www.facebook.com/groups/302590276513997/permalink/'
                                                   '316411988465159/'}]},
                      'from_user': 'Kitana Rayna Webb',
                      'from_user_id': 100001964824717,
                      'from_user_id_str': '100001964824717',
                      'geo': None,
                      'id': '302590276513997_316411988465159',
                      'id_str': '302590276513997_316411988465159',
                      'iso_language_code': 'en',
                      'metadata': {'recent_retweets': 0, 'result_type': 'recent'},
                      'text': u'I <3 fatal frame \uff3c(^o^)\uff0f'},
                     {'created_at': datetime.datetime(2012, 12, 17, 23, 6, 19),
                      'entities': {'urls': [{
                                            'display_url': 'http://www.facebook.com/groups/302590276513997/'
                                                           'permalink/316451585127866/',
                                            'expanded_url': 'http://www.facebook.com/groups/302590276513997/'
                                                            'permalink/316451585127866/',
                                            'indices': [],
                                            'url': 'http://www.facebook.com/groups/302590276513997/permalink/'
                                                   '316451585127866/'}]},
                      'from_user': 'Yami Malik Ishtar',
                      'from_user_id': 100000103765943,
                      'from_user_id_str': '100000103765943',
                      'geo': None,
                      'id': '302590276513997_316451585127866',
                      'id_str': '302590276513997_316451585127866',
                      'iso_language_code': 'en',
                      'metadata': {'recent_retweets': 0, 'result_type': 'recent'},
                      'text': "i couldn't sleep..."},
                     {'created_at': datetime.datetime(2012, 12, 17, 23, 7),
                      'entities': {'urls': [{
                                            'display_url': 'http://www.facebook.com/groups/302590276513997/'
                                                           'permalink/316451585127866/'
                                                           '?comment_id=302590276513997_316451585127866_'
                                                           '316451715127853',
                                            'expanded_url': 'http://www.facebook.com/groups/302590276513997/'
                                                            'permalink/316451585127866/'
                                                            '?comment_id=302590276513997_316451585127866_'
                                                            '316451715127853',
                                            'indices': [],
                                            'url': 'http://www.facebook.com/groups/302590276513997/permalink/'
                                                   '316451585127866/'
                                                   '?comment_id=302590276513997_316451585127866_316451715127853'}]},
                      'from_user': 'Yami Malik Ishtar',
                      'from_user_id': 100000103765943,
                      'from_user_id_str': '100000103765943',
                      'geo': None,
                      'id': '302590276513997_316451585127866_316451715127853',
                      'id_str': '302590276513997_316451585127866_316451715127853',
                      'iso_language_code': 'en',
                      'metadata': {'recent_retweets': 0, 'result_type': 'recent'},
                      'text': 'let me sleep with u hahaha...'},
                     {'created_at': datetime.datetime(2012, 12, 17, 23, 11, 2),
                      'entities': {'urls': [{
                                            'display_url': 'http://www.facebook.com/groups/302590276513997/'
                                                           'permalink/316451585127866/'
                                                           '?comment_id=302590276513997_316451585127866_'
                                                           '316452618461096',
                                            'expanded_url': 'http://www.facebook.com/groups/302590276513997/'
                                                            'permalink/316451585127866/'
                                                            '?comment_id=302590276513997_316451585127866_'
                                                            '316452618461096',
                                            'indices': [],
                                            'url': 'http://www.facebook.com/groups/302590276513997/permalink/'
                                                   '316451585127866/'
                                                   '?comment_id=302590276513997_316451585127866_316452618461096'}]},
                      'from_user': 'Kairis Namine',
                      'from_user_id': 100003032215825,
                      'from_user_id_str': '100003032215825',
                      'geo': None,
                      'id': '302590276513997_316451585127866_316452618461096',
                      'id_str': '302590276513997_316451585127866_316452618461096',
                      'iso_language_code': 'en',
                      'metadata': {'recent_retweets': 0, 'result_type': 'recent'},
                      'text': 'poor miku....'}]


patch_fb = mock.patch.object(facebook_api.GraphAPI, 'request', lambda self, url, args: anyjson.loads(DATA_GET))
"""Define mock decorator to mock facebook's graph remote api calls with static data."""


@patch_fb
def test_get():
    """test .get method of the Facebook wrapper"""

    fb = facebook.Facebook(1, 2)
    results = fb.get(dict(ids=[123123123, 234234234]), 'sometesttoken')
    testfixtures.compare(results[0], EXPECTED_DATA_GET[0])


@patch_fb
def test_get_authorization_url():
    """test .get_authorization_url method of the Facebook wrapper."""

    fb = facebook.Facebook(1, 2)
    url, opts = fb.get_authorization_url('http://some.com', scope=('read', 'write'))
    assert url.startswith(fb.FB_OATH_BASE)
    assert urlparse.parse_qs(urlparse.urlparse(url).query), {
        'scope': ['read,write'],
        'redirect_uri': ['http://some.com'],
        'client_id': ['1']}
    assert opts == ()
