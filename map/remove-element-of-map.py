d.pop("scala") # Raise KeyError if key is missing

d.pop("scala", None) # Don't raise an exception if key is missing
