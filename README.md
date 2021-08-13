# Docker Example
This is an example project that demonstrates building a Docker image for Selenium crawling and spawning multiple parallel containers with an option for limiting the maximum number of concurrently running containers. I use this to manage multiple Docker containers.

## Contents
- `Dockerfile`: Contains instructions for docker to build the image
- `docker-api.py`: Contains a high-level API for common docker commands
- `src`: Contains the actual source code that is to be run inside the container

## Usage
```
usage: docker-api.py [-h] [--build] [--run] [--simulate] [--max-containers MAX_CONTAINERS] [--sleep-duration SLEEP_DURATION]

optional arguments:
  -h, --help            show this help message and exit
  --build               Build docker image
  --run                 Run all docker containers
  --simulate            Simulate container run
  --max-containers MAX_CONTAINERS
                        Maximum number of concurrent containers
  --sleep-duration SLEEP_DURATION
                        Time to sleep (in seconds) when max containers are reached and before spawning additional containers
```
