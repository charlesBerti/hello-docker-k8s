# Kubernetes
Kubernetes coordinates a highly available cluster of computers that are connected to work as a single unit. 

## Cluster & Master & Node  
- cluster: 1 master + n nodes
- master: a VM or a physical PC which coordinates the cluster, each master installs:
  - *kube-apiserver* & *kubectl*: *kubectl* is the CLI for *kube-apiserver*  
  - *kube-controller-manager*: 
  - *kube-scheduler*: 
- node: a VM or a physical PC which serves as a worker that runs applications, each node installs: 
  - *Kubelet*: an agent for managing the node and communicating with the master
  - *kube-proxy*: a network proxy to reflect K8S networking services on each node, a proxy forwards external communications into the private pod network
  - *Docker engine*: a container runtime like 
- master/node: while deploying applications on K8S, the master schedules the containers to run on the nodes. 
The nodes communicate with the master using the K8S API.

### CMD
- `kubectl version`
- `kubectl cluster-info`:
- `kubectl get nodes`
- create a proxy: `kubectl proxy`
  - test: `curl http://localhost:8001/version`
- logs: `kubectl logs $POD_NAME`

## Namespace & POD & Controller & Deployment & Service
- namespace: virtual cluster backed by the same physical cluster, it is a isolated space (isolated network) for a set of Dockers.  
- pod: encapsulates one or multiple application containers, storage resources, a unique IP address, *it always runs on 1 node*, [example](pod.yml). 
  - networking: each pod is assigned a unique IP address, containers inside a pod communicate with one another using `localhost` 
  - storage: all containers in a pod can access the shared volumes
- controller: manages a group of replicated pods
- deployment: describes a desired state, [example](deployment.yml) 
  - deployment controller: changes the actual state to the desired state at a controlled rate
  - deployment vs. pod: while creating a deployment, the deployment creates pods with containers inside them (as opposed to creating containers directly) on each node. 
  - scaling: is accomplished by changing the number of pod replicas in a deployment.
- service: a logical set of pods and a policy by which to access them. 
A Service routes traffic across a set of Pods, it has an integrated load-balancer that distributes network traffics to all pods of an exposed Deployment.
  - the service exposure types include:
    - ClusterIP (default): exposes the Service on an internal IP in the cluster, this type makes the Service only reachable from within the cluster.
    - NodePort: exposes the Service on the same port of each selected Node in the cluster using NAT, it makes a Service accessible from outside the cluster using <NodeIP>:<NodePort>. Superset of ClusterIP.
    - LoadBalancer: creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.
    - ExternalName: exposes the Service using an arbitrary name (specified by externalName in the spec) by returning a CNAME record with the name. No proxy is used. This type requires v1.7 or higher of kube-dns  

### Namespace CMD
- list namespaces: `kubectl get namespaces`
- CMD within one namespace: `kubectl --namespace=NAMESPCE_ID get pods`

### POD CMD
- list pods: `kubectl get pods`
- describe pods: `kubectl describe pods`
- execute CMD on a container of the pod: `kubectl exec $POD_NAME CMD`
  - `kubectl exec $POD_NAME env`
  - launch a `bash`: `kubectl exec -ti $POD_NAME bash`
  - internal access: `kubectl exec -ti $POD_NAME curl localhost:8080`

### Deployment CMD
- list deployments: `kubectl get deployments`
- create a deployment: `kubectl run test1 --image=docker.io/jocatalin/kubernetes-bootcamp:v1 --port=8080`
- create a deployment: `kubectl create -f https://raw.githubusercontent.com/kubernetes/website/master/docs/concepts/workloads/controllers/nginx-deployment.yaml`
- scale: `kubectl scale deployments/kubernetes-bootcamp --replicas=4`

### Service CMD
- list services: `kubectl get services`
- list a service: `kubectl get services/$SERVICE_NAME`
- describe services: `kubectl describe services`
- describe a service: `kubectl describe services/$SERVICE_NAME`
- run a service (expose a deployment): `kubectl expose deployment/$DEP_NAME --type="NodePort" --port 8080`
  - test: `curl $HOST_NAME:$NODE_PORT`
- delete a service: `kubectl delete service -l run=kubernetes-bootcamp`


### K8S Objects
### Label
we can attach labels to service and pod

### Label CMD
- filter with label `run=kubernetes-bootcamp`: `kubectl get pods -l run=kubernetes-bootcamp`
- filter with label `run=kubernetes-bootcamp`: `kubectl get services -l run=kubernetes-bootcamp`
- add a lab: `kubectl label pod $POD_NAME app=v1`

## Volume
