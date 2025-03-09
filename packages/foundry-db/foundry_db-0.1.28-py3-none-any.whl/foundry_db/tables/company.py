from .base_table import BaseTable, IDColumn
from ..enums import IDQueryTypes


class CompanyTable(BaseTable):

    NAME: str = "companies"

    ID_COLUMN = str(IDColumn("ID"))

    NAME_COLUMN: str = "name"
    DATASET_TYPE_COLUMN: str = "dataset_type"
    DESCRIPTION_COLUMN: str = "description"

    MIN_DATE_COLUMN: str = "min_date"
    MAX_DATE_COLUMN: str = "max_date"

    COLUMN_NAMES: list[str] = [
        NAME_COLUMN,
        DATASET_TYPE_COLUMN,
        DESCRIPTION_COLUMN,
        MIN_DATE_COLUMN,
        MAX_DATE_COLUMN,
    ]

    ID_QUERY_TYPE = IDQueryTypes.SINGLE
