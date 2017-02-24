#include<iostream>
#include<vector>
#include<thread>

void f(int& x)
{   
    x *= x;
}

class Pool
{
public:
    static void map(void (*f)(int&), std::vector<int>& input) {
        std::vector<std::thread> threads(input.size());
        for (int i=0;i<input.size();++i) {
            threads[i] = std::thread(f, std::ref(input[i]));
        }
        for (auto& t: threads) {
            t.join();
        }
    }
};

int main()
{
    std::vector<int> v{1,2,3};
    Pool::map(f, v);
    // v is now [1, 4, 9]
}
