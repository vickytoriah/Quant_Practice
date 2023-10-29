"""
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.

"""

def solution(A):
    """
    This creates an empty set, and iterates through A.
    Tries to remove element from unmatched, if not possible, adds it.
    In the end, only 1 item left in the set.
    The return then is the output of set.pop()
    :param A: has (len(A)-1)/2 number of duplicates, odd num of elements
    :type A:
    :return: value of unmatched
    :rtype:
    """
    # Implement your solution here
    unmatched = set()
    for element in A:
        try:
            unmatched.remove(element)
        except KeyError:
            unmatched.add(element)
    return unmatched.pop()


def slow_solution(A):
    # Implement your solution here
    set_A = set(A)
    list_A_uni = list(set_A)
    # print(list_A_uni)

    list_A_uni.sort()
    # print(list_A_uni)
    for i in list_A_uni:
        occur_count = A.count(i)
        odd_even = occur_count % 2

        # print(i, occur_count, odd_even, A, sep='  ')
        if odd_even != 0:
            return i

        A = list(filter(lambda x: x != i, A))
