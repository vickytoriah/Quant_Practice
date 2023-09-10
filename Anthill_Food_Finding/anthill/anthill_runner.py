import Anthill_Food_Finding.anthill.anthill_1 as ah
import Anthill_Food_Finding.core.monte_carlo as mc

anthill1 = ah.anthill_model(
    question_conditions='q1'
)

ah1 = anthill1(
    question_conditions='q1',
).describe()

anthill2 = ah.anthill_model(
    question_conditions='q2'
)

ah2 = anthill2(
    question_conditions='q2',
).describe()

anthill3 = ah.anthill_model(
    question_conditions='q3'
)

ah3 = anthill3(
    question_conditions='q3'
).describe()

breakpoint()
