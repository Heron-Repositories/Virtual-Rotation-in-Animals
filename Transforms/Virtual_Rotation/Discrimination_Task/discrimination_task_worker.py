

# <editor-fold desc="The following 6 lines of code are required to allow Heron to be able to see the Operation without
# package installation. Do not change.">
import sys
from os import path
import numpy as np
import time

current_dir = path.dirname(path.abspath(__file__))
while path.split(current_dir)[-1] != r'Heron':
    current_dir = path.dirname(current_dir)
sys.path.insert(0, path.dirname(current_dir))
# </editor-fold>

from Heron.communication.socket_for_serialization import Socket
from Heron import general_utils as gu, constants as ct
from Heron.gui.visualisation_dpg import VisualisationDPG
import initialisation as init
from screen_state_machine import ScreenFSM
from discriminate_objects_task_state_machine import DiscriminateObjectsTaskFSM
from experiment_state_machine import ExperimentFSM

config_script_file: str
vis: VisualisationDPG
screen_fsm: ScreenFSM
task_fsm: DiscriminateObjectsTaskFSM
experiment_fsm: ExperimentFSM
trial_initialisation: init.Initialisation
object_types: str
number_of_pellets: int
reward_on = False
reward_collected = False
number_of_successful_trials = 0


def initialise(_worker_object):
    global vis
    global trial_initialisation
    global objects_types
    global number_of_pellets
    global experiment_fsm

    visualisation_type = 'Single Pane Plot'
    buffer = 20
    vis = VisualisationDPG(_node_name=_worker_object.node_name, _node_index=_worker_object.node_index,
                           _visualisation_type=visualisation_type, _buffer=buffer)

    try:
        parameters = _worker_object.parameters
        vis.visualisation_on = parameters[0]
        objects_types = parameters[1]
        number_of_pellets = parameters[2]
    except:
        return False

    _worker_object.savenodestate_create_parameters_df(visualisation_on=vis.visualisation_on,
                                                      task_description=objects_types,
                                                      number_of_pellets=number_of_pellets)
    _worker_object.num_of_iters_to_update_savenodestate_substate = 1800

    trial_initialisation = init.Initialisation(objects_types=objects_types,
                                               punish_time=7)

    experiment_fsm = ExperimentFSM(initialisation=trial_initialisation)
    return True


def work_function(data, parameters, savenodestate_update_substate_df):
    global vis
    global number_of_pellets
    global experiment_fsm
    global reward_on
    global reward_collected
    global number_of_successful_trials

    try:
        vis.visualisation_on = parameters[0]
        number_of_pellets = parameters[3]
    except:
        pass

    topic = data[0].decode('utf-8')

    message = data[1:]
    message = Socket.reconstruct_data_from_bytes_message(message)

    if 'Reward_Poke_State' in topic:
        reward_on = message[0]
        reward_collected = message[1]
        number_of_successful_trials = message[2]
        command_to_reward = np.array([ct.IGNORE])

    button = None
    if 'Levers_State' in topic:
        poke = message[0]
        button = np.sign(message[1])
        command_to_reward = np.array([-1])
        #print('poke={}, button={}, reward_on={}, reward_collected={}'.
        #      format(message[0], message[1], reward_on, reward_collected))
        experiment_fsm.step(poke=poke, button=button, reward_on=reward_on, reward_collected=reward_collected,
                            number_of_successful_trials=number_of_successful_trials)

    command_to_screen = np.array([experiment_fsm.screen_fsm.command_to_screen])

    if experiment_fsm.current_state == experiment_fsm.state_Success:
        command_to_reward = np.array([number_of_pellets])

    exp_state = str(experiment_fsm.current_state)
    task_state = str(experiment_fsm.task_fsm.current_state)
    screen_state = str(experiment_fsm.screen_fsm.current_state)
    prob_for_right = str(trial_initialisation.side_probability)
    button_str = str(button)

    savenodestate_update_substate_df(exp_state=exp_state,
                                     task_state=task_state,
                                     screen_state=screen_state,
                                     command_to_screens=command_to_screen[0],
                                     command_to_food_poke=command_to_reward[0],
                                     button=button_str,
                                     prob_for_right=prob_for_right)

    result = [command_to_screen, command_to_reward]
    return result


def on_end_of_life():
    global vis
    #vis.end_of_life()
    gu.accurate_delay(100)


if __name__ == "__main__":
    worker_object = gu.start_the_transform_worker_process(work_function=work_function,
                                                          end_of_life_function=on_end_of_life,
                                                          initialisation_function=initialise)
    worker_object.start_ioloop()