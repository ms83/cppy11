[Dynamic Array](#dynamic-array)
[Map](#map)
[Tuple](#tuple)
[File](#file)
[Lambda](#lambda)
[Thread](#thread)
[DateTime](#datetime)
[DataType](#datatype)
[Regexp](#regexp)



# Dynamic Array

[Initialize array](#initialize-array)

[Initialize N-size array](#initialize-n-size-array)

[Initialize array to [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]](#initialize-array-to-0-1-2-3-4-5-6-7-8-9)

[Initialize array to [1, 1, 1, 1, 1]](#initialize-array-to-1-1-1-1-1)

[Random access](#random-access)

[Insert at the end](#insert-at-the-end)

[Insert at the beginning](#insert-at-the-beginning)

[Iterate over an array](#iterate-over-an-array)

[Reverse array](#reverse-array)

[Filter array](#filter-array)

[Transform array](#transform-array)

[Sort array](#sort-array)

[Get min of elements in array](#get-min-of-elements-in-array)

[Get sum of elements in array](#get-sum-of-elements-in-array)

[Slice array](#slice-array)

[Count filtered elements](#count-filtered-elements)

[Remove first element](#remove-first-element)

[Remove last element](#remove-last-element)

[Remove duplicates from array](#remove-duplicates-from-array)

[Find lower and upper bound](#find-lower-and-upper-bound)

# Initialize array
```c++
v = [1,2,3,4,5]
```
```python
vector<int> v{1,2,3,4,5};
```

# Initialize N-size array
```c++
v = [0] * N
```
```python
vector<int> v(N);
```

# Initialize array to [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```c++
v = range(0, 10)
```
```python
vector<int> v(10);
iota(v.begin(), v.end(), 0);
```

# Initialize array to [1, 1, 1, 1, 1]
```c++
v = [1]*5
```
```python
vector<int> v(5, 1);
```

# Random access
```c++
v[0]    # O(1)
```
```python
v[0]    # O(1)
```

# Insert at the end
```c++
v.append(5) # possible full reallocation
```
```python
v.push_back(5)  // possible full reallocation
```

# Insert at the beginning
```c++
# don't do that. use deque
```
```python
// don't do that. Use deque
```

# Iterate over an array
```c++
for i in [0, 1, 2, 3, 4]:
    pass
```
```python
for (auto i: {0, 1, 2, 3, 4}) {
}
```

# Reverse array
```c++
v.reverse()
```
```python
reverse(v.begin(), v.end());
```

# Filter array
```c++
# In place
v = filter(lambda x: x%2 == 0, v)

# Copy
v2 = filter(lambda x: x%2 == 0, v)
```
```python
// In place
v.erase(remove_if(v.begin(), v.end(), [](const int x){return x%2 == 0;}), v.end());

// Copy
vector<int> v2;
copy_if(v.begin(), v.end(), back_inserter(v2), [](const int x){return x%2 == 0;});
```

# Transform array
```c++
# In place
v = map(lambda x: x*2, v)

# Copy
v2 = map(lambda x: x*2, v)
```
```python
// In place
transform(v.begin(), v.end(), v.begin(), [](const int x){return x*2;});

// Copy
vector<int> v2;
transform(v.begin(), v.end(), back_inserter(v2), [](const int x){return x*2;});
```

# Sort array
```c++
# In place
v.sort()

# Copy
v2 = sorted(v)

# Reversed order #1
v.sort(reverse=True)

# Reversed order #2
sorted(v, reverse=True)
```
```python
// In place
sort(v.begin(), v.end())

// Copy
sort(v.begin(), v.end())
vector<int> v2(v)

// Reversed order
sort(v.rbegin(), v.rend())
```

# Get min of elements in array
```c++
minimal = min(v)
```
```python
auto minimum = min_element(v.begin(), v.end());
```

# Get sum of elements in array
```c++
total = sum(v)
```
```python
int total = accumulate(v.begin(), v.end(), 0)
```

# Slice array
```c++
v = v[2:8]
v = v[2:]
v = v[:-2]
v = v[-2:]
```
```python
v.assign(v.begin()+2, v.begin()+8);
v.assign(v.begin()+2, v.end());
v.assign(v.begin(), v.begin()+v.size()-2);
v.assign(v.begin()+v.size()-2, v.end());
```

# Count filtered elements
```c++
cnt = len(filter(lambda x: x>10, v))
```
```python
int cnt = count_if(v.begin(), v.end(), [](int x) {return x>10;});
```

# Remove first element
```c++
v.pop(0)    # prefer deque
```
```python
v.erase(v.begin()); // prefer deque
```

# Remove last element
```c++
v.pop()
```
```python
v.pop_back();
```

# Remove duplicates from array
```c++
v = list(set(v))
```
```python
sort(v.begin(), v.end())
v.erase(unique(v.begin(), v.end()), v.end());
```

# Find lower and upper bound
```c++
import bisect
v = [3, 5, 5, 5, 6, 8, 10]
lower_bound_index = bisect.bisect_left(v, 5)  # 1
upper_bound_index = bisect.bisect_right(v, 5) # 4
```
```python
vector<int> v {3, 5, 5, 5, 6, 8, 10};
auto lower_bound_index = distance(v.begin(), lower_bound(v.begin(), v.end(), 5));
auto upper_bound_index = distance(v.begin(), upper_bound(v.begin(), v.end(), 5));
```



# Map

[Get size of a map](#get-size-of-a-map)

[Iterate over a map](#iterate-over-a-map)

[Increase the value of an element of a map](#increase-the-value-of-an-element-of-a-map)

[Copy keys of a map to array](#copy-keys-of-a-map-to-array)

[Copy values of a map to array](#copy-values-of-a-map-to-array)

[Store multi values on a map](#store-multi-values-on-a-map)

# Get size of a map
```c++
size = len(d)
```
```python
int size = d.size()
```

# Iterate over a map
```c++
for key, value in d.iteritems():
    pass
```
```python
for (auto& x: d) {
    auto key = x.first;
    auto val = x.second;
}
```

# Increase the value of an element of a map
```c++
d[key] = d.get(key, 0) + 1
```
```python
d[key] += 1;
```

# Copy keys of a map to array
```c++
v = d.keys()
```
```python
vector<type> keys;
boost::copy(d | boost::adaptors::map_keys, std::back_inserter(keys));
```

# Copy values of a map to array
```c++
values = d.values()
```
```python
vector<type> values;
boost::copy(d | boost::adaptors::map_values, std::back_inserter(values));
```

# Store multi values on a map
```c++
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
```python
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



# Tuple

[Initialize tuple](#initialize-tuple)

[Access tuple](#access-tuple)

# Initialize tuple
```c++
t = (10, "some string", 0.5)
```
```python
auto t = make_tuple(10, "some string", 0.5);
```

# Access tuple
```c++
t[0]
t[1]
t[2]
```
```python
get<0>(t)
get<1>(t)
get<2>(t)
```



# File

[Read file line by line](#read-file-line-by-line)

[Write line to file](#write-line-to-file)

# Read file line by line
```c++
for line in open('example.txt'):
    # line with ending \n
```
```python
string line;
ifstream file("example.txt");   // #include<iostream>
while (getline(file, line)) {   // #include<fstream>
    // line without ending \n
}
```

# Write line to file
```c++
with open('example.txt', 'w') as file:
    file.write('some text\n')
```
```python
ofstream file("example.txt");
file << "some text\n";
```



# Lambda

[Create function](#create-function)

# Create function
```c++
f = lambda x: x%2
f(3)
```
```python
auto f = [](int x){return x%2;};
f(3);
```



# Thread

[Start thread](#start-thread)

[Pass read only data to thread](#pass-read-only-data-to-thread)

[Pass writable data to thread](#pass-writable-data-to-thread)

# Start thread
```c++
from threading import Thread

def worker():
    pass

t = Thread(target=worker)
t.start()
t.join()
```
```python
#include<thread>

void worker();

thread t(worker);
t.join();
```

# Pass read only data to thread
```c++
def worker(s):
    s = 'new value' # only local modification

s = "initial value"
t = Thread(target=worker, args=(s, ))
t.start()
t.join()
```
```python
void worker(const string& s)
{
    //s = "new value"; 
}

string s("initial value");
thread t(worker, s);
t.join();
```

# Pass writable data to thread
```c++
def worker(s):
    s['v'] = 'new value'

s = {'v': 'initial value'}
t = Thread(target=worker, args=(s, ))
t.start()
t.join()
```
```python
void worker(string& s)
{
    s = "new value";
}

string s("initial value");
thread t(worker, ref(s));
t.join();
```



# DateTime



# DataType

[Get data type as string](#get-data-type-as-string)

[Convert string to int](#convert-string-to-int)

[Convert int to string](#convert-int-to-string)

[Convert array of ints to string](#convert-array-of-ints-to-string)

# Get data type as string
```c++
type(var)
```
```python
typeid(var).name()

// or

boost::typeindex::type_id_with_cvr<T>().pretty_name()

// or

boost::typeindex::type_id_with_cvr<decltype(param)>().pretty_name()
```

# Convert string to int
```c++
k = int(s)  # throws ValueError
```
```python
auto k = stoi(s);   // throws std::invalid_argument
```

# Convert int to string
```c++
s = str(k)
```
```python
string s = to_string(k);
```

# Convert array of ints to string
```c++
s = ''.join(map(str, v))
```
```python
stringstream ss;
copy(v.begin(), v.end(), ostream_iterator<int>(ss, ""));
string s = ss.str();
```



# Regexp
