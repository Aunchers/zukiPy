from zukipy.SubMods.zukiImageCall import zukiImageCall

class zukiImage:
  def __init__(self, api_key):
    self.api_key = api_key
    self.api_endpoint = "https://zukijourney.xyzbot.net/v1/images/generations"
    self.api_caller = zukiImageCall(self.api_key)
  async def generateImage(prompt, generations=1, size=250):
    return self.api_caller.image_call(prompt, generations, size, self.api_endpoint)
  

  