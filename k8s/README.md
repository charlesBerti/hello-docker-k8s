# Kubernetes/ K8S
k8s coordinates a highly available cluster of computers that are connected to work as a single unit.

## Installation & Configuration
- [K8S Installation & Configuration](installation/README.md)

## Cluster & Master & Node  
- cluster: 1 master + n nodes

### master
a VM or a physical PC which coordinates the cluster, each master installs:
- *kube-apiserver*: all nodes communicate with the master using the K8S API
  - *kubectl* is the CLI for *kube-apiserver*
  - *dashbord* is the GUI for *kube-apiserver*
- *kube-controller-manager*: check and ensure resource availability in the cluster
- *kube-scheduler*: while deploying applications on K8S, the master schedules the containers to run on the nodes
- *etcd*: local database for K8S status store

### node/worker
a VM or a physical PC which serves as a worker that runs applications, each node installs:
- *kubelet*: an agent for managing the node and communicating with the master
- *kube-proxy*: load balancer, a network proxy to reflect K8S networking services on each node, a proxy forwards external communications into the private pod network
- *Docker engine*: a container runtime like

CMD
- `kubectl cluster-info`
- `kubectl get nodes -o yaml`: -o output format
- `kubectl describe node minikube`: detail about a node
- `kubectl logs $RESOURCE_ID`: logs
- `kubectl proxy`: create a proxy, all request to `localhost:8001` will be requested to *api-server*
  - test: `curl http://localhost:8001/version`


## Concepts
### Namespace
virtual cluster backed by the same physical cluster, it is a isolated space (isolated network) for a set of Dockers.
- `kubectl get namespaces`: list namespaces
- `kubectl --namespace=NAMESPACE_ID get pods`: execute CMD within 1 namespace

### Label
we can attach labels to a resource

- `kubectl get pods --show-labels`: show labels
- `kubectl get pods -l run=kubernetes-bootcamp`: select with label `run=kubernetes-bootcamp`
- `kubectl get services -l run=kubernetes-bootcamp`: select with label `run=kubernetes-bootcamp`
- `kubectl label pod $POD_NAME app=v1`: add a lab

### Annotation
supplementary configuration, which will only be used by external applications


## Volume & ConfigSet & Secret
- [Volume & ConfigSet & Secret](volume/README.md)


## Networking
- node IP and external port: the public IP address and port of the node
- cluster IP and internal port: IP address for all the container within 1 pod, the port can be accessed inside the node
- container port: the service port in the container


## YAML Configuration
- [YAML Configuration](yaml/README.md)




