from autogen import ConversableAgent
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

human_player = AssistantAgent(
        "kate",
        system_message="Your name is Kate and you are a human Wizard. You are not very good at fighting, but you are good at magic. You are loyal to your friends and you are always ready to cast a spell.",
        llm_config=llm_config,
        human_input_mode="ALWAYS",  # Always ask for human input.
)
