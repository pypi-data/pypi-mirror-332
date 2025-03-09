"""Functions to build HAL data."""

__all__ = ['build_hal_df_from_api',]

# Internal imports
from HalApyJson.api_manager import get_response_from_api
from HalApyJson.json_parser import parse_json


def build_hal_df_from_api(year, institute):
    """The `build_hal_df_from_api` function gets the response from the HAL API 
    using the `get_response_from_api` function of the 'api_manager' module.
    Then, it parses this response using the `parse_json` of the 'json_parser' module.

    Args:
        year (str): The year to query.
        institute (str): The institute to query.
    Returns
        (pandas.core.frame.DataFrame): The dataframe resulting from the parsed response.
    """
    response, message = get_response_from_api(year, institute)
    print(message)
    hal_df = parse_json(response)
    return hal_df
