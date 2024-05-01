
def suma(numeros):
    s = 0
    for n in numeros:
        s += n
    return s

nums = [10,20,30,40,50,60,70]

res = suma(nums)

print("La suma es ",res)