import multiprocessing
import time
import requests
import sys


def get_image_multiprocess(url):
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f'{filename} Downloaded in {time.time() - start_time:.2f} seconds')


processes = []
start_time = time.time()

if __name__ == '__main__':
    urls = []
    for item in sys.argv:
        if item.endswith('jpg'):
            urls.append(item)
    for url in urls:
        process = multiprocessing.Process(target=get_image_multiprocess, args=[url])
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
