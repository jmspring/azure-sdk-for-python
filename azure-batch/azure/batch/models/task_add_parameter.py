# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TaskAddParameter(Model):
    """An Azure Batch task to add.

    :param id: A string that uniquely identifies the task within the job. The
     id can contain any combination of alphanumeric characters including
     hyphens and underscores, and cannot contain more than 64 characters.
    :type id: str
    :param display_name: A display name for the task.
    :type display_name: str
    :param command_line: The command line of the task. For multi-instance
     tasks, the command line is executed on the primary subtask after all the
     subtasks have finished executing the coordianation command line.
    :type command_line: str
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line. For
     multi-instance tasks, the resource files will only be downloaded to the
     compute node on which the primary subtask is executed.
    :type resource_files: list of :class:`ResourceFile
     <azure.batch.models.ResourceFile>`
    :param environment_settings: A list of environment variable settings for
     the task.
    :type environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param affinity_info: A locality hint that can be used by the Batch
     service to select a compute node on which to start the new task.
    :type affinity_info: :class:`AffinityInformation
     <azure.batch.models.AffinityInformation>`
    :param constraints: The execution constraints that apply to this task.
    :type constraints: :class:`TaskConstraints
     <azure.batch.models.TaskConstraints>`
    :param run_elevated: Whether to run the task in elevated mode.
    :type run_elevated: bool
    :param multi_instance_settings: Information about how to run the
     multi-instance task.
    :type multi_instance_settings: :class:`MultiInstanceSettings
     <azure.batch.models.MultiInstanceSettings>`
    :param depends_on: Any other tasks that this task depends on.
    :type depends_on: :class:`TaskDependencies
     <azure.batch.models.TaskDependencies>`
    """ 

    _validation = {
        'id': {'required': True},
        'command_line': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ResourceFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'affinity_info': {'key': 'affinityInfo', 'type': 'AffinityInformation'},
        'constraints': {'key': 'constraints', 'type': 'TaskConstraints'},
        'run_elevated': {'key': 'runElevated', 'type': 'bool'},
        'multi_instance_settings': {'key': 'multiInstanceSettings', 'type': 'MultiInstanceSettings'},
        'depends_on': {'key': 'dependsOn', 'type': 'TaskDependencies'},
    }

    def __init__(self, id, command_line, display_name=None, resource_files=None, environment_settings=None, affinity_info=None, constraints=None, run_elevated=None, multi_instance_settings=None, depends_on=None):
        self.id = id
        self.display_name = display_name
        self.command_line = command_line
        self.resource_files = resource_files
        self.environment_settings = environment_settings
        self.affinity_info = affinity_info
        self.constraints = constraints
        self.run_elevated = run_elevated
        self.multi_instance_settings = multi_instance_settings
        self.depends_on = depends_on
