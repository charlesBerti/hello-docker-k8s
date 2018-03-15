# Service
access N pods through an integrated load-balancer, a service routes traffic across a set of Pods, it has that distributes network traffics to all pods of an exposed Deployment.

- endpoint: 1 pod for 1 deployment is an endpoint, each pod has an internal IP address
- service vs. deployment: no dependency between service and deployment, a service can use pods from different deployment with the same *selector*.
- exposure types:
  - NodePort: exposes service on the same port of each node using NAT, it makes the Service accessible from outside the cluster using <NodeIP>:<NodePort>
  - ClusterIP (default): exposes Service on an internal IP in the cluster, this makes the Service only reachable from within the cluster.
  - headless: exposes Service by a Pod network instead of Cluster network, conf `ClusterIP=None`
  - LoadBalancer: creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.
  - ExternalName: exposes the Service using an arbitrary name (specified by externalName in the spec) by returning a CNAME record with the name. No proxy is used. This type requires v1.7 or higher of kube-dns

## CMD
- `kubectl get services`: list services
- `kubectl get services/$SERVICE_ID`: list a service
- `kubectl describe services`: describe services
- `kubectl describe services $SERVICE_ID`: describe a service
- `kubectl expose deployment $DEP_ID --type NodePort --port 8080`: create a service (expose a deployment)
  - `curl $(minikube ip):$NODE_PORT`: test
- `kubectl delete service -l run=kubernetes-bootcamp`: delete a service

## YAML
- type: ClusterIP
- selector: e.g. `app:n`
- ports:
  - port: internal port
  - target port: container port inside the container