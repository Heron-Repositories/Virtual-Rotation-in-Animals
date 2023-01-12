
import numpy as np
from statemachine import StateMachine, State


class ButtonToMatchWithTrapTaskFSM(StateMachine):

    # Start States
    state_Wait_to_Poke = State("Wait_to_Poke", initial=True)
    state_Poked = State("Poked", initial=False)
    state_Push_Left = State("Push_Left", initial=False)
    state_Push_Right = State("Push_Right", initial=False)
    state_Success = State("Success", initial=False)
    state_Fail = State("Fail", initial=False)
    # End States

    # Start Transitions
    trans_0_po2po = state_Poked.to(state_Poked)
    trans_2_pl2pl = state_Push_Left.to(state_Push_Left)
    trans_1_po2pl = state_Poked.to(state_Push_Left)
    trans_3_pl2po = state_Push_Left.to(state_Poked)
    trans_4_pr2pr = state_Push_Right.to(state_Push_Right)
    trans_5_po2pr = state_Poked.to(state_Push_Right)
    trans_6_pr2po = state_Push_Right.to(state_Poked)
    trans_7_pl2pr = state_Push_Left.to(state_Push_Right)
    trans_8_pr2pl = state_Push_Right.to(state_Push_Left)
    trans_9_pl2s = state_Push_Left.to(state_Success)
    trans_10_pl2f = state_Push_Left.to(state_Fail)
    trans_11_pr2s = state_Push_Right.to(state_Success)
    trans_12_pr2f = state_Push_Right.to(state_Fail)
    trans_13_s2po = state_Success.to(state_Poked)
    trans_14_f2po = state_Fail.to(state_Poked)
    trans_00_wp2wp = state_Wait_to_Poke.to(state_Wait_to_Poke)
    trans_01_wp2po = state_Wait_to_Poke.to(state_Poked)
    trans_02_po2wp = state_Poked.to(state_Wait_to_Poke)
    # End Transitions

    def __init__(self, screen_fsm):
        super().__init__()
        # Start State Variables
        self.screen_fsm = screen_fsm
        self.previous_button = 0
        # End State Variables

    def step(self, poke, button):
        #print(" State of Task = {}".format(self.current_state.name))

        if False:
            pass

        # Start conditionals
        elif self.current_state == self.state_Wait_to_Poke:
            if False:  # Wait_to_Poke
                pass  # Wait_to_Poke
            elif not poke:
                self.trans_00_wp2wp(poke, button)
            elif poke:
                self.trans_01_wp2po(poke, button)
        # End of Wait_to_Poke conditional
        elif self.current_state == self.state_Poked:
            if False:  # Poked
                pass  # Poked
            elif poke and (not button or button == self.previous_button):
                self.trans_0_po2po(poke, button)
            elif poke and button < 0:
                self.trans_1_po2pl(poke, button)
            elif poke and button > 0:
                self.trans_5_po2pr(poke, button)
            elif not poke:
                self.trans_02_po2wp(poke, button)
        # End of Poked conditional
        elif self.current_state == self.state_Push_Left:
            if False:  # Push_Left
                pass  # Push_Left
            elif poke and self.screen_fsm.target_reached:
                self.trans_9_pl2s(poke, button)
            elif poke and self.screen_fsm.trap_reached:
                self.trans_10_pl2f(poke, button)
            elif not poke or (poke and button == self.previous_button):
                self.trans_3_pl2po(poke, button)
            elif poke and button < self.previous_button:
                self.trans_2_pl2pl(poke, button)
            elif poke and button > self.previous_button:
                self.trans_7_pl2pr(poke, button)
        # End of Push_Left conditional
        elif self.current_state == self.state_Push_Right:
            if False:  # Push_Right
                pass  # Push_Right
            elif poke and self.screen_fsm.target_reached:
                self.trans_11_pr2s(poke, button)
            elif poke and self.screen_fsm.trap_reached:
                self.trans_12_pr2f(poke, button)
            elif not poke or (poke and button == self.previous_button):
                self.trans_6_pr2po(poke, button)
            elif poke and button > self.previous_button:
                self.trans_4_pr2pr(poke, button)
            elif poke and button < self.previous_button:
                self.trans_8_pr2pl(poke, button)
        # End of Push_Right conditional
        elif self.current_state == self.state_Success:
            if False:  # Success
                pass  # Success
            #elif True:
            #    self.trans_13_s2po(poke, button)
        # End of Success conditional
        elif self.current_state == self.state_Fail:
            if False:  # Fail
                pass  # Fail
            #elif True:
            #    self.trans_14_f2po(poke, button)
        # End of Fail conditional
        # End conditionals

    # Start transition callbacks
    def on_trans_00_wp2wp(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_01_wp2po(self, poke, button):
        self.screen_fsm.step(action='show_ttm')

    def on_trans_02_po2wp(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_0_po2po(self, poke, button):
        self.previous_button = button
        self.screen_fsm.step(action='show_ttm')

    def on_trans_2_pl2pl(self, poke, button):
        self.previous_button = button
        self.screen_fsm.step(action='move_ccw')

    def on_trans_1_po2pl(self, poke, button):
        self.previous_button = button
        self.screen_fsm.step(action='show_ttm')

    def on_trans_3_pl2po(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_4_pr2pr(self, poke, button):
        self.previous_button = button
        self.screen_fsm.step(action='move_cw')

    def on_trans_5_po2pr(self, poke, button):
        self.previous_button = button
        self.screen_fsm.step(action='show_ttm')

    def on_trans_6_pr2po(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_7_pl2pr(self, poke, button):
        self.previous_button = button
        self.screen_fsm.step(action='move_cw')

    def on_trans_8_pr2pl(self, poke, button):
        self.previous_button = button
        self.screen_fsm.step(action='move_ccw')

    def on_trans_9_pl2s(self, poke, button):
        self.screen_fsm.step(action='show_ttm')

    def on_trans_10_pl2f(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_11_pr2s(self, poke, button):
        self.screen_fsm.step(action='show_ttm')

    def on_trans_12_pr2f(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_13_s2po(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_14_f2po(self, poke, button):
        self.screen_fsm.step(action='blank')

    # End transition callbacks
