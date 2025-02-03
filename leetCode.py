# sorted array
nums = list(map(int, input("Masukan Array: ").split()))
hasil = []
for i in nums:
    if i not in hasil:
        hasil.append(nums[i])
print(hasil)