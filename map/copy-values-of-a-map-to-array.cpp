vector<type> values;
boost::copy(d | boost::adaptors::map_values, std::back_inserter(values));
