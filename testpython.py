"""
import asyncio
async def fn() :
    print("This is")
    await asyncio.sleep(1)
    print("a test")
    await asyncio.sleep(1)
    print("of async function")
asyncio.run(fn())
"""
"""
import asyncio
async def fn() :
    print("One")
    await asyncio.sleep(1)
    await fn2()
    print("Four")
    await asyncio.sleep(1)
    print("Five")
async def fn2() :
    print("Two")
    await asyncio.sleep(1)
    print("Three")
asyncio.run(fn())
"""
import asyncio
async def fn() :
    task=asyncio.create_task(fn2())
    print("One")
    print("Two")
    await asyncio.sleep(1)
    print("Three")
    await asyncio.sleep(1)
    print("Four")
    await asyncio.sleep(1)
async def fn2() :
    print("Five")
    await asyncio.sleep(1)
    print("Six")
    await asyncio.sleep(1)
    print("Seven")
asyncio.run(fn())

