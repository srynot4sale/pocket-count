import pocket
import requests

from auth import *

pocket_instance = pocket.Pocket(POCKET_CONSUMER_KEY, OAUTH_CODE)


total = 0
while 1:
    res = requests.get('https://getpocket.com/v3/get', {
        'consumer_key': POCKET_CONSUMER_KEY,
        'access_token': OAUTH_CODE,
        'tag': '_untagged_',
        'state': 'unread',
        'sort': 'newest',
        'count': 100,
        'offset': total
        }
    )

    if not len(res.json()['list']):
        break

    total += len(res.json()['list'])
    print(total)
