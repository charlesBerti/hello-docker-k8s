# Installation

## Auto-Install
- through a script: `curl https://get.docker.com/|sh`

## No-Root Configuration
- `sudo groupadd docker`
- `sudo usermod -aG docker $USER`

## Test
- `docker run hello-world`

## Bug
### Cannot load hosts in configuration json file when starting docker daemon
- `vim /lib/systemd/system/docker.service`
- `ExecStart=/usr/bin/dockerd`
- `# -H fd://`
