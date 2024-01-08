import requests
class zukiImageCall:
  def __init__(self, api_key):
    self.api_key = api_key
  def image_data(self, prompt, generations, size):
    data = {
      "prompt": prompt,
      "n": generations,
      "size": size
    }
    return data

  async def image_call(self, prompt, generations, size, endpoint):
    try:
      response = requests.post(endpoint, headers={
         'Content-Type': 'application/json',
         'Authorization': f'Bearer {self.api_key}'
      },
      data=self.image_data(prompt, generations, size))
      imgUrl = response.json()
      return imgUrl['data'][0]['url']
      
    except Exception as e:
      print(f"An error occurred: {e}")