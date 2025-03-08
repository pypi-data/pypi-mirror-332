import numpy as np
import netCDF4 as nc
import gc
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

def loading_data(file):
    nf=nc.Dataset(file)
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
    
    bx=upstream[:,0,:]*unit('B',nf) #nT                 nt x npo 
    by=upstream[:,1,:]*unit('B',nf) #nT                 nt x npo 
    bz=upstream[:,2,:]*unit('B',nf) #nT                 nt x npo 
    Ex=upstream[:,3,:]*unit('E',nf) #m/V                nt x npo 
    Ey=upstream[:,4,:]*unit('E',nf) #m/V                nt x npo 
    Ez=upstream[:,5,:]*unit('E',nf) #m/V                nt x npo 
    Ni=upstream[:,6,:]*unit('N',nf) #1/cc               nt x npo 
    Vix=upstream[:,7,:]*unit('V',nf)  #km/s             nt x npo 
    Viy=upstream[:,8,:]*unit('V',nf)  #km/s             nt x npo 
    Viz=upstream[:,9,:]*unit('V',nf)  #km/s             nt x npo 
    
    dic=dict(time=time,alpha=alpha,logE=logE,phi=phi,theta=theta,r=r,
                vol=vol,flux_nth=flux_nth,flux_sth=flux_sth,position=position,
                Bx=bx,By=by,Bz=bz,Ex=Ex,Ey=Ey,Ez=Ez,Ni=Ni,Vix=Vix,Viy=Viy,Viz=Viz)
    return dic
    del r,theta,phi,logE,alpha,time,position,vol,flux_nth,flux_sth,bx,by,bz,Ex,Ey,Ez,Ni,Vix,Viy,Viz,dic
    gc.collect()

import matplotlib.pyplot as plt
import numpy
#Functions for plotting IMF data
def set_dnum(num):
    dk=10**np.floor(np.log10(num))
    #print(num,dk,round(num/dk)*dk)
    return round(num/dk)*dk

