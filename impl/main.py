import os.path
import base64
import pstats
import marshal

import tornado.template

from . import stats as snakeviz_stats

STATIC_URL = 'https://nejc.saje.info/pstats'

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse

with open('impl/viz.html') as f:
    viz_template = tornado.template.Template(f.read())

class MockProfile:
    def __init__(self, stats_bytes):
        self.stats = marshal.loads(stats_bytes)

    def create_stats(self):
        pass

def handler(event, context):
    qs = urlparse.parse_qs(event.get("body"))
    stats_bytes = base64.b64decode(qs.get("pstats")[0])

    stats = pstats.Stats(MockProfile(stats_bytes))

    return {
        "statusCode": 200,
        "body": viz_template.generate(
            profile_name='myprofile',
            table_rows=snakeviz_stats.table_rows(stats),
            callees=snakeviz_stats.json_stats(stats),
            static_url=STATIC_URL
        ).decode(),
        "headers": {
            "Content-Type": "text/html"
        }
    }
