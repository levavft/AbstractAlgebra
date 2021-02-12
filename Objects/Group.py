from Monoid import Monoid


class Group(Monoid):
    """
    We use the multiplicative notation, e.g: 1, S, f where:
    1, S, f define a monoid and
    for all a in S there exists b in S such that
    f(a,b) = f(b,a) = 1
    """