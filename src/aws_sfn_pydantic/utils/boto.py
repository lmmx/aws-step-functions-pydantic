try:
    import boto3  # noqa: F401
except ImportError:
    HAS_BOTO = False
else:
    HAS_BOTO = True

__all__ = ["HAS_BOTO"]
