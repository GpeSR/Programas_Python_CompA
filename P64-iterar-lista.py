# Iterar sobre los elementos de una lista de numeros

import os; os.system("cls")

nums = [2, 4, 6, 8, 10, 12, 14, 16]
print("Iterar por los elementos de una lista de numeros existente \n")
print(f"Los numeros: {nums}, {len(nums)}")

print("\nIterar por los elementos usando for: ")
for num in nums: 
    print("# :", num, num*2)

print("\nIterar por indice ")
for i in range(len(nums)):
    print("> ", nums[i], nums[i]*3)

print("\nIterar por indice y elevar al cuadrado ")
for i in range(len(nums)):
    nums[i] = nums[i] ** 2

print(f"Los numeros: {nums}, {len(nums)}")
