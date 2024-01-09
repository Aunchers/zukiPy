import requests

class zukiImageCall:
  def __init__(self, api_key):
    self.api_key = api_key
  def image_data(self, prompt, generations, model, negative_prompt, width, height):
    data = {
      "prompt": prompt,
      "n": generations,
      "size": str(width) + "x" + str(height),
      "model": model,
      "negative_prompt": negative_prompt,
      "width": width,
      "height": height
    }
    return data

  async def image_call(self, prompt, generations, endpoint, model, negative_prompt, width, height):
   try:
       response = requests.post(endpoint, headers={
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {self.api_key}'
       },
       json=self.image_data(prompt, generations, model, negative_prompt, width, height))
       imgUrl = response.json()
       if 'detail' in imgUrl:
           raise ValueError(imgUrl)
       else:
           return imgUrl['data'][0]['url']

   except Exception as e:
       print(f"An error occurred: {e}")
       raise

