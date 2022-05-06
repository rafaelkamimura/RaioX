import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from uncertainties import ufloat
from uncertainties.umath import *


#constants:
d = 2.014*constants.angstrom #Angstrom
h = constants.h
n = 1
c = constants.c

#equations
def E(theta):
    return (n*h*c)/(2*d*sin(theta))


#Procedimento 1:
theta_alpha = ufloat(np.deg2rad(22.45), np.deg2rad(0.05))
theta_beta = ufloat(np.deg2rad(20.25), np.deg2rad(0.05))
E_alpha = E(theta_alpha)/constants.eV
E_beta = E(theta_beta)/constants.eV

print(f'$E_alpha$ = {E_alpha*1e-3} keV')
print(f'$E_beta$ = {E_beta*1e-3} keV')

