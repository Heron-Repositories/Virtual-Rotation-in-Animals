
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


    def get_object_positions(self):

        possibilities = np.zeros(10)
        if 'Checkered' in self.objects_types:
            possibilities[[1, 4, 7]] = 1
        if 'White' in self.objects_types:
            possibilities[[2, 5, 8]] = 1
        if 'Black' in self.objects_types:
            possibilities[[3, 6, 9]] = 1

        type_of_line = np.argmax(np.random.random(3)*possibilities[1:4])
        type_of_not_line = np.argmax(np.random.random(6) * possibilities[4:])
        line_position = 400 * np.sign(np.random.random() - 0.5)
        other_position = - line_position

        positions = np.zeros(10)
        positions[type_of_line + 1] = line_position
        positions[type_of_not_line + 4] = other_position

        return positions

    def get_screen_fsm(self, previous_success, number_of_successful_trials):
        positions = self.get_object_positions()

        self.screen_fsm = ScreenFSM(show_objects_at_positions=positions)

        return self.screen_fsm

    def get_task_fsm(self, number_of_successful_trials=0):
        self.task_fsm = DiscriminateObjectsTaskFSM(screen_fsm=self.screen_fsm)
        return self.task_fsm
