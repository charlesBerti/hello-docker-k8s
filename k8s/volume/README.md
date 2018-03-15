# Volume & ConfigSet & Secret

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

## ConfigMap
- `mkdir mysql`
- `echo "[mysqld]" > mysql/my.cnf`
- `echo "[client]" > mysql/client.cnf`
- `kubectl create configmap mysql --from-file=mysql`
- `kubectl get configmap mysql`
- `kubectl describe cm mysql`

## Secret