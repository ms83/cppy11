void worker(string& s)
{
    s = "new value";
}

string s("initial value");
thread t(worker, ref(s));
t.join();
