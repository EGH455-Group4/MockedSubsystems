'''This file holds the models used throughout the Air Quality program.'''

class SensorReading(dict):
    '''Sensor reading is the generic sensor reading object.'''
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

        dict.__init__(self, value=value, unit=unit)

    def __str__(self) -> str:
        return f"{self.value}{self.unit}"

class GasReading(dict):
    '''GasReading is a specific sensor reading of the hazardous_gases'''
    def __init__(self, oxidising_gases: SensorReading = None, reducing_gases: SensorReading = None,
                nh3: SensorReading = None):
        self.oxidising_gases = oxidising_gases
        self.reducing_gases = reducing_gases
        self.nh3 = nh3

        dict.__init__(self, oxidising_gases=oxidising_gases, reducing_gases=reducing_gases, \
                      nh3=nh3)

    def __str__(self) -> str:
        # pylint: disable=C0301
        return f"oxidising_gases: {self.oxidising_gases}, reducing_gases: {self.reducing_gases}, nh3: {self.nh3}"

class IndividualGasReading(dict):
    '''IndividualGasReading is a specific sensor reading of the hazardous gases split out'''
    def __init__(self, carbon_monoxide: SensorReading = None, nitrogen_dioxide: SensorReading = None,
                ethanol: SensorReading = None, hydrogen: SensorReading = None, ammonia: SensorReading = None,
                methane: SensorReading = None, propane: SensorReading = None, iso_butane: SensorReading = None):
        self.carbon_monoxide = carbon_monoxide
        self.nitrogen_dioxide = nitrogen_dioxide
        self.ethanol = ethanol
        self.hydrogen = hydrogen
        self.ammonia = ammonia
        self.methane = methane
        self.propane = propane
        self.iso_butane = iso_butane

        dict.__init__(self, carbon_monoxide=carbon_monoxide, nitrogen_dioxide=nitrogen_dioxide, \
                      ethanol=ethanol, hydrogen=hydrogen, ammonia=ammonia, methane=methane, \
                      propane=propane, iso_butane=iso_butane)

    def __str__(self) -> str:
        # pylint: disable=C0301
        return f"carbon_monoxide: {self.carbon_monoxide}, nitrogen_dioxide: {self.nitrogen_dioxide}, ethanol: {self.ethanol}, hydrogen: {self.hydrogen}, ammonia: {self.ammonia}, methane: {self.methane}, propane: {self.propane}, iso-butane: {self.iso_butane}"

class Sensors(dict):
    '''Sensor is all the required sensor readings.'''
    # pylint: disable=R0913
    def __init__(self, light: SensorReading = None, hazardous_gases: GasReading = None,
                    humidity: SensorReading = None, pressure: SensorReading = None,
                    temperature: SensorReading = None, individual_gases: GasReading = None):
        self.light = light
        self.hazardous_gases = hazardous_gases
        self.humidity = humidity
        self.pressure = pressure
        self.temperature = temperature
        self.individual_gases = individual_gases

        dict.__init__(self, light=light, hazardous_gases=hazardous_gases, humidity=humidity, \
                      pressure=pressure, temperature=temperature, individual_gases=individual_gases)

    def __str__(self) -> str:
        # pylint: disable=C0301
        return f"light: {self.light}, gas_reading: {self.hazardous_gases}, humidity: {self.humidity}, pressure: {self.pressure}, temperature: {self.temperature}, individual_gases: {self.individual_gases}."

class AirQuality(dict):
    '''Air Quality is the entire reading of the sensors with the datetime of the reading.'''
    def __init__(self, sensors: Sensors, timestamp: str):
        self.sensors = sensors
        self.timestamp = timestamp

        dict.__init__(self, sensors=sensors, timestamp=timestamp)

class GeneralResponse:
    '''General response is the generic response object.'''
    def __init__(self, status: str):
        self.status = status
