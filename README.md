
# C++ for Python Programmers

[Datatype](#datatype) &nbsp; [Deque](#deque) &nbsp; [Dynamic Array](#dynamic-array) &nbsp; [File](#file) &nbsp; [Lambda](#lambda) &nbsp; [Map](#map) &nbsp; [Priority Queue](#priority-queue) &nbsp; [Queue](#queue) &nbsp; [Set](#set) &nbsp; [String](#string) &nbsp; [Thread](#thread) &nbsp; [Tuple](#tuple)



## Datatype

[convert array of ints to string](#convert-array-of-ints-to-string)

[convert int to string](#convert-int-to-string)

[convert string to int](#convert-string-to-int)

[get data type as string](#get-data-type-as-string)

### convert int to string
```python
s = str(k)
```
```cpp
string s = to_string(k);
```

### convert array of ints to string
```python
s = ''.join(map(str, v))
```
```cpp
stringstream ss;
copy(v.begin(), v.end(), ostream_iterator<int>(ss, ""));
string s = ss.str();
```

### convert string to int
```python
k = int(s)  # throws ValueError
```
```cpp
auto k = stoi(s);   // throws std::invalid_argument
```

### get data type as string
```python
type(var)
```
```cpp
typeid(var).name()

// or

boost::typeindex::type_id_with_cvr<T>().pretty_name()

// or

boost::typeindex::type_id_with_cvr<decltype(param)>().pretty_name()
```

[&uarr;top](#c-for-python-programmers)



## Deque

[access element](#access-element)

[initialize deque](#initialize-deque)

[insert element](#insert-element)

### access element
```python
dq[0]
dq[-1]
dq[5]   # don't do that. use list instead
```
```cpp
dq.front()
dq.back()
dq[5]   # don't do that. use vector instead
```

### initialize deque
```python
from collections import deque
dq = deque([0,1,2,3,4])
```
```cpp
deque<int> dq {0,1,2,3,4};
```

### insert element
```python
dq.append(10)
dq.appendleft(20)
```
```cpp
dq.push_back(10)
dq.push_front(20)
```

[&uarr;top](#c-for-python-programmers)



## Dynamic Array

[count filtered elements](#count-filtered-elements)

[filter array](#filter-array)

[find lower and upper bound](#find-lower-and-upper-bound)

[get min of elements in array](#get-min-of-elements-in-array)

[get sum of elements in array](#get-sum-of-elements-in-array)

[initialize array](#initialize-array)

[initialize array to 0 1 2 3 4 5 6 7 8 9](#initialize-array-to-0-1-2-3-4-5-6-7-8-9)

[initialize array to 1 1 1 1 1](#initialize-array-to-1-1-1-1-1)

[initialize n size array](#initialize-n-size-array)

[insert at the beginning](#insert-at-the-beginning)

[insert at the end](#insert-at-the-end)

[iterate over an array](#iterate-over-an-array)

[random access](#random-access)

[remove duplicates from array](#remove-duplicates-from-array)

[remove first element](#remove-first-element)

[remove last element](#remove-last-element)

[reverse array](#reverse-array)

[slice array](#slice-array)

[sort array](#sort-array)

[transform array](#transform-array)

### initialize n size array
```python
v = [0] * N
```
```cpp
vector<int> v(N);
```

### filter array
```python
# In place
v = filter(lambda x: x%2 == 0, v)

# Copy
v2 = filter(lambda x: x%2 == 0, v)
```
```cpp
// In place
v.erase(remove_if(v.begin(), v.end(), [](const int x){return x%2 == 0;}), v.end());

// Copy
vector<int> v2;
copy_if(v.begin(), v.end(), back_inserter(v2), [](const int x){return x%2 == 0;});
```

### get min of elements in array
```python
minimal = min(v)
```
```cpp
auto minimum = min_element(v.begin(), v.end());
```

### count filtered elements
```python
cnt = len(filter(lambda x: x>10, v))
```
```cpp
int cnt = count_if(v.begin(), v.end(), [](int x) {return x>10;});
```

### remove last element
```python
v.pop()
```
```cpp
v.pop_back();
```

### remove first element
```python
v.pop(0)    # prefer deque
```
```cpp
v.erase(v.begin()); // prefer deque
```

### insert at the beginning
```python
# don't do that. use deque
```
```cpp
// don't do that. Use deque
```

### remove duplicates from array
```python
v = list(set(v))
```
```cpp
sort(v.begin(), v.end())
v.erase(unique(v.begin(), v.end()), v.end());
```

### initialize array to 1 1 1 1 1
```python
v = [1]*5
```
```cpp
vector<int> v(5, 1);
```

### slice array
```python
v = v[2:8]
v = v[2:]
v = v[:-2]
v = v[-2:]
```
```cpp
v.assign(v.begin()+2, v.begin()+8);
v.assign(v.begin()+2, v.end());
v.assign(v.begin(), v.begin()+v.size()-2);
v.assign(v.begin()+v.size()-2, v.end());
```

### sort array
```python
# In place
v.sort()

# Copy
v2 = sorted(v)

# Reversed order #1
v.sort(reverse=True)

# Reversed order #2
sorted(v, reverse=True)
```
```cpp
// In place
sort(v.begin(), v.end())

// Copy
sort(v.begin(), v.end())
vector<int> v2(v)

// Reversed order
sort(v.rbegin(), v.rend())
```

### find lower and upper bound
```python
import bisect
v = [3, 5, 5, 5, 6, 8, 10]
lower_bound_index = bisect.bisect_left(v, 5)  # 1
upper_bound_index = bisect.bisect_right(v, 5) # 4
```
```cpp
vector<int> v {3, 5, 5, 5, 6, 8, 10};
auto lower_bound_index = distance(v.begin(), lower_bound(v.begin(), v.end(), 5));
auto upper_bound_index = distance(v.begin(), upper_bound(v.begin(), v.end(), 5));
```

### insert at the end
```python
v.append(5) # possible full reallocation
```
```cpp
v.push_back(5)  // possible full reallocation
```

### random access
```python
v[0]    # O(1)
```
```cpp
v[0]    # O(1)
```

### iterate over an array
```python
for i in [0, 1, 2, 3, 4]:
    pass
```
```cpp
for (auto i: {0, 1, 2, 3, 4}) {
}
```

### transform array
```python
# In place
v = map(lambda x: x*2, v)

# Copy
v2 = map(lambda x: x*2, v)
```
```cpp
// In place
transform(v.begin(), v.end(), v.begin(), [](const int x){return x*2;});

// Copy
vector<int> v2;
transform(v.begin(), v.end(), back_inserter(v2), [](const int x){return x*2;});
```

### reverse array
```python
v.reverse()
```
```cpp
reverse(v.begin(), v.end());
```

### initialize array to 0 1 2 3 4 5 6 7 8 9
```python
v = range(0, 10)
```
```cpp
vector<int> v(10);
iota(v.begin(), v.end(), 0);
```

### get sum of elements in array
```python
total = sum(v)
```
```cpp
int total = accumulate(v.begin(), v.end(), 0)
```

### initialize array
```python
v = [1,2,3,4,5]
```
```cpp
vector<int> v{1,2,3,4,5};
```

[&uarr;top](#c-for-python-programmers)



## File

[read file line by line](#read-file-line-by-line)

[write line to file](#write-line-to-file)

### read file line by line
```python
for line in open('example.txt'):
    # line with ending \n
```
```cpp
string line;
ifstream file("example.txt");   // #include<iostream>
while (getline(file, line)) {   // #include<fstream>
    // line without ending \n
}
```

### write line to file
```python
with open('example.txt', 'w') as file:
    file.write('some text\n')
```
```cpp
ofstream file("example.txt");
file << "some text\n";
```

[&uarr;top](#c-for-python-programmers)



## Lambda

[create function](#create-function)

### create function
```python
f = lambda x: x%2
f(3)
```
```cpp
auto f = [](int x){return x%2;};
f(3);
```

[&uarr;top](#c-for-python-programmers)



## Map

[check if key exists in the map](#check-if-key-exists-in-the-map)

[copy keys of a map to array](#copy-keys-of-a-map-to-array)

[copy values of a map to array](#copy-values-of-a-map-to-array)

[get size of a map](#get-size-of-a-map)

[increase the value of an element of a map](#increase-the-value-of-an-element-of-a-map)

[initialize map](#initialize-map)

[iterate over a map](#iterate-over-a-map)

[remove element of map](#remove-element-of-map)

[set element of map](#set-element-of-map)

[store multi values on a map](#store-multi-values-on-a-map)

### increase the value of an element of a map
```python
d[key] = d.get(key, 0) + 1
```
```cpp
d[key] += 1;
```

### initialize map
```python
d = {'c++': 10, 'python': 12, 'java': 5}
```
```cpp
map<string, int> d { {"c++", 10}, {"python", 12}, {"java", 5} };
```

### store multi values on a map
```python
data = (
    ("Toyota", "Avensis"),
    ("Toyota", "Auris"),
    ("Toyota", "Corolla"),
    ("Audi", "A3"),
)

cars = {}
for brand, model in data:
    cars.setdefault(brand, [])
    cars[brand].append(model)

for model in cars.get("Toyota", []):
    print(model)
```
```cpp
vector< pair<string, string> > data {
    make_pair("Toyota", "Avensis"),
    make_pair("Toyota", "Auris"),
    make_pair("Toyota", "Corolla"),
    make_pair("Audi", "A3"),
    make_pair("Audi", "A4")
};

multimap<string, string> cars;
for(auto x: data) {
    cars.insert(x);
}

const auto range = cars.equal_range("Toyota");
for(auto x=range.first; x!=range.second; ++x) {
    cout << x->second << endl;
}
```

### copy keys of a map to array
```python
v = d.keys()
```
```cpp
vector<type> keys;
boost::copy(d | boost::adaptors::map_keys, std::back_inserter(keys));
```

### check if key exists in the map
```python
if 'scala' in d:
    pass

if d.get('scala'):
    pass

if d.has_key('scala'):
    pass
```
```cpp
if (d.find("scala") != d.end()) {
}

if (d.count("scala") > 0) {
}
```

### copy values of a map to array
```python
values = d.values()
```
```cpp
vector<type> values;
boost::copy(d | boost::adaptors::map_values, std::back_inserter(values));
```

### remove element of map
```python
d.pop("scala") # Raise KeyError if key is missing

d.pop("scala", None) # Don't raise an exception if key is missing
```
```cpp
d.erase("scala") // No exception if key is missing
```

### set element of map
```python
d['scala'] = 8
```
```cpp
d["scala"] = 8;
```

### iterate over a map
```python
for key, value in d.iteritems():
    pass
```
```cpp
for (auto& x: d) {
    auto key = x.first;
    auto val = x.second;
}
```

### get size of a map
```python
size = len(d)
```
```cpp
int size = d.size()
```

[&uarr;top](#c-for-python-programmers)



## Priority Queue

[insert element](#insert-element)

[insert to queue](#insert-to-queue)

### insert element
```python
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
```
```cpp

```

### insert to queue
```python

```
```cpp
q.push(10);
```

[&uarr;top](#c-for-python-programmers)



## Queue

[insert to queue](#insert-to-queue)

### insert to queue
```python
q.push(10);
```
```cpp
q.push(10);
```

[&uarr;top](#c-for-python-programmers)



## Set

[check if key exists in the set](#check-if-key-exists-in-the-set)

[initialize set](#initialize-set)

[insert element](#insert-element)

[intialize set](#intialize-set)

[remove element](#remove-element)

### initialize set
```python
s = {0, 1 ,2, 3, 4}
```
```cpp
set<int> s {0,1,2,3,4};
```

### intialize set
```python

```
```cpp
#include<set>
#include<iostream>
using namespace std;

int main()
{
    set<int> s {0,1,2,3,4}; 
}
```

### insert element
```python
s.add('b')
```
```cpp
s.insert("b");
```

### check if key exists in the set
```python
if 5 in s:
    pass
```
```cpp
if (s.find(5) != s.end()) {
}
```

### remove element
```python
s.remove("b");
```
```cpp
s.erase("b");
```

[&uarr;top](#c-for-python-programmers)



## String

[append](#append)

### append
```python
s = 'abcd'
s + 'a'
```
```cpp

```

[&uarr;top](#c-for-python-programmers)



## Thread

[pass read only data to thread](#pass-read-only-data-to-thread)

[pass writable data to thread](#pass-writable-data-to-thread)

[start thread](#start-thread)

### pass read only data to thread
```python
def worker(s):
    s = 'new value' # only local modification

s = "initial value"
t = Thread(target=worker, args=(s, ))
t.start()
t.join()
```
```cpp
void worker(const string& s)
{
    //s = "new value"; 
}

string s("initial value");
thread t(worker, s);
t.join();
```

### pass writable data to thread
```python
def worker(s):
    s['v'] = 'new value'

s = {'v': 'initial value'}
t = Thread(target=worker, args=(s, ))
t.start()
t.join()
```
```cpp
void worker(string& s)
{
    s = "new value";
}

string s("initial value");
thread t(worker, ref(s));
t.join();
```

### start thread
```python
from threading import Thread

def worker():
    pass

t = Thread(target=worker)
t.start()
t.join()
```
```cpp
#include<thread>

void worker();

thread t(worker);
t.join();
```

[&uarr;top](#c-for-python-programmers)



## Tuple

[access tuple](#access-tuple)

[initialize tuple](#initialize-tuple)

### access tuple
```python
t[0]
t[1]
t[2]
```
```cpp
get<0>(t)
get<1>(t)
get<2>(t)
```

### initialize tuple
```python
t = (10, "some string", 0.5)
```
```cpp
auto t = make_tuple(10, "some string", 0.5);
```

[&uarr;top](#c-for-python-programmers)
