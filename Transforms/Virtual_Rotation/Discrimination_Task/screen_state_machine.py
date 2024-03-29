

import numpy as np
from statemachine import StateMachine, State


class ScreenFSM(StateMachine):
    # Start States
    state_Blank = State("Blank", initial=True)
    state_Show_Objects = State("Show_Objects", initial=False)
    state_Show_Success_Cue = State("Show_Success_Cue", initial=False)
    state_Show_Failure_Cue = State("Show_Failure_Cue", initial=False)
    # End States

    # Start Transitions
    trans_0_b2b = state_Blank.to(state_Blank)
    trans_3_show2show = state_Show_Objects.to(state_Show_Objects)
    trans_1_b2show = state_Blank.to(state_Show_Objects)
    trans_2_show2b = state_Show_Objects.to(state_Blank)
    trans_4_show2suc_cue = state_Show_Objects.to(state_Show_Success_Cue)
    trans_5_suc_cue2b = state_Show_Success_Cue.to(state_Blank)
    trans_6_suc_cue2c = state_Show_Success_Cue.to(state_Show_Success_Cue)
    trans_7_show2fail_cue = state_Show_Objects.to(state_Show_Failure_Cue)
    trans_8_fail_cue2b = state_Show_Failure_Cue.to(state_Blank)
    trans_9_fail_cue2c = state_Show_Failure_Cue.to(state_Show_Failure_Cue)

    # End Transitions

    def __init__(self, show_objects_at_positions):
        """
        The Communication protocol is:
        Cue=xRy,CheckeredLine=xRy, WhiteLine=xRy, BlackLine=xRy, CheckeredCircle=xRy,
        WhiteCircle=xRy, BlackCircle=xRy, CheckeredSquare=xRy, WhiteSquare=xRy, BlackSquare=xRy

        where x is the position (between -700 and 700) and y is the rotation in degrees

        :param show_objects_at_positions:
        """
        super().__init__()
        # Start State Variables
        self.hide_objects = [0]*20
        self.show_objects_at_positions = show_objects_at_positions
        self.success_cue = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.failure_cue = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.base_command_to_screen = 'Cue={0}R{10}, ' \
                                      'CheckeredLine={1}R{11}, WhiteLine={2}R{12}, BlackLine={3}R{13}, ' \
                                      'CheckeredCircle={4}R{14}, WhiteCircle={5}R{15}, BlackCircle={6}R{16}, ' \
                                      'CheckeredSquare={7}R{17}, WhiteSquare={8}R{18}, BlackSquare={9}R{19}'
        self.command_to_screen = self.base_command_to_screen.format(*self.hide_objects)

    def step(self, action):
        #print("---- Starting SCREEN state = {}".format(self.current_state.name))
        if False:
            pass

        # Start conditionals
        elif self.current_state == self.state_Blank:
            if False:  # Blank
                pass  # Blank
            elif action == 'blank':
                self.trans_0_b2b(action)
            elif action == 'show_objects':
                self.trans_1_b2show(action)
        # End of Blank conditional
        elif self.current_state == self.state_Show_Objects:
            if False:  # Show_TTM_Still
                pass  # Show_TTM_Still
            elif action == 'show_objects':
                self.trans_3_show2show(action)
            elif action == 'blank':
                self.trans_2_show2b(action)
            elif action == 'show_success_cue':
                self.trans_4_show2suc_cue(action)
            elif action == 'show_failure_cue':
                self.trans_7_show2fail_cue(action)
        # End of Show_TTM_Still conditional
        elif self.current_state == self.state_Show_Success_Cue:
            if False:  # Show_Cue
                pass  # Show_Cue
            elif action == 'show_success_cue':
                self.trans_6_suc_cue2c(action)
            elif action == 'blank':
                self.trans_5_suc_cue2b(action)
        # End of Show_Success_Cue conditional
        elif self.current_state == self.state_Show_Failure_Cue:
            if False:  # Show_Cue
                pass  # Show_Cue
            elif action == 'show_failure_cue':
                self.trans_9_fail_cue2c(action)
            elif action == 'blank':
                self.trans_8_fail_cue2b(action)
        # End of Show_Failure_Cue conditional
        #print("---- Ending SCREEN state = {}".format(self.current_state.name))
        # End conditionals

    # Start transition callbacks
    def on_trans_0_b2b(self, action):
        self.command_to_screen = self.base_command_to_screen.format(*self.hide_objects)

    def on_trans_1_b2show(self, action):
        self.command_to_screen = self.base_command_to_screen.format(*self.show_objects_at_positions)

    def on_trans_2_show2b(self, action):
        self.command_to_screen = self.base_command_to_screen.format(*self.hide_objects)

    def on_trans_3_show2show(self, action):
        self.command_to_screen = self.base_command_to_screen.format(*self.show_objects_at_positions)

    def on_trans_4_show2suc_cue(self, action):
        self.command_to_screen = self.base_command_to_screen.format(*self.success_cue)
        #print(self.command_to_screen)

    def on_trans_5_suc_cue2b(self, action):
        self.command_to_screen = self.base_command_to_screen.format(*self.hide_objects)

    def on_trans_6_suc_cue2c(self, action):
        self.command_to_screen = 'Ignore'

    def on_trans_7_show2fail_cue (self, action):
        self.command_to_screen = self.base_command_to_screen.format(*self.failure_cue)
        #print(self.command_to_screen)

    def on_trans_8_fail_cue2b(self, action):
        self.command_to_screen = self.base_command_to_screen.format(*self.hide_objects)

    def on_trans_9_fail_cue2c(self, action):
        self.command_to_screen = 'Ignore'

    # End transition callbacks








