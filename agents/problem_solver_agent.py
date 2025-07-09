from autogen_agentchat.agents import AssistantAgent

def get_problem_solver_expert(model_client):
    """
    Returns instance of ProblemSolverExpert Agent to solver DSA Problems.

    Returns:
        AssistantAgent: Configured problem solver agent.
    """

    problem_solver_expert = AssistantAgent(
        name="ProblemSolverAgent",
        description="An expert agent that solves problem using code executor.",
        model_client=model_client,
        system_message="""

        You are an problem solving agent That is expert in solving DSA Problems.
        You will be working with code executor agent to execute code. 
        You will be given a task and you should first provide a way to solve the task/problem.
        Then you should give the code in python block format, so that it can be ran by code executor agent. 
        You should only give a single code block and pass it to executor agent.
        You should give the corrected code in python block format If error is there.
        Once the code has been successfully executed You have the results, You should explain the result in detail.
        Make sure that each code has 10(Ten) test cases and the output of each test case is printed.
        If You have to save any file, save it in .txt or .png format
        Once everything is done you should explain the result and should say "STOP" to stop the conversation.
        """,
    )

    return problem_solver_expert
