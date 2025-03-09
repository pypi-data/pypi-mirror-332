from .base_table import BaseTable, IDColumn
from ..enums import IDQueryTypes


class CategoryTable(BaseTable):

    NAME: str = "categories"

    ID_COLUMN = str(IDColumn("ID"))
    NAME_COLUMN: str = "name"
    COMPANY_ID_COLUMN: str = str(IDColumn("companyID"))

    COLUMN_NAMES: list[str] = [NAME_COLUMN, COMPANY_ID_COLUMN]

    ID_QUERY_TYPE = IDQueryTypes.SINGLE
