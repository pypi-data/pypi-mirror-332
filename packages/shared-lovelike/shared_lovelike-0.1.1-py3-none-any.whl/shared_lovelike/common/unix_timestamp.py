# pylint: disable=too-many-ancestors
"""Treatment and conversion of de timestamp."""

from datetime import datetime
from zoneinfo import ZoneInfo

# Set UTC as default
UTC = ZoneInfo("UTC")


class UnixTimestamp:
    """Class to handle Unix timestamp conversions."""

    @staticmethod
    def current_timestamp(timezone: ZoneInfo = UTC) -> int:
        """
        Get the current Unix timestamp in seconds.

        Args:
            timezone (ZoneInfo, optional): Timezone to use. Defaults to UTC.

        Returns:
            int: Current Unix timestamp.

        """
        return int(datetime.now(timezone).timestamp())

    @staticmethod
    def to_datetime(timestamp: int, timezone: ZoneInfo = UTC) -> datetime:
        """
        Convert a Unix timestamp (integer) into a datetime object.

        Args:
            timestamp (int): Unix timestamp in seconds.
            timezone (ZoneInfo, optional): Timezone to convert to. Defaults to UTC.

        Returns:
            datetime: Datetime object in the specified timezone.

        """
        return datetime.fromtimestamp(timestamp, timezone)

    @staticmethod
    def from_datetime(dt: datetime) -> int:
        """
        Convert a datetime object to a Unix timestamp.

        Args:
            dt (datetime): Datetime object.

        Returns:
            int: Unix timestamp (seconds since epoch).

        """
        return int(dt.timestamp())