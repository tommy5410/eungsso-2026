def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False  
            
    return True


limit = int(input("찾고싶은 소수의 범위를 알려주세요: "))
prime_list = []

for i in range(1, limit + 1):
    if is_prime(i):
        prime_list.append(i)
print(f"1부터 {limit}까지의 소수: {prime_list}")