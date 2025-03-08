#
# Copyright 2018-2025 Fragment Contributors
# SPDX-License-Identifier: Apache-2.0
#
import hashlib
import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import networkx as nx

from conformer_core.records import Record
from conformer_core.stages import Link, Stack, Stage
from conformer_core.util import ind, summarize


class CalculationOptions():
    links: List[Tuple[str, str]]

    args: List[Any]
    kwargs: Dict[str, Any]




class CalculationInstance:
    """
    A calculation that includs fresh copies of all stages and variables involved in a calculation.

    Not that this can be saved to a database. Since it's linked to a Calculation stage, the only thing that
    need to be included are the keyword argument
    """
    stages: List[Stage]
    variables: Dict[str, Any]
    aliases: Dict[str, Stage]

    arguments: dict[str, Any]
    data: nx.DiGraph

    def __init__(self,
        edges: List[Tuple[str, ...]],
        aliases: Dict[str, str],
        **kwargs
    ) -> None:
        self.stages = []
        for e in edges:
            l = len(e)
            if l == 3:
                default = None
                source, dest_stage, dest_field  = e
            elif l == 4:
                source, dest_stage, dest_field, default = e
            else:
                raise ValueError("Edges should be formatted as `source`, `destination stage`, `destination field` with and optional `default`")

        pass

class CalculationStep(Stage):
    stage = Link() # The stage we will be working with
    inputs = Stack() # Stages which feed into this one

class Calculation(Stage):
    stages = Stack()


# SPEC FOR CALCULATIONS
"""
+/@!()
calculations:
    -
        name: mbe--xtb
        system: my_system (for backwards compat)
        steps:
            - list
            - of
            - steps
        aliases:
            - MIM_add: rec_add
            - MIM_sub: rec_subtract
            - MBE_ccsd: ccsd
            - superystem_ccsd: ccsd
        links:
            - [$system, pdb-fragmenter:system]
            - [pdb-fragmenter, mbe:view]
            - [mbe, xtb:view]
            - [$order, mbe:order, 3]
            - [xtb, MIM_sub:a]
            - [ccst, MIM_sub:b]
            - [MIM_sub, MIM_add:a]
            - [super, MIM_add:b]
        input:
            -
                system: f12
                order: 3
                ligand: 2

"""

@dataclass
class CalculationRecord(Record):
    steps: List[Tuple["str", Tuple]] = field(default=list)
    name: Optional[str] = None  # Required
    hash: Optional["hashlib._Hash"] = None

    def __init__(self, *args, **kwargs) -> None:
        name = kwargs.pop("name")
        steps = kwargs.pop("steps")
        hash = kwargs.pop("hash", None)

        # Now init the Record dataclass
        super().__init__(*args, **kwargs)

        self.steps = steps
        self.hash = self.make_hash(steps) if hash is None else hash
        self.name = self.hash.hexdigest() if name is None else name

    @staticmethod
    def make_hash(steps: List) -> "hashlib._Hash":
        hash_data = json.dumps(steps, sort_keys=True).encode("utf-8")
        hash = hashlib.new("sha1")
        hash.update(hash_data)
        return hash

    def summarize(self, padding=2, level=0) -> str:
        rec_str = ind(padding, level, f"Calculation {self.name}: \n")

        level += 1
        rec_str += ind(padding, level, f"ID: {self.id}\n")
        rec_str += ind(padding, level, f"Status: {self.status.name}\n")
        rec_str += ind(
            padding,
            level,
            f"Created: {self.start_time.isoformat(timespec='minutes')}\n",
        )

        steps = []
        for k, args in self.steps:
            if args:
                str_args = ",".join(map(str, args))
                steps.append(f"{k}({str_args})")
            else:
                steps.append(f"{k}")
        rec_str += summarize("Steps", steps, padding=padding, level=level)

        if self.meta:
            rec_str += summarize("Meta", self.meta, padding=padding, level=level + 1)

        if self.properties:
            rec_str += ind(padding, level, "Properties:\n")
            rec_str += self.properties.summarize(padding=padding, level=level + 1)
        return rec_str
