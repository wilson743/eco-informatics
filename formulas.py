import numpy as np
import pandas as pd
from scipy.integrate import odeint


def growth_rate(initial,final,):
    rate = ((final - initial) / initial)
    return rate


def growth(biomass,intrinsic_growth_rate):
    gained_biomass = biomass * intrinsic_growth_rate
    return gained_biomass


def compound_annual_growth_rate(initial,final,period,unit='years'):
    rate = ((final/initial) ** (1 / period)) - 1
    return{
        'rate': rate,
        'unit': unit
        }


def respiration_rate(initial_o2, final_o2,t1,t2,unit="mg/L"):
    deltaO2 = final_o2 - initial_o2
    deltaT = t2 - t1
    rate = deltaO2 / deltaT

    return {
        'rate': rate,
        'unit': unit
        }


def respiration_rate_bm(biomass,metabolic_rate):
    rate = biomass * metabolic_rate
    return rate


def predation_rate(prey_biomass,attack_rate,predator_handling_time):
    rate = (attack_rate * prey_biomass) / (1 + attack_rate * prey_biomass * predator_handling_time)
    return rate

def differential_lotka_voltera_equation(y,t,alpha,beta,delta,gamma):
    prey,predator = y
    dydt = [alpha*prey - beta*prey*predator, delta*prey*predator - gamma*predator]
    return dydt

def loss_due_salinity(biomass,salinity_sensitivity_coeffecient, concentration, optimal_concentration):
    biomass_lost = salinity_sensitivity_coeffecient * biomass * (concentration/optimal_concentration)
    return biomass_lost

def loss_due_contaminant(biomass, contaminant_sensivity_coefficient, contaminant_concentration):
    biomass_lost = contaminant_sensivity_coefficient * biomass * contaminant_concentration
    return biomass_lost

def gained_due_tidal_inundation(nutrient_concentration, sediment_deposition_rate, flooding_freq = 2):
    gained_biomass = flooding_freq * nutrient_concentration * sediment_deposition_rate
    return gained_biomass

def primary_productivity_using_rates(intrinsic_growth_rate,biomass,carrying_capacity,respiration_rate,predation_rate,salinity_stress,contaminant_effect,tidal_action,nutrient_uptake_rate):
    dBdt = intrinsic_growth_rate*biomass*(1-(biomass/carrying_capacity)) + tidal_action*biomass + nutrient_uptake_rate*biomass - respiration_rate*biomass - predation_rate*biomass - salinity_stress*biomass - contaminant_effect*biomass
    return dBdt

def primary_productivity_using_biomass(intrinsic_growth_rate, biomass, carrying_capacity, gained_due_tidal_action, gained_due_nutrient_uptake,loss_due_salinity, loss_due_contaminant, loss_due_predation, loss_due_respiration, loss_due_sea_level):
    dBdt = intrinsic_growth_rate*biomass*(1 - (biomass/carrying_capacity)) + gained_due_tidal_action + gained_due_nutrient_uptake - loss_due_salinity - loss_due_contaminant - loss_due_predation - loss_due_respiration - loss_due_sea_level
    return dBdt
