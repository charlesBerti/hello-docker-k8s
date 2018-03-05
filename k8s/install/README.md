# Installation

## kubectl
### Installation
- `curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl`
- or `curl -O https://storage.googleapis.com/kubernetes-release/release/v1.8.0/bin/linux/amd64/kubectl`
- `chmod +x ./kubectl`
- `sudo mv ./kubectl /usr/local/bin/kubectl`
- `echo "source <(kubectl completion bash)" >> ~/.bashrc`: auto-completion in bashrc
- `kubectl cluster-info`: check

# minikube
## Installation
- `sudo apt-get update && sudo apt-get install -y curl virtualbox`
- `curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.24.1/minikube-linux-amd64`
- `chmod +x minikube`
- `sudo mv minikube /usr/local/bin/`
- `minikube start --memory 8192 --kubernetes-version v1.8.0`
- `minikube dashboard`: check

## CMD
- `minikube ip`: IP address of the minikube node
- `minikube ssh`: ssh to minikube

## kubeadm


