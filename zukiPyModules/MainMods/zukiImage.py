from zukiPyModules.SubMods.zukiImageCall import zukiImageCall

class zukiImage:
  def __init__(self, api_key):
    self.api_key = api_key
    self.api_endpoint = "https://zukijourney.xyzbot.net/v1/images/generations"
    self.api_caller = zukiImageCall(self.api_key)
  async def generateImage(self, prompt, generations=1, size=250):
    imgUrl = await self.api_caller.image_call(prompt, generations, self.api_endpoint, model="SDXL", negative_prompt="", width=1024, height=1024)
    if "details" in str(imgUrl):
      return ValueError(imgUrl)
    else:
      return imgUrl
  

  
