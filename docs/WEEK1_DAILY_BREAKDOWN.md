# Week 1-2: Daily Breakdown (Days 1-14)

**Goal:** ROS2 Humble + Unitree sensor integration (10 hrs total)

---

## DAY 1: ROS2 Installation + Concepts (1 hr)

**Time:** 60 minutes  
**Status:** ⏳ Not Started

### Session Plan

**20 min: Read**
- Skim: ROS2_SETUP.md (sections 1-3)
- Understand: ROS2 = middleware for robot communication (pub/sub model)
- Key concepts: nodes (processes), topics (data channels), services (request/reply)

**20 min: Install (on lab machine Ubuntu 22.04)**
```bash
# Prerequisites
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential cmake git python3-pip

# Add ROS2 key
sudo curl -sSL https://repo.ros2.org/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

# Add repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://repo.ros2.org/ubuntu jammy main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Install ROS2 Humble
sudo apt update
sudo apt install -y ros-humble-desktop ros-humble-dev-tools
```

**10 min: Verify**
```bash
# Test installation
source /opt/ros/humble/setup.bash
ros2 --version
# Should print: ROS 2 humble (...)
```

**10 min: Setup bashrc**
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### Commit
```bash
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab
git add docs/WEEK1_DAILY_BREAKDOWN.md
git commit -m "docs(week1): Day 1 - ROS2 Humble installation guide

- Prerequisites: build-essential, cmake, git, python3-pip
- Added ROS2 GPG key + Ubuntu repository
- Verified installation with ros2 --version
- Setup bashrc for auto-sourcing

Day 1 milestone: ROS2 environment ready
"
git push
```

### Next Session Prep
- [ ] Verify `ros2 --version` works
- [ ] Confirm `/opt/ros/humble/` directory exists

---

## DAY 2: First ROS2 Nodes + talker/listener (1 hr)

**Time:** 60 minutes  
**Status:** ⏳ Not Started

### Session Plan

**15 min: Understand talker/listener architecture**
- Talker node publishes string messages to `/chatter` topic
- Listener node subscribes to `/chatter` topic
- Data flows: talker → ROS2 middleware → listener

**20 min: Run demo (on lab machine)**
```bash
# Terminal 1: Start talker
source ~/.bashrc
ros2 run demo_nodes_cpp talker

# Should print:
# [INFO] Publishing: "Hello World: X"
```

```bash
# Terminal 2: Start listener
source ~/.bashrc
ros2 run demo_nodes_cpp listener

# Should print:
# [INFO] I heard: "Hello World: X"
```

**15 min: Inspect ROS2 graph**
```bash
# Terminal 3: Visualize node/topic connections
ros2 graph

# Shows:
# /talker --> /chatter --> /listener
```

**10 min: List topics & introspect**
```bash
# See all active topics
ros2 topic list

# See message structure
ros2 topic info /chatter

# Echo live messages
ros2 topic echo /chatter
```

### Learnings to Document
- How pub/sub decouples components (talker ≠ listener)
- ROS2 graph visualizes data flow
- Real-time message inspection with `ros2 topic echo`

### Commit
```bash
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab
git add docs/WEEK1_DAILY_BREAKDOWN.md
git commit -m "docs(week1): Day 2 - First ROS2 demo (talker/listener)

- Ran demo_nodes_cpp talker publishing to /chatter
- Ran demo_nodes_cpp listener subscribing from /chatter
- Verified data flow with ros2 graph & ros2 topic echo
- Understood pub/sub decoupling

Day 2 milestone: ROS2 message passing verified
"
git push
```

### Next Session Prep
- [ ] Talker/listener working bidirectionally
- [ ] Comfortable with `ros2 topic` commands

---

## DAY 3: ROS2 Workspace Setup + First Package (1 hr)

**Time:** 60 minutes  
**Status:** ⏳ Not Started

### Session Plan

**10 min: Create workspace**
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

**15 min: Clone existing packages (for reference)**
```bash
cd ~/ros2_ws/src
git clone https://github.com/unitreerobotics/unitree_sdk2.git
git clone https://github.com/unitreerobotics/unitree_ros2.git
```

**15 min: Build workspace**
```bash
cd ~/ros2_ws
colcon build --symlink-install

# Should complete without errors
# Creates: build/, install/, log/
```

**15 min: Source & verify**
```bash
source install/setup.bash
ros2 pkg list | grep unitree

# Should show unitree packages
```

**5 min: Understand structure**
```
ros2_ws/
├─ src/         # Source code (packages)
├─ build/       # Compiled binaries
├─ install/     # Installed binaries (sourced)
└─ log/         # Build logs
```

### Learnings
- Workspace = container for ROS2 packages
- `colcon build` compiles all packages
- `source install/setup.bash` adds packages to PATH

