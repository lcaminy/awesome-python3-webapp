#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

async def init(loop): # async 替代 @asyncio.coroutine装饰器,代表这个是要异步运行的函数
    app=web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '0.0.0.0', 5000)  #await 代替yield from ,表示要放入asyncio.get_event_loop中进行的异步操作
    logging.info('server started at http://127.0.0.1:5000...')
    return srv

loop = asyncio.get_event_loop()  #创建asyncio event loop 
try:
    loop.run_until_complete(init(loop)) #用asyncio event loop 来异步运行init()
    loop.run_forever()
except OSError:
    stop()
    logging.info('端口被占用！停止服务')
else:
    stop()




# @asyncio.coroutine
# def init(loop):# async 替代 @asyncio.coroutine装饰器,代表这个是要异步运行的函数
# 	app = web.Application(loop=loop)
# 	app.router.add_route('GET','/',index)
# 	srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000) #await 代替yield from ,表示要放入asyncio.get_event_loop中进行的异步操作
# 	logging.info('server started at http://127.0.0.1:9000 ...')
# 	return srv

# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()


