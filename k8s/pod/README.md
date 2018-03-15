# Pod
Atomic unit in k8s, *it always runs on 1 node*.
- computing: 1 or N containers, but the number of containers within 1 pod is fixed
- storage: all containers in 1 pod have the same mount point, can access the same shared volume
- networking: all the containers in 1 pod use a unique IP address, communicate with one another using `localhost`
- scalability: increase or decrease the number of pods

## CMD
- `kubectl get pods`: list pods
- `kubectl describe pods`: describe pods
- `kubectl create -f $POD_ID.yml`: launch a pod
- `kubectl delete pod $POD_ID` or `kubectl delete -f $POD_ID.yml`: delete pod
- `kubectl exec $POD_ID CMD -c $CONTAINTER_ID`: run a cmd in a container of the pod
  - `kubectl exec $POD_ID env`: list environment variables in the pod
  - `kubectl exec -ti $POD_ID bash`: launch a `bash`
  - `kubectl exec -ti $POD_ID curl localhost:8080`: internal access

## YAML
[example](pod.yml)

- spec
  - container:
  - nodeSelector: to choose node to launch pods
