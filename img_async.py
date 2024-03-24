import asyncio
import aiohttp
import time
import sys


async def get_image_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            img = await response.read()
            filename = url.split('/')[-1]
            with open(filename, 'wb') as file:
                file.write(img)
            print(f'{filename} Downloaded in {time.time() - start_time:.2f} seconds')


start_time = time.time()


async def main():
    urls = []
    for item in sys.argv:
        if item.endswith('jpg'):
            urls.append(item)
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(get_image_async(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
