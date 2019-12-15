import docker


def get_new_container():
    client = docker.from_env()
    return client.containers.run(client.images('dockerfile_fake_worker'))  # TODO: specify normal filename



