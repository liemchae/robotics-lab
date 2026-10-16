# Daily Learning Path: 90 Days Offline

**Schedule:** Mon-Fri, 1 hour per day = 5 hours/week  
**Environment:** Local machine (no lab/hardware needed)  
**Output:** Daily commits on GitHub + theory documentation

Track progress in [PROGRESS.md](PROGRESS.md)

---

## WEEK 1-2: ROS2 Fundamentals (10 hrs)

### MON (Day 1): ROS2 Concepts + Architecture

**1 hour offline session**

**30 min: Read**
- ROS2_SETUP.md (skim all sections)
- Key: nodes, topics, services, middleware architecture
- Diagram in head: how pub/sub decouples components

**20 min: Local Install (Mac/Linux)**
```bash
# Option A: Docker (easiest, isolated)
docker run -it osrf/ros:humble-desktop bash
# Inside container:
ros2 --version

# Option B: Mac (if available)
brew install ros2

# Option C: WSL2 on Windows
# (Follow ROS2_SETUP.md section 8)
```

**10 min: Documentation**
- Write: "Why ROS2? (asynchronous pub/sub, decoupling, scalability)"
- Link: Save to `docs/LEARNINGS.md`

**Commit:**
```bash
git commit -m "day1(theory): ROS2 architecture + local setup

Read: ROS2 core concepts (nodes, topics, services)
Setup: Local ROS2 environment (Docker or native)
Understand: Pub/sub model enables scalable robot systems

Next: Talker/listener demo simulation
"
```

---

### TUE (Day 2): Talker/Listener Simulation

**1 hour offline session**

**30 min: Run & Inspect**
```bash
source /opt/ros/humble/setup.bash  # Or docker equivalent

# Terminal 1: talker (publishes to /chatter)
ros2 run demo_nodes_cpp talker

# Terminal 2: listener (subscribes from /chatter)
ros2 run demo_nodes_cpp listener

# Terminal 3: Introspection
ros2 topic list
ros2 topic info /chatter
ros2 topic echo /chatter
```

**20 min: Understand Data Flow**
- Draw/document: talker → middleware → listener
- Explain: Why pub/sub beats direct coupling
- Measure: Message latency with timestamps

```bash
# Capture output to analyze
ros2 topic echo /chatter --format yaml > chatter_log.txt
```

**10 min: Document Learnings**
- "Pub/sub decoupling in action: talker doesn't know about listener"
- "Message latency: <1ms (localhost)"

**Commit:**
```bash
git commit -m "day2(theory): Pub/sub message passing verified

Ran: demo_nodes_cpp talker + listener
Analyzed: Message flow, latency, decoupling
Learnings:
- Talker/listener completely decoupled
- Middleware routes messages asynchronously
- Localhost latency <1ms
- ros2 topic echo shows real-time data

Key insight: Scalable for multi-node systems
"
```

---

### WED (Day 3): Workspace Setup + Build System

**1 hour offline session**

**20 min: Create Local Workspace**
```bash
mkdir -p ~/ros2_ws_learning/src
cd ~/ros2_ws_learning

# Clone example packages (for study)
cd src
git clone https://github.com/ros2/examples.git
git clone https://github.com/unitreerobotics/unitree_ros2.git
```

**20 min: Understand Build System**
```bash
cd ~/ros2_ws_learning

# Build all packages
colcon build --symlink-install

# Understand structure
ls build/      # Compiled objects
ls install/    # Executables (sourced)
ls src/        # Source code

# Source & verify
source install/setup.bash
ros2 pkg list | head -20
```

**10 min: Document**
- "colcon = ROS2 build system"
- "symlink-install = dev mode (code changes auto-reflect)"
- "install/setup.bash = adds packages to PATH"

**10 min: Inspect Package Structure**
```bash
# Look at example package
cat ~/ros2_ws_learning/src/examples/rclpy_minimal_publisher/package.xml
cat ~/ros2_ws_learning/src/examples/rclpy_minimal_publisher/setup.py
```

**Commit:**
```bash
git commit -m "day3(theory): Workspace + build system fundamentals

Setup: ~/ros2_ws_learning with examples + unitree_ros2
Build: colcon build --symlink-install
Learned:
- package.xml = metadata (name, dependencies, description)
- setup.py = build configuration
- colcon = ROS2 build orchestrator
- symlink-install = enables rapid iteration

Directory structure:
src/ → source code
build/ → intermediate objects
install/ → final executables (sourced)
"
```

---

### THU (Day 4): Create First Custom Python Node

**1 hour offline session**

**30 min: Study Example Node**
```bash
# Read simple publisher example
cat ~/ros2_ws_learning/src/examples/rclpy_minimal_publisher/rclpy_minimal_publisher/publisher_member_function.py
```

**20 min: Write Custom Publisher**

