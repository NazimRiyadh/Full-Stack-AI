"""
we will talk about 'yield'
it uses to play the function once
better memory efficiency
"""

from asyncio import proactor_events
from tracemalloc import start


def start_coding():
    one=yield "project one done"
    print(one)
    two=yield "project two done"
    print(two)
    three=yield "project three done"
    print(three)
"""  
project=start_coding()
for proj in project:
    print(proj)


# if u use start_coding like it will create a generator obj every time
# so the use of reusing generator doesn't work
print(next(start_coding()))
print(next(start_coding()))
print(next(start_coding()))
print(next(start_coding()))

next() is resuming a paused generator until
    the next yield (or until it finishes).
"""

#use in this way
gen=start_coding()
print(next(gen))
print(next(gen))
print(next(gen))


def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai=get_chai_gen()

print(next(chai))
print(next(chai))
print(next(chai))

# so this kind of pause and resume game