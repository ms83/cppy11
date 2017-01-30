// In place
transform(v.begin(), v.end(), v.begin(), [](const int x){return x*2;});

// Copy
vector<int> v2;
transform(v.begin(), v.end(), back_inserter(v2), [](const int x){return x*2;});
