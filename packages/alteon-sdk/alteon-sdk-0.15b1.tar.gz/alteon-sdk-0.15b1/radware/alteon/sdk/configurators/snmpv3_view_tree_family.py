#!/usr/bin/env python
# Copyright (c) 2019 Radware LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# @author: Leon Meguira, Radware


from radware.sdk.common import RadwareParametersStruct, PasswordArgument
from radware.alteon.sdk.alteon_configurator import MSG_UPDATE, AlteonConfigurator
from radware.alteon.beans.VacmViewTreeFamilyTable import *
from typing import Optional, ClassVar, Dict
from radware.alteon.exceptions import AlteonRequestError


class SNMPv3ViewTreeFamilyParameters(RadwareParametersStruct):
    name: str
    tree: str
    mask: Optional[str]
    type: Optional[EnumViewTreeFamilyType]

    def __init__(self, name: str = None, tree: str = None):
        self.name = name
        self.tree = tree
        self.mask = None
        self.type = None

bean_map = {
    VacmViewTreeFamilyTable: dict(
        struct=SNMPv3ViewTreeFamilyParameters,
        direct=True,
        attrs=dict(
            ViewName='name',
            Subtree='tree',
            Mask='mask',
            Type='type',
        )
    )
}


class SNMPv3ViewTreeFamilyConfigurator(AlteonConfigurator):
    parameters_class: ClassVar[SNMPv3ViewTreeFamilyParameters]

    def __init__(self, alteon_connection):
        super(SNMPv3ViewTreeFamilyConfigurator, self).__init__(bean_map, alteon_connection)

    def _read(self, parameters: SNMPv3ViewTreeFamilyParameters) -> SNMPv3ViewTreeFamilyParameters:
        self._read_device_beans(parameters)
        if self._beans:
            return parameters

    def _update(self, parameters: SNMPv3ViewTreeFamilyParameters, dry_run: bool) -> str:
        self._write_device_beans(parameters, dry_run=dry_run)
        return self._get_object_id(parameters) + MSG_UPDATE


    def _entry_bean_instance(self, parameters):
        return self._get_bean_instance(VacmViewTreeFamilyTable, parameters)

