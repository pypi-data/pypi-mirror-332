import numpy as np
import pandas as pd
import netCDF4 as nc
import matplotlib.pyplot as plt

import sys
print(sys.version_info)

#functions for loading data

def unit(label,nf):
    param=nf.variables['param'][:]
    utime=param[15]/60. #min
    uN0=param[13] #1/cc
    uB0=param[11] #nT
    uVa=param[14] #km/s
    uE0=param[12] #m/V
    uT0=param[16] #eV
    para0=dict(B=uB0,N=uN0,E=uE0,V=uVa,T=uT0, time=utime)
    return para0[label]

def loading_hybird_data(nf):
    r=nf.variables['n_r'][:]  #Re                       nr
    theta=nf.variables['n_theta'][:]*180/np.pi #degree  nth
    phi=nf.variables['n_phi'][:]*180/np.pi #degree      nph
    logE=nf.variables['n_e'][:] #lg [eV]                nE
    alpha=nf.variables['n_alpha'][:]*180/np.pi #degree  nA
    time=nf.variables['time'][:]*unit('time',nf) #min   nt
    position=nf.variables['position'][:] #Re            npo x 3
    vol=nf.variables['vol'][:] #Re^3                    nph x nth x nr
    upstream=nf.variables['upstream'][:] #              nt x 10 x npo 
    flux_nth=nf.variables['flux_nth'][:] #              nt x nA x nE x nph x nth x nr
    flux_sth=nf.variables['flux_sth'][:] #              nt x nA x nE x nph x nth x nr   
    
    bx=upstream[:,0,0:2]*unit('B',nf) #nT                 nt x npo 
    by=upstream[:,1,0:2]*unit('B',nf) #nT                 nt x npo 
    bz=upstream[:,2,0:2]*unit('B',nf) #nT                 nt x npo 
    Ex=upstream[:,3,0:2]*unit('E',nf) #m/V                nt x npo 
    Ey=upstream[:,4,0:2]*unit('E',nf) #m/V                nt x npo 
    Ez=upstream[:,5,0:2]*unit('E',nf) #m/V                nt x npo 
    Ni=upstream[:,6,0:2]*unit('N',nf) #1/cc               nt x npo 
    Vix=upstream[:,7,0:2]*unit('V',nf)  #km/s             nt x npo 
    Viy=upstream[:,8,0:2]*unit('V',nf)  #km/s             nt x npo 
    Viz=upstream[:,9,0:2]*unit('V',nf)  #km/s             nt x npo 
    
    return dict(r=r,theta=theta,phi=phi,logE=logE,alpha=alpha,time=time,
                position=position,vol=vol,flux_nth=flux_nth,flux_sth=flux_sth,
                Bx=bx,By=by,Bz=bz,Ex=Ex,Ey=Ey,Ez=Ez,Ni=Ni,Vix=Vix,Viy=Viy,Viz=Viz)