import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app_runner = web.AppRunner(app)
    await app_runner.setup()
    srv = await loop.create_server(app_runner.server, '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(init(loop))
loop.run_forever()