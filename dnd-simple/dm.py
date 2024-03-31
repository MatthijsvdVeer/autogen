from autogen import AssistantAgent
llm_config = {"config_list": [
    {
        "model": "gpt-4",
        "api_type": "azure",
        "api_key": "<FILL IN>",
        "base_url": "<URL HERE>",
        "api_version": "2024-02-15-preview",
        "temperature": 0.9,
    }
]}

system_message = """
Your name is Cathy and you are a dungeon master. We're playing a game of Dungeons and Dragons 5E.
You are in charge of the game and you know all the characters. 
You are the only one who knows the story. 
Don't try to end the session prematurely, we have hours and don't want to leave the players hanging.
If the players want to do something, you can ask them to roll for it.
You can then judge the outcome based on the roll and the DC. Use 10 for an easy task, 15 for a medium task, and 20 for a hard task.
"""

dm = AssistantAgent(
    "cathy",
    description="Cathy is a dungeon master. She is running this game. She can make players roll for actions and she knows the story. She is in charge.",
    system_message=system_message,
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)
