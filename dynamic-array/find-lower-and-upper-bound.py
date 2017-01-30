import bisect
v = [3, 5, 5, 5, 6, 8, 10]
lower_bound_index = bisect.bisect_left(v, 5)  # 1
upper_bound_index = bisect.bisect_right(v, 5) # 4
