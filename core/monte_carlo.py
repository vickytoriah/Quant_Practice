import core.utility as ut
import numpy as np
import functools as ft

pd = ut.pd


class MonteCarlo(object):
    def __init__(
            self,
            objective_func,
            random_walk_upper_limit=5,
            random_walk_lower_limit=1,
            iterations=100,
    ):
        self._memory = []
        self.objective_func = objective_func
        self.iterations = iterations
        self.random_walk_upper_limit = random_walk_upper_limit
        self.random_walk_lower_limit = random_walk_lower_limit
        self.random_walk = self.simulator_random_walk()
        ft.update_wrapper(
            self,
            objective_func,
        )

    def __call__(
            self,
            question_conditions,
    ):
        """
        makes the class callable, otherwise it would only be initialised as a class object when used
        :param question_conditions:
        :return:
        """
        print(question_conditions)
        self._memory.clear()

        def wrapper(*args, **kwargs):
            for i in range(self.iterations):
                self.random_walk = self.simulator_random_walk()
                simulated_output = self.objective_func(
                    self.random_walk,
                    *args,
                    **kwargs,
                )
                self._memory.append(simulated_output)
            return pd.DataFrame(self._memory, columns=['runtime_sec'])

        return wrapper

    def memory(self):
        return self._memory

    def simulator_random_walk(
            self,
    ):
        random_walk = np.random.randint(
            self.random_walk_lower_limit,
            self.random_walk_upper_limit,
            self.iterations,
        )

        return random_walk
