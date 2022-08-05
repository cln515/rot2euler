import numpy as np
import math


def idx(ax_str):
    if ax_str == 'x' or ax_str == '-x':
        return 0
    if ax_str == 'y' or ax_str == '-y':
        return 1
    if ax_str == 'z' or ax_str == '-z':
        return 2
    return -1

def isCCw(ax_str):
    if ax_str == '-x' or ax_str == '-y'or ax_str == '-z':
        return 1
    else:
        return 0

def remainAxis(axidx1,axidx2):
    ax = [axidx1,axidx2]
    if not 0 in ax:
        return 0
    if not 1 in ax:
        return 1
    if not 2 in ax:
        return 2
    return -1

def rot2eular(rot,axis):

    #center
    euler = [0,0,0]

    coli=idx(axis[0]) # first matrix axis
    rowi=idx(axis[2]) # third matrix axis
    ceni = idx(axis[1])

    elm = rot[rowi][coli]
    #print(elm)
    if coli == rowi:
        secang = math.acos(elm)    #todo +-
    else:
        secang = math.asin(elm)    
        if (coli == 1 and rowi == 0) or (coli == 2 and rowi == 1) or (coli == 0 and rowi == 2):
            secang = -secang
    
    if isCCw(axis[1])==1:
        secang = -secang

    euler[1]=secang
    
    #first matrix
    #candidate: row != ceni
    
    # (rowi, not coli)-> combi
    firang = math.atan2(rot[rowi][ceni],rot[rowi][remainAxis(ceni,coli)])
    #minus row: 
    if isCCw(axis[0]) == 1:
        mrowf = coli - 1
        if mrowf == -1:
            mrowf = 2
    else:
        mrowf = coli + 1
        if mrowf == 3:
            mrowf = 0
    if not mrowf == ceni:
        firang = -firang
    
    euler[0]=firang
    


    thirdang = math.atan2(rot[ceni][coli],rot[remainAxis(ceni,rowi)][coli])
    if isCCw(axis[2]) == 1:
        mcolf = rowi - 2
        if mcolf < 0:
            mcolf = mcolf + 3
    else:
        mcolf = rowi + 2
        if mcolf > 2:
            mcolf = mcolf - 3
    if not mcolf == ceni:
        thirdang = -thirdang

    euler[2]=thirdang


    return euler

def euler2rot(euler,axis):
    ret = np.array(
                [[1,0,0],
                [0,1,0],
                [0,0,1]]
            )
    for i in range(3):
        angle = euler[i]
        if axis[i]=='x':
            mrot = np.array(
                [[1,0,0],
                [0,math.cos(angle),-math.sin(angle)],
                [0,math.sin(angle),math.cos(angle)]]
            )
        if axis[i]=='-x':
            mrot = np.array(
                [[1,0,0],
                [0,math.cos(angle),math.sin(angle)],
                [0,-math.sin(angle),math.cos(angle)]]
            )    
        if axis[i]=='y':
            mrot = np.array(
                [[math.cos(angle),0,math.sin(angle)],
                [0,1,0],
                [-math.sin(angle),0,math.cos(angle)]]
            )    
        if axis[i]=='-y':
            mrot = np.array(
                [[math.cos(angle),0,-math.sin(angle)],
                [0,1,0],
                [math.sin(angle),0,math.cos(angle)]]
            )    
        if axis[i]=='z':
            mrot = np.array(
                [[math.cos(angle),-math.sin(angle),0],
                [math.sin(angle),math.cos(angle),0],
                [0,0,1]]
            )    
        if axis[i]=='-z':
            mrot = np.array(
                [[math.cos(angle),math.sin(angle),0],
                [-math.sin(angle),math.cos(angle),0],
                [0,0,1]]
            )    
        ret = np.dot(mrot, ret)

    return ret

if __name__ == '__main__':

    r1 = 0.5
    r2 = 0
    r3 = 0.9

    order = ['x','y','z']

    r = euler2rot([r1,r2,r3],order)
    #print(r)
    eu = rot2eular(r,order)

    #print(eu)


    #tests
    eu = [r1,r2,r3]
    order = ['x','y','z']
    print(order)
    print(eu)
    r = euler2rot([r1,r2,r3],order)
    eu = rot2eular(r,order)
    print(eu)

    eu = [r1,r2,r3]
    order = ['z','y','x']
    print(order)
    print(eu)
    r = euler2rot([r1,r2,r3],order)
    eu = rot2eular(r,order)
    print(eu)

    eu = [r1,r2,r3]
    order = ['y','z','x']
    print(order)
    print(eu)
    r = euler2rot([r1,r2,r3],order)
    eu = rot2eular(r,order)
    print(eu)

    eu = [r1,r2,r3]
    order = ['z','x','y']
    print(order)
    print(eu)
    r = euler2rot([r1,r2,r3],order)
    eu = rot2eular(r,order)
    print(eu)

    eu = [r1,r2,r3]
    order = ['x','z','y']
    print(order)
    print(eu)
    r = euler2rot([r1,r2,r3],order)
    eu = rot2eular(r,order)
    print(eu)

    eu = [r1,r2,r3]
    order = ['y','x','z']
    print(order)
    print(eu)
    r = euler2rot([r1,r2,r3],order)
    eu = rot2eular(r,order)
    print(eu)


    #tests
    eu = [-r1,r2,r3]
    order = ['x','y','z']
    print(order)
    print(eu)
    r = euler2rot(eu,order)
    eu = rot2eular(r,order)
    print(eu)

    eu = [r1,-r2,r3]
    order = ['z','y','x']
    print(order)
    print(eu)
    r = euler2rot(eu,order)
    eu = rot2eular(r,order)
    print(eu)

    eu = [r1,-r2,-r3]
    order = ['y','z','x']
    print(order)
    print(eu)
    r = euler2rot(eu,order)
    eu = rot2eular(r,order)
    print(eu)

    eu = [-r1,r2,-r3]
    order = ['z','x','y']
    print(order)
    print(eu)
    r = euler2rot(eu,order)
    eu = rot2eular(r,order)
    print(eu)

    eu = [-r1,-r2,-r3]
    order = ['x','z','y']
    print(order)
    print(eu)
    r = euler2rot(eu,order)
    eu = rot2eular(r,order)
    print(eu)

    eu = [r1,r2,-r3]
    order = ['y','x','z']
    print(order)
    print(eu)
    r = euler2rot(eu,order)
    eu = rot2eular(r,order)
    print(eu)
