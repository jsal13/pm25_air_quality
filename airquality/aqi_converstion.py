import aqi


def convert_pm25_to_iaqi(value: int) -> int:
    """
    Convert PM25 to IAQI.

    See: <https://pypi.org/project/python-aqi/>
    """
    return aqi.to_iaqi(aqi.POLLUTANT_PM25, str(value), algo=aqi.ALGO_EPA)

def convert_pm10_to_iaqi(value: int) -> int:
    """
    Convert PM10 to IAQI.

    See: <https://pypi.org/project/python-aqi/>
    """
    return aqi.to_iaqi(aqi.POLLUTANT_PM10, str(value), algo=aqi.ALGO_EPA)


