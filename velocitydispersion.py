##Velocity Dispersion

def luminosity(h,R):       
    lum = ((10**10.2*h**-2)*(R/10**0.52*h**-1)**1.5)
    return lum

def vel_dispersion(L,h):
    sigma = (((L/10**10.2*h**-2)**0.25)*10**2.197)
    return sigma

R = float(input("Enter the effective radius in kpc: "))
h = float(0.72/0.7)           # h=h70 is reduced Hubbles constant
lum = luminosity(h,R)           # In terms of solar luminosity
sigma = vel_dispersion(lum,h)   # In kilometer/sec 
print("Lum in 1e10 Lsun:",lum/1.e10)
print("Velocity dispersion in km/s:",sigma)


