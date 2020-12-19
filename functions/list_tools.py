import itertools

# Objects included in this file:
# None

# Functions included in this file:
# # pairwise


def pairwise(iterable):
    """See: https://docs.python.org/3/library/itertools.html#recipes
    s -> (s0,s1), (s1,s2), (s2, s3), ...
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return list(zip(a, b))
