def ant():
    n = 4
    arr = [1, 3, 1, 5]

    dp_table = [0] * 100

    dp_table[0] = arr[0]
    dp_table[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp_table[i] = max(dp_table[i] + dp_table[i - 2], dp_table[i - 1])

    print(dp_table[n-1])

if __name__ == '__main__':
    ant()