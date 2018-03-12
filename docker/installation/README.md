# Installation

## Auto-Install
- through a script: `curl https://get.docker.com/|sh`

## New Installation
```bash
sudo apt-get remove docker docker-engine docker.io
sudo apt-get remove docker-compose
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce
```
Test: `docker run hello-world`

## No-Root Configuration
- `sudo groupadd docker`
- `sudo usermod -aG docker $USER`
- logout and then login to take effect

## docker-compose Installation
```bash
sudo apt-get install python-pip
sudo pip install docker-compose
```
## Chinese docker hub mirrors
```bash
sudo vi /etc/docker/daemon.json
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
}
systemctl daemon-reload
systemctl restart docker
```

## Bug
### Failed to start Docker Application Container Engine
Cannot load hosts in configuration json file when starting docker daemon
- `vim /lib/systemd/system/docker.service`
- `ExecStart=/usr/bin/dockerd`
- `# -H fd://`

