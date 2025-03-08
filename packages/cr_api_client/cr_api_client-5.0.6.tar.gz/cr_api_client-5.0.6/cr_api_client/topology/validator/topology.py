# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2021 AMOSSYS. All rights reserved.
#
# This file is part of Cyber Range AMOSSYS.
#
# Cyber Range AMOSSYS can not be copied and/or distributed without the express
# permission of AMOSSYS.
#
from pathlib import Path
from typing import List

from mantis_scenario_model.common import NotEmptyList  # type: ignore[import-untyped]
from mantis_scenario_model.common import NotEmptyStr
from mantis_scenario_model.link import Link  # type: ignore[import-untyped]
from mantis_scenario_model.node import Node  # type: ignore[import-untyped]
from mantis_scenario_model.node import NodeType
from pydantic import BaseModel
from pydantic import validator
from ruamel.yaml import YAML


class Topology(BaseModel):
    name: NotEmptyStr
    nodes: NotEmptyList[NodeType]
    links: NotEmptyList[Link]

    @validator("nodes")
    def check_nodes(cls, v: List[Node]):
        names = [node.name for node in v]
        if len(names) != len(set(names)):
            raise ValueError("Names of the node list must be unique")
        return v

    @staticmethod
    def from_yaml_string(value: str) -> "Topology":
        loader = YAML(typ="rt")
        return Topology(**loader.load(value))

    @staticmethod
    def from_yaml_file(path: Path) -> "Topology":
        return Topology.from_yaml_string(path.read_text())

    def to_yaml_string(self) -> str:
        # TODO: add custom yaml representers
        yaml = YAML(typ="rt")
        return yaml.dump(self.dict())
