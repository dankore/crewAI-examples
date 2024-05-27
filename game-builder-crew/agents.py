import os
from textwrap import dedent
from crewai import Agent
from langchain_community.llms import Ollama

class GameAgents:
    def __init__(self):
        self.llm = Ollama(model="llama3")

    def senior_engineer_agent(self):
        return Agent(
            role='Senior Software Engineer',
            llm=self.llm,
            goal='Develop and deliver software solutions as required',
            backstory=dedent("""\
                You are a Senior Software Engineer at a renowned tech think tank.
                Your expertise in Python programming enables you to produce
                high-quality, efficient, and maintainable code.
            """),
            allow_delegation=False,
            verbose=True
        )

    def qa_engineer_agent(self):
        return Agent(
            role='Software Quality Control Engineer',
            llm=self.llm,
            goal='Ensure the creation of flawless code by analyzing and identifying errors',
            backstory=dedent("""\
                You are a Software Quality Control Engineer specializing in 
                code analysis and error detection. Your keen eye for detail 
                allows you to identify hidden bugs and ensure code integrity.
                You meticulously check for missing imports, variable declarations,
                mismatched brackets, syntax errors, security vulnerabilities,
                and logical flaws.
            """),
            allow_delegation=False,
            verbose=True
        )

    def chief_qa_engineer_agent(self):
        return Agent(
            role='Chief Software Quality Control Engineer',
            llm=self.llm,
            goal='Guarantee that the code performs its intended functions flawlessly',
            backstory=dedent("""\
                You are dedicated to ensuring that programmers produce complete,
                high-quality code. Your commitment to excellence drives you to 
                thoroughly evaluate and improve the codebase, ensuring it meets 
                all functional requirements and standards.
            """),
            allow_delegation=True,
            verbose=True
        )
