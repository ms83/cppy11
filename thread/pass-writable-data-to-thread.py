def worker(s):
    s['v'] = 'new value'

s = {'v': 'initial value'}
t = Thread(target=worker, args=(s, ))
t.start()
t.join()
