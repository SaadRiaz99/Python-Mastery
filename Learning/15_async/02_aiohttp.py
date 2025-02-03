# Async HTTP Patterns

import asyncio

# Simulated async HTTP
async def fetch(url):
    print(f'Fetching {url}...')
    await asyncio.sleep(1)
    return f'Data from {url}'

async def fetch_all(urls):
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    urls = [
        'https://api.example.com/users',
        'https://api.example.com/posts',
        'https://api.example.com/comments'
    ]
    results = await fetch_all(urls)
    for r in results:
        print(r)

asyncio.run(main())

# Rate limiting
async def rate_limited_fetch(url, semaphore):
    async with semaphore:
        print(f'Fetching {url}')
        await asyncio.sleep(0.5)
        return f'Data from {url}'

async def main_limited():
    semaphore = asyncio.Semaphore(3)
    urls = [f'https://api.example.com/item/{i}' for i in range(10)]
    tasks = [rate_limited_fetch(url, semaphore) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main_limited())

