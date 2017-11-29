# Consul
Consul is the service discovery module 

## Conception
### Service Definition
```json
{
  "service": {
    "name": "redis",
    "tags": ["primary"],
    "address": "",
    "port": 8000,
    "enable_tag_override": false,
    "checks": [
      {
        "script": "/usr/local/bin/check_redis.py",
        "interval": "10s"
      }
    ]
  }
}
```

### Terminology
- ID: Consul internal identity
- Datacenter: 
- Node: node is equivant to a host/physical server
- Address: 
- Service: 



## Installation
### Docker Install
`docker container run -p 8400:8400 -p 8500:8500 -p 8600:8600 --name=test_consul consul`
- 8400 (RPC)
- *8500 (HTTP)*: web UI endpoint 
- 8600 (DNS)


## Test
### Web Access
- `http://localhost:8888`

### Bash Manipulation
- register: 
    - `curl -X PUT -d '{
        "Datacenter": "dc1", 
        "Node": "amazon", 
        "Address": "www.amazon.com", 
        "Service": {"Service": "shop", "Port": 80}}' 
        http://127.0.0.1:8500/v1/catalog/register`
- deregister: `curl -X PUT -d '{"Datacenter": "dc1", "Node": "amazon"}' http://127.0.0.1:8500/v1/catalog/deregister`

### Python Access

