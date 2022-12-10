def dict_zip(*dicts, strict=False):
    keys = set(dicts[0].keys())
    for d in dicts[1:]:
        keys &= set(d.keys())

    if strict and not all(len(d) == len(dicts[0]) for d in dicts):
        raise ValueError("Strict is set to True, all dictionaries must have the same length.")

    for key in keys:
        # Only yield the key and values if the key exists in every dictionary
        if all(key in d for d in dicts):
            yield key, *(d[key] for d in dicts)

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 2, 'b': 3, 'c': 4}
d3 = {'a': 3, 'b': 4, 'c': 5, 'd': 6}

for key, v1, v2, v3 in dict_zip(d1, d2, d3):
    print(key, v1, v2, v3)
 
 """
 a 1 2 3
 b 2 3 4
 c 3 4 5
 """
  
