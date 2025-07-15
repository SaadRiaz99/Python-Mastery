# Python Async/Await

import asyncio
import time

# Basic async function
async def say_hello():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

# Run async function
asyncio.run(say_hello())

# Multiple async tasks
async def fetch_data(name, delay):
    print(f'Fetching {name}...')
    await asyncio.sleep(delay)
    print(f'Got {name}!')
    return f'{name} data'

async def main():
    # Sequential (slow)
    start = time.time()
    await fetch_data('A', 2)
    await fetch_data('B', 2)
    print(f'Sequential: {time.time() - start:.2f}s')

    # Parallel (fast)
    start = time.time()
    task1 = asyncio.create_task(fetch_data('C', 2))
    task2 = asyncio.create_task(fetch_data('D', 2))
    result1 = await task1
    result2 = await task2
    print(f'Parallel: {time.time() - start:.2f}s')
    print(f'Results: {result1}, {result2}')

asyncio.run(main())

# Gather multiple tasks
async def process(name, delay):
    await asyncio.sleep(delay)
    return f'{name} done'

async def main_gather():
    tasks = [process(f'Task {i}', 1) for i in range(5)]
    results = await asyncio.gather(*tasks)
    return results

results = asyncio.run(main_gather())
print(f'All results: {results}')

# Async with timeout
async def slow():
    await asyncio.sleep(10)
    return 'slow done'

async def main_timeout():
    try:
        result = await asyncio.wait_for(slow(), timeout=2)
    except asyncio.TimeoutError:
        print('Timed out!')

asyncio.run(main_timeout())

