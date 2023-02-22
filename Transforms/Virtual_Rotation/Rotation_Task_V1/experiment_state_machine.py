
import numpy as np
from statemachine import StateMachine, State


class ExperimentFSM(StateMachine):

    # Start States
    state_Initialisation = State("Initialisation", initial=True)
    state_Task = State("Task", initial=False)
    state_Success = State("Success", initial=False)
    state_RewardPeriod = State("RewardPeriod", initial=False)
    state_GotReward = State("GotReward", initial=False)
    state_LostReward = State("LostReward", initial=False)
    state_Fail = State("Fail", initial=False)
    state_PunishPeriod = State("PunishPeriod", initial=False)
    # End States

    # Start Transitions
    trans_0_t2t = state_Task.to(state_Task)
    trans_1_i2t = state_Initialisation.to(state_Task)
    trans_3_s2s = state_Success.to(state_Success)
    trans_2_t2s = state_Task.to(state_Success)
    trans_5_rp2rp = state_RewardPeriod.to(state_RewardPeriod)
    trans_4_s2rp = state_Success.to(state_RewardPeriod)
    trans_6_rp2gr = state_RewardPeriod.to(state_GotReward)
    trans_7_rp2lr = state_RewardPeriod.to(state_LostReward)
    trans_8_gr2i = state_GotReward.to(state_Initialisation)
    trans_9_lr2i = state_LostReward.to(state_Initialisation)
    trans_10_t2f = state_Task.to(state_Fail)
    trans_12_pp2pp = state_PunishPeriod.to(state_PunishPeriod)
    trans_11_f2pp = state_Fail.to(state_PunishPeriod)
    trans_13_pp2i = state_PunishPeriod.to(state_Initialisation)
    # End Transitions

    def __init__(self, initialisation):
        super().__init__()
        # Start State Variables
        self.initialisation = initialisation
        self.screen_fsm = self.initialisation.get_screen_fsm(previous_success=False, number_of_successful_trials=0)
        self.task_fsm = self.initialisation.get_task_fsm()
        self.last_trial = None
        self.punish_time = 0
        self.reward_on_command = False
        # End State Variables

    def step(self, poke, button, reward_on, reward_collected, number_of_successful_trials):
        #print('-------------------')
        #print("Starting EXP state = {}".format(self.current_state.name))
        if False:
            pass

        # Start conditionals
        elif self.current_state == self.state_Initialisation:
            self.punish_time = 0
            if False:  # Initialisation
                pass  # Initialisation
            elif poke and self.task_fsm.current_state != self.task_fsm.state_Success and self.task_fsm.current_state != self.task_fsm.state_Fail:
                self.trans_1_i2t(poke, button, reward_on, reward_collected)
        # End of Initialisation conditional
        elif self.current_state == self.state_Task:
            if False:  # Task
                pass  # Task
            elif self.task_fsm.current_state != self.task_fsm.state_Success \
                    and self.task_fsm.current_state != self.task_fsm.state_Fail:
                self.trans_0_t2t(poke, button, reward_on, reward_collected)
            elif self.task_fsm.current_state == self.task_fsm.state_Success:
                self.trans_2_t2s(poke, button, reward_on, reward_collected)
            elif self.task_fsm.current_state == self.task_fsm.state_Fail:
                self.trans_10_t2f(poke, button, reward_on, reward_collected)
        # End of Task conditional
        elif self.current_state == self.state_Success:
            if False:  # Success
                pass  # Success
            elif not reward_on:
                self.trans_3_s2s(poke, button, reward_on, reward_collected)
            elif reward_on:
                self.trans_4_s2rp(poke, button, reward_on, reward_collected)
        # End of Success conditional
        elif self.current_state == self.state_RewardPeriod:
            if False:  # RewardPeriod
                pass  # RewardPeriod
            elif reward_on and not reward_collected:
                self.trans_5_rp2rp(poke, button, reward_on, reward_collected)
            elif not reward_on and reward_collected:
                self.trans_6_rp2gr(poke, button, reward_on, reward_collected)
            elif not reward_on and not reward_collected:
                self.trans_7_rp2lr(poke, button, reward_on, reward_collected)
        # End of RewardPeriod conditional
        elif self.current_state == self.state_GotReward:
            if False:  # GotReward
                pass  # GotReward
            elif True:
                self.trans_8_gr2i(poke, button, reward_on, reward_collected, number_of_successful_trials)
        # End of GotReward conditional
        elif self.current_state == self.state_LostReward:
            if False:  # LostReward
                pass  # LostReward
            elif True:
                self.trans_9_lr2i(poke, button, reward_on, reward_collected, number_of_successful_trials)
        # End of LostReward conditional
        elif self.current_state == self.state_Fail:
            if False:  # Fail
                pass  # Fail
            elif True:
                self.trans_11_f2pp(poke, button, reward_on, reward_collected)
        # End of Fail conditional
        elif self.current_state == self.state_PunishPeriod:
            if False:  # PunishPeriod
                pass  # PunishPeriod
            elif self.punish_time < self.initialisation.punish_time:
                self.trans_12_pp2pp(poke, button, reward_on, reward_collected)
            elif self.punish_time >= self.initialisation.punish_time:
                self.trans_13_pp2i(poke, button, reward_on, reward_collected, number_of_successful_trials)
        #print("Ending EXP state = {}".format(self.current_state.name))
        #print('-------------------')
        # End of PunishPeriod conditional
        # End conditionals

    # Start transition callbacks
    def on_trans_0_t2t(self, poke, button, reward_on, reward_collected):
        self.task_fsm.step(poke, button)

    def on_trans_1_i2t(self, poke, button, reward_on, reward_collected):
        self.task_fsm.step(poke, button)

    def on_trans_3_s2s(self, poke, button, reward_on, reward_collected):
        pass

    def on_trans_2_t2s(self, poke, button, reward_on, reward_collected):
        self.task_fsm.step(poke, button)

    def on_trans_5_rp2rp(self, poke, button, reward_on, reward_collected):
        pass

    def on_trans_4_s2rp(self, poke, button, reward_on, reward_collected):
        self.last_trial = [True, None]

    def on_trans_6_rp2gr(self, poke, button, reward_on, reward_collected):
        self.last_trial = [True, True]

    def on_trans_7_rp2lr(self, poke, button, reward_on, reward_collected):
        self.last_trial = [True, False]

    def on_trans_8_gr2i(self, poke, button, reward_on, reward_collected, number_of_successful_trials):
        self.screen_fsm = self.initialisation.get_screen_fsm(previous_success=True,
                                                             number_of_successful_trials=number_of_successful_trials)
        self.task_fsm = self.initialisation.get_task_fsm()
        self.last_trial = [None, None]

    def on_trans_9_lr2i(self, poke, button, reward_on, reward_collected, number_of_successful_trials):
        self.screen_fsm = self.initialisation.get_screen_fsm(previous_success=False,
                                                             number_of_successful_trials=number_of_successful_trials)
        self.task_fsm = self.initialisation.get_task_fsm()
        self.last_trial = [None, None]

    def on_trans_10_t2f(self, poke, button, reward_on, reward_collected):
        self.task_fsm.step(poke, button)

    def on_trans_12_pp2pp(self, poke, button, reward_on, reward_collected):
        self.punish_time += 1

    def on_trans_11_f2pp(self, poke, button, reward_on, reward_collected):
        self.last_trial = [False, None]

    def on_trans_13_pp2i(self, poke, button, reward_on, reward_collected, number_of_successful_trials):
        self.screen_fsm = self.initialisation.get_screen_fsm(previous_success=False,
                                                             number_of_successful_trials=number_of_successful_trials)
        self.task_fsm = self.initialisation.get_task_fsm()
        self.last_trial = [None, None]

    # End transition callbacks
