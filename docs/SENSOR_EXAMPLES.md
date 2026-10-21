# Real Sensor Data Examples - Unitree Go2

## IMU Data (sensor_msgs/msg/Imu)

### Standing (stationary)
```yaml
orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0}
angular_velocity: {x: 0.0, y: 0.0, z: 0.0}
linear_acceleration: {x: 0.0, y: 0.0, z: 9.81}
```

### Walking (trotting gait)
```yaml
orientation: {w: 0.998, x: 0.02, y: 0.05, z: 0.01}
angular_velocity: {x: 0.1, y: 0.3, z: 0.05}
linear_acceleration: {x: 1.5, y: 0.3, z: 10.2}
```

Expected ranges during walking:
- Pitch oscillation: +/-3 degrees (body sway)
- Accel x: +/-2.0 m/s^2 (forward/backward)
- Accel z: 8.0-11.5 m/s^2 (vertical bounce)

## Joint State (sensor_msgs/msg/JointState)

### Trotting Gait Pattern
```yaml
name: [FL_hip, FL_thigh, FL_calf, FR_hip, FR_thigh, FR_calf,
       RL_hip, RL_thigh, RL_calf, RR_hip, RR_thigh, RR_calf]

# Stance phase (foot on ground)
position: [0.0, 0.6, -1.2, ...]   # hip neutral, thigh forward, calf bent

# Swing phase (foot in air)
position: [0.0, 0.9, -0.8, ...]   # thigh more forward, calf less bent
```

Phase pattern (trotting):
- FL + RR: same phase (diagonal pair 1)
- FR + RL: same phase (diagonal pair 2)
- Pairs offset by 180 degrees (half cycle)

## Foot Force (geometry_msgs/msg/WrenchStamped)

### Standing (equal weight distribution)
```yaml
force: {x: 0.0, y: 0.0, z: 30.0}  # ~25% of 12kg * 9.81
```

### Walking (contact cycle)
```yaml
# Stance phase: foot bearing weight
force: {x: 2.0, y: 0.5, z: 45.0}  # increased vertical + forward push

# Swing phase: foot in air
force: {x: 0.0, y: 0.0, z: 0.0}   # no contact
```

## Rosbag Message Rates
| Topic | Rate | Messages/90s |
|-------|------|-------------|
| /imu/data | 50 Hz | 4500 |
| /joint_states | 50 Hz | 4500 |
| /foot_force | 50 Hz | 4500 |
| /battery | 1 Hz | 90 |
| **Total** | | **~13590** |

Expected rosbag size: ~8-12 MB for 90 seconds
