import pandas as pd


def results_calculator(
        output_df: pd.DataFrame,
        function_ran,
        results_origin: str = None,
        # return_results: bool = True,
        print_bool: bool = True,
):
    """

    :param output_df:
    :type output_df:
    :param function_ran:
    :type function_ran:
    :param results_origin:
    :type results_origin:
    :param print_bool:
    :type print_bool:
    :return:
    :rtype:
    """
    if output_df is None:
        raise ValueError(f'No data to run on.')
    raw_data = output_df.copy()
    # mean_results = output_list.mean()
    stats_analysis = raw_data.describe()

    if print_bool:
        if results_origin is not None:
            print(f"{results_origin}'s results for {function_ran.__name__}: \n {stats_analysis}.")
        else:
            print(f"The results for {function_ran.__name__}: \n {stats_analysis}.")
    return stats_analysis


def simulation_decorator(
        objective_function,
        _selected_function=None,
):
    """
A decorator that can be used for functions with and without specific conditions.
Where it is called without an argument, it runs as normal and returns the function undecorated,
if it is called with an argument, the returned function is modified accordingly
    :param objective_function: function to run simulator one
    :type objective_function:
    :param _selected_function: if a specific parameter exists in the objective function, this detail is used
    :type _selected_function:
    :return:
    :rtype:
    """

    def sim_wrapper(
            *args,
            **kwargs,
    ):
        """

        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        """
        simulated_output = objective_function(
            _selected_function,
            *args,
            **kwargs,
        )
        return simulated_output

    if _selected_function is None:
        return sim_wrapper
    else:
        return sim_wrapper(_selected_function)

# def output_debugger(
#         original_func,
# ):
#     """
#
#     :param original_func:
#     :return:
#     :rtype:
#     """
#     @ft.wraps(original_func)
#     def func_info_logger(
#             *args,
#             **kwargs,
#     ):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
#         signature = ', '.join(args_repr + kwargs_repr)
#         print(f'Running {} with the args: {}, and the kwargs: {})'.format(original_func.__name__, args, kwargs))
#         # args_repr, kwargs_repr))
#         value = original_func(*args, **kwargs)
#         print(f'{original_func.__name__!r} returned {value!r}')
#         # original_func(*args, **kwargs)
#         return original_func(*args, **kwargs)
#     return func_info_logger