def plot_SW_data(dict,pos=1,path='',tmin=0,tmax=0):
    i=pos-1
    bxi=dict['Bx'][:,i]
    byi=dict['By'][:,i]
    bzi=dict['Bz'][:,i]
    bt=np.sqrt(dict['Bx'][:]*dict['Bx'][:]+dict['By'][:]*dict['By'][:]+dict['Bz'][:]*dict['Bz'][:])
    bti=bt[:,i]
    Nii=dict['Ni'][:,i]
    Exi=dict['Ex'][:,i]
    Eyi=dict['Ey'][:,i]
    Ezi=dict['Ez'][:,i]
    Et=np.sqrt(dict['Ex'][:]*dict['Ex'][:]+dict['Ey'][:]*dict['Ey'][:]+dict['Ez'][:]*dict['Ez'][:])
    Eti=Et[:,i]
    Vixi=dict['Vix'][:,i]
    Viyi=dict['Viy'][:,i]
    Vizi=dict['Viz'][:,i]
    Vit=np.sqrt(dict['Vix'][:]*dict['Vix'][:]+dict['Viy'][:]*dict['Viy'][:]+dict['Viz'][:]*dict['Viz'][:])
    Viti=Vit[:,i]
    posi=dict['position'][i,:]
    time=dict['time'][:]
    
    if tmin==tmax:
        dt=round((max(time)-min(time))/10)
        mint=round(np.floor(min(time)/dt))
        maxt=round(np.ceil(max(time)/dt))
    else:
        dt=round((tmax-tmin)/10)
        mint=round(np.floor(tmin/dt))
        maxt=round(np.ceil(tmax/dt))
    pt=np.where((time>tmin) & (time <tmax))[0]
    db=set_dnum(max([np.max(bt[pt,:]),1.5*np.median(bt[pt,:])])/3)
    minbt=0
    maxbt=round(np.ceil(max([np.max(bt[pt,:]),1.5*np.median(bt[pt,:])])/db))
    #print(maxbt,db,np.max(bt),1.5*np.median(bt),np.shape(bt),pt,time,mint,maxt)
    v1=abs(min([np.min(dict['Bx'][pt,:]),np.min(dict['By'][pt,:]),np.min(dict['Bz'][pt,:])]))
    v2=abs(max([np.max(dict['Bx'][pt,:]),np.max(dict['By'][pt,:]),np.max(dict['Bz'][pt,:])]))
    vk=1.3*max([v1,v2])
    minbk=round(np.floor(-vk/db))
    maxbk=round(np.ceil(vk/db))
    dE=set_dnum(max([np.max(Et[pt,:]),1.5*np.median(Et[pt,:])])/3)#0.005
    minEt=0
    maxEt=round(np.ceil(max([np.max(Et[pt,:]),1.5*np.median(Et[pt,:])])/dE))
    v1=abs(min([np.min(dict['Ex'][pt,:]),np.min(dict['Ey'][pt,:]),np.min(dict['Ez'][pt,:])]))
    v2=abs(max([np.max(dict['Ex'][pt,:]),np.max(dict['Ey'][pt,:]),np.max(dict['Ez'][pt,:])]))        
    vk=1.3*max([v1,v2])
    minEk=round(np.floor(-vk/dE))
    maxEk=round(np.ceil(vk/dE))
    dN=set_dnum(max([np.max(dict['Ni'][pt,:]),1.5*np.median(dict['Ni'][pt,:])])/4)#20
    minN=0
    maxN=round(np.ceil(max([np.max(dict['Ni'][pt,:]),1.5*np.median(dict['Ni'][pt,:])])/dN))
    dV=set_dnum(max([np.max(Vit[pt,:]),1.5*np.median(Vit[pt,:])])/3)#100
    Vx0=np.median(dict['Vix'][pt,:])#-350
    minVt=0
    maxVt=round(np.ceil(max([np.max(Vit[pt,:]),1.5*np.median(Vit[pt,:])])/dV))
    v1=min([np.min(dict['Vix'][pt,:]-Vx0),np.min(dict['Viy'][pt,:]),np.min(dict['Viz'][pt,:])])
    v2=max([np.max(dict['Vix'][pt,:]-Vx0),np.max(dict['Viy'][pt,:]),np.max(dict['Viz'][pt,:])])
    vs=max([np.std(dict['Vix'][pt,:]-Vx0),np.std(dict['Viy'][pt,:]),np.std(dict['Viy'][pt,:])])
    #print(v2,v1,vs)
    dVc=set_dnum(max([v2-v1,1.5*vs])/3)
    vk=1.3*max([abs(v1),abs(v2)])
    minVk=round(np.floor(-vk/dVc))
    maxVk=round(np.ceil(vk/dVc))
  
    
    my_dpi=200
    fig, axs=plt.subplots(7,1,figsize=(1200/my_dpi,1500/my_dpi),dpi=my_dpi,sharex=True)
    textp=[0.05,0.1,0.15]
    
    axs[0].plot(time,bti,color='k')
    axs[0].plot(time,bti,color='k')
    axs[0].set_xlim(mint*dt,maxt*dt)
    axs[0].set_ylim(minbt*db,maxbt*db)
    axs[0].set_ylabel('B [nT]')
    #axs[0].set_yticks([float(j)*db for j in range(minbt,maxbt,1)])
    #axs[0].set_xticks([float(j)*dt for j in range(mint,maxt+1,1)])
    axs[0].tick_params(axis='x',labelsize=0,top=True)
    axs[0].minorticks_on()

    axs[1].plot(time,bxi,color='r')
    axs[1].plot(time,byi,color='g')
    axs[1].plot(time,bzi,color='b')
    axs[1].set_ylim(minbk*db,maxbk*db)
    axs[1].set_ylabel('$B_{x, y, z}$ [nT]')
    #axs[1].set_yticks([float(j)*db for j in range(minbk+1,maxbk,1)])
    axs[1].tick_params(axis='x',labelsize=0,top=True)
    axs[1].text(maxt*dt-(maxt-mint)*dt*(textp[0]+3*textp[1]),maxbk*db-(maxbk-minbk)*db*textp[2],'$B_x$',color='r')
    axs[1].text(maxt*dt-(maxt-mint)*dt*(textp[0]+2*textp[1]),maxbk*db-(maxbk-minbk)*db*textp[2],'$B_y$',color='g')
    axs[1].text(maxt*dt-(maxt-mint)*dt*(textp[0]+1*textp[1]),maxbk*db-(maxbk-minbk)*db*textp[2],'$B_z$',color='b')
    axs[1].minorticks_on()
    
    axs[2].plot(time,Nii,color='k')
    axs[2].set_ylim(minN*dN,maxN*dN)
    axs[2].set_ylabel('$N_i$ [$cm^{-3}$]')
    #axs[2].set_yticks([float(j)*dN for j in range(minN+1,maxN+1,1)])
    axs[2].tick_params(axis='x',labelsize=0,top=True)
    axs[2].minorticks_on()

    axs[3].plot(time,Eti,color='k')
    axs[3].plot(time,Eti,color='k')
    axs[3].set_ylim(minEt*dE,maxEt*dE)
    #axs[3].set_yticks([float(j)*dE for j in range(minEt,maxEt+1,1)])
    axs[3].set_ylabel('E [m/V]')
    axs[3].tick_params(axis='x',labelsize=0,top=True)
    axs[3].minorticks_on()

    axs[4].plot(time,Exi,color='r')
    axs[4].plot(time,Eyi,color='g')
    axs[4].plot(time,Ezi,color='b')
    axs[4].set_ylim(minEk*dE,maxEk*dE)
    axs[4].set_ylabel('$E_{x, y, z}$ [m/V]')
    #axs[4].set_yticks([float(j)*dE for j in range(minEk,maxEk,1)])
    axs[4].tick_params(axis='x',labelsize=0,top=True)
    axs[4].text(maxt*dt-(maxt-mint)*dt*(textp[0]+3*textp[1]),maxEk*dE-(maxEk-minEk)*dE*textp[2],'$E_x$',color='r')
    axs[4].text(maxt*dt-(maxt-mint)*dt*(textp[0]+2*textp[1]),maxEk*dE-(maxEk-minEk)*dE*textp[2],'$E_y$',color='g')
    axs[4].text(maxt*dt-(maxt-mint)*dt*(textp[0]+1*textp[1]),maxEk*dE-(maxEk-minEk)*dE*textp[2],'$E_z$',color='b')
    axs[4].minorticks_on()

    axs[5].plot(time,Viti,color='k')    
    axs[5].set_ylim(minVt*dV,maxVt*dV)
    axs[5].set_ylabel('$V_i$ [km/s]')
    #axs[5].set_yticks([float(j)*dV for j in range(minVt+1,maxVt,1)])
    axs[5].tick_params(axis='x',labelsize=0,top=True)
    axs[5].minorticks_on()

    axs[6].plot(time,Vixi-Vx0,color='r')
    axs[6].plot(time,Viyi,color='g')
    axs[6].plot(time,Vizi,color='b')
    axs[6].set_ylim(minVk*dVc,maxVk*dVc)
    axs[6].set_ylabel('$V_{iy, iz}$ [km/s]')
    #axs[6].set_yticks([float(j)*dVc for j in range(minVk,maxVk+1,1)])
    axs[6].tick_params(axis='x',top=True)
    zz=axs[6].twinx()
    zz.set_ylabel('$V_{ix}$ [km/s]',color='r')
    zz.set_ylim(minVk*dVc+Vx0,maxVk*dVc+Vx0)
    #print(minVk*dV+Vx0,maxVk*dV+Vx0,[float(j)*dV+Vx0 for j in range(minVk,maxVk+1,1)])

    zz.spines['right'].set_color('red')
    zz.minorticks_on()
    zz.tick_params(axis='y', colors='red',which='both')
    axs[6].text(maxt*dt-(maxt-mint)*dt*(textp[0]+3*textp[1]),maxVk*dVc-(maxVk-minVk)*dVc*textp[2],'$V_{ix}$',color='r')
    axs[6].text(maxt*dt-(maxt-mint)*dt*(textp[0]+2*textp[1]),maxVk*dVc-(maxVk-minVk)*dVc*textp[2],'$V_{iy}$',color='g')
    axs[6].text(maxt*dt-(maxt-mint)*dt*(textp[0]+1*textp[1]),maxVk*dVc-(maxVk-minVk)*dVc*textp[2],'$V_{iz}$',color='b')
    axs[6].minorticks_on()
    axs[6].set_xlabel('t (min)')
    
    axs[0].set(title='Position '+str(pos)+' at (x, y, z)=('+str(round(posi[0],2))+', '+str(round(posi[1],2))+', '+str(round(posi[2],2))+") $R_E$")
    
    plt.subplots_adjust(left=0.16,
                    bottom=0.07,
                    right=0.88,
                    top=0.95,
                    wspace=0.2,
                    hspace=0.05
                   )
    if path!='':
        plt.savefig(r''+path+'SW_position_'+str(i)+'.jpeg')
    #plt.close(fig)

