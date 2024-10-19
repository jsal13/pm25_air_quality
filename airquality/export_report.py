from air_quality_report import AirQualityReport


def export_report(report: "AirQualityReport"):
    """Export report."""
    concentrations = report.ambient_concentration
    particulate_count = report.particulate_count
    recorded_at = report.recorded_at
    print(concentrations, particulate_count, recorded_at)

