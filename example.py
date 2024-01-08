import zukiPy
import asyncio
import os

api_key = os.environ['APIKEY']
zukiAI = zukiPy.zukiCall(api_key)


async def main():
  chatresponse = await zukiAI.zuki_chat.sendMessage("Launchers", "Hello")
  print("Chat Response:", chatresponse)
  imageresponse = await zukiAI.zuki_image.generateImage("Horror version of Garfield the Cat",1,) # options generateImage(prompt, generations, model, negative_prompt height, width)
  print("\n Image Response:", imageresponse)


# You also need to run the async function
asyncio.run(main())

#Hey 1_aunchers(creator of this) here. This is made by heavily referencing Sabsterrexx. You can find him @ https://replit.com/Sabsterrexx2
