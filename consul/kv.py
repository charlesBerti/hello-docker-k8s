import base64
import json
import requests

CONSUL_HOST = "127.0.0.1"
CONSUL_PORT = "8500"

DATABASE = "database"
SLAVE = "slave"
MESSENGER = "messenger"
KEYSTONE = "keystone"
DOCKER = "docker"
COMPONENTS = "components"


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
    data = {
        "aaa": "bbb",
        "ccc": "ddd",
        "eee": "fff"
    }
    req = requests.put(
        "http://{}:{}/v1/kv/{}".format(CONSUL_HOST, CONSUL_PORT, key),
        headers={"content-type": "application/json"},
        json=data
    )

create_configuration("www")
print(get_configuration("www"))

