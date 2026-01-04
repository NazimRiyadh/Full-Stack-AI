#suppose buffet plating system, but need to count the plate

from weakref import ref


def count_plate():
    count=1
    while True:
        yield f"Refill {count}"
        count+=1

refill= count_plate()
print(next(refill))
print(next(refill))
print(next(refill))

riyadh= count_plate()
print(f"riyad's {next(riyadh)}")
print(f"riyad's {next(riyadh)}")
print(f"riyad's {next(riyadh)}")
