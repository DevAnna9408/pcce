from bisect import bisect_left, bisect_right

# Q1
def binary_search():
    n, m = 4, 6
    arr = [19, 15, 10, 17]
    # [10, 15, 17, 19]
    arr.sort()

    start = 0
    end = max(arr)
    result = 0

    while(start <= end):
        sum = 0
        mid = (start + end) // 2

        for i in arr:
            if i > mid:
                sum += i - mid

        if sum < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)

def bisect_search():
    arr = [1, 1, 2, 2, 2, 2, 3]

    def count(arr, a, b):
        end = bisect_right(arr, a)
        start = bisect_left(arr, b)
        return end - start

    print(count(arr, 2, 2))

if __name__ == '__main__':
    binary_search()
    bisect_search()



