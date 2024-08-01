import formulas

class Species:
    def __init__(self,name,trophic_level,biomass,growth_rate=None,respiration_rate=None,intrinsic_growth_rate=None,metabolic_rate=None,
                 predation_rate=None,delta13C=None,delta15N=None,preys=[],population=1,prey_biomass=None,carrying_capacity=None,mortality_rate=0,
                 contaminant_effect=0,environmental_effect=0,):

        self.name = name
        self.trophic_level = trophic_level
        self.biomass = biomass
        self.population = population
        self.growth_rate = growth_rate
        self.respiration_rate = respiration_rate
        self.intrinsic_growth_rate = intrinsic_growth_rate
        self.metabolic_rate = metabolic_rate
        self.predation_rate = predation_rate
        self.delta13C = delta13C
        self.delta15N = delta15N
        self.preys = preys
        self.carrying_capacity = carrying_capacity
        self.prey_biomass = prey_biomass
        self.mortality_rate = mortality_rate
        self.contaminant_effect = contaminant_effect
        self.environmental_effect = environmental_effect

        self.properties = {
            'name': self.name,
            'trophic_level': self.trophic_level,
            'biomass': self.biomass,
            'population': self.population,
            'growth_rate': self.growth_rate,
            'respiration_rate': self.respiration_rate,
            'intrinsic_growth_rate': self.intrinsic_growth_rate,
            'metabolic_rate': self.metabolic_rate,
            'predation_rate': self.predation_rate,
            'delta13C': self.delta13C,
            'delta15N': self.delta15N,
            'preys': self.preys,
            'prey_biomass': self.prey_biomass,
            'carrying_capacity':self.carrying_capacity,
            "mortality_rate":self.mortality_rate,
            "contaminant_effect": self.contaminant_effect,
            "environmental_effects": self.environmental_effect
        }


    def __repr__(self):
        return f"Species(name={self.name}, trophic_level={self.trophic_level}, biomass={self.biomass}, population={self.population}, carrying capacity={self.carrying_capacity})"


    def get_properties(self):
        return self.properties


    def get_specific_property(self,name):
        properties = self.get_properties()
        return properties[name]

    def update_specific_property(self,name,value):
        self.properties[name] = value


    def calculate_growth_rate_intrinsic(self,percentage=False):
        try:
            rate = formulas.growth_rate_intrisic(biomass=self.biomass,intrinsic_growth_rate=self.intrinsic_growth_rate,percentage=percentage)
            return rate

        except TypeError:
            print('[error] One of the parameters is set to None')
            return "ERROR"



    def calculate_growth_rate(self,final_biomass,percentage=False):
        try:
            rate = formulas.growth_rate(initial=self.biomass,final=final_biomass,percentage=percentage)
            return rate

        except TypeError as error:
            print(f"!! {error}")
            return "ERROR"


    def calculate_compound_annual_growth_rate(self,final_biomass,period,unit='years',percentage=False):
        try:
            rate = formulas.compound_annual_growth_rate(initial=self.biomass,final=final_biomass,unit=unit,period=period,percentage=percentage)
            return rate

        except TypeError as error:
            print(f"!! {error}")
            return "ERROR"


    def calculate_respiration_rate_using_biomass(self,percentage=False):
        try:
            rate = formulas.respiration_rate_bm(biomass=self.biomass,metabolic_rate=self.metabolic_rate,percentage=percentage)
            return rate

        except TypeError as error:
            print(f"!! {error} :: one of the parameters empty")
            return 'ERROR'


    def calculate_predation_rate(self,attack_rate,prey_handling_time,percentage=False):
        global total_prey_biomass
        try:
            for prey in self.preys:
                total_prey_biomass =+ prey.biomass
            rate = formulas.predation_rate(prey_biomass=total_prey_biomass,attack_rate=attack_rate,predator_handling_time=prey_handling_time,percentage=percentage)
            return rate

        except TypeError as error:
            print(f"!! {error}")
            return "ERROR"


