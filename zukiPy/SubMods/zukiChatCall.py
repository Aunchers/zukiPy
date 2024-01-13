import requests
import json


class zukiChatCall:
    def __init__(self, api_key):
        self.api_key = api_key

    def chat_data(self, userName, userMessage, requestedModel, systemPrompt, currTemp):
        data = {
            "model": requestedModel,
            "messages": [
                {
                    "role": "system",
                    "content": systemPrompt,
                },
                {
                    "role": "user",
                    "content": systemPrompt + '\n Here is a message a user called ' + userName + ' sent you: ' + userMessage,
                },
            ],
            "temperature": currTemp,
        }

        return data

    async def chat_call(self, userName, userMessage, requestedModel, systemPrompt, currTemp, endpoint):

        try:
            response = requests.post(endpoint, headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.api_key}'
            },

                data=json.dumps(self.chat_data(userName, userMessage, requestedModel, systemPrompt, currTemp)))
            responseData = response.json()
            return responseData['choices'][0]['message']['content']
        except Exception as e:
            print(f"An error occurred: {e}")
