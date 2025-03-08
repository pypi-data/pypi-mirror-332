import datetime
from pydantic import UUID4, BaseModel
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
    amount: int
    created_at: datetime.datetime
    cycle_type: CycleType
    current_cycle_start: datetime.datetime
    current_cycle_end: datetime.datetime
    status: Status


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
