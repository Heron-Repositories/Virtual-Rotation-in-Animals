

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
import initialisation


visualisation_on: bool
config_script_file: str
vis: VisualisationDPG


def initialise(_worker_object):
    global vis

    global visualisation_on
    global config_script_file

    # INITIALISE PARAMETERS
    # Put the initialisation of the Node's parameter's in a try loop to take care of the time it takes for the GUI to
    # update the SinkWorker object.
    try:
        parameters = _worker_object.parameters
        visualisation_on = parameters[1]
        config_script_file = parameters[2]
    except:
        return False
    print('Hello')
    print(initialisation.screen_fsm.current_state)
    visualisation_type = 'Single Pane Plot'
    buffer = 20
    vis = VisualisationDPG(_node_name=_worker_object.node_name, _node_index=_worker_object.node_index,
                           _visualisation_type=visualisation_type, _buffer=buffer)

    _worker_object.relic_create_parameters_df(visualisation_on=visualisation_on, config_script_file=config_script_file)

    return True


def work_function(data, parameters, relic_update_substate_df):
    global vis
    global visualisation_on
    global config_script_file

    # If any parameters need to be updated during runtime then do that here, e.g.
    # Also update the visualisation parameter. This allows to turn on and off the visualisation window during
    # run time
    try:
        visualisation_on = parameters[1]
        vis.visualisation_on = parameters[0]
    except:
        pass

    topic = data[0]
    print(topic)  # prints will not work if the operation is running on a different computer.

    message = data[1:]
    message = Socket.reconstruct_array_from_bytes_message(message)
    print(message)

    #print(message.shape)
    #some_data_to_visualise = message
    #relic_update_substate_df(image__shape=message.shape)
    #vis.visualise(some_data_to_visualise)

    command_to_screen = np.array(['Cue=0, Manipulandum=0, Target=0, Trap=0'])
    command_to_reward = np.array([-1])
    result = [command_to_screen, command_to_reward]

    return result


def on_end_of_life():
    global vis
    vis.end_of_life()


if __name__ == "__main__":
    worker_object = gu.start_the_transform_worker_process(work_function=work_function,
                                                          end_of_life_function=on_end_of_life,
                                                          initialisation_function=initialise)
    worker_object.start_ioloop()