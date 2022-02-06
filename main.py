import time
import threading 
import requests
import pyglet
        
def femlove(n):
    while n>0:
        n -= 7
        time.sleep(1)
        print(n)

def zxctilt():  
    song = pyglet.media.load('foo.mp3')
    song.play()
    pyglet.app.run()

request = requests.get('https://zamp3.net/uploads/music/2021/07/fem-love-1000-7-mp3.mp3')
with open('foo.mp3', 'wb') as file:
    file.write(request.content)

t1 = threading.Thread(target=femlove, args=(1000,))
t2 = threading.Thread(target=zxctilt)
t1.start()
t2.start()
t1.join()
t2.join()