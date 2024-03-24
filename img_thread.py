import threading
import requests
import time
import sys

# urls = ['https://kartinkof.club/uploads/posts/2022-04/1650009724_4-kartinkof-club-p-khryushki-kartinki-prikolnie-4.jpg',
#         'https://wp-s.ru/wallpapers/1/42/296531240125415/malenkij-poros-nok-gulyayushhix-po-trave.jpg',
#         'https://foodbay.com/wiki/wp-content/uploads/2020/08/f44d75c20c-2.jpg']


def get_image_threading(url):
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f'{filename} Downloaded in {time.time() - start_time:.2f} seconds')


start_time = time.time()

if __name__ == '__main__':
    urls = []
    for item in sys.argv:
        if item.endswith('jpg'):
            urls.append(item)
    threads = []
    for url in urls:
        tread = threading.Thread(target=get_image_threading, args=[url])
        threads.append(tread)
        tread.start()
    for t in threads:
        t.join()
