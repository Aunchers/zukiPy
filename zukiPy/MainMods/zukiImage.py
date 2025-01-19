from zukiPy.SubMods.zukiImageCall import zukiImageCall


class zukiImage:

    def __init__(self, api_key, api_key_backup=""):
        self.api_key = api_key
        self.api_endpoint = "https://zukijourney.xyzbot.net/v1/images/generations"
        self.api_endpoint_backup = "https://api.webraft.in/api/images/generations"
        self.api_caller = zukiImageCall(self.api_key)
        self.api_key_backup = api_key_backup
        self.api_caller_backup = zukiImageCall(self.api_key_backup)

    def change_backup_endpoint(self, endpoint):
        self.api_endpoint_backup = endpoint

    async def generateImage(self, prompt, generations=1, size=250, model = "flux-schnell"):
        imgUrl = await self.api_caller.image_call(prompt, generations, self.api_endpoint, model, negative_prompt="", width=1024, height=1024)
        if "details" in str(imgUrl):
            return ValueError(imgUrl)
        else:
            return imgUrl

    async def generateImageBackup(self, prompt, generations=1, size=250, model="flux-schnell"):
        imgUrl = await self.api_caller_backup.image_call(prompt, generations, self.api_endpoint_backup, model, negative_prompt="", width=1024, height=1024)
        if "details" in str(imgUrl):
            return ValueError(imgUrl)
        else:
            return imgUrl
