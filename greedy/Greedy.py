# Q2. 거스름 돈 문제

def change(input):
    money = input
    list = [500, 100, 50, 10]
    result = 0
    for l in list:
        result += money // l
        money %= l
    print(result)

# Q3. 1이 될 때 까지

def until_one(N, K):
    result = 0
    while N != 1:
        if N % K == 0:
            N = N // K
            result += 1
        else:
            N -= 1
            result += 1

    print(result)

# Q4. 곱하기 혹은 더하기

def multi_or_plus(input):
    arr = list(input)
    arr.sort(reverse=True)
    result = int(arr[0])
    for a in range(1, len(arr)):
        if int(arr[a]) >= 2:
            result *= int(arr[a])
        else:
            result += int(arr[a])

    print(result)

if __name__ == '__main__':
    change(1260)
    until_one(17, 4)
    multi_or_plus("2231")

