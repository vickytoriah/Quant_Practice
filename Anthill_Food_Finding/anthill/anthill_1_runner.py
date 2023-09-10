import Anthill_Food_Finding.anthill.anthill_1 as ah1

trial_run1 = ah1.time_runner(
    run_times=10000
)
run_avg = trial_run1.mean()
print(run_avg)

breakpoint()
