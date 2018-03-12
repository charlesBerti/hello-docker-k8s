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
- *Kubelet*: an agent for managing the node and communicating with the master
- *kube-proxy*: load balancer, a network proxy to reflect K8S networking services on each node, a proxy forwards external communications into the private pod network
- *Docker engine*: a container runtime like

### CMD
- `kubeclt cluster-info`
- `kubectl get nodes -o yaml`: -o output format
- `kubectl describe node minikube`: detail about a node

### proxy
- create a proxy: `kubectl proxy`: all request to `localhost:8001` will be requested to *api-server*
- test: `curl http://localhost:8001/version`

### log
- logs: `kubectl logs $POD_NAME`

## namespace
virtual cluster backed by the same physical cluster, it is a isolated space (isolated network) for a set of Dockers.

### CMD
- `kubectl get namespaces`: list namespaces
- `kubectl --namespace=NAMESPACE_ID get pods`: execute CMD within 1 namespace

## Pod
Atomic unit in k8s, it encapsulates 1 or N application container, storage resources, a unique IP address, *it always runs on 1 node*, [example](pod.yml).
- computing: 1 or N containers, but the number of containers within 1 pod is fixed
- storage: all containers in 1 pod have the same mount point, can access the same shared volumes
- networking: all the containers in 1 pod use a unique IP address, communicate with one another using `localhost`

### CMD
- `kubectl get pods`: list pods
- `kubectl describe pods`: describe pods
- `kubectl exec $POD_ID CMD -c $CONTAINTER_ID`: run a cmd the container of the pod
  - `kubectl exec $POD_ID env`: specify environment variables
  - `kubectl exec -ti $POD_ID bash`: launch a `bash`
  - `kubectl exec -ti $POD_ID curl localhost:8080`: internal access

## Replica Set
controls a group of replicated pods for scalability

## Deployment
manage N pods through a ReplicaSet, describes and manages a desired state, [example](deployment.yml)
- docker image update
  - rolling update: create a new deploy to increase and decrease the old one
- scaling: change the number of pod replicas in a deployment.
- patterns:
  - sidecar
  - ambassador
  - adapter

### CMD
- `kubectl get deployments`: list deployments
- `kubectl run test1 --image=docker.io/jocatalin/kubernetes-bootcamp:v1 --port=8080`: create a deployment
- `kubectl create -f https://raw.githubusercontent.com/kubernetes/website/master/docs/concepts/workloads/controllers/nginx-deployment.yaml`: create a deployment
- `kubectl scale deployments/kubernetes-bootcamp --replicas=4`: scale

## Service
access N pods through an integrated load-balancer, a service routes traffic across a set of Pods, it has that distributes network traffics to all pods of an exposed Deployment.
The service exposure types include:
- NodePort: exposes Service on the same port of each selected Node using NAT, it makes the Service accessible from outside the cluster using <NodeIP>:<NodePort>
- ClusterIP (default): exposes Service on an internal IP in the cluster, this makes the Service only reachable from within the cluster.
- headless: exposes Service by a Pod network instead of Cluster network, conf `ClusterIP=None`
- LoadBalancer: creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.
- ExternalName: exposes the Service using an arbitrary name (specified by externalName in the spec) by returning a CNAME record with the name. No proxy is used. This type requires v1.7 or higher of kube-dns

#### endpoint
1 pod for 1 deployment is an endpoint, each pod has an internal IP address

#### service vs. deployment
no dependency between service and deployment, a service can use pods from different deployment with the same `selector`

Service CMD
- `kubectl get services`: list services
- list a service: `kubectl get services/$SERVICE_NAME`
- `kubectl describe services`: describe services
- `kubectl describe services $SERVICE_NAME`: describe a service
- `kubectl expose deployment $DEP_ID --type="NodePort" --port 8080`: create a service (expose a deployment)
  - `curl $(minikube ip):$NODE_PORT`: test
- `kubectl delete service -l run=kubernetes-bootcamp`: delete a service

## K8S Objects
### Basic Conception
- node IP and external port: the public IP address and port of the node
- cluster IP and internal port: IP address for all the container within 1 pod, the port can be accessed inside the node
- container port: the service port in the container

### Label
we can attach labels to a resource

Label CMD
- `kubectl get pods --show-labels`: show labels
- `kubectl get pods -l run=kubernetes-bootcamp`: select with label `run=kubernetes-bootcamp`
- `kubectl get services -l run=kubernetes-bootcamp`: select with label `run=kubernetes-bootcamp`
- `kubectl label pod $POD_NAME app=v1`: add a lab

### Annotation
supplementary configuration, which will only be used by external applications


## Volume
- PersistentVolume
There are 3 types of PV

### PersistentVolumeClaim
PVC is used to create a PV which will be later declared and used in a pod.
- `kubectl apply -f mysql-pvc.yml`: create a PVC

### emptyDir
```
volumes:
  - name: cache-volume
    emptyDir: {}
```

### hostPath
```
volumes:
  - name: test-volume
    hostPath:
      path: /data   # directory location on host
```

### ConfigMap
- `mkdir mysql`
- `echo "[mysqld]" > mysql/my.cnf`
- `echo "[client]" > mysql/client.cnf`
- `kubectl create configmap mysql --from-file=mysql`
- `kubectl get configmap mysql`
- `kubectl describe cm mysql`

### Secret

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
- create 1 mysql deployment
  - `kubectl apply -f mysql-deployment.yml`
- create 1 mysql service
  - `kubectl apply -f mysql-service.yml`
- create 1 wordpress deployment
  - `kubectl apply -f wordpress-deployment.yml`
- create 1 wordpress service
  - `kubectl apply -f wordpress-service.yml`
- create 1 ingress LB
  - `minikube addons enable ingress`: install ingress
  - `echo "$(minikube ip) ingress.minikube" | sudo tee -a /etc/hosts`: add host name to /etc/hosts
  - `kubectl apply -f wordpress-ingress.yml`: create ingress
- create 2 persistent volumes
  - `/var/lib/mysql` for MySQL deployment
    - `kubectl apply -f mysql-pvc.yml`: create `mysql-pvc`
    - `kubectl apply -f mysql-deployment2.yml`
    - `kubectl apply -f mysql-service.yml`
  - `/var/www/html` for Wordpress deployment
    - `kubectl apply -f wordpress-pvc.yml`: create `wordpress-pvc`
    - `kubectl apply -f wordpress-deployment2.yml`
    - `kubectl apply -f wordpress-service.yml`
-



