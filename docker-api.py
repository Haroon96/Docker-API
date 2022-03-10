from argparse import ArgumentParser
import docker
from time import sleep
import os
import requests

# change this to your own ID
IMAGE_NAME = 'haroon/docker-example'
# change this to output dir to mount to container
OUTPUT_DIR = os.path.join(os.getcwd(), 'output')
# set to current user
USERNAME = '%s:%s' % (os.getuid(), os.getgid())

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--build', action="store_true", help='Build docker image')
    parser.add_argument('--run', action="store_true", help='Run all docker containers')
    parser.add_argument('--simulate', action="store_true", help='Simulate container run')
    parser.add_argument('--max-containers', default=None, type=int, help="Maximum number of concurrent containers")
    parser.add_argument('--sleep-duration', default=60, type=int, help="Time to sleep (in seconds) when max containers are reached and before spawning additional containers")
    args = parser.parse_args()
    return args, parser

def build_image():
    # get docker client and build image
    client = docker.from_env()

    # build the image from the Dockerfile
    #   -> tag specifies the name
    #   -> rm specifies that delete intermediate images after build is completed
    client.images.build(path='.', tag=IMAGE_NAME, rm=True)

def get_mount_volumes():
    # binds "/output" on the container -> "OUTPUT_DIR" actual folder on disk

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # mapping format for binding OUTPUT_DIR to /output
    return { OUTPUT_DIR: { "bind": "/output"} }

def max_containers_reached(client, max_containers):
    try:
        return max_containers is not None and 
            len(client.containers.list()) >= max_containers
    except:
        return True

def spawn_containers(args):
    # get docker client
    client = docker.from_env()

    # get sample list of data to process
    r = requests.get("https://reqres.in/api/users")
    users = r.json()['data']
    
    # spawn containers for each user
    count = 0

    for user in users:
        # get userId
        userId = str(user['id'])

        # check for running container list
        while max_containers_reached(client, args.max_containers):
            # sleep for a minute if maxContainers are active
            print("Max containers reached. Sleeping...")
            sleep(args.sleep_duration)

        # spawn container if it's not a simulation
        if not args.simulate:
            print("Spawning container...")
            
            # set OUTPUT_DIR as "/output"
            command = ['python', 'main.py', userId, '/output']

            # run the container with these params
            #   -> command specifies the command to run
            #   -> volumes specifies which folders to mount and where
            #   -> shm_size specifies the memory of the container. 512M is sufficient for Chrome.
            #   -> detach specifies that the container should be spawned in the background
            #   -> remove specifies that the container should be deleted after it has completed
            client.containers.run(IMAGE_NAME, command, volumes=get_mount_volumes(), user=USERNAME, shm_size='512M', detach=True, remove=True)
        
        # increment count of containers
        count += 1

    print("Total containers spawned:", count)

def main():

    args, parser = parse_args()

    if args.build:
        print("Starting docker build...")
        build_image()
        print("Build complete!")

    if args.run:
        spawn_containers(args)

    if not args.build and not args.run:
        parser.print_help()


if __name__ == '__main__':
    main()
