import math

'''
Jump Search function
Arguments:
A    - The source list
item - Element for which the index needs to be found
'''


def jump_search(A, item):
    print("Entering Jump Search")
    n = len(A)
    m = int(math.sqrt(n))
    i = 0

    while i != len(A)-1 and A[i] < item:
        print("Processing Batch - {}".format(A[i: i+m]))
        if A[i+m-1] == item:
            return i+m-1
        elif A[i+m-1] > item:
            B = A[i: i+m-1]
            return linear_search(B, item, i)
        i += m

    B = A[i:i+m]
    print("Processing Batch - {}".format(B))
    return linear_search(B, item, i)


'''
Linear Search function
Arguments:
B    - The derived list
item - Element for which the index needs to be found
loc  - The Index where the remaining batch begins
'''


def linear_search(B, item, loc):
    print("\t Entering Linear Search")
    i = 0

    while i != len(B):
        if B[i] == item:
            return loc+i
        i += 1
    return -1


if __name__ == "__main__":
    A = [1, 2, 3, 5, 9, 22, 36, 76, 123, 124, 1345, 1345]
    # print (jump_search(A, 124))
    print(jump_search(A, 1345))
