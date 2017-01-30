#include<thread>

void worker();

thread t(worker);
t.join();
