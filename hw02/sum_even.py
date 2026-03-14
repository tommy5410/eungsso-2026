nums = [x for x in range(1, 101) if x % 2 == 0]
result1 = sum(nums)
print(f"지능형 리스트 결과: {result1}")

result2 = 0
for i in range(1, 101):
    if i % 2 == 0:
        result2 += i
print(f"결과: {result2}")