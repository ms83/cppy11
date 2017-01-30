from threading import Thread

def worker():
    pass

t = Thread(target=worker)
t.start()
t.join()
