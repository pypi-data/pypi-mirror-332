from datetime import datetime, timezone
from sqlalchemy import TIMESTAMP, Column, Integer
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class TimestampMixin:
    """FastAPI mixin which automatically add TIMESTAMP column to your model"""

    created = Column(
        TIMESTAMP(timezone=True),
        default=datetime.now(timezone.utc),
        nullable=False,
        db_index=True,
    )
    modified = Column(
        TIMESTAMP(timezone=True),
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
        nullable=False,
        db_index=True,
    )


@declarative_mixin
class BaseModel:
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
