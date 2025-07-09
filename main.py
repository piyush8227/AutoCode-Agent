import asyncio
from teams.dsa_solver_team import get_team
from agents.code_executor_agent import get_code_executor_agent
from agents.problem_solver_agent import get_problem_solver_expert
from config.model_client import get_model_client
from config.docker_utils import get_docker_executor, start_docker_executor, stop_docker_executor
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage

async def get_team_and_docker():

    docker = get_docker_executor()
    model_client = get_model_client()
    problem_solver_agent = get_problem_solver_expert(model_client)
    code_executor_agent = get_code_executor_agent(docker)
    team = get_team(problem_solver_agent, code_executor_agent)

    return team, docker

async def run_team(docker, team, task):

    try:
        await start_docker_executor(docker)

        async for message in team.run_stream(task=task):
            print("-"*100)

            if isinstance(message, TextMessage):
                print(msg:= f"{message.source}: {message.content}")
            
            elif isinstance(message, TaskResult):
                print(msg:= f"Task Result: {message.stop_reason}")
            
            else:
                print(message)
            print("="*100)
    except Exception as e:
        print(f"Error occured: {e}")

    finally:
        await stop_docker_executor(docker)


async def main():
    team, docker = await get_team_and_docker()
    task = """Give code for prime number"""
    await run_team(task, team, docker)

if __name__ == "__main__":
    asyncio.run(main())
    print("Code executor agent ran successfully")