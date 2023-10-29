import Codility.solution_classes.Cyclic_Rotation_solution as cr
import core.utility as ut

unittest = ut.unittest

ARRAY_RANGE = (-1000, 1000)
INT_RANGE = (0, 100)


class TestCyclicRotation(ut.unittest.TestCase):
    def _init_(
            self,
            # unittester = ut.unittest.TestCase
            # ut.unittest.TestCase,
    ):
        self.array_range = (-1000, 1000)
        self.int_range = (0, 100)
        # self.unittester = ut.unittest.TestCase,

    def test_examples(self):
        self.assertEqual(cr.solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertEqual(cr.solution([0, 0, 0], 1), [0, 0, 0])
        self.assertEqual(cr.solution([1, 2, 3, 4], 4), [1, 2, 3, 4])

    def test_zero(self):
        self.assertEqual(cr.solution([6, 3, 8, 9, 7], 0), [6, 3, 8, 9, 7])

    def test_one(self):
        self.assertEqual(cr.solution([6, 3, 8, 9, 7], 1), [7, 6, 3, 8, 9])

    def test_full(self):
        self.assertEqual(cr.solution([6, 3, 8, 9, 7], 5), [6, 3, 8, 9, 7])

    def test_empty(self):
        self.assertEqual(cr.solution([], 5), [])

    def test_random(self):
        N = ut.random.randint(*self.int_range)
        K = ut.random.randint(*self.int_range)
        A = [ut.random.randint(*self.array_range) for _ in range(0, N)]
        print(K, A)
        print(cr.solution(A, K))
