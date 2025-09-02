# table with 10 buckets
my_list = [[] for _ in range(10)]

def hash_function(name: str) -> int:
    # simple hash: sum of code points, then mod bucket count
    return sum(ord(c) for c in name) % len(my_list)

def storeInHash(name: str) -> None:
    idx = hash_function(name)
    bucket = my_list[idx]
    if name not in bucket:          # optional: avoid duplicates
        bucket.append(name)          # append INTO the bucket

def isPresent(name: str) -> bool:
    idx = hash_function(name)
    bucket = my_list[idx]
    return name in bucket            # check within the bucket
