import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from uncertainties import ufloat, unumpy
from uncertainties.umath import *
import scipy.optimize as opt


#constants:
d = 2.014*constants.angstrom #Angstrom
h = constants.h
n = 1
c = constants.c
e = constants.elementary_charge

#equations
def E(theta):
    return (n*h*c)/(2*d*unumpy.sin(theta))

def lambda_min(theta):
    n = 2
    return np.hstack(np.array(2*d*np.sin(theta))/n)


#Procedimento 1:
theta_alpha = ufloat(np.deg2rad(22.45), np.deg2rad(0.05))
theta_beta = ufloat(np.deg2rad(20.25), np.deg2rad(0.05))
E_alpha = E(theta_alpha)/constants.eV
E_beta = E(theta_beta)/constants.eV

print(f'Procedimento 1 :\n', f'$E_alpha$ = {E_alpha*1e-3} keV \n', f'$E_beta$ = {E_beta*1e-3} keV')

#Procedimento 3:

dataP3 = np.loadtxt('dataP3.dat', dtype=np.float64)
U_P3 = dataP3[:,0]*1e3
theta_alpha_P3 = np.deg2rad(dataP3[:,2]/2)
theta_beta_P3 = np.deg2rad(dataP3[:,1]/2)

lambda_alpha = lambda_min(theta_alpha_P3)
lambda_beta = np.sort(lambda_min(theta_beta_P3))

#print(lambda_alpha)
#print(lambda_beta)

#print(U_P3*lambda_beta)

def DH(U, lamb):
    return U*lamb


popt, _ = opt.curve_fit(DH, 1/U_P3, lambda_beta)


print(popt)


plt.scatter(1/U_P3, lambda_beta*1e2)
#plt.plot(1/U_P3, lambda_beta)
#plt.plot(DH(popt, lambda_beta))
plt.xlabel('1/U (keV)')
plt.ylabel('$\lambda$ (pm)')
#plt.plot(1/(U_P3/constants.eV), DH(1/(U_P3/constants.eV), lambda_beta))
plt.savefig('procedimento3-1.png')
plt.show()


