
def each(a, fn):
    for item in a:
        fn(item)


def lol(a, fn):
    each(a, lambda item: each(item, fn))
