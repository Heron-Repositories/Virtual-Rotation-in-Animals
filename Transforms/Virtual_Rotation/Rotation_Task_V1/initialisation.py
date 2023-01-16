
from screen_state_machine import ScreenFSM
from wait_to_match_task_state_machine import WaitToMatchTaskFSM
from button_to_match_with_trap_task_state_machine import ButtonToMatchWithTrapTaskFSM

import numpy as np


class Initialisation:
    def __init__(self, task_description='Wait', vert_or_hor='random', speed=20, angle_dif_between_man_and_target_trap=10,
                 time_to_target=0.5, punish_time=7):
        assert task_description == 'PokeAndWait' or task_description == 'PokeAndButton', \
        print('Wrong Task {} in the Initialisation object'.format(task_description))
        assert vert_or_hor == 'random' or vert_or_hor == 'vertical' or vert_or_hor == 'horizontal', \
            print('Wrong vert_or_hor value {} in the Initialisation object'.format(vert_or_hor))

        self.task_description = task_description
        self.speed = int(speed / 10)
        self.angle_dif_between_man_and_target_trap = angle_dif_between_man_and_target_trap
        self.vert_or_hor = vert_or_hor
        self.time_to_target = time_to_target
        self.punish_time = punish_time * 10
        self.target_angle: int
        self.trap_angle: int
        self.manip_angle: int

        self.setup_angles()

        self.screen_fsm = self.get_screen_fsm(previous_success=False)
        self.task_fsm = self.get_task_fsm()

    def setup_angles(self):
        if self.vert_or_hor == 'vertical':
            self.target_angle = 90
            self.trap_angle = 1
        elif self.vert_or_hor == 'horizontal':
            self.target_angle = 1
            self.trap_angle = 90
        elif self.vert_or_hor == 'random':
            self.target_angle = np.random.choice([1, 90])
            self.trap_angle = 90 if self.target_angle == 1 else 1

        self.manip_angle = int((self.time_to_target * 10) * self.speed) if self.target_angle == 1 else \
            90 - int((self.time_to_target * 10) * self.speed)

        print('Speed = {}, Time to target = {}'.format(self.speed, self.time_to_target))
        #print('Manip = {}, Target = {}, Trap = {}'.format(self.manip_angle, self.target_angle, self.trap_angle))
        #print('-------------------')

    def get_init_values(self, previous_success):

        if previous_success and self.task_description == 'PokeAndWait':
            self.time_to_target = self.time_to_target * 1.01

        self.setup_angles()

        return self.target_angle, self.trap_angle, int(self.manip_angle), \
               self.speed, self.angle_dif_between_man_and_target_trap

    def get_screen_fsm(self, previous_success):
        target_angle, trap_angle, manip_angle, speed, angle_dif_between_man_and_target_trap = \
            self.get_init_values(previous_success)
        self.screen_fsm = ScreenFSM(target_angle, trap_angle, manip_angle, speed, angle_dif_between_man_and_target_trap)

        return self.screen_fsm

    def get_task_fsm(self):
        if self.task_description == 'PokeAndWait':
            self.task_fsm = WaitToMatchTaskFSM(screen_fsm=self.screen_fsm)
        elif self.task_description == 'PokeAndButton':
            self.task_fsm = ButtonToMatchWithTrapTaskFSM(screen_fsm=self.screen_fsm)
        return self.task_fsm

