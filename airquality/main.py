import time
from pathlib import Path

from adafruit_pm25.i2c import PM25_I2C
from air_quality_report import AirQualityReport, create_report
from device import device_setup, read_data
from export_report import create_csv
from upload_to_s3 import upload_to_s3

S3_BUCKET = "pm25-air-quality-data-james-salvatore"


if __name__ == "__main__":
    TOTAL_ITERATIONS = 12
    SLEEP_BETWEEN_ITERATIONS_SECS = 5

    for t in range(TOTAL_ITERATIONS):
        print(
            f"{SLEEP_BETWEEN_ITERATIONS_SECS * t}s"
            + "/"
            + f"{SLEEP_BETWEEN_ITERATIONS_SECS * TOTAL_ITERATIONS}s"
        )

        # Get the report.
        pm25_i2c: "PM25_I2C" = device_setup()
        air_quality_data: dict[str, int] = read_data(pm25_i2c=pm25_i2c)
        report: "AirQualityReport" = create_report(air_quality_data=air_quality_data)

        # Create CSV / insert CSV row.
        file_loc: Path = create_csv(report=report)

        # Wait a bit to iterate.
        time.sleep(SLEEP_BETWEEN_ITERATIONS_SECS)

    upload_to_s3(file_loc=file_loc, bucket=S3_BUCKET)
