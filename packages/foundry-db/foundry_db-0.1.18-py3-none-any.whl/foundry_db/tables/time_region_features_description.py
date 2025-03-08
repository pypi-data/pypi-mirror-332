from .base_table import BaseTable, IDColumn
from ..enums import IDQueryTypes


class TimeRegionFeaturesDescriptionTable(BaseTable):
    NAME: str = "time_region_features_description"

    # "ID" is provided as a primary key column
    ID_COLUMN = str(IDColumn("ID"))

    NAME_COLUMN = "name"
    DESCRIPTION_COLUMN = "description"
    COMPANY_ID_COLUMN = str(IDColumn("companyID"))

    COLUMN_NAMES: list[str] = [NAME_COLUMN, DESCRIPTION_COLUMN, COMPANY_ID_COLUMN]

    ID_QUERY_TYPE = IDQueryTypes.BATCH