import numpy as np
import gc

def check_pos(array,pp):
    if np.size(pp)==1:
        dis=abs(array-pp[0])
        pos=np.where(dis==min(dis))[0]
        return pos
    else:
        pmin=np.min(pp)
        pmax=np.max(pp)
        if pmin==pmax:
            return check_pos(array,pmin)
        else:
            pos=np.where((array>=pmin)&(array<=pmax))[0]
        #print(pmin,pmax,pos)
            if len(pos)==0:
                pos=[0]
            return pos
            

def calcu_vk(Ek):
    c=2.998e8
    mi=1.673e-27
    p=np.sqrt(2*mi*c**2*Ek+Ek**2)/c
    gama=(mi*c**2+Ek)/(mi*c**2)
    vk=p/mi/gama
    return vk
    
def convertdata(dic,para='energy flux',condition='differential',sumPA=1,meant=0,times=0,lats=45,rs=4,lons=0,lgEs=[0,6],
                PAs=[0,180],M=1):
    rr=dic['r'][:]
    theta=dic['theta'][:]
    phi=dic['phi'][:]
    EE=dic['logE'][:]
    PA=dic['alpha'][:]
    time=dic['time'][:]
    vo=dic['vol'][:]
    northf=dic['flux_nth'][:]
    southf=dic['flux_sth'][:]

    pr=check_pos(rr,[rs])
    ptheta=check_pos(theta,[np.abs(lats)])
    pphi=check_pos(phi,[lons])
    pt=check_pos(time,[times])
    pe=check_pos(EE,[lgEs])
    pPA=check_pos(PA,[PAs])
    
    Re=6370e3
    MN=M/Re**3
    mi=1.673e-27
    C=1.602e-19
    Ek=10**EE
    vk=calcu_vk(Ek*C)

    ne=len(Ek)
    from scipy.interpolate import interp1d
    f=interp1d(np.linspace(1,ne,ne),EE,fill_value='extrapolate')
    EEn=f(np.linspace(0.5,ne+0.5,ne+1))
    EEk=10**EEn
    dE=EEk[1:ne+1]-EEk[0:ne]
    nPA=len(PA)
    f=interp1d(np.linspace(1,nPA,nPA),PA,fill_value='extrapolate')
    PAn=f(np.linspace(0.5,nPA+0.5,nPA+1))
    PAn[0]=0
    PAn[nPA]=180
    ome=2*np.pi*(np.cos(PAn[0:nPA]/180*np.pi)-np.cos(PAn[1:nPA+1]/180*np.pi))

    
    if np.min([lats])>0:
        ff=northf
    if np.min([lats])<0:
        ff=southf
    
    Ef=np.zeros((len(pt),len(pPA),len(pe),len(pphi),len(ptheta),len(pr)))
    nf=Ef*0
    
    match condition:
        case 'differential':
            rat=dE
        case 'integrated':
            rat=dE*0.+1
            
    for k in range(len(pe)):
        Ei=Ek[pe[k]]
        vi=vk[pe[k]]
        rati=rat[pe[k]]
        for i in range(len(pt)):
            for j in range(len(pPA)):
                omei=ome[pPA[j]]
                for l in range(len(pphi)):
                    for m in range(len(ptheta)):
                        for n in range(len(pr)):
                            voin=vo[pphi[l],ptheta[m],pr[n]]
                            ffi=max(ff[pt[i],pPA[j],pe[k],pphi[l],ptheta[m],pr[n]],0)
                            nf[i,j,k,l,m,n]=1e-4*MN*ffi/voin*vi/omei/rati
        Ef[:,:,k,:,:,:]=nf[:,:,k,:,:,:]*Ei
    
    if condition=='integrated':
        Ef=np.sum(Ef,2)
        nf=np.sum(nf,2)
    #print(np.shape(Ef))
    if sumPA>0:
        Ef=np.sum(Ef,1)
        nf=np.sum(nf,1)
    if meant>0:
        Ef=np.sum(Ef,0)/len(pt)
        nf=np.sum(nf,0)/len(pt)       
    #print(np.shape(Ef))
    meanE=Ef*0
    ps=np.where(nf>0)
    meanE[ps]=Ef[ps]/nf[ps]
    
    match para:
        case 'mean energy':
            data=meanE
            unit='eV'
            
        case 'energy flux':
            data=Ef
            if condition=='integrated':
                unit=r'eV/($cm^2\cdot$s$\cdot$sr)'
            if condition=='differential':
                unit=r'1/($cm^2\cdot$s$\cdot$sr)'            
        case 'number flux':
            data=nf   
            if condition=='integrated':
                unit=r'1/($cm^2\cdot$s$\cdot$sr)'
            if condition=='differential':
                unit=r'1/(eV$\cdot cm^2\cdot$s$\cdot$sr)'
    return dict(data=data,name=para,unit=unit,time=time[pt],alpha=PA[pPA],logE=EE[pe],phi=phi[pphi],theta=theta[ptheta],
                    r=rr[pr])
    del northf,southf,Ef,nf,meanE,data
    gc.collect()

