import numpy as np
import abc
from abc import ABC, abstractmethod
from progressbar import ProgressBar


class BaseAntRandomWalk(
    ABC,
):
    def __init__(
            self,
            ant_number=100000,
            start_x=0.0,
            start_y=0.0,
            dt=1,
            v0=10,
    ):
        """

        :param ant_number:
        :type ant_number:
        :param start_x:
        :type start_x:
        :param start_y:
        :type start_y:
        :param dt:
        :type dt:
        :param v0:
        :type v0:
        """
        self.ant_number = ant_number  # Number of ants we release
        self.start_x, self.start_y = start_x, start_y  # starting x and y coordinate
        self.xy_positions = self.initialize_position_array()  # initialized array of particle positions
        self.time = self.initialize_time_array()  # initialized array of particle time
        self.dt = dt  # integration timestep (seconds)
        self.v0 = v0  # walk speek (cm / s)

    def initialize_position_array(
            self,
    ):
        """

        :return:
        :rtype:
        """
        # Initializing the array in which we store the ants' x and y positions
        xy_positions = np.zeros(shape=(self.ant_number, 2))
        xy_positions[:, 0] = self.start_x
        xy_positions[:, 1] = self.start_y
        print(xy_positions)
        return xy_positions

    def initialize_time_array(
            self,
    ):
        """

        :return:
        :rtype:
        """
        return np.zeros(shape=self.ant_number)

    def random_walk(
            self,
            xy_positions,
    ):
        """

        :param xy_positions:
        :type xy_positions:
        :return:
        :rtype:
        """
        # Generate an array with random integers between 0 - 3 which will set the direction of the random walks
        walk_direction = np.random.randint(
            low=0,
            high=4,
            size=self.ant_number,
        )

        # If walk_direction == 0, move north by v0 * dt
        north = np.where(walk_direction == 0)[0]
        xy_positions[north, 1] += self.dt * self.v0
        # if walk_direction == 1, move south by v0 * dt
        south = np.where(walk_direction == 1)[0]
        xy_positions[south, 1] -= self.dt * self.v0
        # if walk_direction == 2, move east by v0 * dt
        east = np.where(walk_direction == 2)[0]
        xy_positions[east, 0] += self.dt * self.v0
        # if walk_direction == 3, move west by v0 * dt
        west = np.where(walk_direction == 3)[0]
        xy_positions[west, 0] -= self.dt * self.v0

        return xy_positions

    def calculate_walk(
            self,
            steps,
    ):
        """

        :param steps:
        :type steps:
        :return:
        :rtype:
        """
        for i in ProgressBar()(range(steps)): # i not even used, for def is wrong
            # Calculate the random walk procedure
            self.xy_positions = self.random_walk(self.xy_positions)
            # Update the time tracker of each ant
            self.time[~np.isnan(self.xy_positions[:, 0])] += 1
            # Set to np.nan all particles that are at or have crossed the boundary condition
            at_boundary = self.boundary_condition()
            self.xy_positions[at_boundary, :] = np.nan

        return self.xy_positions, self.time

    @abstractmethod
    def boundary_condition(
            self,
    ):
        """

        """
        # Define the specific condition when the ant encounters food
        pass

    def mean_travel_time(
            self,
            steps=1000,
    ):
        """

        :param steps:
        :type steps:
        :return:
        :rtype:
        """
        self.xy_positions, self.time = self.calculate_walk(steps=steps)

        # Determine the particles that are at the food
        at_food = np.isnan(self.xy_positions[:, 0])

        # Calculate the mean time
        mean_time = self.time[at_food].mean()
        std_time = self.time[at_food].std()
        error_time = std_time / np.sqrt(np.sum(at_food))

        # Calculate the number of ants that have reached the food
        at_food_percentage = np.sum(at_food) / self.ant_number * 100

        str_format = steps, mean_time, error_time
        print('After {} seconds, it takes the ant {:.2f}{:.2f} seconds to encounter food.'.format(*str_format))
        print('In this time, {:.2f}% of ants have reached the food.\n'.format(at_food_percentage))


class AntRandomWalkQ1(
    BaseAntRandomWalk,
):
    def __init__(
            self,
    ):
        """

        """
        super().__init__()

    def boundary_condition(
            self,
    ):
        # if either the absolute x or y position is >= 20, then the ant has reached food
        boundary = (np.abs(self.xy_positions[:, 0]) >= 20) | (np.abs(
            self.xy_positions[:, 1]) >= 20)
        return boundary


class AntRandomWalkQ2(
    BaseAntRandomWalk,
):

    def __init__(
            self,
    ):
        """

        """
        super().__init__()

    def boundary_condition(
            self,
    ):
        boundary = np.nansum(self.xy_positions, axis=1) == 10  # not right
        return boundary


class AntRandomWalkQ3(
    BaseAntRandomWalk,
):

    def __init__(
            self,
    ):
        """

        """
        super().__init__()

    def boundary_condition(
            self,
    ):
        boundary = np.square((self.xy_positions[:, 0] - 2.5) / 30) + np.square(
            (self.xy_positions[:, 1] - 2.5) / 40) >= 1
        return boundary


if __name__ == '__main__':
    # Question 1
    AntRandomWalkQ1().mean_travel_time()

    # Question 2
    AntRandomWalkQ2().mean_travel_time(steps=100)
    AntRandomWalkQ2().mean_travel_time(steps=1000)
    AntRandomWalkQ2().mean_travel_time(steps=10000)

    # Question 3
    AntRandomWalkQ3().mean_travel_time()

    breakpoint()
