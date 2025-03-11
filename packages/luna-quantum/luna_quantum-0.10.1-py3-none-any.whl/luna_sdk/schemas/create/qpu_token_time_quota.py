from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class QpuTokenTimeQuotaIn(BaseModel):
    """
    Pydantic model for creating a time quota on a qpu token.

    Attributes
    ----------
    quota: int
        The amount of quota.
    start: datetime | None
        Effective start date of the time quota policy.
        If None, policy will be in effect immediately.
    end: datetime | None
        Effective end date of the time quota policy.
        If None, policy will be in effect until 365 days after the start date.
    """

    quota: int
    start: Optional[datetime]
    end: Optional[datetime]
