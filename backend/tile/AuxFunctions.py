from collections import Counter


def merge_dicts(*ds):
    cdict = Counter({})
    for d in ds:
        cdict += Counter(d)
    print(cdict)
    return cdict
