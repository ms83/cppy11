void worker(const string& s)
{
    //s = "new value"; 
}

string s("initial value");
thread t(worker, s);
t.join();
