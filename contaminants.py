
class Contaminant:
    def __init__(self,name,concentration,unit, bioaccumilates=False):
        self.name = name
        self.concentration = concentration
        self.unit = unit
        self.bioaccumilates = bioaccumilates


    def get_properties(self):
        properties = {
            'name': self.name,
            'concentration': self.concentration,
            'bioaccumilates': self.bioaccumilates,
            'unit': self.unit
        }
        return properties


    def get_specific_property(self,record):
        property = self.get_properties()
        return property[record]

