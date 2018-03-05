# Kubernetes
Kubernetes coordinates a highly available cluster of computers that are connected to work as a single unit. 

## Cluster & Master & Node  
- cluster: 1 master + n nodes
- master: a VM or a physical PC which coordinates the cluster, each master installs:
  - *kube-apiserver*: all nodes communicate with the master using the K8S API
    - *kubectl* is the CLI for *kube-apiserver*
    - *dashbord* is the GUI for *kube-apiserver*
  - *kube-controller-manager*: check and ensure resource availability in the cluster
  - *kube-scheduler*: while deploying applications on K8S, the master schedules the containers to run on the nodes
  - *etcd*: local database for K8S status store
- node/worker: a VM or a physical PC which serves as a worker that runs applications, each node installs:
  - *Kubelet*: an agent for managing the node and communicating with the master
  - *kube-proxy*: load balancer, a network proxy to reflect K8S networking services on each node, a proxy forwards external communications into the private pod network
  - *Docker engine*: a container runtime like

### CMD
- `kubectl version`
#### config
- context: cluser + user as 1 config
  - `kubectl config get-contexts`: context is the config of a K8S cluster for kubectl
  - `kubectl config set-context $CONTEXT_ID --user=admin-formation --cluster=cluster-demo`: set a context by binding cluster and user
  - `kubectl config use-context $CONTEXT_ID`: switch to another K8S context
#### node
- `kubectl get nodes -o yaml`: -o output format
- `kubectl describe node minikube`: detail about a node
#### cluster
- `kubectl cluster-info`:
#### proxy
- create a proxy: `kubectl proxy`: all request to `localhost:8001` will be requested to *api-server*
  - test: `curl http://localhost:8001/version`
#### log
- logs: `kubectl logs $POD_NAME`

## Namespace & POD & Controller & Deployment & Service
- namespace: virtual cluster backed by the same physical cluster, it is a isolated space (isolated network) for a set of Dockers.  
- pod: encapsulates 1 or N application containers, storage resources, a unique IP address, *it always runs on 1 node*, [example](pod.yml).
  - networking: all the containers inside 1 pod share a unique IP address, communicate with one another using `localhost`
  - storage: all containers in 1 pod share the same mount point, can access the shared volumes
  - the number of containers in 1 pod cannot increase or decrease
- ReplicaSet/ controller: controls a group of replicated pods
- deployment: manage N pods through a ReplicaSet, describes and manages a desired state, [example](deployment.yml)
  - docker image update
    - rolling update: create a new deploy to increase and decrease the old one
  - scaling: change the number of pod replicas in a deployment.
  - patterns:
    - sidecar
    - ambassador
    - adapter
- service: access N pods through an integrated load-balancer, a service routes traffic across a set of Pods, it has that distributes network traffics to all pods of an exposed Deployment.
  - the service exposure types include:
    - ClusterIP (default): exposes the Service on an internal IP in the cluster, this type makes the Service only reachable from within the cluster.
    - NodePort: exposes the Service on the same port of each selected Node in the cluster using NAT, it makes a Service accessible from outside the cluster using <NodeIP>:<NodePort>. Superset of ClusterIP.
    - LoadBalancer: creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.
    - ExternalName: exposes the Service using an arbitrary name (specified by externalName in the spec) by returning a CNAME record with the name. No proxy is used. This type requires v1.7 or higher of kube-dns  
  - service vs. deployment: no dependency between service and deployment, a service can use pods from different deployment with the same `selector`
- Basic Conception
  - node IP and external port: the public IP address and port of the node
  - cluster IP and internal port: IP address for all the container within 1 pod, the port can be accessed inside the node
  - container port: the service port in the container

### Namespace CMD
- list namespaces: `kubectl get namespaces`
- CMD within one namespace: `kubectl --namespace=NAMESPCE_ID get pods`

### POD CMD
- `kubectl get pods`: list pods
- `kubectl describe pods`: describe pods
- `kubectl exec $POD_NAME CMD -c $CONTAINTER_NAME`: run a cmd in a pod (one container of a pod)
  - `kubectl exec $POD_NAME env`
  - launch a `bash`: `kubectl exec -ti $POD_NAME bash`
  - internal access: `kubectl exec -ti $POD_NAME curl localhost:8080`

### Deployment & ReplicaSet CMD
- `kubectl get deployments`: list deployments
- `kubectl run test1 --image=docker.io/jocatalin/kubernetes-bootcamp:v1 --port=8080`: create a deployment
- `kubectl create -f https://raw.githubusercontent.com/kubernetes/website/master/docs/concepts/workloads/controllers/nginx-deployment.yaml`: create a deployment
- `kubectl scale deployments/kubernetes-bootcamp --replicas=4`: scale

### Service CMD
- `kubectl get services`: list services
- list a service: `kubectl get services/$SERVICE_NAME`
- `kubectl describe services`: describe services
- `kubectl describe services $SERVICE_NAME`: describe a service
- `kubectl expose deployment $DEP_ID --type="NodePort" --port 8080`: create a service (expose a deployment)
  - test: `curl $(minikube ip):$NODE_PORT`
- `kubectl delete service -l run=kubernetes-bootcamp`: delete a service
#### endpoint: pods for 1 deployment, each pod has an internal IP address


## K8S Objects
### Label
we can attach labels to a resource
#### Label CMD
- `kubectl get pods --show-labels`: show labels
- `kubectl get pods -l run=kubernetes-bootcamp`: select with label `run=kubernetes-bootcamp`
- `kubectl get services -l run=kubernetes-bootcamp`: select with label `run=kubernetes-bootcamp`
- `kubectl label pod $POD_NAME app=v1`: add a lab

### Annotation
supplementary configuration, which will only be used by external applications


## Volume

## YAML
- `kubectl apply -f $FILE_ID.yaml`: create a resource through YAML file
- `kubectl delete -f $FILE_ID.yaml`: delete a resource through YAML file
- `apiVersion`: k8s API version
- `kind`: resource type
- `meta-data`: pre-defined meta-data
  - `name`
  - `lables`
  - `annotations`
- `spec`: parameters for different resource type
### deployment
  - `deployment spec`
    - `replicas`
    - `template`: parameters for the sub-resource type, e.g. the sub-resource of deployment is pod

### pod
  - `pod spec`
    - container:
    - nodeSelector: to choose node to launch pods

### container
- `container`:
  - `name`:
  - `image`
  - `ports`
    - `containerPort`

### service
- type: ClusterIP
- selector: e.g. `app:n`
- ports:
  - port: internal port
  - target port: container port inside the container

## TP Wordpress
- create mysql deployment
- create mysql service