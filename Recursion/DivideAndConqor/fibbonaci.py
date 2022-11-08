# def fibb(num):
#     return 5
def fibb(num,cache={}):
    if num in cache.keys():
        return cache[num]
    else:
        if num < 2:
            cache[num]=num
            return cache[num]
        else:
            cache[num]=fibb(num-1,cache)+fibb(num-2,cache)
            print(cache)
            return cache[num]



print(fibb(10))