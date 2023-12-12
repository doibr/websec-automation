import argparse
import http.client
from urllib.parse import urlparse

parser = argparse.ArgumentParser('HTTPHeader')
parser.add_argument('-u', '--url', required=True)
args = parser.parse_args()

o = urlparse(args.url)

conn = http.client.HTTPConnection(o.hostname)
headers = {"Authorization": "Basic dGVzdDp0ZXN0"}
conn.request("PUT", o.path, {}, headers)
response = conn.getresponse()

print(response.read().decode("utf-8"))

conn.close()
