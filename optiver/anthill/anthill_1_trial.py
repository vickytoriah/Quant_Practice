import pandas as pd
import numpy as np
import typing as ty
import optiver.core as ut

from abc import ABC, abstractmethod
from progressbar import ProgressBar

times = []


class AntHillFoodFinder(
    ABC,
):
    def __init__(
            self,
            iterations: int,
            random_walk: np.ndarray[int],
            times: list,
            directional_dict: dict,
    ):
        self.iterations = iterations
        self.random_walk = random_walk
        self.times = times
        self.directional_dict = directional_dict

    def time_runner(
            self,
            # run_times: int,
            # food_found: bool = False,
    ):
        """
    runner of simulation
        :param run_times:
        :type run_times:
        :return:
        :rtype:
        """
        timing = []
        dir_dist = pd.DataFrame(
            [[0, 0]],
            # index=[0],
            columns=['x_moves', 'y_moves'],
        )

        for i in range(self.iterations):
            rand_list = np.random.randint(1, 5, run_times)
            print(rand_list)
            t_sec_list = direction_distance(
                # iter_count=i,
                nsew=rand_list,
                dir_dist=dir_dist,
                threshold_cond=20,
            )
            # need to append to get it out of the loop, but can just create df with times
            # instead of getting the t-sec list item, u need do the average of each iteration and then append to sth else
            timing.append(t_sec_list.__getitem__(i-1))
        return pd.DataFrame(timing, columns=['runtime_sec'])

    def direction_distance(
            # nsew_dict: ty.Dict,
            self,
            nsew: np.ndarray,
            dir_dist: pd.DataFrame,
            threshold_cond: int,
    ):
        """

        :param threshold_cond:
        :type threshold_cond:
        :param nsew:
        :param dir_dist:
        :return:
        :rtype:
        """

        for dist in nsew:
            direction = nsew_dict.__getitem__(dist)
            # print(direction)
            coords = pd.DataFrame(
                [direction.values()],
                # index=[dist],
                columns=[*direction.keys()],
            )
            moves_df = pd.concat(
                [
                    dir_dist,
                    coords,
                ],
                axis=0,
                names=['x_moves', 'y_moves'],
                ignore_index=True,
            )
            moves_df['x_dist'] = moves_df['x_moves'].cumsum()
            moves_df['y_dist'] = moves_df['y_moves'].cumsum()

            food_found = cond_checker(
                moves_df=moves_df,
                threshold_cond=threshold_cond,
            )
            # len(moves_df) !=
            found_check = food_found.dropna(axis=0, how='any')
            #if food_found.notnull():
            if len(moves_df) != len(found_check):
                found = True
                t_sec = len(moves_df['x_moves'])
                times.append(t_sec)
                # timing[iter_count] = t_sec
                break
            else:
                dir_dist = moves_df.copy()
                continue
        return times
        # return dir_dist_df

    def cond_checker(
            self,
            moves_df: pd.DataFrame,
            threshold_cond: int,
    ):
        """

        :param moves_df:
        :type moves_df:
        :param threshold_cond:
        :type threshold_cond:
        :return:
        :rtype: bool
        """
        dist_df = moves_df.loc[:, ['x_dist', 'y_dist']]
        dist_df_abs = dist_df.abs()
        found_bool = dist_df_abs == threshold_cond

        # this is the whole column, need to do the row
        # if moves_df['x_dist'].abs() == threshold_cond or moves_df.abs()['y_dist'] == threshold_cond:
        #     found = True
        # else:
        #     found = False
        matched_df = dist_df[~found_bool]
        return matched_df

