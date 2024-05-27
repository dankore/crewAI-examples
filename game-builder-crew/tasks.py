from textwrap import dedent
from crewai import Task

class GameTasks:
    def code_task(self, agent, game):
        return Task(
            description=dedent(f"""\
                You will create a game using Python. Follow the instructions below:

                Instructions
                ------------
                {game}

                Your final answer must be the complete Python code, with no additional text.
            """),
            agent=agent
        )

    def review_task(self, agent, game):
        return Task(
            description=dedent(f"""\
                You are assisting in the creation of a game using Python. Follow the instructions below:

                Instructions
                ------------
                {game}

                Review the provided code for errors, including:
                - Logic errors
                - Syntax errors
                - Missing imports
                - Variable declarations
                - Mismatched brackets
                - Security vulnerabilities

                Your final answer must be the corrected Python code, with no additional text.
            """),
            agent=agent
        )

    def evaluate_task(self, agent, game):
        return Task(
            description=dedent(f"""\
                You are evaluating the creation of a game using Python. Follow the instructions below:

                Instructions
                ------------
                {game}

                Ensure that the code is complete and performs its intended functions correctly.

                Your final answer must be the evaluated Python code, with no additional text.
            """),
            agent=agent
        )
