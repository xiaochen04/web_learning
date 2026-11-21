"""
    测试创建协程对象
"""
import asyncio


async def fun():
    print("hello")
    await asyncio.sleep(1)
    print("world")
print(fun())

coro_obj = fun()
print(type(coro_obj))






