// In place
v.erase(remove_if(v.begin(), v.end(), [](const int x){return x%2 == 0;}), v.end());

// Copy
vector<int> v2;
copy_if(v.begin(), v.end(), back_inserter(v2), [](const int x){return x%2 == 0;});
