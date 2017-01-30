vector<type> keys;
boost::copy(d | boost::adaptors::map_keys, std::back_inserter(keys));
