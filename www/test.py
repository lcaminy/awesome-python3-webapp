import asyncio,orm
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop,user='root', password='root', db='awesome')
    u = User(name='zj', email='12323@example.com', passwd='12312312312', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
# loop.close()