def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

num = int(input("팩토리얼을 구할 숫자를 입력하세요: "))

result = fact(num)
print(f"{num}!의 결과는 {result}입니다.")