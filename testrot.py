import rot2euler


eu = [0.2,0.4,0.6]
order = ['x','y','z']
print(order)
print(eu)
r = rot2euler.euler2rot(eu,order)
eu = rot2euler.rot2eular(r,order)
print(eu)
