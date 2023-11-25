# Q1
def change_sort():
    arr1 = [1, 2, 5, 4, 3]
    arr2 = [5, 5, 6, 6, 5]
    k = 3

    arr1.sort()
    arr2.sort(reverse=True)

    for i in range(k):
        if arr1[i] < arr2[i]:
            arr1[i], arr2[i] = arr2[i], arr1[i]
        else:
            break

    print(sum(arr1))

if __name__ == '__main__':
    change_sort()