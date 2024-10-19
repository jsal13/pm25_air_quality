

from adafruit_pm25.i2c import PM25_I2C
from air_quality_report import AirQualityReport, create_report
from device import device_setup, read_data
from export_report import export_report

if __name__ == "__main__":
    pm25_i2c: 'PM25_I2C' = device_setup()
    air_quality_data: dict[str, int] = read_data(pm25_i2c=pm25_i2c)
    report: 'AirQualityReport' = create_report(air_quality_data=air_quality_data)
    export_report(report=report)
