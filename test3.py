import requests
import pyglet


def download_file(file_):
    print(file_)
    data = {'file_': file_}
    r = requests.get("http://localhost:8080/index",
                     params=data,
                     stream=True
                     )

    local_filename = './tmp.mp3'
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    print(local_filename)
    return local_filename

src = pyglet.media.StaticSource(pyglet.media.load(download_file('Intro.mp3')))
print('aaaaaaaa')
player = pyglet.media.Player()
player.queue(src)
player.play()
pyglet.app.run()