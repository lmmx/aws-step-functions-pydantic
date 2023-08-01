from ..utils.boto import HAS_BOTO

__all__ = ["get_sfn_defn"]


def get_sfn_defn(state_machine_arn: str) -> str:
    if not HAS_BOTO:
        raise ImportError(
            "The boto3 package is required to use this function. "
            "Please install it with `pip install aws-step-functions-pydantic[boto3]`."
        )
    import boto3

    sfn = boto3.client("stepfunctions")
    response = sfn.describe_state_machine(stateMachineArn=state_machine_arn)
    defn = response["definition"]
    return defn
