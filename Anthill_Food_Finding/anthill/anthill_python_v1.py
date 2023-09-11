import pandas as pd
import numpy as np

times = []

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


def time_runner(
        run_times: int,
        question_conditions: int | str,
):
    """
runner of simulation
    :param run_times:
    :param question_conditions:
    :return:
    :rtype:
    """
    timing = []
    dir_dist = pd.DataFrame(
        [[0, 0]],
        columns=['x_moves', 'y_moves'],
    )

    for i in range(run_times):
        rand_list = np.random.randint(1, 5, run_times)
        print(rand_list)
        t_sec_list = direction_distance(
            nsew=rand_list,
            dir_dist=dir_dist,
            question_conditions=question_conditions,
        )
        timing.append(t_sec_list.__getitem__(i-1))
    return pd.DataFrame(timing, columns=['runtime_sec'])


def direction_distance(
        nsew: np.ndarray,
        dir_dist: pd.DataFrame,
        question_conditions: int | str,
):
    """

    :param question_conditions:
    :type question_conditions:
    :param nsew:
    :param dir_dist:
    :return:
    :rtype:
    """

    for dist in nsew:
        direction = nsew_dict.__getitem__(dist)
        coords = pd.DataFrame(
            [direction.values()],
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

        found_check = food_found.dropna(axis=0, how='any')

        if len(moves_df) != len(found_check):

            t_sec = len(moves_df['x_moves'])
            times.append(t_sec)

            break
        else:
            dir_dist = moves_df.copy()
            continue
    return times


def cond_checker(
        moves_df: pd.DataFrame,
        question_conditions: int,
):
    """

    :param moves_df:
    :type moves_df:
    :param question_conditions:
    :type question_conditions:
    :return:
    :rtype: pd.DataFrame
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

    if not question_conditions == 2:
        matched_df = dist_df[~conditions_met]
    else:
        matched_df = dist_df[~conditions_met['coord_sum']]
    dist_df_abs = dist_df.abs()

    found_bool = dist_df_abs == question_conditions
    matched_df = dist_df[~found_bool]

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
    coord_sum = dist_df['x_dist'] + dist_df['y_dist']
    coord_df = coord_sum.to_frame('coord_sum')

    found_bool = coord_df == 10
    found_bool['filler'] = 0

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

    return boundary_function