### Commit
```bash
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab
git add docs/WEEK1_DAILY_BREAKDOWN.md
git commit -m "docs(week1): Day 3 - Workspace setup + first build

- Created ~/ros2_ws/{src,build,install,log}
- Cloned unitree_sdk2 + unitree_ros2 for reference
- Built workspace with colcon
- Verified package discovery with ros2 pkg list

Day 3 milestone: Workspace structure & build system working
"
git push
```

---

## DAY 4: Core ROS2 Concepts (Nodes, Topics, Services) (1 hr)

**Time:** 60 minutes  
**Status:** ⏳ Not Started

### Session Plan

**15 min: Node concept**
- Node = executable process in ROS2
- Each node has its own namespace
- Nodes communicate via topics/services

```bash
# List active nodes
ros2 node list

# Inspect node details
ros2 node info /talker
```

**15 min: Topic concept**
- Topic = named channel for messages
- Pub/sub model (many pubs/subs possible)
- Asynchronous communication

```bash
# List all topics
ros2 topic list -t

# Shows: /chatter [std_msgs/msg/String]
```

**15 min: Service concept**
- Service = synchronous request/reply
- Client sends request → server responds
- Blocking (waits for reply)

```bash
# List services
ros2 service list

# Call service
ros2 service call /example_service std_srvs/srv/Empty
```

**15 min: Create simple Python node (sensor simulator)**

