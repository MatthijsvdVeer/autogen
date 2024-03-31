from autogen import ConversableAgent
from autogen import GroupChat
from autogen import GroupChatManager

llm_config = {"config_list": [
    {
        "model": "gpt-3.5-turbo",
        "api_type": "azure",
        "api_key": "<FILL IN>",
        "base_url": "<URL HERE>",
        "api_version": "2024-02-15-preview",
        "temperature": 0.9,
    }
]}
llm_config2 = {"config_list": [
    {
        "model": "gpt-3.5-turbo",
        "api_type": "azure",
        "api_key": "<FILL IN>",
        "base_url": "<URL HERE>",
        "api_version": "2024-02-15-preview",
        "temperature": 0.9,
    }
]}


# create 100 conversableagents with random names
conversable_agents = []
for i in range(10):
    conversable_agents.append(ConversableAgent(
        "random_name_" + str(i),
        system_message="Your are in a panel discussion Your only job is to disagree with the everyone else. Explain why you disagree. You will never agree to disagree. You cannot agree. Disagree always.",
        llm_config=llm_config,
        human_input_mode="NEVER",  # Never ask for human input.
    ))
    
# create a group chat with the conversable agents
group_chat = GroupChat(
    agents=conversable_agents,
    messages=[],
    max_round=100,
    send_introductions=True
)

# group chat manager
group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config2
)

chat_result = conversable_agents[1].initiate_chat(
    group_chat_manager,
    message="The earth is round.",
    summary_method="reflection_with_llm",
)

# save the result
with open("chat_result.json", "w") as f:
    f.write(chat_result)
