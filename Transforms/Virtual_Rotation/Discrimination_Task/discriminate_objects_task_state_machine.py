
import numpy as np
from statemachine import StateMachine, State

class DiscriminateObjectsTaskFSM(StateMachine):

    # Start States
    state_Wait_to_Start = State("Wait_to_Start", initial=True)
    state_Wait_in_Poke = State("Wait_in_Poke", initial=False)
    state_Success = State("Success", initial=False)
    state_Fail = State("Fail", initial=False)
    # End States

    # Start Transitions
    trans_0_st2st = state_Wait_to_Start.to(state_Wait_to_Start)
    trans_1_s2p = state_Wait_to_Start.to(state_Wait_in_Poke)
    trans_2_p2p = state_Wait_in_Poke.to(state_Wait_in_Poke)
    trans_3_p2suc = state_Wait_in_Poke.to(state_Success)
    trans_4_p2f = state_Wait_in_Poke.to(state_Fail)
    trans_5_p2st = state_Wait_in_Poke.to(state_Wait_to_Start)
    trans_6_s2ws = state_Success.to(state_Wait_to_Start)
    trans_7_f2ws = state_Fail.to(state_Wait_to_Start)
    # End Transitions

    def __init__(self, screen_fsm):
        super().__init__()
        # Start State Variables
        self.screen_fsm = screen_fsm
        self.buttons_off_timer = 0

    def step(self, poke, button):
        #print('== Starting DO state = {}'.format(self.current_state.name))
        #print('Button {}'.format(button))
        if False:
            pass

        # Start conditionals
        elif self.current_state == self.state_Wait_to_Start:
            if False:  # Wait_to_Start
                pass  # Wait_to_Start
            elif not poke:
                self.trans_0_st2st(poke)
            elif poke:
                self.trans_1_s2p(poke)
        # End of Wait_to_Start conditional
        elif self.current_state == self.state_Wait_in_Poke:
            if False:  # Wait_in_Poke
                pass  # Wait_in_Poke
            elif poke and not button:
                print('Timer {}'.format(self.buttons_off_timer))
                self.trans_2_p2p(poke)
            elif poke and button:
                if self.buttons_off_timer < 6:
                    self.buttons_off_timer = 0
                    self.trans_2_p2p(poke)
                elif self.buttons_off_timer >= 6 and ((button > 0 and np.any(self.screen_fsm.show_objects_at_positions[1:4] > 0)) or \
                        (button < 0 and np.any(self.screen_fsm.show_objects_at_positions[1:4] < 0))):
                    self.trans_3_p2suc(poke)
                else:
                    self.trans_4_p2f(poke)
            elif not poke:
                self.trans_5_p2st(poke)
        # End of Wait_in_Poke conditional
        elif self.current_state == self.state_Success:
            if False:  # Success
                pass  # Success
            elif not poke:
                self.trans_6_s2ws(poke)
        # End of Success conditional
        elif self.current_state == self.state_Fail:
            if False:  # Fail
                pass  # Fail
            elif not poke:
                self.trans_7_f2ws(poke)

        #print('== Ending state = {}'.format(self.current_state.name))
        # End of Fail conditional
        # End conditionals

    # Start transition callbacks
    def on_trans_0_st2st(self, poke):
        self.buttons_off_timer = 0
        self.screen_fsm.step(action='blank')

    def on_trans_1_s2p(self, poke):
        self.buttons_off_timer += 1
        self.screen_fsm.step(action='show_objects')

    def on_trans_2_p2p(self, poke):
        self.buttons_off_timer += 1
        self.screen_fsm.step(action='show_objects')

    def on_trans_3_p2suc(self, poke):
        self.buttons_off_timer = 0
        self.screen_fsm.step(action='blank')

    def on_trans_4_p2f(self, poke):
        self.buttons_off_timer = 0
        self.screen_fsm.step(action='blank')

    def on_trans_5_p2st(self, poke):
        self.buttons_off_timer = 0
        self.screen_fsm.step(action='blank')

    def on_trans_6_s2ws(self, poke):
        self.screen_fsm.step(action='blank')

    def on_trans_7_f2ws(self, poke):
        self.screen_fsm.step(action='blank')

    # End transition callbacks
