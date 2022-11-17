
import numpy as np
from statemachine import StateMachine, State


class ButtonToMatchWithTrapTask():

    # Start States
    state_Wait_to_Poke = State("Wait_to_Poke", initial=True)
    state_Push_Left = State("Push_Left", initial=False)
    state_Push_Right = State("Push_Right", initial=False)
    state_Success = State("Success", initial=False)
    state_Fail = State("Fail", initial=False)
    # End States

    # Start Transitions
    trans_0_wp2wp = state_Wait_to_Poke.to(state_Wait_to_Poke)
    trans_2_pl2pl = state_Push_Left.to(state_Push_Left)
    trans_1_wp2pl = state_Wait_to_Poke.to(state_Push_Left)
    trans_3_pl2wp = state_Push_Left.to(state_Wait_to_Poke)
    trans_4_pr2pr = state_Push_Right.to(state_Push_Right)
    trans_5_wp2pr = state_Wait_to_Poke.to(state_Push_Right)
    trans_6_pr2wp = state_Push_Right.to(state_Wait_to_Poke)
    trans_7_pl2pr = state_Push_Left.to(state_Push_Right)
    trans_8_pr2pl = state_Push_Right.to(state_Push_Left)
    trans_9_pl2s = state_Push_Left.to(state_Success)
    trans_10_pl2f = state_Push_Left.to(state_Fail)
    trans_11_pr2s = state_Push_Right.to(state_Success)
    trans_12_pr2f = state_Push_Right.to(state_Fail)
    trans_13_s2wp = state_Success.to(state_Wait_to_Poke)
    trans_14_f2wp = state_Fail.to(state_Wait_to_Poke)
    # End Transitions

    def __init__(self, screen_fsm):
        super().__init__(StateMachine)
        # Start State Variables
        self.screen_fsm = screen_fsm
        # End State Variables

    def step(self, poke, button):
        if False:
            pass

        # Start conditionals
        elif self.current_state == self.state_Wait_to_Poke:
            if False:  # Wait_to_Poke
                pass  # Wait_to_Poke
            elif not poke:
                self.trans_0_wp2wp(poke, button)
            elif poke and button < 0:
                self.trans_1_wp2pl(poke, button)
            elif poke and button > 0:
                self.trans_5_wp2pr(poke, button)
        # End of Wait_to_Poke conditional
        elif self.current_state == self.state_Push_Left:
            if False:  # Push_Left
                pass  # Push_Left
            elif poke and button < 0:
                self.trans_2_pl2pl(poke, button)
            elif not poke:
                self.trans_3_pl2wp(poke, button)
            elif poke and button > 0:
                self.trans_7_pl2pr(poke, button)
            elif poke and self.screen_fsm.has_man_reached_target:
                self.trans_9_pl2s(poke, button)
            elif poke and self.screen_fsm.has_man_reached_trap:
                self.trans_10_pl2f(poke, button)
        # End of Push_Left conditional
        elif self.current_state == self.state_Push_Right:
            if False:  # Push_Right
                pass  # Push_Right
            elif poke and button > 0:
                self.trans_4_pr2pr(poke, button)
            elif not poke:
                self.trans_6_pr2wp(poke, button)
            elif poke and button < 0:
                self.trans_8_pr2pl(poke, button)
            elif poke and self.screen_fsm.has_man_reached_target:
                self.trans_11_pr2s(poke, button)
            elif poke and self.screen_fsm.has_man_reached_trap:
                self.trans_12_pr2f(poke, button)
        # End of Push_Right conditional
        elif self.current_state == self.state_Success:
            if False:  # Success
                pass  # Success
            elif True:
                self.trans_13_s2wp(poke, button)
        # End of Success conditional
        elif self.current_state == self.state_Fail:
            if False:  # Fail
                pass  # Fail
            elif True:
                self.trans_14_f2wp(poke, button)
        # End of Fail conditional
        # End conditionals

    # Start transition callbacks
    def on_trans_0_wp2wp(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_2_pl2pl(self, poke, button):
        self.screen_fsm.step(action='move_ccw')

    def on_trans_1_wp2pl(self, poke, button):
        self.screen_fsm.step(action='show_ttm')

    def on_trans_3_pl2wp(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_4_pr2pr(self, poke, button):
        self.screen_fsm.step(action='move_cw')

    def on_trans_5_wp2pr(self, poke, button):
        self.screen_fsm.step(action='show_ttm')

    def on_trans_6_pr2wp(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_7_pl2pr(self, poke, button):
        self.screen_fsm.step(action='move_cw')

    def on_trans_8_pr2pl(self, poke, button):
        self.screen_fsm.step(action='move_ccw')

    def on_trans_9_pl2s(self, poke, button):
        self.screen_fsm.step(action='show_ttm')

    def on_trans_10_pl2f(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_11_pr2s(self, poke, button):
        self.screen_fsm.step(action='show_ttm')

    def on_trans_12_pr2f(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_13_s2wp(self, poke, button):
        self.screen_fsm.step(action='blank')

    def on_trans_14_f2wp(self, poke, button):
        self.screen_fsm.step(action='blank')

    # End transition callbacks
