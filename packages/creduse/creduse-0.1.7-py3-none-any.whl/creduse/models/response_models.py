import datetime
from pydantic import UUID4, BaseModel, Field
from enum import Enum


class CycleType(str, Enum):
    one_time = "one-time"
    recurring = "recurring"


class Status(str, Enum):
    active = "active"
    canceled = "canceled"


class AddCreditModel(BaseModel):
    end_user_id: UUID4
    amount: int
    validity_days: int = 31


class SubtractCreditModel(BaseModel):
    end_user_id: UUID4
    amount: int


class StartCycleModel(BaseModel):
    end_user_id: UUID4
    amount: int
    validity_days: int = 31


class StopCycleModel(BaseModel):
    end_user_id: UUID4


class CycleModelResponse(BaseModel):
    end_user_id: UUID4
    """
    The unique identifier of the end user.
    """
    amount: int
    """
    The amount of credits in the cycle.
    """
    created_at: datetime.datetime
    """
    The time when the cycle was created.
    """
    cycle_type: CycleType
    """
    The type of cycle (one-time or recurring).
    """
    current_cycle_start: datetime.datetime
    """
    The start time of the current cycle.
    """
    current_cycle_end: datetime.datetime
    """
    The end time of the current cycle.
    """
    status: Status
    """
    The status of the cycle (active or canceled).
    """


class GetBalanceRequest(BaseModel):
    end_user_id: UUID4


class ActiveBalanceByCycle(BaseModel):
    cycle_start: datetime.datetime
    """
    Cycle start time.
    """
    cycle_end: datetime.datetime
    """
    Cycle end time.
    """
    amount: int
    """
    Amount of the active balance.
    """
    status: Status
    """
    Status of the active balance.
    """
    cycle_type: CycleType
    """
    Type of the active balance cycle.
    """


class ActiveBalance(BaseModel):
    end_user_id: UUID4
    """
    User ID.
    """
    active_balance_by_cycle: list[ActiveBalanceByCycle]
    """
    List of active balances by cycle.
        [
        cycle_start: datetime.datetime
        cycle_end: datetime.datetime
        amount: int
        status: Status
        cycle_type: CycleType
        ]
    """
    active_balance: int
    """
    The current active balance.
    """


class CreditTransaction(BaseModel):
    """
    Represents a ledger entry for a transaction.

    Attributes:
        transaction_id (UUID or None): The unique identifier of the transaction.
        user_id (UUID): The unique identifier of the user associated with the transaction.
        amount (int): The absolute amount of the transaction.
        created_at (datetime): The time at which the transaction was created.
        expire_at (datetime): The time at which the transaction will expire.
        
    """
    transaction_id: UUID4 | None
    user_id: UUID4 = Field(exclude=True, alias="end_user_id", serialization_alias="end_user_id")
    amount: int
    created_at: datetime.datetime
    expire_at: datetime.datetime