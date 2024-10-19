import os
from pathlib import Path

from air_quality_report import AirQualityReport

USER_DIRECTORY = os.path.expanduser("~")
CSV_HEADER: str = ",".join(
    [
        "diameter_at_most_1_0",
        "diameter_at_most_2_5",
        "diameter_at_most_10_0",
        "number_of_particles_size_0_3um",
        "number_of_particles_size_0_5um",
        "number_of_particles_size_1_0um",
        "number_of_particles_size_2_5um",
        "number_of_particles_size_5_0um",
        "number_of_particles_size_10_0um",
    ]
)

def create_csv(report: "AirQualityReport") -> Path:
    """Create CSV to send to S3, return Path loc of file."""
    # Do the report hourly.
    report_suffix: str = report.recorded_at.strftime("%y%m%d_%H0000")
    report_output_name: str = f"aqr_{report_suffix}.csv"

    # Make output directory.
    data_dir = Path(f"{USER_DIRECTORY}/data")
    data_dir.mkdir(exist_ok=True)

    csv_line: str = ",".join(
        [
            report.ambient_concentration.diameter_at_most_1_0,
            report.ambient_concentration.diameter_at_most_2_5,
            report.ambient_concentration.diameter_at_most_10_0,
            report.particulate_count.number_of_particles_size_0_3um,
            report.particulate_count.number_of_particles_size_0_5um,
            report.particulate_count.number_of_particles_size_1_0um,
            report.particulate_count.number_of_particles_size_2_5um,
            report.particulate_count.number_of_particles_size_5_0um,
            report.particulate_count.number_of_particles_size_10_0um,
            report.recorded_at.isoformat(),
        ]
    )

    output_path: Path = data_dir.joinpath(report_output_name)

    # Create file if not yet created...
    # If not, then create the file and append the header.
    if not output_path.is_file():
        with open(output_path, "w+", encoding="utf-8") as out:
            out.write(CSV_HEADER + "\n")
    # Then append the CSV row.
    else:
        with open(output_path, "a", encoding="utf-8") as out:
            out.write(csv_line + "\n")

    return output_path
