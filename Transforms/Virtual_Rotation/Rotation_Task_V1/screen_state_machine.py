import numpy as np
from statemachine import StateMachine, State


class ScreenFSM(StateMachine):
    # Start States
    state_Blank = State("Blank", initial=True)
    state_Show_TTM_Still = State("Show_TTM_Still", initial=False)
    state_Show_Cue = State("Show_Cue", initial=False)
    state_Move_CW = State("Move_CW", initial=False)
    state_Move_CCW = State("Move_CCW", initial=False)
    # End States

    # Start Transitions
    trans_0_b2b = state_Blank.to(state_Blank)
    trans_3_stiil2still = state_Show_TTM_Still.to(state_Show_TTM_Still)
    trans_6_c2c = state_Show_Cue.to(state_Show_Cue)
    trans_1_b2still = state_Blank.to(state_Show_TTM_Still)
    trans_2_still2b = state_Show_TTM_Still.to(state_Blank)
    trans_4_still2c = state_Show_TTM_Still.to(state_Show_Cue)
    trans_5_c2b = state_Show_Cue.to(state_Blank)
    trans_7_still2mcw = state_Show_TTM_Still.to(state_Move_CW)
    trans_8_cw2still = state_Move_CW.to(state_Show_TTM_Still)
    trans_9_mcw2c = state_Move_CW.to(state_Show_Cue)
    trans_10_cw2b = state_Move_CW.to(state_Blank)
    trans_11_mcw2mcw = state_Move_CW.to(state_Move_CW)
    trans_12_mcw2c = state_Move_CW.to(state_Show_Cue)
    trans_13_ccw2ccw = state_Move_CCW.to(state_Move_CCW)
    trans_14_mcw2b = state_Move_CW.to(state_Blank)
    trans_15_still2mccw = state_Show_TTM_Still.to(state_Move_CCW)
    trans_16_mccw2still = state_Move_CCW.to(state_Show_TTM_Still)
    trans_17_mccw2c = state_Move_CCW.to(state_Show_Cue)
    trans_18_mcw2mccw = state_Move_CW.to(state_Move_CCW)
    trans_19_mccw2mcw = state_Move_CCW.to(state_Move_CW)
    trans_20_mccw2b = state_Move_CCW.to(state_Blank)

    # End Transitions

    def __init__(self, target_angle, trap_angle, manip_angle, speed, angle_dif_between_man_and_target_trap,
                 catch_trial=False):
        super().__init__()
        # Start State Variables
        self.target_angle = target_angle
        self.trap_angle = trap_angle
        self.initial_manip_angle = manip_angle
        self.manip_angle = manip_angle
        self.visible_manip_angle = manip_angle
        self.command_to_screen = 'Cue=0, Manipulandum=0, Target=0, Trap=0'
        self.speed = speed
        self.target_reached = False
        self.trap_reached = False
        self.angle_dif_between_man_and_target_trap = angle_dif_between_man_and_target_trap
        self.catch_trial = catch_trial
        self.reward_on_catch_trial = True
        if self.catch_trial:
            # Set the reward_on_catch_trial to reward only 50% of the times (it is read in the worker script)
            self.reward_on_catch_trial = True if np.random.random() > 0.5 else False
            print('CATCH TRIAL with reward: ', self.reward_on_catch_trial)
            # End State Variables

    def step(self, action):

        self.get_visible_manip_angle()

        #print("---- Starting SCREEN state = {}".format(self.current_state.name))
        if False:
            pass

        # Start conditionals
        elif self.current_state == self.state_Blank:
            if False:  # Blank
                pass  # Blank
            elif action == 'blank':
                self.trans_0_b2b(action)
            elif action == 'show_ttm':
                self.trans_1_b2still(action)
        # End of Blank conditional
        elif self.current_state == self.state_Show_TTM_Still:
            if False:  # Show_TTM_Still
                pass  # Show_TTM_Still
            elif action == 'show_ttm':
                self.trans_3_stiil2still(action)
            elif action == 'blank':
                self.trans_2_still2b(action)
            elif action == 'show_cue':
                self.trans_4_still2c(action)
            elif action == 'move_cw':
                self.trans_7_still2mcw(action)
            elif action == 'move_ccw':
                self.trans_15_still2mccw(action)
        # End of Show_TTM_Still conditional
        elif self.current_state == self.state_Show_Cue:
            if False:  # Show_Cue
                pass  # Show_Cue
            elif action == 'show_cue':
                self.trans_6_c2c(action)
            elif action == 'blank':
                self.trans_5_c2b(action)
        # End of Show_Cue conditional
        elif self.current_state == self.state_Move_CW:
            if False:  # Move_CW
                pass  # Move_CW
            elif action == 'show_ttm':
                self.trans_8_cw2still(action)
            elif action == 'show_cue':
                self.trans_9_mcw2c(action)
            elif action == 'blank':
                self.trans_10_cw2b(action)
            elif action == 'move_cw':
                self.trans_11_mcw2mcw(action)

            elif action == 'show_cue':
                self.trans_12_mcw2c(action)
            elif action == 'blank':
                self.trans_14_mcw2b(action)
            elif action == 'move_ccw':
                self.trans_18_mcw2mccw(action)
        # End of Move_CW conditional
        elif self.current_state == self.state_Move_CCW:
            if False:  # Move_CCW
                pass  # Move_CCW
            elif action == 'move_ccw':
                self.trans_13_ccw2ccw(action)
            elif action == 'show_ttm':
                self.trans_16_mccw2still(action)
            elif action == 'show_cue':
                self.trans_17_mccw2c(action)
            elif action == 'move_cw':
                self.trans_19_mccw2mcw(action)
            elif action == 'blank':
                self.trans_20_mccw2b(action)
        #print("---- Ending SCREEN state = {}".format(self.current_state.name))
        # End of Move_CCW conditional
        # End conditionals

    # Start transition callbacks
    def on_trans_0_b2b(self, action):
        self.command_to_screen = 'Cue=0, Manipulandum=0, Target=0, Trap=0'

    def on_trans_3_stiil2still(self, action):
        self.command_to_screen = 'Cue=0, Manipulandum={}, Target={}, Trap={}'.format(self.visible_manip_angle,
                                                                                     self.target_angle, self.trap_angle)

    def on_trans_6_c2c(self, action):
        self.command_to_screen = 'Ignore'

    def on_trans_1_b2still(self, action):
        self.command_to_screen = 'Cue=0, Manipulandum={}, Target={}, Trap={}'.format(self.visible_manip_angle,
                                                                                     self.target_angle, self.trap_angle)

    def on_trans_2_still2b(self, action):
        self.command_to_screen = 'Cue=0, Manipulandum=0, Target=0, Trap=0'

    def on_trans_4_still2c(self, action):
        self.command_to_screen = 'Cue=1, Manipulandum=0, Target=0, Trap=0'

    def on_trans_5_c2b(self, action):
        self.command_to_screen = 'Cue=0, Manipulandum=0, Target=0, Trap=0'

    def on_trans_7_still2mcw(self, action):
        self.manip_angle -= self.speed
        self.command_to_screen = 'Cue=0, Manipulandum={}, Target={}, Trap={}'.format(self.visible_manip_angle,
                                                                                     self.target_angle, self.trap_angle)
        self.check_manip_and_rezero()

    def on_trans_8_cw2still(self, action):
        self.command_to_screen = 'Cue=0, Manipulandum={}, Target={}, Trap={}'.format(self.visible_manip_angle,
                                                                                     self.target_angle, self.trap_angle)

    def on_trans_9_mcw2c(self, action):
        self.command_to_screen = 'Cue=1, Manipulandum=0, Target=0, Trap=0'

    def on_trans_10_cw2b(self, action):
        self.command_to_screen = 'Cue=0, Manipulandum=0, Target=0, Trap=0'

    def on_trans_11_mcw2mcw(self, action):
        self.manip_angle -= self.speed
        self.command_to_screen = 'Cue=0, Manipulandum={}, Target={}, Trap={}'.format(self.visible_manip_angle,
                                                                                     self.target_angle, self.trap_angle)
        self.check_manip_and_rezero()

    def on_trans_12_mcw2c(self, action):
        self.command_to_screen = 'Cue=1, Manipulandum=0, Target=0, Trap=0'

    def on_trans_13_ccw2ccw(self, action):
        self.manip_angle += self.speed
        self.command_to_screen = 'Cue=0, Manipulandum={}, Target={}, Trap={}'.format(self.visible_manip_angle,
                                                                                     self.target_angle, self.trap_angle)
        self.check_manip_and_rezero()

    def on_trans_14_mcw2b(self, action):
        self.command_to_screen = 'Cue=0, Manipulandum=0, Target=0, Trap=0'

    def on_trans_15_still2mccw(self, action):
        self.manip_angle += self.speed
        self.command_to_screen = 'Cue=0, Manipulandum={}, Target={}, Trap={}'.format(self.visible_manip_angle,
                                                                                     self.target_angle, self.trap_angle)
        self.check_manip_and_rezero()

    def on_trans_16_mccw2still(self, action):
        self.command_to_screen = 'Cue=0, Manipulandum={}, Target={}, Trap={}'.format(self.visible_manip_angle,
                                                                                     self.target_angle, self.trap_angle)

    def on_trans_17_mccw2c(self, action):
        self.command_to_screen = 'Cue=1, Manipulandum=0, Target=0, Trap=0'

    def on_trans_18_mcw2mccw(self, action):
        self.manip_angle += self.speed
        self.command_to_screen = 'Cue=0, Manipulandum={}, Target={}, Trap={}'.format(self.visible_manip_angle,
                                                                                     self.target_angle, self.trap_angle)
        self.check_manip_and_rezero()

    def on_trans_19_mccw2mcw(self, action):
        self.manip_angle -= self.speed
        self.command_to_screen = 'Cue=0, Manipulandum={}, Target={}, Trap={}'.format(self.visible_manip_angle,
                                                                                     self.target_angle, self.trap_angle)
        self.check_manip_and_rezero()

    def on_trans_20_mccw2b(self, action):
        self.command_to_screen = 'Cue=0, Manipulandum=0, Target=0, Trap=0'

        # End transition callbacks

    def get_visible_manip_angle(self):
        """
        If the trial is a catch one then keep the angle shown to the initial one (the mainpulandum doesn't appear to move)
        but still run proper calculations with the manip_angle to see if the manipulandum would have reached the target
        :return:
        """
        self.visible_manip_angle = self.initial_manip_angle if self.catch_trial else self.manip_angle

    def check_manip_and_rezero(self):
        if not self.target_reached:
            self.target_reached = self.has_man_reached_target()
        if not self.trap_reached:
            self.trap_reached = self.has_man_reached_trap()
        self.rezero_angle()

    def rezero_angle(self):
        if self.manip_angle < 0:
            self.manip_angle = 360 + self.manip_angle
        if self.manip_angle > 359:
            self.manip_angle = self.manip_angle - 359
        if self.manip_angle == 0:
            self.manip_angle = 1

    def has_man_reached_target(self):
        man_pos = self.manip_angle
        target_pos = self.target_angle
        comparator_angle = np.max([self.speed, self.angle_dif_between_man_and_target_trap])
        if np.abs(target_pos - man_pos) < comparator_angle \
                or np.abs(target_pos - man_pos) > 360 - comparator_angle:
            self.target_reached = True
            return True
        else:
            return False

    def has_man_reached_trap(self):
        man_pos = self.manip_angle
        trap_pos = self.trap_angle
        comparator_angle = np.max([self.speed, self.angle_dif_between_man_and_target_trap])
        if np.abs(trap_pos - man_pos) < comparator_angle \
                or np.abs(trap_pos - man_pos) > 360 - comparator_angle:
            self.trap_reached = True
            return True
        else:
            return False
