import pandas as pd
import numpy as np
import typing as ty

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
        food_found: bool = False,
        run_times: int,
):
    """
asd
    :param food_found:
    :type food_found:
    :param rand_list:
    :type rand_list:
    :return:
    :rtype:
    """
    timing = []
    dir_dist = pd.DataFrame([0, 0], index=None, columns=['x_moves', 'y_moves'])
    for i in range(run_times):
        rand_list = np.random.randint(1, 4, run_times)
        t_sec_list = direction_distance(
            iter_count=i,
            nsew=rand_list,
            dir_dist_in=dir_dist,
            threshold_cond=20,
        )
        timing.append(t_sec_list.__getitem__(i))
    return pd.concat(pd.Series(timing), axis=1, names=['runtime_sec'])


def direction_distance(
        # nsew_dict: ty.Dict,
        iter_count: int,
        nsew: np.ndarray,
        dir_dist_in: pd.DataFrame,
        threshold_cond: int,
):
    """

    :param iter_count:
    :type iter_count:
    :param nsew:
    :param dir_dist:
    :return:
    :rtype:
    """
    timing = []
    for dist in nsew:
        direction = nsew_dict.__getitem__(dist)
        print(direction)
        coords = pd.DataFrame([*direction])
        moves_df = pd.concat(
            [
                dir_dist,
                coords,
            ],
            axis=0,
            names=['x_moves', 'y_moves'],
        )
        moves_df['x_dist'] = moves_df['x_moves'].cumsum()
        moves_df['y_dist'] = moves_df['y_moves'].cumsum()

        food_found = cond_checker(
            moves_df=moves_df,
            threshold_cond=threshold_cond,
        )
        if len(moves_df) != sum(food_found):
            found = True
            t_sec = len(moves_df)
            timing.append(t_sec)
            # timing[iter_count] = t_sec
            break
        else:
            continue
    return timing
    # return dir_dist_df


def cond_checker(
        moves_df: pd.DataFrame,
        threshold_cond: int,
):
    """

    :param moves_df:
    :type moves_df:
    :param threshold_cond:
    :type threshold_cond:
    :return:
    :rtype:
    """
    dist_df = moves_df.loc[:, ['x_dist', 'y_dist']]
    dist_df_abs = dist_df.abs()
    found_bool = dist_df_abs == threshold_cond

    # this is the whole column, need to do the row
    # if moves_df['x_dist'].abs() == threshold_cond or moves_df.abs()['y_dist'] == threshold_cond:
    #     found = True
    # else:
    #     found = False

    return found_bool

