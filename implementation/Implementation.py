# Q1. 상하좌우

def imp1(n, input):

    direction = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    x, y = 1, 1
    walk = input.split()

    for w in walk:
        for d in range(len(direction)):
            if w == direction[d]:
                new_dx = x + dx[d]
                new_dy = y + dy[d]
        if new_dx > n or new_dx < 1 or new_dy > n or new_dy < 1:
            continue

        x, y = new_dx, new_dy

    print(x, y)

# Q2. 시각

def time(n):
    result = 0
    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h) or '3' in str(m) or '3' in str(s):
                    result += 1
    print(result)

# Q3. 왕실의 나이트
def knight(input):
    result = 0
    direction = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    replace_direction = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
    x, y = replace_direction[list(input)[0]], int(list(input)[1])

    for d in range(len(direction)):
        new_dx, new_dy = x + direction[d][0], y + direction[d][1]
        if 1 <= new_dx <= 8 and 1 <= new_dy <= 8:
            result += 1

    print(result)

# Q4. 문자열 재정렬
def replacement(input):
    visited = []
    sum = 0
    for i in input:
        if i.isalpha():
            visited.append(i)
        else:
            sum += int(i)
    visited.sort()
    visited.append(str(sum))
    print(''.join(visited))

if __name__ == '__main__':
    imp1(5, 'R R R U D D')
    time(5)
    knight('a1')
    replacement('K1KA5CB7')

