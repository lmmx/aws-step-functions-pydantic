from __future__ import annotations

from textwrap import indent

import yaml

from ..generated.base_state_machine import StateMachine as BaseStateMachine
from .define import get_sfn_defn

__all__ = ["StateMachine"]


class StateMachine(BaseStateMachine):
    @classmethod
    def from_arn(cls, state_machine_arn: str) -> StateMachine:
        defn = get_sfn_defn(state_machine_arn=state_machine_arn)
        return cls.model_validate_json(defn)

    def model_to_yaml(self, indent: int = 2, level: int = 0) -> str:
        """
        Dump the Step Function definition to YAML.

        - `indent` can be 2, 4, or 8. (default: 2)
        - `level` how many levels of indentation to prefix each line by (default: 0).
        """
        sfn = self.model_dump(exclude_unset=True)
        prefix = " " * indent * level
        yml = yaml.dump(sfn, indent=indent, sort_keys=False)
        return indent(yml, prefix=prefix)
