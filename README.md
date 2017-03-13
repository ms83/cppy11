
# C++ for Python Programmers

[Datatype](#datatype) &nbsp; [Datetime](#datetime) &nbsp; [Deque](#deque) &nbsp; [Dynamic Array](#dynamic-array) &nbsp; [File](#file) &nbsp; [Lambda](#lambda) &nbsp; [Map](#map) &nbsp; [Priority Queue](#priority-queue) &nbsp; [Queue](#queue) &nbsp; [Set](#set) &nbsp; [String](#string) &nbsp; [Thread](#thread) &nbsp; [Tuple](#tuple)



## Datatype

[convert array of ints to string](#convert-array-of-ints-to-string)

[convert int to string](#convert-int-to-string)

[convert string to int](#convert-string-to-int)

[get data type as string](#get-data-type-as-string)

### convert int to string


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s = str(k)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
string s = to_string(k);
</pre>
</td>
</tr>
</table>
    

### convert array of ints to string


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s = ''.join(map(str, v))
</pre>
</td>
<td valign="top">
<pre lang="cpp">
stringstream ss;
copy(v.begin(), v.end(), ostream_iterator<int>(ss, ""));
string s = ss.str();
</pre>
</td>
</tr>
</table>
    

### convert string to int


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
k = int(s)  # throws ValueError
</pre>
</td>
<td valign="top">
<pre lang="cpp">
auto k = stoi(s);   // throws std::invalid_argument
</pre>
</td>
</tr>
</table>
    

### get data type as string


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
type(var)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
typeid(var).name()

// or

boost::typeindex::type_id_with_cvr<T>().pretty_name()

// or

boost::typeindex::type_id_with_cvr<decltype(param)>().pretty_name()
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Datetime

[get datetime difference](#get-datetime-difference)

[print current timestamp](#print-current-timestamp)

### print current timestamp


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
print(int(time.time()))
</pre>
</td>
<td valign="top">
<pre lang="cpp">
std::cout << std::time(0);
</pre>
</td>
</tr>
</table>
    

### get datetime difference


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
yesterday = datetime.now() - timedelta(hours=24)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
auto yesterday = std::chrono::system_clock::now() - std::chrono::hours(24);
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Deque

[access element](#access-element)

[initialize deque](#initialize-deque)

[insert element](#insert-element)

### access element


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
dq[0]
dq[-1]
dq[5]   # don't do that. use list instead
</pre>
</td>
<td valign="top">
<pre lang="cpp">
dq.front()
dq.back()
dq[5]   # don't do that. use vector instead
</pre>
</td>
</tr>
</table>
    

### initialize deque


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
from collections import deque
dq = deque([0,1,2,3,4])
</pre>
</td>
<td valign="top">
<pre lang="cpp">
deque<int> dq {0,1,2,3,4};
</pre>
</td>
</tr>
</table>
    

### insert element


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
dq.append(10)
dq.appendleft(20)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
dq.push_back(10)
dq.push_front(20)
</pre>
</td>
</tr>
</table>
    

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


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v = [0] * N
</pre>
</td>
<td valign="top">
<pre lang="cpp">
vector<int> v(N);
</pre>
</td>
</tr>
</table>
    

### filter array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
# In place
v = filter(lambda x: x%2 == 0, v)

# Copy
v2 = filter(lambda x: x%2 == 0, v)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
// In place
v.erase(remove_if(v.begin(), v.end(), [](const int x){return x%2 == 0;}), v.end());

// Copy
vector<int> v2;
copy_if(v.begin(), v.end(), back_inserter(v2), [](const int x){return x%2 == 0;});
</pre>
</td>
</tr>
</table>
    

### get min of elements in array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
minimal = min(v)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
auto minimum = min_element(v.begin(), v.end());
</pre>
</td>
</tr>
</table>
    

### count filtered elements


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
cnt = len(filter(lambda x: x>10, v))
</pre>
</td>
<td valign="top">
<pre lang="cpp">
int cnt = count_if(v.begin(), v.end(), [](int x) {return x>10;});
</pre>
</td>
</tr>
</table>
    

### remove last element


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v.pop()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
v.pop_back();
</pre>
</td>
</tr>
</table>
    

### remove first element


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v.pop(0)    # prefer deque
</pre>
</td>
<td valign="top">
<pre lang="cpp">
v.erase(v.begin()); // prefer deque
</pre>
</td>
</tr>
</table>
    

### insert at the beginning


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
# don't do that. use deque
</pre>
</td>
<td valign="top">
<pre lang="cpp">
// don't do that. Use deque
</pre>
</td>
</tr>
</table>
    

### remove duplicates from array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v = list(set(v))
</pre>
</td>
<td valign="top">
<pre lang="cpp">
sort(v.begin(), v.end())
v.erase(unique(v.begin(), v.end()), v.end());
</pre>
</td>
</tr>
</table>
    

### initialize array to 1 1 1 1 1


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v = [1]*5
</pre>
</td>
<td valign="top">
<pre lang="cpp">
vector<int> v(5, 1);
</pre>
</td>
</tr>
</table>
    

### slice array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v = v[2:8]
v = v[2:]
v = v[:-2]
v = v[-2:]
</pre>
</td>
<td valign="top">
<pre lang="cpp">
v.assign(v.begin()+2, v.begin()+8);
v.assign(v.begin()+2, v.end());
v.assign(v.begin(), v.begin()+v.size()-2);
v.assign(v.begin()+v.size()-2, v.end());
</pre>
</td>
</tr>
</table>
    

### sort array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
# In place
v.sort()

# Copy
v2 = sorted(v)

# Reversed order #1
v.sort(reverse=True)

# Reversed order #2
sorted(v, reverse=True)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
// In place
sort(v.begin(), v.end())

// Copy
sort(v.begin(), v.end())
vector<int> v2(v)

// Reversed order
sort(v.rbegin(), v.rend())
</pre>
</td>
</tr>
</table>
    

### find lower and upper bound


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
import bisect
v = [3, 5, 5, 5, 6, 8, 10]
lower_bound_index = bisect.bisect_left(v, 5)  # 1
upper_bound_index = bisect.bisect_right(v, 5) # 4
</pre>
</td>
<td valign="top">
<pre lang="cpp">
vector<int> v {3, 5, 5, 5, 6, 8, 10};
auto lower_bound_index = distance(v.begin(), lower_bound(v.begin(), v.end(), 5));
auto upper_bound_index = distance(v.begin(), upper_bound(v.begin(), v.end(), 5));
</pre>
</td>
</tr>
</table>
    

### insert at the end


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v.append(5) # possible full reallocation
</pre>
</td>
<td valign="top">
<pre lang="cpp">
v.push_back(5)  // possible full reallocation
</pre>
</td>
</tr>
</table>
    

### random access


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v[0]    # O(1)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
v[0]    # O(1)
</pre>
</td>
</tr>
</table>
    

### iterate over an array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
for i in [0, 1, 2, 3, 4]:
    pass
</pre>
</td>
<td valign="top">
<pre lang="cpp">
for (auto i: {0, 1, 2, 3, 4}) {
}
</pre>
</td>
</tr>
</table>
    

### transform array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
# In place
v = map(lambda x: x*2, v)

# Copy
v2 = map(lambda x: x*2, v)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
// In place
transform(v.begin(), v.end(), v.begin(), [](const int x){return x*2;});

// Copy
vector<int> v2;
transform(v.begin(), v.end(), back_inserter(v2), [](const int x){return x*2;});
</pre>
</td>
</tr>
</table>
    

### reverse array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v.reverse()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
reverse(v.begin(), v.end());
</pre>
</td>
</tr>
</table>
    

### initialize array to 0 1 2 3 4 5 6 7 8 9


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v = range(0, 10)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
vector<int> v(10);
iota(v.begin(), v.end(), 0);
</pre>
</td>
</tr>
</table>
    

### get sum of elements in array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
total = sum(v)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
int total = accumulate(v.begin(), v.end(), 0)
</pre>
</td>
</tr>
</table>
    

### initialize array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v = [1,2,3,4,5]
</pre>
</td>
<td valign="top">
<pre lang="cpp">
vector<int> v{1,2,3,4,5};
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## File

[read file line by line](#read-file-line-by-line)

[write line to file](#write-line-to-file)

### read file line by line


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
for line in open('example.txt'):
    # line with ending \n
</pre>
</td>
<td valign="top">
<pre lang="cpp">
string line;
ifstream file("example.txt");   // #include<iostream>
while (getline(file, line)) {   // #include<fstream>
    // line without ending \n
}
</pre>
</td>
</tr>
</table>
    

### write line to file


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
with open('example.txt', 'w') as file:
    file.write('some text\n')
</pre>
</td>
<td valign="top">
<pre lang="cpp">
ofstream file("example.txt");
file << "some text\n";
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Lambda

[create function](#create-function)

### create function


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
f = lambda x: x%2
f(3)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
auto f = [](int x){return x%2;};
f(3);
</pre>
</td>
</tr>
</table>
    

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


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
d[key] = d.get(key, 0) + 1
</pre>
</td>
<td valign="top">
<pre lang="cpp">
d[key] += 1;
</pre>
</td>
</tr>
</table>
    

### initialize map


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
d = {'c++': 10, 'python': 12, 'java': 5}
</pre>
</td>
<td valign="top">
<pre lang="cpp">
map<string, int> d { {"c++", 10}, {"python", 12}, {"java", 5} };
</pre>
</td>
</tr>
</table>
    

### store multi values on a map


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
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
</pre>
</td>
<td valign="top">
<pre lang="cpp">
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
</pre>
</td>
</tr>
</table>
    

### copy keys of a map to array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
v = d.keys()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
vector<type> keys;
boost::copy(d | boost::adaptors::map_keys, std::back_inserter(keys));
</pre>
</td>
</tr>
</table>
    

### check if key exists in the map


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
if 'scala' in d:
    pass

if d.get('scala'):
    pass

if d.has_key('scala'):
    pass
</pre>
</td>
<td valign="top">
<pre lang="cpp">
if (d.find("scala") != d.end()) {
}

if (d.count("scala") > 0) {
}
</pre>
</td>
</tr>
</table>
    

### copy values of a map to array


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
values = d.values()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
vector<type> values;
boost::copy(d | boost::adaptors::map_values, std::back_inserter(values));
</pre>
</td>
</tr>
</table>
    

### remove element of map


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
d.pop("scala") # Raise KeyError if key is missing

d.pop("scala", None) # Don't raise an exception if key is missing
</pre>
</td>
<td valign="top">
<pre lang="cpp">
d.erase("scala") // No exception if key is missing
</pre>
</td>
</tr>
</table>
    

### set element of map


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
d['scala'] = 8
</pre>
</td>
<td valign="top">
<pre lang="cpp">
d["scala"] = 8;
</pre>
</td>
</tr>
</table>
    

### iterate over a map


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
for key, value in d.iteritems():
    pass
</pre>
</td>
<td valign="top">
<pre lang="cpp">
for (auto& x: d) {
    auto key = x.first;
    auto val = x.second;
}
</pre>
</td>
</tr>
</table>
    

### get size of a map


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
size = len(d)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
int size = d.size()
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Priority Queue

[insert element](#insert-element)

[insert to queue](#insert-to-queue)

### insert element


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
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
</pre>
</td>
<td valign="top">
<pre lang="cpp">

</pre>
</td>
</tr>
</table>
    

### insert to queue


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">

</pre>
</td>
<td valign="top">
<pre lang="cpp">
q.push(10);
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Queue

[insert to queue](#insert-to-queue)

### insert to queue


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
q.push(10);
</pre>
</td>
<td valign="top">
<pre lang="cpp">
q.push(10);
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Set

[check if key exists in the set](#check-if-key-exists-in-the-set)

[initialize set](#initialize-set)

[insert element](#insert-element)

[intialize set](#intialize-set)

[remove element](#remove-element)

### initialize set


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s = {0, 1 ,2, 3, 4}
</pre>
</td>
<td valign="top">
<pre lang="cpp">
set<int> s {0,1,2,3,4};
</pre>
</td>
</tr>
</table>
    

### intialize set


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">

</pre>
</td>
<td valign="top">
<pre lang="cpp">
#include<set>
#include<iostream>
using namespace std;

int main()
{
    set<int> s {0,1,2,3,4}; 
}
</pre>
</td>
</tr>
</table>
    

### insert element


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s.add('b')
</pre>
</td>
<td valign="top">
<pre lang="cpp">
s.insert("b");
</pre>
</td>
</tr>
</table>
    

### check if key exists in the set


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
if 5 in s:
    pass
</pre>
</td>
<td valign="top">
<pre lang="cpp">
if (s.find(5) != s.end()) {
}
</pre>
</td>
</tr>
</table>
    

### remove element


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s.remove("b");
</pre>
</td>
<td valign="top">
<pre lang="cpp">
s.erase("b");
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## String

[append](#append)

### append


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
s = 'abcd'
s + 'a'
</pre>
</td>
<td valign="top">
<pre lang="cpp">

</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Thread

[map array concurrently](#map-array-concurrently)

[pass read only data to thread](#pass-read-only-data-to-thread)

[pass writable data to thread](#pass-writable-data-to-thread)

[start thread](#start-thread)

### pass read only data to thread


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
def worker(s):
    s = 'new value' # only local modification

s = "initial value"
t = Thread(target=worker, args=(s, ))
t.start()
t.join()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
void worker(const string& s)
{
    //s = "new value"; 
}

string s("initial value");
thread t(worker, s);
t.join();
</pre>
</td>
</tr>
</table>
    

### pass writable data to thread


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
def worker(s):
    s['v'] = 'new value'

s = {'v': 'initial value'}
t = Thread(target=worker, args=(s, ))
t.start()
t.join()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
void worker(string& s)
{
    s = "new value";
}

string s("initial value");
thread t(worker, ref(s));
t.join();
</pre>
</td>
</tr>
</table>
    

### start thread


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
from threading import Thread

def worker():
    pass

t = Thread(target=worker)
t.start()
t.join()
</pre>
</td>
<td valign="top">
<pre lang="cpp">
#include<thread>

void worker();

thread t(worker);
t.join();
</pre>
</td>
</tr>
</table>
    

### map array concurrently


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    p.map(f, [1, 2, 3]))
    # p is not [1, 4, 9]
</pre>
</td>
<td valign="top">
<pre lang="cpp">
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
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)



## Tuple

[access tuple](#access-tuple)

[initialize tuple](#initialize-tuple)

### access tuple


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
t[0]
t[1]
t[2]
</pre>
</td>
<td valign="top">
<pre lang="cpp">
get<0>(t)
get<1>(t)
get<2>(t)
</pre>
</td>
</tr>
</table>
    

### initialize tuple


<table>
<tr>
<th>
Python
</th>
<th>
C++11
</th>
</tr>
<tr>
<td  valign="top">
<pre lang="py">
t = (10, "some string", 0.5)
</pre>
</td>
<td valign="top">
<pre lang="cpp">
auto t = make_tuple(10, "some string", 0.5);
</pre>
</td>
</tr>
</table>
    

[&uarr;top](#c-for-python-programmers)
