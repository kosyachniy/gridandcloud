import docker


def get_new_container():
    client = docker.from_env()
    container = client.containers.run(client.images('worker_dockerfile')) # TODO: specify normal filename



