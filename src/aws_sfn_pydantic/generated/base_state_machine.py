# generated by datamodel-codegen:
#   filename:  base-state-machine.json
#   timestamp: 2023-08-01T12:32:48+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, confloat, conint, constr


class AslPath(RootModel):
    root: Optional[str]


class AslRefPath(RootModel):
    root: Optional[str]


class Operator(BaseModel):
    Variable: Optional[str] = None
    And: Optional[List[Operator]] = None
    Or: Optional[List[Operator]] = None
    Not: Optional[Operator] = None
    IsNull: Optional[bool] = None
    IsPresent: Optional[bool] = None
    BooleanEquals: Optional[bool] = None
    BooleanEqualsPath: Optional[AslPath] = None
    IsBoolean: Optional[bool] = None
    NumericEquals: Optional[float] = None
    NumericEqualsPath: Optional[AslPath] = None
    NumericGreaterThan: Optional[float] = None
    NumericGreaterThanPath: Optional[AslPath] = None
    NumericGreaterThanEquals: Optional[float] = None
    NumericGreaterThanEqualsPath: Optional[AslPath] = None
    NumericLessThan: Optional[float] = None
    NumericLessThanPath: Optional[AslPath] = None
    NumericLessThanEquals: Optional[float] = None
    NumericLessThanEqualsPath: Optional[AslPath] = None
    IsNumeric: Optional[bool] = None
    StringEquals: Optional[str] = None
    StringEqualsPath: Optional[AslPath] = None
    StringGreaterThan: Optional[str] = None
    StringGreaterThanPath: Optional[AslPath] = None
    StringGreaterThanEquals: Optional[str] = None
    StringGreaterThanEqualsPath: Optional[AslPath] = None
    StringLessThan: Optional[str] = None
    StringLessThanPath: Optional[AslPath] = None
    StringLessThanEquals: Optional[str] = None
    StringLessThanEqualsPath: Optional[AslPath] = None
    StringMatches: Optional[str] = None
    IsString: Optional[bool] = None
    TimestampEquals: Optional[str] = None
    TimestampEqualsPath: Optional[AslPath] = None
    TimestampGreaterThan: Optional[str] = None
    TimestampGreaterThanPath: Optional[AslPath] = None
    TimestampGreaterThanEquals: Optional[str] = None
    TimestampGreaterThanEqualsPath: Optional[AslPath] = None
    TimestampLessThan: Optional[str] = None
    TimestampLessThanPath: Optional[AslPath] = None
    TimestampLessThanEquals: Optional[str] = None
    TimestampLessThanEqualsPath: Optional[AslPath] = None
    IsTimestamp: Optional[bool] = None


