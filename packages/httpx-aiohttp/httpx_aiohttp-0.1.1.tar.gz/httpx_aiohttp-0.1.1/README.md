
<p align="center"><strong>httpx-aiohttp</strong> <em>- provides transports for httpx to work on top of aiohttp, handling all high-level features like authentication, retries, and cookies through httpx, while delegating low-level socket-level HTTP messaging to aiohttp</em></p>

<p align="center">

  <a href="https://pypi.org/project/httpx-aiohttp">
      <img src="https://img.shields.io/pypi/v/httpx-aiohttp.svg" alt="pypi">
  </a>

  <a href="https://img.shields.io/pypi/l/httpx-aiohttp">
      <img src="https://img.shields.io/pypi/l/httpx-aiohttp" alt="license">
  </a>
</p>

## Installation

```shell
uv pip install httpx-aiohttp
```

## Examples

### Basic GET request

```python
import asyncio
import httpx
from httpx_aiohttp import AiohttpTransport
from aiohttp import ClientSession


async def main() -> None:
    async with AiohttpTransport(client=ClientSession()) as aiohttp_transport:
        httpx_client = httpx.AsyncClient(transport=aiohttp_transport)
        response = await httpx_client.get("https://www.encode.io")
        print(response)  # <Response [200]>


asyncio.run(main())
```

### Timeouts

```python
import asyncio
import httpx
from httpx_aiohttp import AiohttpTransport
from aiohttp import ClientSession


async def main() -> None:
    async with AiohttpTransport(client=ClientSession()) as aiohttp_transport:
        httpx_client = httpx.AsyncClient(transport=aiohttp_transport)
        response = await httpx_client.get("https://www.encode.io", timeout=httpx.Timeout(
            connect=5.0,
            read=5.0,
            pool=5.0,
            write=None  # Does not support for aiohttp transport
        ))
        print(response)  # <Response [200]>


asyncio.run(main())
```

### Proxies

```python
import asyncio
import httpx
from httpx_aiohttp import AiohttpTransport
from aiohttp import ClientSession


async def main() -> None:
    async with AiohttpTransport(
        client=ClientSession(proxy="https://my-lovely-proxy")
    ) as aiohttp_transport:
        httpx_client = httpx.AsyncClient(
            transport=aiohttp_transport,
            mounts={"all://": AiohttpTransport(client=ClientSession())},
        )
        response = await httpx_client.get("https://www.encode.io")
        print(response)  # <Response [200]>


asyncio.run(main())
```
