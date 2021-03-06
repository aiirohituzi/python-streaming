import requests
import pyglet
import os
from pyglet.window import key

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    print("A key was pressed")
    if symbol == key.P:
        player.pause()
    elif symbol == key.O:
        player.play()
    elif symbol == key.Q:
        pyglet.app.exit()
        os.remove('./tmp.mp3')

def download_file(file_):
    data = {'file_': file_}
    r = requests.get("http://localhost:8080/index",
                     params=data,
                     stream=True
                     )
    
    print(r)
    local_filename = './tmp.mp3'
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

def some_function():
    pyglet.app.exit()
    os.remove('./tmp.mp3')

src = pyglet.media.StaticSource(pyglet.media.load(download_file('Intro.mp3')))
player = pyglet.media.Player()
player.queue(src)
player.push_handlers(on_eos=some_function)
player.play()
pyglet.app.run()

# print(player.playing)