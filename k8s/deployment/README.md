# Deployment
Deployment changes the actual state to the desired state at a controlled rate.
It manages N pods through a ReplicaSet.
- docker image update
  - rolling update: create a new deploy to increase and decrease the old one
- scaling: change the number of pod replicas in a deployment.
- patterns:
  - sidecar
  - ambassador
  - adapter

## CMD
- `kubectl get deployments`: list deployments
- `kubectl run nginx --image=nginx --port=80 --replicas=3`: create a deploymet
- `kubectl create -f deployment.yml`: create a deployment
- `kubectl rollout status deployment $DEP_ID`: set rollout status
- `kubectl edit deployment $DEP_ID`: edit deployment
- `kubectl set image deployment $DEP_ID nginx=nginx:1.9.1`: update image
- `kubectl scale deployments $DEP_ID --replicas=4`: scale out

## YAML
[Deployment YAML example](deployment.yml)

- `deployment spec`
  - `replicas`
  - `template`: parameters for the sub-resource type, e.g. the sub-resource of deployment is pod


# ReplicaSet
ReplicaSet ensures a fixed number of running pods through selector which is the next generation of ReplicaController.
*It is recommended to be replaced by Deployment.*

- `kubectl create -t $REPLICASET_ID`: create replicaset
- `kubectl get replicasets`: list replicasets
- `kubectl delete replicasets $REPLICASET_ID`: delete replicaset

## YAML
[ReplicaSet YAML example](replicaset.yml)
