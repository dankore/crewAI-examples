import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from tasks import GameTasks
from agents import GameAgents
import datetime

# Ensure the games directory exists
if not os.path.exists('games'):
    os.makedirs('games')

tasks = GameTasks()
agents = GameAgents()

print("## Welcome to the Game Crew")
print('-------------------------------')
game = input("What is the game you would like to build? What will be the mechanics?\n")

# Create Agents
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# Create Tasks
code_game = tasks.code_task(senior_engineer_agent, game)
review_game = tasks.review_task(qa_engineer_agent, game)
approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

# Create Crew responsible for Copy
crew = Crew(
    agents=[
        senior_engineer_agent,
        qa_engineer_agent,
        chief_qa_engineer_agent
    ],
    tasks=[
        code_game,
        review_game,
        approve_game
    ],
    verbose=True
)

def clean_code_output(code):
    # Remove enclosing backticks if present
    if code.startswith("```") and code.endswith("```"):
        code = code[3:-3].strip()
    
    # Additional cleaning steps if necessary
    code = code.replace("```python", "").replace("```", "").strip()
    
    return code

try:
    game_code = crew.kickoff()
    game_code = clean_code_output(game_code)

    # Debug: Print the cleaned game code
    print("Cleaned game code:\n")
    print(game_code)
    print("\nEnd of cleaned game code\n")

    # Generate a unique filename based on the game description
    game_type = game.split()[0].lower().replace(':', '').replace(' ', '_')
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"games/{game_type}_{timestamp}.py"

    # Write the game code to the uniquely named file
    with open(filename, 'w') as file:
        file.write(game_code)

    # Print results
    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print(f"Final code for the game has been written to {filename}")
except Exception as e:
    print("An error occurred during the kickoff process:")
    print(e)
