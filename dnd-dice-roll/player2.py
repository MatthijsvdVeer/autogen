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

player2 = AssistantAgent(
        "matt",
        system_message="Your name is Matt and you're a human Bard. You are a smooth talker and a good singer. You are not very good at fighting, but you are good at talking. You are loyal to your friends and you are always ready to talk your way out of a fight.",
        llm_config=llm_config,
        human_input_mode="NEVER",  # Never ask for human input.
)