class Fail(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    Type: Literal["Fail"]
    Comment: Optional[str] = None
    Cause: Optional[str] = None
    Error: Optional[str] = None


class Errors(RootModel):
    root: Union[
        str,
        Literal["States.ALL"],
        Literal["States.HeartbeatTimeout"],
        Literal["States.Timeout"],
        Literal["States.TaskFailed"],
        Literal["States.Permissions"],
        Literal["States.ResultPathMatchFailure"],
        Literal["States.ParameterPathFailure"],
        Literal["States.BranchFailed"],
        Literal["States.NoChoiceMatched"],
        Literal["States.IntrinsicFailure"],
    ] = Field(..., description="https://states-language.net/#appendix-a")


class Succeed(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    Type: Literal["Succeed"]
    Comment: Optional[str] = None
    OutputPath: Optional[AslPath] = None
    InputPath: Optional[AslPath] = None


class ResourceItem(BaseModel):
    Ref: Optional[str] = None


class RetryItem(BaseModel):
    ErrorEquals: List[Errors]
    IntervalSeconds: Optional[confloat(ge=0.0)] = None
    MaxAttempts: Optional[confloat(ge=0.0)] = None
    BackoffRate: Optional[confloat(ge=0.0)] = None


class CatchItem1(BaseModel):
    ErrorEquals: List[Errors]
    Next: str
    ResultPath: Optional[AslRefPath] = None


class Wait(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    Type: Literal["Wait"]
    Next: Optional[str] = None
    End: Optional[Literal[True]] = None
    Comment: Optional[str] = None
    OutputPath: Optional[AslPath] = None
    InputPath: Optional[AslPath] = None
    Seconds: Optional[confloat(ge=0.0)] = None
    Timestamp: Optional[str] = None
    SecondsPath: Optional[AslRefPath] = None
    TimestampPath: Optional[AslRefPath] = None


class ReaderConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    MaxItems: Optional[conint(ge=1)] = None
    MaxItemsPath: Optional[AslRefPath] = None


class ProcessorConfigItem(BaseModel):
    Mode: Literal["INLINE"]


class ExecutionType(Enum):
    EXPRESS = "EXPRESS"
    STANDARD = "STANDARD"


class ProcessorConfigItem1(BaseModel):
    Mode: Literal["DISTRIBUTED"]
    ExecutionType: ExecutionType


class CatchItem2(BaseModel):
    ErrorEquals: List[Errors]
    Next: str


class Choice1(Operator):
    Next: str


class Choice(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    Type: Literal["Choice"]
    Next: Optional[str] = None
    End: Optional[Literal[True]] = None
    Comment: Optional[str] = None
    OutputPath: Optional[AslPath] = None
    InputPath: Optional[AslPath] = None
    Choices: List[Choice1]
    Default: Optional[str] = None


class CatchItem(BaseModel):
    ErrorEquals: List[Errors]
    Next: str
    ResultPath: Optional[AslRefPath] = None


class Model(BaseModel):
    Comment: Optional[str] = None
    StartAt: str
    States: Dict[constr(pattern=r"^.{1,80}$"), State]


class State(RootModel):
    root: Union[Choice, Fail, Parallel, Pass, Succeed, Task, Wait, Map]


class FieldPayloadTemplateObject(RootModel):
    root: Union[
        Dict[constr(pattern=r"^.+\.\$$"), str],
        Dict[
            constr(pattern=r"^.+(([^.][^$])|([^.][$]))$"),
            Union[
                Optional[Union[float, bool, str]],
                List[AslPayloadTemplate],
                FieldPayloadTemplateObject,
            ],
        ],
    ]


class AslPayloadTemplate(RootModel):
    root: Union[
        FieldPayloadTemplateObject, List[AslPayloadTemplate], Union[str, bool, float]
    ]


class Parallel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    Type: Literal["Parallel"]
    Parameters: Optional[AslPayloadTemplate] = None
    ResultSelector: Optional[AslPayloadTemplate] = None
    Next: Optional[str] = None
    End: Optional[Literal[True]] = None
    Comment: Optional[str] = None
    OutputPath: Optional[AslPath] = None
    InputPath: Optional[AslPath] = None
    ResultPath: Optional[AslRefPath] = None
    Branches: List[StateMachine]
    Retry: Optional[List[RetryItem]] = None
    Catch: Optional[List[CatchItem]] = None


class StateMachine(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    Comment: Optional[str] = None
    StartAt: str
    States: Dict[constr(pattern=r"^.{1,80}$"), State]
    Version: Optional[str] = None
    TimeoutSeconds: Optional[conint(ge=0)] = None


class Pass(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    Type: Literal["Pass"]
    Next: Optional[str] = None
    End: Optional[Literal[True]] = None
    Comment: Optional[str] = None
    OutputPath: Optional[AslPath] = None
    InputPath: Optional[AslPath] = None
    ResultPath: Optional[AslRefPath] = None
    Parameters: Optional[AslPayloadTemplate] = None
    Result: Optional[Any] = None


class Task(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    Type: Literal["Task"]
    Next: Optional[str] = None
    End: Optional[Literal[True]] = None
    Comment: Optional[str] = None
    OutputPath: Optional[AslPath] = None
    InputPath: Optional[AslPath] = None
    Resource: Union[str, constr(pattern=r"^\$\{[^\}]+\}$"), ResourceItem]
    ResultPath: Optional[AslRefPath] = None
    Retry: Optional[List[RetryItem]] = None
    Catch: Optional[List[CatchItem1]] = None
    TimeoutSeconds: Optional[confloat(ge=1.0)] = None
    TimeoutSecondsPath: Optional[AslRefPath] = None
    HeartbeatSeconds: Optional[confloat(ge=1.0)] = None
    HeartbeatSecondsPath: Optional[AslRefPath] = None
    ResultSelector: Optional[AslPayloadTemplate] = None
    Parameters: Optional[AslPayloadTemplate] = None
    Credentials: Optional[AslPayloadTemplate] = None


class ItemReader(BaseModel):
    Resource: str
    Parameters: Optional[AslPayloadTemplate] = None
    ReaderConfig: Optional[ReaderConfig] = None


class ItemBatcher(BaseModel):
    MaxItemsPerBatch: Optional[confloat(ge=0.0)] = None
    MaxItemsPerBatchPath: Optional[AslRefPath] = None
    MaxInputBytesPerBatch: Optional[confloat(ge=0.0, le=262144.0)] = None
    MaxInputBytesPerBatchPath: Optional[AslRefPath] = None
    BatchInput: Optional[AslPayloadTemplate] = None


class Map(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    Type: Literal["Map"]
    Next: Optional[str] = None
    End: Optional[Literal[True]] = None
    Comment: Optional[str] = None
    OutputPath: Optional[AslPath] = None
    InputPath: Optional[AslPath] = None
    ResultPath: Optional[AslRefPath] = None
    ItemsPath: Optional[AslRefPath] = None
    Label: Optional[str] = None
    MaxConcurrency: Optional[confloat(ge=0.0)] = None
    MaxConcurrencyPath: Optional[AslRefPath] = None
    ItemReader: Optional[ItemReader] = None
    ItemProcessor: Optional[ItemProcessor] = None
    Iterator: Optional[Model] = None
    Parameters: Optional[AslPayloadTemplate] = None
    ItemSelector: Optional[AslPayloadTemplate] = None
    ItemBatcher: Optional[ItemBatcher] = None
    ResultSelector: Optional[AslPayloadTemplate] = None
    ResultWriter: Optional[Dict[str, Any]] = None
    Retry: Optional[List[RetryItem]] = None
    Catch: Optional[List[CatchItem2]] = None
    ToleratedFailureCount: Optional[conint(ge=0)] = None
    ToleratedFailureCountPath: Optional[AslRefPath] = None
    ToleratedFailurePercentage: Optional[conint(ge=0, le=100)] = None
    ToleratedFailurePercentagePath: Optional[AslRefPath] = None


class ItemProcessor(Model):
    ProcessorConfig: Optional[Union[ProcessorConfigItem, ProcessorConfigItem1]] = None


Operator.model_rebuild()
Model.model_rebuild()
State.model_rebuild()
FieldPayloadTemplateObject.model_rebuild()
Parallel.model_rebuild()
Map.model_rebuild()
ItemProcessor.model_rebuild()
