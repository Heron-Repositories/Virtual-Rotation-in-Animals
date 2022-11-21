

import numpy as np
from button_to_match_with_trap_task_state_machine import ButtonToMatchWithTrapTaskFSM
from screen_state_machine import ScreenFSM
from wait_to_match_task_state_machine import WaitToMatchTaskFSM
from experiment_state_machine import ExperimentFSM

def testing_for_wait_task():
    target_angle = np.random.randint(10, 80)
    trap_angle = 90
    manip_angle = 0
    speed = 5
    angle_dif_between_man_and_target_trap = 10

    return target_angle, trap_angle, manip_angle, speed, angle_dif_between_man_and_target_trap
