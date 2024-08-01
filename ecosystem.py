import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class SaltEcosystem:
    def __init__(self,foodweb,environment,nutrients=None,contaminants=None,size=None,age=None):
        self.foodweb = foodweb
        self.nutrients = nutrients
        self.environment = environment
        self.size = size
        self.age = age
        self.contaminants = contaminants

    def get_foodweb(self):
        if self.foodweb is not None:
            return self.foodweb
        else:
            return None

    def get_nutrients(self):
        if self.nutrients is not None:
            return self.nutrients
        else:
            return None

    def get_environment(self):
        if self.environment is not None:
            return self.environment
        else:
            return None

    def get_contanminants(self):
        if self.contaminants is not None:
            return self.contaminants
        else:
            return None

    def get_size(self):
        if self.size is not None:
            return self.size
        else:
            return 0

    def get_age(self):
        if self.age is not None:
            return self.age
        else:
            return None


