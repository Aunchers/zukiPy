from zukiPyModules.MainMods.zukiChat import zukiChat
from zukiPyModules.MainMods.zukiImage import zukiImage

class zukiCall:
  def __init__(self, api_key, model="gpt-3.5"):
    self.api_key = api_key
    self.model = model
    self.zuki_chat = zukiChat(api_key, model)
    self.zuki_image = zukiImage(api_key)