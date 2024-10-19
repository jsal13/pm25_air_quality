from datetime import UTC, datetime

import attrs

from aqi_converstion import convert_pm10_to_iaqi, convert_pm25_to_iaqi


@attrs.define
class AirQualityReport:
    """
    Represents an Air Quality Report from the PM 2.5.

    ## Particulate Matter

    Airborne particulate matter (PM) is not a single pollutant, but rather is a
    mixture of many chemical species. It is a complex mixture of solids and
    aerosols composed of small droplets of liquid, dry solid fragments, and
    solid cores with liquid coatings. Particles vary widely in size, shape and
    chemical composition, and may contain inorganic ions, metallic compounds,
    elemental carbon, organic compounds, and compounds from the earth's crust.
    Particles are defined by their diameter for air quality regulatory
    purposes. Those with a diameter of 10 microns or less (PM10) are inhalable
    into the lungs and can induce adverse health effects. Fine particulate
    matter is defined as particles that are 2.5 microns or less in diameter
    (PM2.5). Therefore, PM2.5 comprises a portion of PM10.  [1]

    ## What is the Difference Between PM10 and PM2.5?

    PM10 and PM2.5 often derive from different emissions sources, and also have
    different chemical compositions. Emissions from combustion of gasoline,
    oil, diesel fuel or wood produce much of the PM2.5 pollution found in
    outdoor air, as well as a significant proportion of PM10. PM10 also
    includes dust from construction sites, landfills and agriculture, wildfires
    and brush/waste burning, industrial sources, wind-blown dust from open
    lands, pollen and fragments of bacteria.  [1]

                      |  PM2.5	                |  PM10
    Ambient Air       |                         |
    Quality Standard  |  Annual Avg  24H Avg	|  Annual Avg	24H Avg
    ------------------+-------------------------+-----------------------
    National          |  9 µg/m3	 35 µg/m3   |  None	        150 µg/m3
    California        |  12 µg/m3	 None	    |  20 µg/m3	    50 µg/m3

    ## References

    [1] https://ww2.arb.ca.gov/resources/inhalable-particulate-matter-and-health

    """

    standard_concentration: "PMStandardConcentration"
    ambient_concentration: "PMAmbientConcentration"
    particulate_count: "PMCount"
    aqis: "AQIs"
    recorded_at: datetime


@attrs.define()
class PMStandardConcentration:
    """
    PM Values at "Standard" Concentration (ie, standard pressure at sea level).

    See: https://learn.adafruit.com/pm25-air-quality-sensor/usage-notes
    """

    diameter_at_most_1_0: int
    diameter_at_most_2_5: int
    diameter_at_most_10_0: int


@attrs.define()
class PMAmbientConcentration:
    """
    PM Values at "Ambient/Environment" Concentration (ie, ambient pressure).

    See: https://learn.adafruit.com/pm25-air-quality-sensor/usage-notes
    """

    diameter_at_most_1_0: int
    diameter_at_most_2_5: int
    diameter_at_most_10_0: int


@attrs.define()
class AQIs:
    """
    PM Values at "Ambient/Environment" Concentration (ie, ambient pressure).

    See: https://learn.adafruit.com/pm25-air-quality-sensor/usage-notes
    """

    aqi_pm25: int
    aqi_pm10: int


@attrs.define()
class PMCount:
    """The raw number of particles in 0.1 Litre of air."""

    number_of_particles_size_0_3um: int
    number_of_particles_size_0_5um: int
    number_of_particles_size_1_0um: int
    number_of_particles_size_2_5um: int
    number_of_particles_size_5_0um: int
    number_of_particles_size_10_0um: int


def create_report(air_quality_data: dict[str, int]) -> "AirQualityReport":
    """Create report for PM concentrations and particulate count."""
    ambient_concentration: PMAmbientConcentration = PMAmbientConcentration(
        diameter_at_most_1_0=air_quality_data.get("pm10 env"),
        diameter_at_most_2_5=air_quality_data.get("pm25 env"),
        diameter_at_most_10_0=air_quality_data.get("pm100 env"),
    )
    standard_concentration: PMStandardConcentration = PMStandardConcentration(
        diameter_at_most_1_0=air_quality_data.get("pm10 standard"),
        diameter_at_most_2_5=air_quality_data.get("pm25 standard"),
        diameter_at_most_10_0=air_quality_data.get("pm100 standard"),
    )
    particulate_count: PMCount = PMCount(
        number_of_particles_size_0_3um=air_quality_data.get("particles 03um"),
        number_of_particles_size_0_5um=air_quality_data.get("particles 05um"),
        number_of_particles_size_1_0um=air_quality_data.get("particles 10um"),
        number_of_particles_size_2_5um=air_quality_data.get("particles 25um"),
        number_of_particles_size_5_0um=air_quality_data.get("particles 50um"),
        number_of_particles_size_10_0um=air_quality_data.get("particles 100um"),
    )
    aqis: AQIs = AQIs(
        aqi_pm25=convert_pm25_to_iaqi(air_quality_data.get("pm25 env")),
        aqi_pm10=convert_pm10_to_iaqi(air_quality_data.get("pm10 env")),
    )

    return AirQualityReport(
        standard_concentration=standard_concentration,
        ambient_concentration=ambient_concentration,
        particulate_count=particulate_count,
        aqis=aqis,
        recorded_at=datetime.now(tz=UTC),
    )
