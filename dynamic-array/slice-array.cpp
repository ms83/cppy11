v.assign(v.begin()+2, v.begin()+8);
v.assign(v.begin()+2, v.end());
v.assign(v.begin(), v.begin()+v.size()-2);
v.assign(v.begin()+v.size()-2, v.end());
