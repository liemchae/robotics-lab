# Sensor Data Expectations - Unitree Go2

## Expected Sensor Ranges

### IMU (50 Hz)
- Standing: accel z ~9.81 m/s^2, gyro ~0
- Walking: accel x +/-2 m/s^2, z 8-11 m/s^2
- Orientation: quaternion (w,x,y,z)

### Joint State (50 Hz)
- 12 joints: 4 legs x 3 joints (hip, thigh, calf)
- Hip range: +/-0.8-1.0 rad (real), +/-0.5 rad (URDF)
- Calf range: -1.0 to +0.5 rad
- Position + velocity + effort

### Foot Force (50 Hz)
- Standing: ~25% body weight per foot
- Walking: 0-100% cycle (stance vs swing phase)
- 4 sensors (one per foot)

### Battery (1 Hz)
- Voltage: 24-29V range
- SOC: 0-100%

## Trotting Gait Expectations
- Frequency: 0.5 Hz (2 sec cycle)
- Pattern: diagonal pairs (FL+RR, FR+RL)
- 12-joint synchronization

## CP1 Measurement Plan
- 45s standing + 45s walking
- Expected rosbag size: ~8 MB
- Topics: /imu/data, /joint_states, /foot_force, /battery
