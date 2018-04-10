def make_multiset(l):
    return dict((i, l.count(i)) for i in l)


def ordered_dict(d):
    return sorted(d.items())


def reversed_dict(d):
    return dict((d[i], i) for i in d)
    # return(dict(map(reversed, d.items())))


def unique_objects(objects):
    return len(set(map(id, objects)))