Create file: `~/ros2_ws/src/unitree_control/unitree_control/simple_publisher.py`

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher = self.create_publisher(Float32, '/test_sensor', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.counter = 0.0
    
    def timer_callback(self):
        msg = Float32()
        msg.data = self.counter
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {self.counter}')
        self.counter += 1.0

def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

Build & run:
```bash
cd ~/ros2_ws
colcon build --packages-select unitree_control
source install/setup.bash
ros2 run unitree_control simple_publisher
```

### Commit
```bash
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab
git add ros2_ws/src/unitree_control/unitree_control/simple_publisher.py
git commit -m "feat(day4): Simple publisher node demonstrating ROS2 concepts

- Created SimplePublisher node publishing Float32 to /test_sensor
- Node publishes every 0.5s with incrementing counter
- Demonstrates node creation, timer callbacks, message publishing

Day 4 milestone: First custom ROS2 node running
"
git push
```

---

## DAY 5: Custom Message Types (1 hr)

**Time:** 60 minutes  
**Status:** ⏳ Not Started

### Session Plan

**15 min: Understand message types**
- Built-in: std_msgs (Float32, String, Int32)
- Custom: Define own .msg files
- Needed for Unitree: sensor data structure

**20 min: Create custom message**

Create: `~/ros2_ws/src/unitree_control/msg/UnitreeSensorData.msg`

```
# Unitree sensor data structure
float32 timestamp
float32[3] imu_accel     # X, Y, Z acceleration
float32[3] imu_gyro      # X, Y, Z angular velocity
float32[12] joint_pos    # 12 joint positions (radians)
float32[12] joint_vel    # 12 joint velocities (rad/s)
float32[4] foot_force    # FL, FR, RL, RR foot contact forces
uint8 battery_percent
```

**15 min: Build & verify message**
```bash
# Build workspace
cd ~/ros2_ws
colcon build --packages-select unitree_control

# Verify message generated
ros2 interface show unitree_control/msg/UnitreeSensorData
```

**10 min: Use custom message in publisher**

Update `simple_publisher.py` to publish UnitreeSensorData:

```python
from unitree_control.msg import UnitreeSensorData

# In timer_callback:
msg = UnitreeSensorData()
msg.timestamp = self.get_clock().now().nanoseconds / 1e9
msg.imu_accel = [0.0, 0.0, 9.81]
msg.imu_gyro = [0.0, 0.0, 0.0]
msg.joint_pos = [0.0] * 12
msg.joint_vel = [0.0] * 12
msg.foot_force = [0.0, 0.0, 0.0, 0.0]
msg.battery_percent = 85

self.publisher.publish(msg)
```

### Commit
```bash
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab
git add ros2_ws/src/unitree_control/msg/UnitreeSensorData.msg
git commit -m "feat(day5): Custom message type for Unitree sensor data

- Created UnitreeSensorData.msg with IMU, joint, foot force fields
- Message captures: accel[3], gyro[3], pos[12], vel[12], force[4], battery
- Verified message generation with ros2 interface show

Day 5 milestone: Custom message types for Unitree protocol
"
git push
```

---

## DAY 6: Subscriber Node + Data Flow (1 hr)

**Time:** 60 minutes  
**Status:** ⏳ Not Started

### Session Plan

**20 min: Create subscriber**

File: `~/ros2_ws/src/unitree_control/unitree_control/sensor_subscriber.py`

```python
import rclpy
from rclpy.node import Node
from unitree_control.msg import UnitreeSensorData

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.subscription = self.create_subscription(
            UnitreeSensorData,
            '/unitree/sensor_data',
            self.listener_callback,
            10
        )
    
    def listener_callback(self, msg):
        self.get_logger().info(
            f'Timestamp: {msg.timestamp:.3f}, '
            f'AccelZ: {msg.imu_accel[2]:.2f}, '
            f'Battery: {msg.battery_percent}%'
        )

def main(args=None):
    rclpy.init(args=args)
    node = SensorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

**20 min: Test pub/sub data flow**
```bash
# Terminal 1: Start subscriber
source ~/.bashrc
ros2 run unitree_control sensor_subscriber

# Terminal 2: Start publisher
source ~/.bashrc
ros2 run unitree_control simple_publisher

# See messages flow: publisher → /unitree/sensor_data → subscriber
```

**10 min: Monitor with RViz**
```bash
# Terminal 3: Visualize graph
ros2 graph
```

**10 min: Log data to file**
```bash
# Record data for analysis
ros2 bag record /unitree/sensor_data -o test_data.bag

# Later, replay
ros2 bag play test_data.bag
```

### Commit
```bash
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab
git add ros2_ws/src/unitree_control/unitree_control/sensor_subscriber.py
git commit -m "feat(day6): Subscriber node + end-to-end data flow

- Created SensorSubscriber listening to /unitree/sensor_data
- Verified pub/sub with publisher → subscriber flow
- Demonstrated data logging with ros2 bag record

Day 6 milestone: Full pub/sub pipeline working
"
git push
```

---

## DAY 7: Connect Real Unitree (Week 1 → Week 2 Bridge) (1 hr)

**Time:** 60 minutes  
**Status:** ⏳ Not Started

### Session Plan

**15 min: Review Unitree SDK integration**
- Check `/dev/ttyUSB0` for serial connection
- Verify Unitree firmware updated
- Test communication with low-level SDK

```bash
# Check device
ls -la /dev/ttyUSB*

# Test SDK (if available)
cd ~/ros2_ws/src/unitree_sdk2
./examples/basic_test  # Or per SDK docs
```

**20 min: Modify sensor_reader.py for hardware**

Update: `~/ros2_ws/src/unitree_control/unitree_control/sensor_reader.py`

```python
# Replace synthetic data with actual Unitree SDK calls:
# - Import Unitree SDK2 (Go2/H1)
# - Connect to robot via /dev/ttyUSB0
# - Read real IMU, joint state, foot force
# - Publish to /unitree/imu, /unitree/joint_state, /unitree/foot_force
```

**15 min: Test with real hardware (safe speeds)**
```bash
# Start sensor reader
ros2 run unitree_control sensor_reader

# Monitor in another terminal
ros2 topic echo /unitree/imu
```

**10 min: Measure latency**
```bash
# Check publish rate
ros2 topic bw /unitree/imu

# Should be ~50 Hz for IMU
```

### Blockers & Solutions
- **No /dev/ttyUSB0:** Check USB cable, driver (CH340 or similar)
- **Permission denied:** `sudo usermod -aG dialout $USER` (logout/login)
- **Sensor data garbage:** Verify baud rate (115200), check firmware

### Commit
```bash
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab
git add ros2_ws/src/unitree_control/unitree_control/sensor_reader.py docs/WEEK1_DAILY_BREAKDOWN.md
git commit -m "feat(day7): Hardware integration - real Unitree sensor reading

- Connected to Unitree Go2/H1 via /dev/ttyUSB0 (115200 baud)
- Replaced synthetic data with real IMU, joint state, foot force
- Verified publish rate ~50 Hz for IMU topic
- Measured latency: <50ms (acceptable for walking controller)

Day 7 milestone: Real robot sensor data flowing
Week 1 complete. Week 2: Simulation + Gazebo
"
git push
```

---

## DAY 8-14: Week 2 Preview

**Days 8-14** continue with:
- Day 8-9: Gazebo URDF model + simulation
- Day 10-11: Sim-to-real comparison (timing, accuracy)
- Day 12-13: Record data to rosbag, analyze
- Day 14: Week 1-2 review, commit summary

(Detailed breakdown in WEEK2_DAILY_BREAKDOWN.md)

---

## Progress Tracking

| Day | Task | Status | Commit |
|-----|------|--------|--------|
| 1 | ROS2 install | ⏳ | pending |
| 2 | talker/listener demo | ⏳ | pending |
| 3 | Workspace + build | ⏳ | pending |
| 4 | Nodes/topics/services | ⏳ | pending |
| 5 | Custom message types | ⏳ | pending |
| 6 | Publisher/subscriber | ⏳ | pending |
| 7 | Real Unitree connection | ⏳ | pending |

**Total hours Week 1-2:** 14 hours planned (adjust as needed)  
**Commits by Day 7:** 7 commits + daily updates

