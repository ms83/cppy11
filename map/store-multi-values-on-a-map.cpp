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
