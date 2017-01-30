vector<int> v {3, 5, 5, 5, 6, 8, 10};
auto lower_bound_index = distance(v.begin(), lower_bound(v.begin(), v.end(), 5));
auto upper_bound_index = distance(v.begin(), upper_bound(v.begin(), v.end(), 5));
