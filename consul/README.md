# Consul
Consul is the service discovery module 

## Service Registration
### Terminology
- ID: Consul internal identity
- Datacenter: 
- Node: node is equivant to a host/physical server
- Address: 
- Service: 

### Basic Manipulation
- list data centers: `curl http://localhost:8500/v1/catalog/datacenters`
- list nodes: `curl http://localhost:8500/v1/catalog/nodes`
- list services: `curl http://localhost:8500/v1/catalog/services`
- list nodes for a service: `curl https://consul.rocks/v1/catalog/service/shop`

### Bash Registration
- register: 
    - `curl --request PUT --data @service-sample.json http://localhost:8500/v1/catalog/register`
    - `curl -X PUT -d '{
        "Datacenter": "dc1", 
        "Node": "amazon", 
        "Address": "www.amazon.com", 
        "Service": {"Service": "shop", "Port": 80}}' http://127.0.0.1:8500/v1/catalog/register`
- deregister: `curl -X PUT -d '{"Datacenter": "dc1", "Node": "amazon"}' http://127.0.0.1:8500/v1/catalog/deregister`

### Web Access
- `http://localhost:8500`

## Key-Value Store
### Basic Manipulation
- list: `curl http://127.0.0.1:8500/v1/kv/xxx`
- create/update key-value: `curl -X PUT -d 'bbb' http://127.0.0.1:8500/v1/kv/aaa`
- delete key-value: `curl -X DELETE http://127.0.0.1:8500/v1/kv/aaa`

### Python Manipulation
- `python kv.py`

## Installation
### Docker Install
`docker container run -p 8500:8500 --rm --name=test_consul consul`
- 8400 (RPC)
- *8500 (HTTP)*: web UI endpoint 
- 8600 (DNS)

