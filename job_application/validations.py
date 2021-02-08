from filters.validations import IntegerLike, DatetimeWithTZ
from filters.schema import base_query_params_schema

applications_query_schema = base_query_params_schema.extend(
    {
        "id": IntegerLike(),
        "salary": IntegerLike(),
        "date_applied": DatetimeWithTZ(),
        "start": DatetimeWithTZ(),
        "end": DatetimeWithTZ(),
    }
)