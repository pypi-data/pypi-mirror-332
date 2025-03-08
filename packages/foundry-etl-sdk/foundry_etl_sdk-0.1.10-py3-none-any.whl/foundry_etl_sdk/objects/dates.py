import pandas as pd

from .table_manager import BaseMultiRowManager
from foundry_db.tables import DatesTable

from foundry_db.sdk import SQLDatabase


class Dates(BaseMultiRowManager):

    @classmethod
    def from_series(cls, series: pd.Series, db: SQLDatabase):
        """
        Create a Dates object from a pandas Series object.

        Args:
        series: pd.Series
            Series object containing dates
        """

        start_date = series.min()
        end_date = series.max()

        return cls(start_date, end_date, db)

    def __init__(
        self, start_date: pd.Timestamp, end_date: pd.Timestamp, db: SQLDatabase
    ):
        """
        Initialize Dates object

        Args:

        start_date: pd.Timestamp
            Start date
        end_date: pd.Timestamp
            End date
        """


        self._start_date = start_date
        self._end_date = end_date


        rows = [
            (date.date(),) for date in self.get_date_range()
        ]

        super().__init__(DatesTable, rows, db)

   
    def get_start_date(self):
        """
        Get start date

        Returns:
        pd.Timestamp
            Start date
        """
        return self._start_date
    
    def get_end_date(self):
        """
        Get end date

        Returns:
        pd.Timestamp
            End date
        """
        return self._end_date

    def get_date_range(self):
        """
        Get date range

        Returns:
        pd.date_range
            Date range
        """
        min_date = self.get_start_date()
        max_date = self.get_end_date()
        return pd.date_range(start=min_date, end=max_date)
 