#Functions for plotting ion distribution on section surface

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import math
import matplotlib
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import os

def plot_meridian_data(dic,nf,sf,vmin,vmax,title,textc,lato,lono,name=''):
    
    left=-0.25
    right=0.99
    top=0.98
    bottom=0
    lw=1

    r=dic['r']
    theta=dic['theta']*np.pi/180
    R, Theta = np.meshgrid(r, theta)
    alpha= [ (i/12.-0.5)*np.pi  for i in range(12)]
    phi= [ i/72.*2*np.pi for i in range(73)]
    rr=[3,6,9,12]
    
    my_dpi=200
    fig=plt.figure(figsize=(800/my_dpi,1200/my_dpi),dpi=my_dpi,clear=True) 
    ax=plt.subplot(111, projection='polar')
    ax.set_xlim(-80/90.*0.5*np.pi,80/90.*0.5*np.pi)
    ax.set_ylim(0,13)
    ax.set_yticks(rr)
    #print(np.max(nf),np.min(nf))
    caxn=ax.contourf(Theta,R,nf,levels=np.linspace(vmin,vmax,256),vmin=vmin,vmax=vmax,extend='both',cmap='jet')
    caxs=ax.contourf(-Theta,R,sf,levels=np.linspace(vmin,vmax,256),vmin=vmin,vmax=vmax,extend='both',cmap='jet')
    
    dx=(right-left)/(2*13)
    dy=(top-bottom)/(2*13) 
    xc=0.5*(left+right)-13/2*dx
    yc=0.5*(top+bottom)
    ax2=plt.axes([xc-dx,yc-dy,2*dx,2*dy],projection=ccrs.Orthographic(central_longitude=lono,central_latitude=lato))
    ax2.add_feature(cartopy.feature.OCEAN,color='blue')
    ax2.add_feature(cartopy.feature.LAND,color='green')
    ax2.set_global()
    
    
    for n in range(12):
        ax.plot([alpha[n],alpha[n]],[0,30],'k',linewidth=lw)
    for m in range(4):
        ax.plot(phi,rr[m]+np.array(phi)*0.,'k',linewidth=lw)
    
    ax.text(-0.49*np.pi,13,'r($R_E$)',color='k')
    ax.text(80/90.*0.5*np.pi,14,'lat.',color='k')
    for k in range(len(textc)):
        x=11
        y=13-1.2*k
        theta = np.arctan2(y, x)
        r = np.sqrt(x**2 + y**2)
        ax.text(theta,r,textc[k])
    
    #ax_cb=inset_axes(ax, bbox_to_anchor=(510,120, 100, 200),width='25%',height='120%')
    ax_cb=ax.inset_axes([0.8,0,0.05,0.3])
    #r'''
    plt.colorbar(caxn, cax=ax_cb, label=title,orientation='vertical',extend='both',ticks=np.linspace(vmin,vmax,vmax-vmin+1))
    
    plt.subplots_adjust(left=left,
                    bottom=bottom,
                    right=right,
                    top=top,
                    wspace=0.06,
                    hspace=0.05
                   )
    #r'''
    if name!='':
        plt.savefig(r''+name)
        plt.close(fig)


