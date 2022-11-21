

# <editor-fold desc="The following 6 lines of code are required to allow Heron to be able to see the Operation without
# package installation. Do not change.">
import sys
from os import path
import cv2
import numpy as np

current_dir = path.dirname(path.abspath(__file__))
while path.split(current_dir)[-1] != r'Heron':
    current_dir = path.dirname(current_dir)
sys.path.insert(0, path.dirname(current_dir))
# </editor-fold>

from Heron.communication.socket_for_serialization import Socket
from Heron import general_utils as gu
from Heron.gui.visualisation_dpg import VisualisationDPG
import initialisation as init
from screen_state_machine import ScreenFSM
from wait_to_match_task_state_machine import WaitToMatchTaskFSM

config_script_file: str
vis: VisualisationDPG
screen_fsm: ScreenFSM
task_fsm: WaitToMatchTaskFSM

def initialise(_worker_object):
    global vis
    global config_script_file

    visualisation_type = 'Single Pane Plot'
    buffer = 20
    vis = VisualisationDPG(_node_name=_worker_object.node_name, _node_index=_worker_object.node_index,
                           _visualisation_type=visualisation_type, _buffer=buffer)

    try:
        parameters = _worker_object.parameters
        vis.visualisation_on = parameters[0]
        config_script_file = parameters[1]
    except:
        return False

    _worker_object.relic_create_parameters_df(visualisation_on=vis.visualisation_on,
                                              config_script_file=config_script_file)

    initialised_trial()
    return True


def initialised_trial():
    global screen_fsm
    global task_fsm

    target_angle, trap_angle, manip_angle, speed, angle_dif_between_man_and_target_trap = init.testing_for_wait_task()
    screen_fsm = ScreenFSM(target_angle, trap_angle, manip_angle, speed, angle_dif_between_man_and_target_trap)
    task_fsm = WaitToMatchTaskFSM(screen_fsm=screen_fsm)


def work_function(data, parameters):
    global vis
    global config_script_file
    global screen_fsm
    global task_fsm

    try:
        vis.visualisation_on = parameters[0]
    except:
        pass

    if task_fsm.current_state == task_fsm.state_Wait_to_Start:
        initialised_trial()

    topic = data[0].decode('utf-8')

    message = data[1:]
    message = Socket.reconstruct_array_from_bytes_message(message)

    if 'Levers_State' in topic:
        task_fsm.step(poke=message[0])

    command_to_screen = np.array([screen_fsm.command_to_screen])
    command_to_reward = np.array([-1])
    if task_fsm.current_state == task_fsm.state_Success:
        command_to_reward = np.array([1])

    result = [command_to_screen, command_to_reward]
    print(screen_fsm.current_state)
    print(task_fsm.current_state)
    print(result)
    print('----------------------------------------')
    return result


def on_end_of_life():
    global vis
    vis.end_of_life()

if __name__ == "__main__":
    worker_object = gu.start_the_transform_worker_process(work_function=work_function,
                                                          end_of_life_function=on_end_of_life,
                                                          initialisation_function=initialise)
    worker_object.start_ioloop()