# rot2euler

Rotation matrix to euler angle converter

## Usage example

```
euler = [0.2,0.4,0.6]
order = ['x','y','z']
r = rot2euler.euler2rot(eu,order)
euler = rot2euler.rot2eular(r,order)
```

## Todo
Handling gimbal lock, rotation with same axis in first and third (e.g. ["x","y","x"])
