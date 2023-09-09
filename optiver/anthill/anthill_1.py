import pandas as pd
import numpy as np
import typing as ty
# import optiver.anthill.anthill_runner as ar
import optiver.core.monte_carlo as mc

from abc import ABC, abstractmethod
from progressbar import ProgressBar


north_dict = dict(  # north
    x_moves=0,
    y_moves=10,
)

south_dict = dict(  # south
    x_moves=0,
    y_moves=-10,
)

east_dict = dict(  # east
    x_moves=10,
    y_moves=0,
)

west_dict = dict(  # west
    x_moves=-10,
    y_moves=0,
)


nsew_dict = (
    {
        1: north_dict,
        2: south_dict,
        3: east_dict,
        4: west_dict,
    }
)


@mc.MonteCarlo
def anthill_model(
        # output: list,
        # directional_dict: dict,
        # nsew_dict: ty.Dict = None,
        # dir_dist: pd.DataFrame,
        question_conditions: str | int = None,
        random_walk: np.ndarray = None,
):
    """

    :param random_walk:
    :param question_conditions:
    :param nsew_dict:
    :return:
    :rtype:
    """
    times = []
    dir_dist = pd.DataFrame(
        [[0, 0]],
        # index=[0],
        columns=['x_moves', 'y_moves'],
    )

    for dist in random_walk:
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
            question_conditions=question_conditions,
        )
        # len(moves_df) !=
        found_check = food_found.dropna(axis=0, how='any')

        # if food_found.notnull():

        if len(moves_df) != len(found_check):
            # found = True
            t_sec = len(moves_df['x_moves'])
            times.append(t_sec)
            # timing[iter_count] = t_sec
            break
        else:
            dir_dist = moves_df.copy()
            continue
    return times


def cond_checker(
        moves_df: pd.DataFrame,
        question_conditions: str | int,
):
    """

    :param moves_df:
    :type moves_df:
    :param question_conditions:
    :type question_conditions:
    :return:
    :rtype: bool
    """
    dist_df = moves_df.loc[:, ['x_dist', 'y_dist']]

    if question_conditions == 1 or question_conditions == 'q1':
        conditions_met = _cond_q1(dist_df=dist_df)

    elif question_conditions == 2 or question_conditions == 'q2':
        conditions_met = _cond_q2(dist_df=dist_df)
    elif question_conditions == 3 or question_conditions == 'q3':
        conditions_met = _cond_q3(dist_df=dist_df)
    else:
        raise ValueError(f'Unknown Question Reference: {question_conditions}')

    # this is the whole column, need to do the row
    # if moves_df['x_dist'].abs() == threshold_cond or moves_df.abs()['y_dist'] == threshold_cond:
    #     found = True
    # else:
    #     found = False
    matched_df = dist_df[~conditions_met]
    return matched_df


def _cond_q1(
        dist_df: pd.DataFrame,
):
    dist_df_abs = dist_df.abs()
    found_bool = dist_df_abs == 20
    return found_bool


def _cond_q2(
        dist_df: pd.DataFrame,
):
    coord_sum = dist_df.sum(axis='rows')
    found_bool = coord_sum == 10
    return found_bool


def _cond_q3(
        dist_df: pd.DataFrame,
):
    """
    boundary function assumed to be:
    ((x-2.5)/20)^2 + ((y-2.5)/40)^2 < 1
    so outside of it would be:
    ((x-2.5)/20)^2 + ((y-2.5)/40)^2 >= 1
    :param dist_df:
    :type dist_df:
    :return:
    :rtype:
    """
    boundary_function = ((dist_df['x_dist'] - 2.5) / 20) ** 2 + ((dist_df['y_dist'] - 2.5) / 40) ** 2 >= 1
    # found_bool = coord_sum == 10
    return boundary_function
