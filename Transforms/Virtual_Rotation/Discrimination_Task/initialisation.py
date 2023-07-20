
from screen_state_machine import ScreenFSM
from discriminate_objects_task_state_machine import DiscriminateObjectsTaskFSM

import numpy as np


class Initialisation:
    def __init__(self, objects_types='Checkered', punish_time=7):

        self.update_constant_seconds = 10
        self.side_probability = 0.5
        self.objects_types = objects_types
        self.punish_time = punish_time * self.update_constant_seconds

        self.screen_fsm = self.get_screen_fsm(previous_success=False, number_of_successful_trials=0)
        self.task_fsm = self.get_task_fsm(number_of_successful_trials=0)



    def get_object_positions_and_rotations(self):

        possibilities = np.zeros(10)
        if 'Checkered' in self.objects_types:
            possibilities[[1, 4, 7]] = 1
        if 'White' in self.objects_types:
            possibilities[[2, 5, 8]] = 1
        if 'Black' in self.objects_types:
            possibilities[[3, 6, 9]] = 1

        type_of_line = np.argmax(np.random.random(3)*possibilities[1:4]) + 1
        type_of_not_line = np.argmax(np.random.random(6) * possibilities[4:]) + 4
        line_position = 400 * np.sign(np.random.binomial(n=1, p=self.side_probability) - 0.2)
        other_position = - line_position

        positions_and_rotations = np.zeros(20)
        positions_and_rotations[type_of_line] = line_position
        positions_and_rotations[type_of_not_line] = other_position

        positions_and_rotations[type_of_line + 10] = np.random.randint(0, 90)
        positions_and_rotations[type_of_not_line + 10] = np.random.randint(0, 90)

        return positions_and_rotations

    def get_screen_fsm(self, previous_success, number_of_successful_trials):
        positions_and_rotations = self.get_object_positions_and_rotations()

        self.screen_fsm = ScreenFSM(show_objects_at_positions=positions_and_rotations)

        return self.screen_fsm

    def get_task_fsm(self, number_of_successful_trials=0):
        self.task_fsm = DiscriminateObjectsTaskFSM(screen_fsm=self.screen_fsm)
        return self.task_fsm
