typeid(var).name()

// or

boost::typeindex::type_id_with_cvr<T>().pretty_name()

// or

boost::typeindex::type_id_with_cvr<decltype(param)>().pretty_name()
