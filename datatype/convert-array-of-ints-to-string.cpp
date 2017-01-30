stringstream ss;
copy(v.begin(), v.end(), ostream_iterator<int>(ss, ""));
string s = ss.str();
