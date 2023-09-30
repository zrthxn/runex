from runex import experiment


def loop():
    for k in [1,2,3,4,5]:
        print(f"Loop -- {k}")
        ...
    return k

@experiment
def expt(a: int):
    for l in [1,2,3]:
        print(f"Expt -- {l}")
        k = loop()
        yield l * k * a

# out = expt()