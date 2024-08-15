import random

def toss(options):
    systoss = random.randint(1,2)
    if options[0] == systoss:
        return True
    return False