def plot_colatplane_data(dic,ff,vmin,vmax,title,textc,name=''):
    r=dic['r']#90-dic['theta']/np.pi*180
    theta=dic['phi']*np.pi/180+np.pi/2
    R, Theta = np.meshgrid(r, theta)
    alpha=[ (i/12.)*np.pi  for i in range(12)]# 
    phi= [ i/72.*2*np.pi for i in range(73)]
    rr=[ i*2  for i in range(7)]
    lw=1
    
    my_dpi=200
    fig=plt.figure(figsize=(800/my_dpi,800/my_dpi),dpi=my_dpi,clear=True) 
    ax=plt.subplot(111, projection='polar')
    ax.set_xlim(60/90.*0.5*np.pi,120/90.*0.5*np.pi)
    ax.set_ylim(0,12)
    ax.set_xticks((np.array(range(5)))*np.pi/12+60/90.*0.5*np.pi,np.roll(np.array(range(5))+10,5))
    ax.set_yticks(range(0,14,2))
    #caxn = ax.pcolormesh(Theta,R,ff,vmin=vmin,vmax=vmax,cmap='jet',shading='gouraud')
    caxn=ax.contourf(Theta,R,ff,levels=np.linspace(vmin,vmax,256),vmin=vmin,vmax=vmax,extend='both',cmap='jet')
 
    for n in range(12):
        ax.plot([alpha[n],alpha[n]],[0,70],'k',linewidth=lw)
    for m in range(7):
        ax.plot(phi,rr[m]+np.array(phi)*0.,'k',linewidth=lw)
       
    ax.text(63/90.*0.5*np.pi,13,'MLT',color='k')
    ax.text(20/90.*0.5*np.pi,1,'r($R_E$)',color='k')
    for k in range(len(textc)):
        x=-6
        y=5-1*k
        theta = np.arctan2(y, x)
        r = np.sqrt(x**2 + y**2)
        ax.text(theta,r,textc[k])
    #ax_cb = ax.inset_axes(bbox_to_anchor=(540,120, 100, 200),width='25%',height='120%')
    ax_cb=ax.inset_axes([0.85,0,0.05,0.4])
    plt.colorbar(caxn, cax=ax_cb, label=title,orientation='vertical',extend='both',ticks=np.linspace(vmin,vmax,vmax-vmin+1))
    plt.subplots_adjust(left=0.05,
                    bottom=0.05,
                    right=0.9,
                    top=0.9,
                    wspace=0.06,
                    hspace=0.05
                   )
    if name!='':
        plt.savefig(r''+name)
        plt.close(fig)

    
def plot_spheresurface_data(dic,ff,vmin,vmax,title,textc,name=''):
    r=90-dic['theta']
    theta=dic['phi']*np.pi/180+np.pi/2
    R, Theta = np.meshgrid(r, theta)
    alpha= [ (i/12.)*np.pi  for i in range(12)]
    phi= [ i/72.*2*np.pi for i in range(73)]
    rr=range(10,80,10)
    lw=1
    
    my_dpi=200
    fig=plt.figure(figsize=(800/my_dpi,800/my_dpi),dpi=my_dpi,clear=True) 
    ax=plt.subplot(111, projection='polar')
    ax.set_xlim(60/90.*0.5*np.pi,120/90.*0.5*np.pi)
    ax.set_ylim(0,60)
    ax.set_xticks((np.array(range(5)))*np.pi/12+60/90.*0.5*np.pi,np.roll(np.array(range(5))+10,5))
    ax.set_yticks(range(10,70,10),['80$\degree$','70$\degree$','60$\degree$','50$\degree$','40$\degree$','30$\degree$'])
    #caxn = ax.pcolormesh(Theta,R,ff,vmin=vmin,vmax=vmax,cmap='jet',shading='gouraud')
    caxn=ax.contourf(Theta,R,ff,levels=np.linspace(vmin,vmax,256),vmin=vmin,vmax=vmax,extend='both',cmap='jet')
 
    for n in range(12):
        ax.plot([alpha[n],alpha[n]],[0,70],'k',linewidth=lw)
    for m in range(7):
        ax.plot(phi,rr[m]+np.array(phi)*0.,'k',linewidth=lw)

    ax.text(63/90.*0.5*np.pi,67,'MLT',color='k')
    ax.text(20/90.*0.5*np.pi,3,'lat.',color='k')
    
    for k in range(len(textc)):
        x=-30
        y=20-5*k
        theta = np.arctan2(y, x)
        r = np.sqrt(x**2 + y**2)
        ax.text(theta,r,textc[k])
    #ax_cb = inset_axes(ax,bbox_to_anchor=(570,120, 100, 200),width='25%',height='120%')
    ax_cb=ax.inset_axes([0.85,0,0.05,0.4])
    plt.colorbar(caxn, cax=ax_cb, label=title,orientation='vertical',extend='both',ticks=np.linspace(vmin,vmax,vmax-vmin+1))
    plt.subplots_adjust(left=0.05,
                    bottom=0.05,
                    right=0.9,
                    top=0.9,
                    wspace=0.06,
                    hspace=0.05
                   )
    if name!='':
        plt.savefig(r''+name)
        plt.close(fig)

        
