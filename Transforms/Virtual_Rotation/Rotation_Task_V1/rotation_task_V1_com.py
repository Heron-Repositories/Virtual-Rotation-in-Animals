
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

ParameterNames = ['Visualisation', 'Task Type', 'Speed', 'Number of Pellets', 'Wait period / s']

ParameterTypes = ['bool', 'str', 'int', 'int', 'float']  # The types of the parameters (in string form).
# types allowed are: 'bool', 'str', 'list', 'int' and 'float'. Again for no parameters make an empty list.

ParametersDefaultValues = [False, 'Wait', 20, 1, 0.1]

WorkerDefaultExecutable = os.path.join(os.path.dirname(Exec), 'rotation_task_V1_worker.py')


if __name__ == "__main__":
    rotation_task_V1_com = gu.start_the_transform_communications_process(NodeAttributeType, NodeAttributeNames)
    gu.register_exit_signals(rotation_task_V1_com.on_kill)
    rotation_task_V1_com.start_ioloop()

