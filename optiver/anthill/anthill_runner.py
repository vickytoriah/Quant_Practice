import optiver.anthill.anthill_1 as ah
import optiver.core.monte_carlo as mc

#
# @mc.MonteCarlo(conditions='q1',random_walk_upper_limit=5,random_walk_lower_limit=1,iterations=10)
anthill1 = ah.anthill_model(
    question_conditions='q1'
)

ah1 = anthill1(
    # nsew_dict=nsew_dict,
    question_conditions='q1',
).describe()

anthill2 = ah.anthill_model(
    question_conditions='q2'
)

ah2 = anthill2(
    # nsew_dict=nsew_dict,
    question_conditions='q2',
).describe()

# anthill2 = anthill.__setattr__('question_conditions', 'q2')
anthill3 = ah.anthill_model(
    question_conditions='q3'
)

ah3 = anthill3(
    question_conditions='q3'
).describe()
#
# anthill_q1 = mc.MonteCarlo(
#     conditions='q1',
#     iterations=2,
#     _objective_func=anthill,
#     random_walk_lower_limit=5,
#     random_walk_upper_limit=1,
# )

breakpoint()


# run_avg = anthill_q1.mean()
# print(run_avg)
# need to now create the backtesting bit, like average on it.
breakpoint()