Create: `~/ros2_ws_learning/src/my_first_node/my_first_node/simple_sensor.py`

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math
import time

class SimpleSensorNode(Node):
    """Simulates a sensor publishing distance measurements."""
    
    def __init__(self):
        super().__init__('simple_sensor')
        self.publisher_ = self.create_publisher(Float32, '/sensor/distance', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)  # 2 Hz
        self.counter = 0
    
    def timer_callback(self):
        # Simulate sinusoidal sensor reading
        msg = Float32()
        msg.data = 1.0 + 0.5 * math.sin(self.counter * 0.1)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published distance: {msg.data:.2f}m')
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = SimpleSensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

**10 min: Build & Test**
```bash
cd ~/ros2_ws_learning
colcon build --packages-select my_first_node
source install/setup.bash
ros2 run my_first_node simple_sensor
```

**Commit:**
```bash
git commit -m "day4(theory): First custom ROS2 node (publisher)

Created: SimpleSensorNode simulating distance sensor
Publishes: /sensor/distance with sinusoidal pattern (2 Hz)
Learned:
- Node creation with rclpy.Node
- Timer callbacks (periodic execution)
- Publishing Float32 messages
- get_logger() for debugging

Output: Data publishes every 0.5s
"
```

---

### FRI (Day 5): Custom Message Types + Subscriber

**1 hour offline session**

**20 min: Create Custom Message**

Create: `~/ros2_ws_learning/src/my_messages/msg/SensorReading.msg`

```
# Sensor reading with metadata
builtin_interfaces/Time timestamp
string sensor_name
float32 value
uint8 confidence    # 0-100
```

Update package.xml:
```xml
<depend>builtin_interfaces</depend>
<depend>rosidl_default_generators</depend>
```

Update CMakeLists.txt (if using C++) or setup.py (if Python):
```python
# In setup.py
from rosidl_cmake import get_rosidl_interfaces_from_dir

setup(
    name='my_messages',
    ...
)
```

**15 min: Build & Verify Message**
```bash
cd ~/ros2_ws_learning
colcon build --packages-select my_messages
source install/setup.bash
ros2 interface show my_messages/msg/SensorReading
```

**15 min: Create Subscriber Node**

Create: `~/ros2_ws_learning/src/my_first_node/my_first_node/subscriber.py`

```python
import rclpy
from rclpy.node import Node
from my_messages.msg import SensorReading

class SensorSubscriber(Node):
    """Subscribes to sensor readings and logs them."""
    
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.subscription = self.create_subscription(
            SensorReading,
            '/sensor/reading',
            self.listener_callback,
            10
        )
        self.get_logger().info('Subscriber initialized')
    
    def listener_callback(self, msg):
        self.get_logger().info(
            f'[{msg.sensor_name}] Value: {msg.value:.2f}, '
            f'Confidence: {msg.confidence}%'
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

**10 min: Test Pub/Sub**
```bash
# Terminal 1: Publisher
ros2 run my_first_node sensor_publisher /sensor/reading

# Terminal 2: Subscriber
ros2 run my_first_node subscriber
```

**Commit:**
```bash
git commit -m "day5(theory): Custom message types + subscriber node

Created: SensorReading.msg (timestamp, name, value, confidence)
Built: Message package with rosidl generator
Created: Subscriber node listening to /sensor/reading
Verified: Pub/sub with custom types working

Learnings:
- Define .msg files for domain-specific data
- rosidl generates C++/Python bindings automatically
- Subscribers receive typed messages

Complete Week 1: Full ROS2 pub/sub pipeline
"
```

---

## WEEK 3-4: Simulation + Gazebo (10 hrs)

### MON (Day 6): Gazebo Basics + URDF

**1 hour offline session**

**20 min: Install Gazebo**
```bash
sudo apt install ros-humble-gazebo-ros-pkgs  # On Linux
# Or Docker: already included in osrf/ros:humble-desktop
```

**20 min: Learn URDF Format**

Read: http://wiki.ros.org/urdf/XML/robot

Create: `~/ros2_ws_learning/src/unitree_models/urdf/simple_robot.urdf`

```xml
<?xml version="1.0" ?>
<robot name="simple_quadruped">
  <link name="base_link">
    <inertial>
      <mass value="10.0"/>
      <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <geometry>
        <box size="0.5 0.3 0.2"/>
      </geometry>
      <material name="red">
        <color rgba="1 0 0 1"/>
      </material>
    </visual>
  </link>

  <!-- Front-left leg -->
  <joint name="FL_hip" type="revolute">
    <parent link="base_link"/>
    <child link="FL_thigh"/>
    <axis xyz="0 1 0"/>
    <limit lower="-0.5" upper="0.5" effort="10" velocity="1"/>
  </joint>
  
  <link name="FL_thigh">
    <visual>
      <geometry>
        <cylinder length="0.3" radius="0.05"/>
      </geometry>
    </visual>
  </link>
