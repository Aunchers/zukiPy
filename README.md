
# zukiPy

`zukiPy` is a Python wrapper for the `zukijourney` API. The wrapper is made by **1_aunchers**, heavily referencing the `zukijs` wrapper by **Saberstexx**.

## Installation

To install `zukiPy`, simply run:
```python
pip install git+https://github.com/Launchers-1/zukipy
```
## Usage

Here's an example of how to use `zukiPy`:

```python
import zukiPy
import asyncio

api_key ="{your-api-key}" #Get your API key from discord.gg/zukijourney
zukiAI = zukiPy.zukiCall(api_key)


async def main():
  chatresponse = await zukiAI.zuki_chat.sendMessage("Launchers", "Hello")
  print("Chat Response:", chatresponse)


# You also need to run the async function
asyncio.run(main())
```

## Credits

- `zukiPy` wrapper: **1_aunchers**
- `zukijs` wrapper: **Saberstexx**
- `zukijourney` API: **zukixa**
