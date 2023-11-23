# the config file to store all the variables.
import dataclasses


@dataclasses.dataclass
class Config:
    # langfuse keys
    langfuse_secret_key: str = "sk-lf-9762a089-ae52-45f5-9731-6bcad705927e"
    langfuse_public_key: str = "pk-lf-faf8377a-498a-4499-b930-07ab037c5529"