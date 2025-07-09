import streamlit as st
import asyncio
from main import get_team_and_docker
from config.docker_utils import start_docker_executor, stop_docker_executor
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage

st.title("DSA SOLVER")
st.write("A Simple DSA Solver Application")

async def run(team,task,docker):

    try:
        await start_docker_executor(docker)
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source}: {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:= f"Task Result: {message.stop_reason}")
                yield msg
            else:
                print(message)

    except Exception as e:
        print(f"Error occured: {e}")

    finally:
        await stop_docker_executor(docker)
        
task = st.text_area(
    "Enter a DSA Question here", 
    value="Can you give a solution to add 2 numbers."
    )

if st.button("Solve"):
    st.write("Solving your question")

    task = task
        
    async def collect_messages():
        team, docker = await get_team_and_docker()
        async for msg in run(team, task, docker):
            if msg.startswith('user'):
                with st.chat_message('user',avatar='👤'):
                    st.markdown(msg)
            elif msg.startswith('ProblemSolverExpert'):
                with st.chat_message('ProblemSolverExpert',avatar='🧑🏻‍💻') :
                    st.markdown(msg)
            elif msg.startswith('CodeExecutorAgent'):
                with st.chat_message('CodeExecutorAgent',avatar='🤖'):
                    st.markdown(msg)
            else:
                st.markdown(msg)

    asyncio.run(collect_messages())
