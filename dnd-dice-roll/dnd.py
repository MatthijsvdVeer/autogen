import os
from typing_extensions import Annotated
from autogen import GroupChat
from autogen import GroupChatManager
import autogen
from dm import dm
from player1 import player1
from player2 import player2
from human_player import human_player


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
llm_config2 = {"config_list": [
    {
        "model": "gpt-4",
        "api_type": "azure",
        "api_key": "<FILL IN>",
        "base_url": "<URL HERE>",
        "api_version": "2024-02-15-preview",
        "temperature": 0.9,
    }
]}

diceroller = autogen.AssistantAgent(
    description="Roll a specific number of polyhedral dice, you can decide the number of faces. A number is returned.",
    name="diceroller",
    llm_config=llm_config,
    code_execution_config={
        'use_docker': False,
    }
)

# A function to roll a number of polyhedral dice
from random import randint
def roll_dice(number: int, sides: int) -> int:
    print(f"Rolling {number} {sides}-sided dice.")
    result = 0
    for i in range(number):
        result += randint(1, sides)
    return result

@dm.register_for_execution()
@player1.register_for_execution()
@player2.register_for_execution()
@human_player.register_for_execution()
@diceroller.register_for_llm(description="Roll a specific number of polyhedral dice, you can decide the number of faces. A number is returned.")
def dice_roller(
    number: Annotated[int, "how many dice you want to roll"],
    sides: Annotated[int, "how many sides the dice have"]
) -> str:
    result = roll_dice(int(sides))
    print(result)
    return f"{result}"




group_chat = GroupChat(
    agents=[dm, player1, player2, human_player],
    messages=[],
    max_round=160,
    send_introductions=True
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config2
)

chat_result = dm.initiate_chat(
    group_chat_manager,
    message="Welcome to our first session. Like all good adventures, we start in a tavern. You are all sitting at a table in the corner of the tavern. The tavern is full of people, and the barkeep is busy. What do you do?",
    summary_method="reflection_with_llm",
)
