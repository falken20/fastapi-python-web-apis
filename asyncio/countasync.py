# by Richi Rod AKA @richionline / falken20
# asyncio/countasync.py

import asyncio
import time


async def count():
    print("One")
    # The keyword await passes function control back to the event loop
    await asyncio.sleep(1)
    print("Two")


async def main():
    # it is a SyntaxError to use await outside of an async def coroutine
    # asyncio.gather is to run multiple asynchronous operations. Returns 
    # the results of awaitables as a tuple with the same order as you pass 
    # the awaitables to the function
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
