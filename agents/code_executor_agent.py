from autogen_agentchat.agents import CodeExecutorAgent

def get_code_executor_agent(docker_executor):
    """
    Returns instance of CodeExecutorAgent to Execute code in Docker container.

    Returns:
        CodeExecutorAgent: Configured problem solver agent.
    """
    code_executor_agent = CodeExecutorAgent(
        name="CodeExecutorAgent",
        description="An agent that executes code in Docker container",
        code_executor=docker_executor,
    )

    return code_executor_agent