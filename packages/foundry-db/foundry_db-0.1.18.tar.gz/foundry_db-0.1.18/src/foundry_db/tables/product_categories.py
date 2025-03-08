from .base_table import BaseTable, IDColumn
from ..enums import IDQueryTypes


class ProductCategoriesTable(BaseTable):

    NAME: str = "product_categories"

    ID_COLUMN = str(IDColumn("productID"))
    PRODUCT_ID_COLUMN: str = str(IDColumn("productID"))
    CATEGORY_ID_COLUMN: str = str(IDColumn("categoryID"))

    COLUMN_NAMES: list[str] = [PRODUCT_ID_COLUMN, CATEGORY_ID_COLUMN]

    ID_QUERY_TYPE = IDQueryTypes.BATCH
