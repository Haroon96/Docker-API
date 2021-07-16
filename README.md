# Docker Example
## Contents
- `Dockerfile`: Contains instructions for docker to build the image
- `docker-api.py`: Contains a high-level API for common docker commands
- `src`: Contains source code that is to be run inside the container

## Usage
```
usage: docker-api.py [-h] [--build] [--runAll] [--simulate]
                     [--max-containers MAX_CONTAINERS]
                     [--sleep-duration SLEEP_DURATION]

optional arguments:
  -h, --help            show this help message and exit
  --build               Build docker image
  --runAll              Run all docker containers
  --simulate            Simulate container run
  --max-containers MAX_CONTAINERS
                        Maximum number of concurrent containers
  --sleep-duration SLEEP_DURATION
                        Time to sleep (in seconds) when max containers are
                        reached and before spawning additional containers
```