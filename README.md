
# zukipy

`zukipy` is a Python wrapper for the `zukijourney` API. The wrapper is made by **1_aunchers**, heavily referencing the `zukijs` wrapper by **Saberstexx**.

## Installation

To install `zukipy`, simply run:

```python
pip install zukipy
```
```python
#not available atm. you can currently use it by downloading the folder into your project. Will be added to PyPi in the future
```
## Usage

Here's an example of how to use `zukipy`:

```python
import zukipy
import asyncio

api_key ="{your-api-key}" #Get your API key from discord.gg/zukijourney
zukiAI = zukipy.zukiCall(api_key)


async def main():
  chatresponse = await zukiAI.zuki_chat.sendMessage("Launchers", "Hello")
  print("Chat Response:", chatresponse)


# You also need to run the async function
asyncio.run(main())
```

## Credits

- `zukipy` wrapper: **1_aunchers**
- `zukijs` wrapper: **Saberstexx**
- `zukijourney` API: **zukixa**
