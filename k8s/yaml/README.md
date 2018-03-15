# YAML Configuration
## Execution
- `kubectl apply -f $FILE_ID.yaml`: create a resource through YAML file
- `kubectl delete -f $FILE_ID.yaml`: delete a resource through YAML file


## Meta-data
- `apiVersion`: k8s API version
- `kind`: resource type
- `meta-data`: pre-defined meta-data
  - `name`
  - `lables`
  - `annotations`
- `spec`: parameters for different resource type


## container
- `container`:
  - `name`:
  - `image`
  - `ports`
    - `containerPort`