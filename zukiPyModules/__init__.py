from zukiPyModules.MainMods.zukiChat import zukiChat
from zukiPyModules.MainMods.zukiImage import zukiImage


class zukiCall:
    def __init__(self, api_key, api_key_backup="", model="gpt-3.5"):
        self.api_key = api_key
        self.api_key_backup = api_key_backup
        self.model = model
        self.zuki_chat = zukiChat(api_key, api_key_backup, model)
        self.zuki_image = zukiImage(api_key, api_key_backup)
