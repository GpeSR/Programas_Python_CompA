import os, random

MAX = 20

def genale():
    nums = []
    for i in range(MAX):
        nums.append(random.randint(1,10))
    return nums

def sumalistas(l1, l2):
    ls = []
    for i in range(MAX):
        ls.append( l1[i] + l2[i] )
    return ls

# Programa principal
os.system("cls")

nums1 = genale()
nums2 = genale()
lsuma = sumalistas(nums1, nums2)

print(f"Lista 1: \n {nums1} , {len(nums1)}")
print(f"\nLista 2: \n {nums2} , {len(nums2)}")
print(f"\nsuma: \n {lsuma} , {len(lsuma)}\n")
