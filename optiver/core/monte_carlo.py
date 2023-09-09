import optiver.core.utility as ut
import numpy as np
import functools as ft

pd = ut.pd


class MonteCarlo(object):
    def __init__(
            self,
            objective_func,
            # conditions,
            random_walk_upper_limit=5,
            random_walk_lower_limit=1,
            iterations=100,
    ):
        ft.update_wrapper(
            self,
            objective_func,
        )
        self._memory = []
        self.objective_func = objective_func
        # if [*random_walk_lower_limit, random_walk_upper_limit, iterations] is not None:
        self.iterations = iterations
        # self.conditions = conditions
        self.random_walk_upper_limit = random_walk_upper_limit
        self.random_walk_lower_limit = random_walk_lower_limit
        self.random_walk = self.simulator_random_walk()
        # else:
        #     self.iterations = 10
        #     self.random_walk_upper_limit = 5
        #     self.random_walk_lower_limit = 1
        #     self.conditions = 1

    # todo: call needs the question conditions
    def __call__(
            self,
            question_conditions,
            # random_walk
            # **kwargs,
    ):
        print(question_conditions)
        # self.conditions += 1
        # running_func = self.objective_func(*args, **kwargs)
        self._memory.clear()

        def wrapper(*args, **kwargs):
            for i in range(self.iterations):
                self.random_walk = self.simulator_random_walk()
                simulated_output = self.objective_func(
                    self.random_walk,
                    *args,
                    **kwargs,
                    # question_conditions,
                    # **kwargs,
                )
                # self._memory.append(simulated_output.__getitem__(i - 1))
                self._memory.append(simulated_output)
            return pd.DataFrame(self._memory, columns=['runtime_sec'])
            # simulated_output
            # simulated_output

        return wrapper

        # return self.simulator_random_walk()

    def memory(self):
        return self._memory

    def simulator_random_walk(
            self,
            # *args,
            # **kwargs,
    ):
        """

        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        """
        output_list = []
        random_walk = np.random.randint(
                        self.random_walk_lower_limit,
                        self.random_walk_upper_limit,
                        self.iterations,
                    )
        return random_walk