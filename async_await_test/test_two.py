"""
    测试协程的执行和同步效果
"""
import asyncio
import time


async def fun(name,delay):
    print(f'任务{name}开始')
    await asyncio.sleep(delay)
    print(f'任务{name}完成')
    return f'任务{name}结果'

# async def main():
#     await fun("A",1)
#     await fun("B", 2)

# async def main():
#     task1=asyncio.create_task(fun("A",1))
#     task2=asyncio.create_task(fun("B", 2))
#     #results中保存的是每个并发执行的任务的返回值
#     results=await  asyncio.gather(task1,task2)
#     print(results)

# async def main():
#     results=await  asyncio.gather(
#         fun("A",1)
#         ,fun("B", 2)
#     )
#     print(results)

async def main():
    asyncio.create_task(fun("A", 1))
    asyncio.create_task(fun("B", 2))


if __name__== "__main__":
    start_time=time.time()
    asyncio.run(main())
    print(f'耗时{time.time()-start_time}')






