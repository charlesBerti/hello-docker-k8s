# Kubernetes

## Terminology
- cluster: 1 master + n nodes
- master: which coordinates the cluster
- node: a VM or a physical PC which serves as a worker that run applications. each node has a Kubelet which is an agent for managing the node and communicating with the master and a container engine like Docker.
- master/node: while deploying applications on K8S, the master schedules the containers to run on the nodes. The nodes communicate with the master using the K8S API.
- client: kubectl
- server: the K8S version installed on the master
- Kubelet: the K8S version installed on the node

### Deployment & Pod
Deployment is the implementation of an application.
When we create a Deployment on K8S, that Deployment creates Pods with containers inside them (as opposed to creating containers directly) on each node.
- Deployment: instance of an application.
- Pod = application instance: all resource of an application on 1 node

### Service
Service is the exposure of an application/deployment which uses a set of Pods and a policy by which to access them.
A Service routes traffic across a set of Pods.
Services have an integrated load-balancer that will distribute network traffic to all PODs of an exposed Deployment.
The service types include:
- ClusterIP (default): exposes the Service on an internal IP in the cluster. This type makes the Service only reachable from within the cluster.
- NodePort: exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using <NodeIP>:<NodePort>. Superset of ClusterIP.
- LoadBalancer: creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.
- ExternalName: exposes the Service using an arbitrary name (specified by externalName in the spec) by returning a CNAME record with the name. No proxy is used. This type requires v1.7 or higher of kube-dns

### Label
we can attach labels to service and pod

### Scaling
Scaling is accomplished by changing the number of POD replicas in a Deployment.


## Kubectl
- `minikube version`
- `minikube start`: start the cluster

### Cluster/ Master/ Node
- `kubectl version`
- `kubectl cluster-info`:
- `kubectl get nodes`
- `kubectl get pods`: details of each POD
- `kubectl logs $POD_ID`:
- `kubectl exec $POD_ID CMD`: execute a cmd in a container
    - `kubectl exec $POD_ID env`
    - `kubectl exec -ti $POD_ID bash`: launch a `bash`

### Deployment
- `kubectl get deployments`
- `kubectl run kubernetes-bootcamp --image=docker.io/jocatalin/kubernetes-bootcamp:v1 --port=8080`

### Proxy
create a proxy to access to the API of a POD which is in a private network
- in one terminal: `kubectl proxy`
- in another terminal: `curl http://localhost:8001/version`

### Service
expose a deployment to external traffic
- `kubectl get services`
- `kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080`
- `kubectl delete service -l run=kubernetes-bootcamp`

### Label
- `kubectl get pods -l run=kubernetes-bootcamp`: filter with label `run=kubernetes-bootcamp`
- `kubectl get services -l run=kubernetes-bootcamp`
- `kubectl label pod $POD_ID app=v1`: add a new lab

### Scale
- `kubectl scale deployments/kubernetes-bootcamp --replicas=4`