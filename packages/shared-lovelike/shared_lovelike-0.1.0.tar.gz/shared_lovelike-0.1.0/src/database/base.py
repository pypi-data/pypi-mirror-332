
from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class BaseModel(DeclarativeBase):
    """Base class for all models."""

    __abstract__ = True

    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),  # pylint: disable=not-callable
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),  # pylint: disable=not-callable
        onupdate=func.now(),  # pylint: disable=not-callable
        nullable=False,
    )

    def soft_delete(self, session: Session) -> None:
        """
        Marks the record as deleted by setting the `deleted_at` timestamp.

        Args:
            session (Session): The SQLAlchemy session to use for the operation.
        """
        self.deleted_at = datetime.now()
        session.add(self)
        session.flush()
