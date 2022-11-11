
import numpy as np
from statemachine import StateMachine, State


class ButtonToMatchWithTrapTask():

    # Start States
    state_Wait_to_Poke = State("Wait_to_Poke", initial=True)
    state_Push_Left = State("Push_Left", initial=False)
    # End States

    # Start Transitions
    trans_0_wp2wp = state_Wait_to_Poke.to(state_Wait_to_Poke)
    trans_2_pl2pl = state_Push_Left.to(state_Push_Left)
    trans_1_wp2pl = state_Wait_to_Poke.to(state_Push_Left)
    trans_3_pl2wp = state_Push_Left.to(state_Wait_to_Poke)
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
        # End of Wait_to_Poke conditional
        elif self.current_state == self.state_Push_Left:
            if False:  # Push_Left
                pass  # Push_Left
            elif poke and button < 0:
                self.trans_2_pl2pl(poke, button)
            elif not poke:
                self.trans_3_pl2wp(poke, button)
        # End of Push_Left conditional
        # End conditionals

    # Start transition callbacks
    def on_trans_0_wp2wp(self, poke, button):
        self.screen_fsm(action='blank')

    def on_trans_2_pl2pl(self, poke, button):
        self.screen_fsm.step(action='move_ccw')

    def on_trans_1_wp2pl(self, poke, button):
        self.screen_fsm.step(action='show_ttm')

    def on_trans_3_pl2wp(self, poke, button):
        self.screen_fsm.step(action='blank')

    # End transition callbacks
