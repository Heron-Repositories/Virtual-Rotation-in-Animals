
import os
import sys
from os import path

current_dir = path.dirname(path.abspath(__file__))
while path.split(current_dir)[-1] != r'Heron':
    current_dir = path.dirname(current_dir)
sys.path.insert(0, path.dirname(current_dir))

from Heron import general_utils as gu
Exec = os.path.abspath(__file__)
# </editor-fold>

"""
Properties of the generated Node
"""
BaseName = 'Rotation Task V1'
NodeAttributeNames = ['Parameters', 'Reward Poke State', 'Levers State', 'Command to Screen', 'Command to Reward']

NodeAttributeType = ['Static', 'Input', 'Input', 'Output', 'Output']

ParameterNames = ['Visualisation', 'Objects Types', 'Number of Pellets']

ParameterTypes = ['bool', 'list', 'int']

ParametersDefaultValues = [False, ['Checkered', 'White', 'Black', 'Checkered & White', 'Checkered & Black',
                           'Black & White','Checkered, White & Black'], 1]

WorkerDefaultExecutable = os.path.join(os.path.dirname(Exec), 'discrimination_task_worker.py')


if __name__ == "__main__":
    rotation_task_V1_com = gu.start_the_transform_communications_process(NodeAttributeType, NodeAttributeNames)
    gu.register_exit_signals(rotation_task_V1_com.on_kill)
    rotation_task_V1_com.start_ioloop()

