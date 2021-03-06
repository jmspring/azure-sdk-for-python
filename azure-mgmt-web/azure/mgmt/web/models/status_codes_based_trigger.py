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


class StatusCodesBasedTrigger(Model):
    """StatusCodeBasedTrigger.

    :param status: HTTP status code
    :type status: int
    :param sub_status: SubStatus
    :type sub_status: int
    :param win32_status: Win32 error code
    :type win32_status: int
    :param count: Count
    :type count: int
    :param time_interval: TimeInterval
    :type time_interval: str
    """ 

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'sub_status': {'key': 'subStatus', 'type': 'int'},
        'win32_status': {'key': 'win32Status', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'time_interval': {'key': 'timeInterval', 'type': 'str'},
    }

    def __init__(self, status=None, sub_status=None, win32_status=None, count=None, time_interval=None):
        self.status = status
        self.sub_status = sub_status
        self.win32_status = win32_status
        self.count = count
        self.time_interval = time_interval
