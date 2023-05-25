
from screen_state_machine import ScreenFSM
from discriminate_objects_task_state_machine import DiscriminateObjectsTaskFSM

import numpy as np


class Initialisation:
    def __init__(self, objects_types='Checkered', punish_time=7):

        self.update_constant_seconds = 10
        self.objects_types = objects_types
        self.punish_time = punish_time * self.update_constant_seconds

        self.screen_fsm = self.get_screen_fsm(previous_success=False, number_of_successful_trials=0)
        self.task_fsm = self.get_task_fsm(number_of_successful_trials=0)

    def get_init_values(self):

        

        return

    def get_screen_fsm(self, previous_success, number_of_successful_trials):
        target_angle, trap_angle, manip_angle, speed, angle_dif_between_man_and_target_trap = \
            self.get_init_values()

        self.screen_fsm = ScreenFSM(target_angle, trap_angle, manip_angle, speed, angle_dif_between_man_and_target_trap,
                                    catch_trial=self.catch_trial)

        return self.screen_fsm

    def get_task_fsm(self, number_of_successful_trials=0):
        self.task_fsm = DiscriminateObjectsTaskFSM(screen_fsm=self.screen_fsm)
        return self.task_fsm
