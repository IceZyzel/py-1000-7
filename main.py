import imp
import time
from weakref import ref
from playsound import *
import threading 
import requests
import pyglet
def req(l):
        request = requests.get('https://zamp3.net/uploads/music/2021/07/fem-love-1000-7-mp3.mp3')
        with open('foo.mp3', 'wb') as file:
            file.write(request.content)
def femlove(n):
    while n>0:
        n-=7
        time.sleep(1)
        print(n)
    return n
def zxctilt (n):  
    song = pyglet.media.load('foo.mp3')
    song.play()
    pyglet.app.run()
t0 = threading.Thread(target=req,args=(1,))
t1 = threading.Thread(target= femlove,args=(1000,))
t2 = threading.Thread(target= zxctilt,args=(1,))
t0.start
t0.join
t1.start()
t2.start()
t1.join
t2.join