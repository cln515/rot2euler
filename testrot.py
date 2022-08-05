import rotation


eu = [0.2,0.4,0.6]
order = ['x','y','z']
print(order)
print(eu)
r = rotation.euler2rot(eu,order)
eu = rotation.rot2eular(r,order)
print(eu)