def plot_energyflux_section(dic,figpath='',value=[5,7],surface='meridian',para='energy flux',times=0,
                            lats=[35,80],rs=[4,12],lons=0,lgEs=3,PAs=[0,180],M=1):
    rr=dic['r'][:]
    theta=dic['theta'][:]
    phi=dic['phi'][:]
    EE=dic['logE'][:]
    PA=dic['alpha'][:]
    time=dic['time'][:]

    pr=check_pos(rr,[rs])
    ptheta=check_pos(theta,[np.abs(lats)])
    pphi=check_pos(phi,[lons])
    pt=check_pos(time,[times])
    pe=check_pos(EE,[lgEs])
    pPA=check_pos(PA,[PAs])
    
    minv=min(value)
    maxv=max(value)
    
    if len(pe)==1:
        EEt='lg(E[eV])='+str(round(EE(pe[0]),1))
    else:
        EEt='lg(E[eV]):['+str(round(np.min(lgEs),1))+','+str(round(np.max(lgEs),1))+']'
    
    if len(pPA)==1:
        PAt='PA='+str(np.min(PAs))+'$\degree$'
    else:
        PAt='PA:['+str(np.min(PAs))+'$\degree$,'+str(np.max(PAs))+'$\degree$]'
        
    rrt='r='+str(round(rr[pr[0]],1))+'$R_E$'
    if np.size([lats])>1:
        lat0=lats[0]
    else:
        lat0=lats
    if lat0>0:
        latstr='N'
        lathm='North'
    if lat0<0:
        latstr='S'
        lathm='South'
    if lat0==0:
        latstr=''
    thetat='lat.='+str(round(abs(theta[ptheta[0]])))+'$\degree$'+latstr
    phit='lon.='+str(round(phi[pphi[0]]))+'$\degree$'
    match para:
        case 'energy flux':
            title='Ions Log Energy Flux\n [eV/($cm^2\cdot$s$\cdot$sr)]'
        case 'number flux':
            title='Ions Log Flux\n [1/($cm^2\cdot$s$\cdot$sr)]'
        case 'mean energy':
            title='Ions Log Mean Energy\n [eV]' 
        
    match surface:
        case 'meridian':
            if figpath!='':
                spath=figpath+'meridian/'
                if not os.path.isdir(spath):
                    os.mkdir(spath)
                    
            for i in range(len(pt)):
                timet='t='+str(round(dic['time'][pt[i]],1))+'min'
                text=[timet,phit,EEt,PAt]                 
                dicn=convertdata(dic,para=para,condition='integrated',times=time[pt[i]],lats=[min(theta),max(theta)]
                                   ,rs=[min(rr),max(rr)],lons=phi[pphi[0]],lgEs=lgEs,PAs=PAs,M=M,sumPA=1)
                fnorth=dicn['data'][:]
                dics=convertdata(dic,para=para,condition='integrated',times=time[pt[i]],lats=[-max(theta),-min(theta)]
                                   ,rs=[min(rr),max(rr)],lons=phi[pphi[0]],lgEs=lgEs,PAs=PAs,M=M,sumPA=1)
                fsouth=dics['data'][:]
                fnorth[np.where(fnorth<=0)]=1e-10
                logfn=np.log10(fnorth)
                logfn=np.reshape(logfn,(len(theta),len(rr)))
                fsouth[np.where(fsouth<=0)]=1e-10
                logfs=np.log10(fsouth)
                logfs=np.reshape(logfs,(len(theta),len(rr)))
                if figpath!='':
                    figname=spath+'EF_'+str(i//100)+str((i//10)%10)+str(i%10)+'.jpeg'
                else:
                    figname=''
                plot_meridian_data(dic,logfn,logfs,minv,maxv,title,text,0,0,name=figname)
        
        case 'colat':
            if figpath!='':
                spath=figpath+'colat/'
                if not os.path.isdir(spath):
                    os.mkdir(spath)              
                
            for i in range(len(pt)):
                timet='t='+str(round(dic['time'][pt[i]],1))+'min'
                text=[timet,thetat,EEt,PAt]  
                dicl=convertdata(dic,para=para,condition='integrated',times=time[pt[i]],lats=lat0,rs=[min(rr),max(rr)],
                                   lons=[min(phi),max(phi)],lgEs=lgEs,PAs=PAs,M=M,sumPA=1)
                fsec=dicl['data'][:]
                fsec[np.where(fsec<=0)]=1e-20
                logf=np.log10(fsec)
                logf=np.reshape(logf,(len(phi),len(rr)))
                if figpath!='':
                    figname=spath+'EF_'+str(i//100)+str((i//10)%10)+str(i%10)+'.jpeg'
                else:
                    figname=''
                plot_colatplane_data(dic,logf,minv,maxv,title,text,name=figname)
                
        case 'spheresurface':
            if figpath!='':
                spath=figpath+'sphere_surface/'
                if not os.path.isdir(spath):
                    os.mkdir(spath)                
        
            for i in range(len(pt)):
                timet='t='+str(round(dic['time'][pt[i]],1))+'min'
                text=[timet,rrt,lathm,EEt,PAt]  
                dics=convertdata(dic,para=para,condition='integrated',times=time[pt[i]],lats=[min(theta),max(theta)]
                                 ,rs=rr[pr[0]],lons=[min(phi),max(phi)],lgEs=lgEs,PAs=PAs,M=M,sumPA=1)
                fsec=dics['data'][:]
                fsec[np.where(fsec<=0)]=1e-20
                logf=np.log10(fsec)
                logf=np.reshape(logf,(len(phi),len(theta)))
                if figpath!='':
                    figname=spath+'EF_'+str(i//100)+str((i//10)%10)+str(i%10)+'.jpeg'
                else:
                    figname=''
                plot_spheresurface_data(dic,logf,minv,maxv,title,text,name=figname)     

def plot_spectrum_coPA_data(time,PA,logE,ff,vmin,vmax,title,textc,name=''):
    time2, logE2 = np.meshgrid(time, logE)
    nPA=len(PA)
    
    my_dpi=200
    fig,axs=plt.subplots(nPA,1,figsize=(1200/my_dpi,2400/my_dpi),dpi=my_dpi,sharex=True) 
    axs[0].set(title=textc)
    axs[0].set_xlim(min(time),max(time))
    axs[nPA-1].set_xlabel('t (min)')
    for i in range(nPA):
        axs[i].set_ylim(min(logE),max(logE))
        axs[i].set_ylabel('logE\n(eV)')        
        axs[i].minorticks_on()
        if i<nPA-1:
            axs[i].tick_params(axis='x',labelsize=0,top=True)
        
        #print(np.shape(time2),np.shape(logE2),np.shape(ff))
        cs=axs[i].contourf(time2.T,logE2.T,np.reshape(ff[:,i,:],(len(time),len(logE))),levels=np.linspace(vmin,vmax,256),
                           vmin=vmin,vmax=vmax,extend='both',cmap='jet')
        cbar=plt.colorbar(cs,ax=axs[i],location='right',fraction=0.1,pad=0.01,shrink=0.9,aspect=10,
                          ticks=np.linspace(vmin,vmax,vmax-vmin+1))        
        PAtitle='PA='+str(round(PA[i]))+'$\degree$'
        axs[i].text(0.02,0.75,PAtitle,fontsize=10,bbox={'facecolor':'white','alpha':1,'pad':2},transform=axs[i].transAxes)
    
    plt.subplots_adjust(left=0.1,
                    bottom=0.04,
                    right=1.03,
                    top=0.95,
                    wspace=0.06,
                    hspace=0.05
                   )
    if name!='':
        plt.savefig(r''+name)
        plt.close(fig)

def plot_spectrum_coE_data(time,PA,logE,ff,vmin,vmax,title,textc,name=''):
    time2, PA2 = np.meshgrid(time, PA)
    nE=len(logE)
    num=int(round(nE/19.))
    if num==0:
        num=1
    col=int(np.ceil(nE/num))
    
    my_dpi=200
    fig,axs=plt.subplots(col,num,figsize=(1200*num/my_dpi,125*col/my_dpi),dpi=my_dpi,sharex=True) 
    fig.suptitle(textc,y=0.993)
    for j in range(num):
        axs[0][j].set_xlim(min(time),max(time))
        axs[col-1][j].set_xlabel('t (min)')
        for i in range(col):
            axs[i][j].set_ylim(min(PA),max(PA))
            axs[i][j].set_ylabel('PA($\degree$)')        
            axs[i][j].minorticks_on()
            if i<col-1:
                axs[i][j].tick_params(axis='x',labelsize=0,top=True)

            k=j*col+i
            if k<nE:
                cs=axs[i][j].contourf(time2.T,PA2.T,np.reshape(ff[:,:,k],(len(time),len(PA))),levels=np.linspace(vmin,vmax,256),
                                   vmin=vmin,vmax=vmax,extend='both',cmap='jet')
                cbar=plt.colorbar(cs,ax=axs[i][j],location='right',fraction=0.1,pad=0.01,shrink=0.9,aspect=10,
                                  ticks=np.linspace(vmin,vmax,vmax-vmin+1)) 
                if logE[k]<3:
                    Etitle='E='+format(10**logE[k],".1f")+'eV'
                if logE[k]>3:
                    Etitle='E='+format(10**(logE[k]-3),".1f")+'keV'
                axs[i][j].text(0.02,0.75,Etitle,fontsize=10,bbox={'facecolor':'white','alpha':1,'pad':2},
                               transform=axs[i][j].transAxes)
    
    plt.subplots_adjust(left=0.08,
                    bottom=0.04,
                    right=0.99,
                    top=0.95,
                    wspace=0.1,
                    hspace=0.05
                   )
    if name!='':
        plt.savefig(r''+name)
        plt.close(fig)
    
def plot_spectrum_point(dic,figpath='',value=[5,7],style='coPA',para='energy flux',times=[0,40],
                            lats=45,rs=4,lons=0,lgEs=[2,4],PAs=[0,180],M=1):
    rr=dic['r'][:]
    theta=dic['theta'][:]
    phi=dic['phi'][:]
    EE=dic['logE'][:]
    PA=dic['alpha'][:]
    time=dic['time'][:]

    pr=check_pos(rr,[rs])
    ptheta=check_pos(theta,[np.abs(lats)])
    pphi=check_pos(phi,[lons])
    pt=check_pos(time,[times])
    pe=check_pos(EE,[lgEs])
    pPA=check_pos(PA,[PAs])
    minv=min(value)
    maxv=max(value)
    
    rrt='r='+str(round(rr[pr[0]],1))+'$R_E$'
    if lats>0:
        latstr='N'
        lathm='North'
    if lats<0:
        latstr='S'
        lathm='South'
    if lats==0:
        latstr=''
    thetat='lat.='+str(round(abs(theta[ptheta[0]])))+'$\degree$'+latstr
    phit='lon.='+str(round(phi[pphi[0]]))+'$\degree$'
    match para:
        case 'energy flux':
            title='Ions Log Energy Flux [1/($cm^2\cdot$s$\cdot$sr)]'
        case 'number flux':
            title='Ions Log Flux [1/(eV$\cdot cm^2\cdot$s$\cdot$sr)]'
   
    text=title+'\n'+'at '+rrt+', '+thetat+', and '+phit  

    dicc=convertdata(dic,para=para,condition='differential',times=time[pt],lats=theta[ptheta[0]],rs=rr[pr[0]],
                       lons=phi[pphi[0]],lgEs=lgEs,PAs=PAs,M=M,sumPA=0)
    ff=dicc['data'][:]
    ff[np.where(ff<=0)]=1e-20
    logf=np.log10(ff) 
    
    figname=''
    match style:
        case 'coPA':
            if figpath!='':
                figname=figpath+'Spectrum_coPA.jpeg'
            plot_spectrum_coPA_data(time[pt],PA[pPA],EE[pe],logf,minv,maxv,title,text,name=figname) 
        case 'coE':
            if figpath!='':
                figname=figpath+'Spectrum_coE.jpeg'
            plot_spectrum_coE_data(time[pt],PA[pPA],EE[pe],logf,minv,maxv,title,text,name=figname) 
            

def plot_disperson_data(lat,logE,ff,vmin,vmax,title,textc,name=''):
    lat2, logE2 = np.meshgrid(lat, logE)
    
    my_dpi=200
    fig=plt.figure(figsize=(1400/my_dpi,800/my_dpi),dpi=my_dpi)
    axs=plt.subplot(111) 
    axs.set(title=textc)
    axs.set_xlim(min(lat),max(lat))
    axs.set_xlabel('lat. ($\degree$)')
    axs.set_ylim(min(logE),max(logE))
    axs.set_ylabel('logE (eV)')        
    axs.minorticks_on()
   
    #print(np.shape(time2),np.shape(logE2),np.shape(ff))
    cs=axs.contourf(lat2.T,logE2.T,np.reshape(ff,(np.size(logE),np.size(lat))).T,levels=np.linspace(vmin,vmax,256),
                       vmin=vmin,vmax=vmax,extend='both',cmap='jet')
    cbar=plt.colorbar(cs,ax=axs,location='right',fraction=0.1,pad=0.01,shrink=0.9,aspect=20,label=title,
                      ticks=np.linspace(vmin,vmax,vmax-vmin+1))        
   
    plt.subplots_adjust(left=0.1,
                    bottom=0.04,
                    right=0.8,
                    top=0.95,
                    wspace=0.06,
                    hspace=0.05
                   )
    if name!='':
        plt.savefig(r''+name)
        plt.close(fig)
    
  
    
def plot_latitudinal_disperson(dic,figpath='',value=[5,7],para='energy flux',times=10,
                            lats=[35,80],rs=5.2,lons=0,lgEs=[1,5],PAs=[0,20],M=1):
    rr=dic['r'][:]
    theta=dic['theta'][:]
    phi=dic['phi'][:]
    EE=dic['logE'][:]
    PA=dic['alpha'][:]
    time=dic['time'][:]

    pr=check_pos(rr,[rs])
    ptheta=check_pos(theta,[np.abs(lats)])
    pphi=check_pos(phi,[lons])
    pt=check_pos(time,[times])
    pe=check_pos(EE,[lgEs])
    pPA=check_pos(PA,[PAs])
    minv=min(value)
    maxv=max(value)
    
    rrt='r='+str(round(rr[pr[0]],1))+'$R_E$'
    lat0=np.min([lats])
    if lat0>0:
        latstr='N'
        lathm='North'
    if lat0<0:
        latstr='S'
        lathm='South'
    if lat0==0:
        latstr=''
    if len(pt)==1:
        timet='t='+str(round(dic['time'][pt[0]],1))+'min'
        meant=0
    else:

        timet='t:['+str(round(dic['time'][pt[0]],1))+', '+str(round(dic['time'][max(pt)-1],1))+']min'
        meant=1
        
    phit='lon.='+str(round(phi[pphi[0]]))+'$\degree$'
    if len(pPA)==1:
        PAt='PA='+str(np.min(PAs))+'$\degree$'
    else:
        PAt='PA:['+str(np.min(PAs))+'$\degree$,'+str(np.max(PAs))+'$\degree$]'
        

    match para:
        case 'energy flux':
            title='Ions Log Energy Flux [1/($cm^2\cdot$s$\cdot$sr)]'
        case 'number flux':
            title='Ions Log Flux [1/(eV$\cdot cm^2\cdot$s$\cdot$sr)]'
   
    text=timet+', '+rrt+', '+phit+', '+PAt  

    dicd=convertdata(dic,para=para,condition='differential',times=time[pt],lats=lats,rs=rr[pr[0]],meant=meant,
                       lons=phi[pphi[0]],lgEs=lgEs,PAs=PAs,M=M,sumPA=1)
    ff=dicd['data'][:]
    ff[np.where(ff<=0)]=1e-20
    logf=np.log10(ff) 
    
    figname=''
    if figpath!='':
        figname=figpath+'disperson.jpeg'
    plot_disperson_data(theta[ptheta],EE[pe],logf,minv,maxv,title,text,name=figname) 

