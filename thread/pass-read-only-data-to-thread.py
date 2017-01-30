def worker(s):
    s = 'new value' # only local modification

s = "initial value"
t = Thread(target=worker, args=(s, ))
t.start()
t.join()