</robot>
```

**15 min: Visualize with RViz**
```bash
ros2 launch joint_state_publisher_gui demo.launch.py model:=simple_robot.urdf
```

**5 min: Document**
- "URDF = Unified Robot Description Format (XML)"
- "Defines: links (rigid bodies), joints (connections), geometry, mass"

**Commit:**
```bash
git commit -m "day6(theory): URDF basics + quadruped model

Created: simple_robot.urdf (base + 4 legs skeleton)
Components:
- Links: rigid bodies (base_link, thighs, calves)
- Joints: revolute (hip, knee) with limits
- Visual: mesh/primitive geometry + materials
- Inertial: mass + inertia tensor

Visualized: RViz joint_state_publisher_gui
"
```

---

### TUE (Day 7): Gazebo Simulation Setup

**1 hour offline session**

**20 min: Study Gazebo Concepts**
- Physics engine (bullet/ODE)
- Sensors (camera, lidar, imu)
- Controllers (joint position, velocity)

**20 min: Create Gazebo World**

Create: `~/ros2_ws_learning/src/unitree_models/worlds/simple.world`

```xml
<?xml version="1.0" ?>
<sdf version="1.7">
  <world name="default">
    <physics type="bullet">
      <gravity>0 0 -9.81</gravity>
      <max_step_size>0.001</max_step_size>
    </physics>
    
    <plugin
      filename="libgazebo_ros_state.so"
      name="gazebo_ros_state"/>

    <!-- Ground plane -->
    <include>
      <uri>model://ground_plane</uri>
    </include>

    <!-- Lighting -->
    <include>
      <uri>model://sun</uri>
    </include>

    <!-- Include robot -->
    <include>
      <uri>model://simple_quadruped</uri>
      <pose>0 0 0.5 0 0 0</pose>
    </include>
  </world>
</sdf>
```

**15 min: Launch Gazebo**
```bash
gazebo ~/ros2_ws_learning/src/unitree_models/worlds/simple.world
```

**5 min: Observe**
- Robot spawns 0.5m above ground
- Falls due to gravity
- Physics simulation running

**Commit:**
```bash
git commit -m "day7(theory): Gazebo simulation environment

Created: simple.world (physics, lighting, ground, robot)
Physics: Bullet engine, 9.81 m/s² gravity, 1kHz timestep
Observed: Robot spawning + physics simulation
"
```

---

### WED-FRI (Days 8-10): Unitree Model + Sensors + Analysis

**Follow similar pattern for each day:**
- 20 min: Theory/reading
- 20 min: Coding (URDF, sensors, controllers)
- 15 min: Testing (Gazebo, RViz)
- 5 min: Documentation + commit

---

## WEEK 5-8: Control Systems (20 hrs)

### Daily Pattern (5 hrs/week = Mon-Fri)

**MON:** Theory (kinematics, control loops, PID)  
**TUE:** Implement simple controller (simulation)  
**WED:** Tune parameters (local optimization)  
**THU:** Analyze stability/performance  
**FRI:** Document + commit findings

---

## WEEK 9-10: Machine Learning (10 hrs)

**MON-TUE:** Study imitation learning (PyTorch)  
**WED-THU:** Implement training pipeline (local data)  
**FRI:** Policy evaluation + docs

---

## WEEK 11-12: Capstone (10 hrs)

**MON-WED:** Write program plan (5-7 pages)  
- Goal: Humanoid control stack for production
- Architecture, risks, timeline, costs

**THU:** Clean repo + final docs  
**FRI:** Prepare for applications

---

## Progress Tracking

Update [PROGRESS.md](PROGRESS.md) after each session:

```markdown
### Week 1-2 Daily Progress

- [x] Day 1 (MON): ROS2 concepts + local install
- [x] Day 2 (TUE): Talker/listener simulation
- [x] Day 3 (WED): Workspace + build system
- [ ] Day 4 (THU): Custom Python node
- [ ] Day 5 (FRI): Custom messages + subscriber
```

---

## Commit Format (Daily)

```
day<N>(theory|impl|analysis): <1-line summary>

<20-char concept or learning>
<specific code/experiment>
<1-2 insights>

Next: <what's coming>
```

Example:
```
day4(impl): First custom ROS2 publisher node

SimpleSensorNode simulates distance sensor (2 Hz)
Publishes Float32 to /sensor/distance
Demonstrates: timer callbacks, logging, pub model

Next: Subscriber + custom message types
```

---

## Resources

- [ROS2 Humble Docs](https://docs.ros.org/en/humble/)
- [URDF Wiki](http://wiki.ros.org/urdf/XML/robot)
- [Gazebo Docs](https://gazebosim.org/)
- [ROS2 Examples](https://github.com/ros2/examples)

