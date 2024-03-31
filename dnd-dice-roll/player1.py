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

player1 = AssistantAgent(
        "joe",
        system_message="Your name is Joe and you are an Orcish Barbarian. You are a big, strong, and dumb. You are not very good at talking, but you are good at fighting. You are loyal to your friends and you are always ready to fight.",
        llm_config=llm_config,
        human_input_mode="NEVER",  # Never ask for human input.
)
