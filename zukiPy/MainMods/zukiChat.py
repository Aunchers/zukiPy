from zukiPy.SubMods.zukiChatCall import zukiChatCall


class zukiChat:

    def __init__(self, api_key, api_key_backup="", model="gpt-3.5", systemPrompt="You are a helpful assistant.", temperature=0.7):
        self.api_key = api_key
        self.api_endpoint = "https://zukijourney.xyzbot.net/v1/chat/completions"
        self.api_endpoint_unfiltered = "https://zukijourney.xyzbot.net/unf/chat/completions"
        # A backup endpoint, if appplicable. Usually meant to utilize another API. By default it's set to the WebRaft API due to its rate limit being ideal for testing purposes.
        # Get key @https://discord.gg/XwxUdHhF59
        self.api_endpoint_backup = 'https://thirdparty.webraft.in/v1/chat/completions'

        self.systemPrompt = systemPrompt
        modelsList = ['gpt-3.5-turbo', 'gpt-3.5-turbo-instruct', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k', 'gpt-4-1106-preview', 'gpt-4-0125-preview', 'gpt-4-vision-preview', 'claude', 'claude-2', 'claude-2.1', 'claude-instant-v1', 'claude-instant-v1-100k', 'pplx-70b-online', 'palm-2', 'bard', 'gemini-pro', 'gemini-pro-vision', 'mixtral-8x7b', 'mixtral-8x7b-instruct', 'mistral-tiny', 'mistral-small', 'mistral-medium', 'mistral-7b-instruct', 'codellama-7b-instruct', 'llama-2-7b', 'llama-2-70b-chat', 'mythomax-l2-13b-8k', 'sheep-duck-llama', 'goliath-120b', 'nous-llama2', 'yi-34b', 'openchat', 'solar10-7b', 'pi']

        self.api_key_backup = api_key_backup

        if (model in modelsList):
            self.model = model
        else:
            raise ValueError(
                "Invalid model. Please choose from the following: " + str(modelsList))

        self.temperature = temperature

    def change_backup_endpoint(self, endpoint):
        self.api_endpoint_backup = endpoint

    def setSystemPrompt(self, systemprompt):
        if (isinstance(systemprompt, str)):
            self.systemPrompt = systemprompt
        else:
            raise ValueError("System prompt must be a string")

    def setTemp(self, newTemp):
        if (0 <= newTemp <= 1):
            self.temperature = newTemp
        else:
            raise ValueError("Temperature must be between 0 and 1")

    async def sendMessage(self, userName, userMessage):
        return await zukiChatCall(self.api_key).chat_call(userName, userMessage, self.model, self.systemPrompt, self.temperature, self.api_endpoint)

    async def sendUnfilteredMessage(self, userName, userMessage):
        return await zukiChatCall(self.api_key).chat_call(userName, userMessage, self.model, self.systemPrompt, self.temperature, self.api_endpoint_unfiltered)

    async def sendBackupMessage(self, userName, userMessage):
        return await zukiChatCall(self.api_key_backup).chat_call(userName, userMessage, self.model, self.systemPrompt, self.temperature, self.api_endpoint_backup)
