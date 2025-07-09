from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination


def get_team(problem_solver_expert, code_executor_agent):

    """
    Returns a RoundRobinGroupChat team configured with the provided agents and termination condition.
    """

    termination_condition = TextMentionTermination("STOP")
    
    team = RoundRobinGroupChat(
    participants=[problem_solver_expert, code_executor_agent],
    termination_condition=termination_condition,
    max_turns=10,
    )

    return team