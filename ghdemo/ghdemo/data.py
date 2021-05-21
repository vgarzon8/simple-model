# Data handler class

import pandas as pd
from sqlalchemy import MetaData
from sqlalchemy.engine.url import URL
from sqlalchemy.engine import create_engine


class DataHandler:
    """Data handler for PostgreSQL database connections"""

    def __init__(self, config):
        self._config = config
        self._engine = create_engine(URL.create(**self._config))
        self._meta = MetaData()
        self._meta.reflect(bind=self._engine)

    def get_table(self, table_name):
        """Get table object from reflected metadata
        Args:
            table_name (str): Table name

        Returns:
            sqlalchemy.sql.schema.Table

        """
        return self._meta.tables[table_name]

    def read_table(self, table_name):
        """Select all columns from table
        Args:
            table_name (str): Table name

        Returns:
            pandas.core.frame.DataFrame
        """
        _table = self.get_table(table_name)
        with self._engine.connect() as con:
            df = pd.read_sql(_table.select(), con)
        return df
