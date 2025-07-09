from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import DOCKER_TIMEOUT, DOCKER_WORK_DIR

def get_docker_executor():
    """
    Returns a DockerCommandLineCodeExecutor instance configured with the specified work directory and timeout.

    Returns:
        DockerCommandLineCodeExecutor: Configured Docker Command Line Code Executor
    """

    docker_executor = DockerCommandLineCodeExecutor(
        work_dir=DOCKER_WORK_DIR,
        timeout=DOCKER_TIMEOUT
    )

    return docker_executor

async def start_docker_executor(docker_executor):
    """
    Starts Docker Command Line Code Executor
    """

    await docker_executor.start()
    print("Docker Command Line Code Executor Started.")

async def stop_docker_executor(docker_executor):
    """
    Stops Docker Command Line Code Executor

    """
    await docker_executor.stop()
    print("Docker Command Line Code Executor Stopped.")