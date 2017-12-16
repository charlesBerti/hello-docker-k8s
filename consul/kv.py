import sys
import requests
import base64
import json


CONSUL_HOST = "127.0.0.1"
CONSUL_PORT = "8500"

data1 = '888888888888888888888'

data2 = {
    "aaa": "bbb",
    "ccc": "ddd",
    "eee": "fff"
}


def get_configuration(key):
    url = "http://{}:{}/v1/kv/{}".format(CONSUL_HOST, CONSUL_PORT, key)
    req = requests.get(url)
    data = req.json()
    if len(data) == 1:
        data = data[0]
        return {data["Key"]: json.loads(base64.b64decode(data["Value"]).decode("utf-8"))}
    else:
        return [
            {item["Key"]: json.loads(base64.b64decode(item["Value"]).decode("utf-8"))}
            for item in data
        ]


def create_configuration(key):
    req = requests.put(
        "http://{}:{}/v1/kv/{}".format(CONSUL_HOST, CONSUL_PORT, key),
        headers={"content-type": "application/json"},
        json=data1
    )

create_configuration(sys.argv[1])
print(get_configuration(sys.argv[1])[sys.argv[1]])
