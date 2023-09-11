import Anthill_Food_Finding.anthill.anthill_python_v1 as ah1

q1_anthill = ah1.time_runner(
    run_times=10000,
    question_conditions='q1'
)
desc_q1 = q1_anthill.mean()

q2_anthill = ah1.time_runner(
    run_times=10000,
    question_conditions='q2',
)
desc_q2 = q2_anthill.mean()

q3_anthill = ah1.time_runner(
    run_times=10000,
    question_conditions='q3',
)
desc_q3 = q3_anthill.mean()

breakpoint()
