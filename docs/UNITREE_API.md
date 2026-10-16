# Unitree Humanoid API Reference

**Target:** Unitree Go2 / H1 (adjust based on lab model)

---

## 1. Hardware Overview

### Unitree H1 / Go2 Specs
| Parameter | Value |
|-----------|-------|
| DOF (degrees of freedom) | 12 (3 per leg) or 19 (H1 with arms) |
| Weight | ~25 kg (Go2) / ~47 kg (H1) |
| Max speed | ~2.5 m/s |
| Battery | ~2-4 hours runtime |
| IMU | 9-axis (accel, gyro, compass) |
| Foot pressure sensors | 4 (one per leg) |

### Joint Names (Quadruped)
```
Front-Left:  FL_hip, FL_thigh, FL_calf
Front-Right: FR_hip, FR_thigh, FR_calf
Rear-Left:   RL_hip, RL_thigh, RL_calf
Rear-Right:  RR_hip, RR_thigh, RR_calf
```

---

## 2. SDK Integration

### Unitree SDK2 (C++)
```bash
# Clone
git clone https://github.com/unitreerobotics/unitree_sdk2.git

# Build
cd unitree_sdk2
mkdir build && cd build
cmake ..
make
```

### Python Wrapper (via ROS2)
```bash
git clone https://github.com/unitreerobotics/unitree_ros2.git
# Integrate into ros2_ws/src/
```

---

## 3. ROS2 Topics

### Publishers (Unitree → ROS2)

#### IMU Data
**Topic:** `/unitree/imu`  
**Type:** `sensor_msgs/Imu`
```python
{
  "header": {"stamp": ..., "frame_id": "base_link"},
  "linear_acceleration": {"x": 0.0, "y": 0.0, "z": 9.81},
  "angular_velocity": {"x": 0.0, "y": 0.0, "z": 0.0},
  "orientation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0}
}
```

#### Joint State
**Topic:** `/unitree/joint_state`  
**Type:** `sensor_msgs/JointState`
```python
{
  "name": ["FL_hip", "FL_thigh", "FL_calf", ...],
  "position": [pos_0, pos_1, ..., pos_11],  # radians
  "velocity": [vel_0, vel_1, ..., vel_11],  # rad/s
  "effort": [eff_0, eff_1, ..., eff_11]     # N*m
}
```

#### Foot Force (Contact Detection)
**Topic:** `/unitree/foot_force`  
**Type:** `std_msgs/Float32MultiArray`
```python
{
  "data": [FL_force, FR_force, RL_force, RR_force]  # Newtons
}
```

#### Battery
**Topic:** `/unitree/battery`  
**Type:** `std_msgs/Float32`
```python
{"data": 85.0}  # Battery percentage
```

### Subscribers (ROS2 → Unitree)

#### Velocity Command
**Topic:** `/unitree/cmd_vel`  
**Type:** `geometry_msgs/Twist`
```python
{
  "linear": {"x": 0.5, "y": 0.0, "z": 0.0},   # m/s
  "angular": {"x": 0.0, "y": 0.0, "z": 0.1}   # rad/s
}
```

#### Joint Command (Direct Control)
**Topic:** `/unitree/joint_commands`  
**Type:** `trajectory_msgs/JointTrajectory`
```python
{
  "joint_names": ["FL_hip", "FL_thigh", ...],
  "points": [{
    "positions": [pos_0, ..., pos_11],
    "velocities": [vel_0, ..., vel_11],
    "effort": [eff_0, ..., eff_11],
    "time_from_start": {"secs": 0, "nsecs": 20000000}  # 50 Hz
  }]
}
```

---

## 4. Control Modes

### High-Level: Velocity Command
Simple approach for walking/balance.
```python
import rclpy
from geometry_msgs.msg import Twist

node = rclpy.create_node('walk_test')
pub = node.create_publisher(Twist, '/unitree/cmd_vel', 10)

cmd = Twist()
cmd.linear.x = 0.5   # Forward 0.5 m/s
cmd.angular.z = 0.1  # Turn 0.1 rad/s

pub.publish(cmd)
```

### Low-Level: Joint Commands
Direct motor control for complex behaviors.
```python
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

# Create trajectory
traj = JointTrajectory()
traj.joint_names = ['FL_hip', 'FL_thigh', 'FL_calf', ...]

point = JointTrajectoryPoint()
point.positions = [0.0] * 12  # All neutral
point.velocities = [0.0] * 12
point.effort = [0.0] * 12
point.time_from_start.nanosec = 20_000_000  # 50 Hz

traj.points = [point]

pub.publish(traj)
```

---

## 5. Gait Parameters

### Walk Gait
| Parameter | Range | Default |
|-----------|-------|---------|
| `stride_length` | 0.2 - 0.8 m | 0.4 m |
| `stride_frequency` | 0.5 - 3.0 Hz | 2.0 Hz |
| `base_height` | 0.3 - 0.6 m | 0.45 m |
| `foot_lift_height` | 0.05 - 0.15 m | 0.08 m |

### Trotting (Faster)
- Diagonal legs move together
- More dynamic, less stable on uneven terrain

### Crawling (Slower)
- 3-leg stance, 1 leg swings
- More stable, better for obstacles

---

## 6. Sensor Calibration

### IMU Calibration
```bash
# Place robot on flat surface
ros2 service call /unitree/calibrate_imu std_srvs/srv/Empty

# Wait 5-10 seconds (stays still)
# Recalibration complete
```

### Joint Offset Calibration
```bash
# Return to neutral stance
ros2 service call /unitree/set_neutral std_srvs/srv/Empty
```

---

## 7. Safety Features

### Emergency Stop
```python
from std_msgs.msg import Bool

estop_pub = node.create_publisher(Bool, '/unitree/emergency_stop', 1)
estop_pub.publish(Bool(data=True))  # Trigger e-stop

# Motors disable, robot goes limp
```

### Motion Limits
- Always check joint limits before sending commands
- Motor current limits auto-trigger safety shutoff (~20 A)
- Foot pressure > threshold triggers alarm

---

## 8. Week 1-2 Integration Checklist

- [ ] Read Unitree specifications (Go2 or H1)
- [ ] Install Unitree SDK2 + ROS2 wrapper
- [ ] Start `unitree_sensor_reader` node
- [ ] Verify IMU data publishing (use `ros2 topic echo`)
- [ ] Verify joint state publishing
- [ ] Log 60 seconds of sensor data to rosbag
- [ ] Analyze latency & data quality
- [ ] Document any calibration steps needed

---

## Resources

- [Unitree Robotics GitHub](https://github.com/unitreerobotics)
- [Unitree Go2 Quick Start](https://support.unitreerobotics.com/)
- [ROS2 std_msgs](https://wiki.ros.org/std_msgs)

