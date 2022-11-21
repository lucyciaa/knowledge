from collections import Counter

if __name__ == '__main__':


    a = [[1, 2, 3, 1, 1, 2],[1, 2, 3, 1, 1, 2]]
    b = []
    for l in a:
        b += l
    print(b)
    result = Counter(b)
    print(result)

