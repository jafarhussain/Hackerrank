def person_lister(f):
    def inner(people):
        v= [*map(f, list(sorted(people, key=lambda p: int(p[2]))))]
        return v
    return inner