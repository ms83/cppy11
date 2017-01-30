#include<iostream>
#include<queue>
using namespace std;

int main()
{
    priority_queue<int> q;
    //queue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);
    q.push(44);

    while(!q.empty()) {
        //int e = q.front(); q.pop();
        int e = q.top(); q.pop();
        cout << e << endl;
    }
}
