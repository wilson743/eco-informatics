class Environment:
    def __init__(self, temperature, salinity, carbon_dioxide_conc, humidity, light_intensity=None, tidal_action=None, soil_oxygen_conc=None):
        self.light_intensity = light_intensity
        self.temperature = temperature
        self.tidal_action = tidal_action
        self.salinity = salinity
        self.soil_oxygen_conc = soil_oxygen_conc
        self.carbon_dioxide_conc = carbon_dioxide_conc
        self.humidity = humidity


    def get_properties(self):
        self.properties = {
            'light intensity': self.light_intensity,
            'temperature': self.temperature,
            'tidal action': self.tidal_action,
            'salinity': self.salinity,
            'soil oxygen': self.soil_oxygen_conc,
            'carbon dioxide': self.carbon_dioxide_conc,
            'humidity': self.humidity
        }
        return self.properties


    def update_property(self,name,value):
        self.properties[name] = value


class Nutrient:
    def __init__(self,name,concentration):
        self.name = name
        self.concentration = concentration
