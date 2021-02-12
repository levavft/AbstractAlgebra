from Relations import Relation


class EquivalenceRelation(Relation):
    """
    Assume:
    a~b, b~c => b~a, a~c
    """