# Progress Log

## Week 1-2: ROS2 Fundamentals

### Day 1 (Friday, Oct 16)
- [x] Read ROS2 concepts (pub/sub, nodes, middleware)
- [x] Local ROS2 install (Docker or native)
- [x] Verified ros2 --version
- [x] Setup bashrc auto-sourcing

Time: 60 minutes ✓

Key Learnings:
- Pub/sub decoupling enables scalable robot systems
- ROS2 = middleware (not language/OS bound)
- Topics = asynchronous message channels
- Nodes = independent executable processes

Next: Day 2 - Talker/listener demo (message passing)

### Day 2 (Friday, Oct 16)
- [x] Ran demo_nodes_cpp talker + listener in Docker
- [x] Verified pub/sub decoupling (stop listener, talker keeps going)
- [x] Inspected live messages with ros2 topic echo

Time: 15 minutes ✓

Key Learnings:
- Talker publishes to /chatter (string messages)
- Listener subscribes from /chatter
- Messages flow asynchronously without coupling
- Stopped listener: talker kept publishing
- Middleware routes all messages to all subscribers
- ros2 topic echo shows live YAML data stream

Key Insight:
- Pub/sub enables scalable multi-component systems
- No direct connections needed
- Ready for distributed robot architecture

Next: Day 3 - Write custom publisher node (Python)

### Day 3 (Friday, Oct 16)
- [x] Created ~/ros2_ws_learning workspace
- [x] Ran colcon build --symlink-install
- [x] Verified build/, install/, log/ directories created
- [x] ros2 pkg list shows 20+ packages from workspace

Time: 25 minutes ✓

Key Learnings:
- colcon = ROS2 build orchestrator (CMake wrapper)
- package.xml = metadata (name, deps, description)
- CMakeLists.txt or setup.py = build instructions
- symlink-install = dev mode (code changes auto-reflect)
- install/setup.bash = sourcing adds packages to PATH
- Multiple packages in one workspace build independently

Key Insight:
- Modular package structure enables distributed development
- Source once per session: source install/setup.bash

Next: Day 4 - Custom Python node (publisher)

### Day 4 (Friday, Oct 16)
- [x] Created my_sensor_node package (ros2 pkg create)
- [x] Wrote SensorPublisher: Float32 on /sensor/distance
- [x] Registered entry point in setup.py
- [x] Built, ran, verified sinusoidal output

Time: 25 minutes ✓

Key Learnings:
- Node class inherits from rclpy.Node
- create_publisher(MsgType, topic, queue_size)
- create_timer(period, callback) for periodic execution
- setup.py console_scripts registers the executable
- colcon build --packages-select for single package rebuild

Key Insight:
- Entry point registration is the link between code and ros2 run
- Timer callbacks = the heartbeat of sensor nodes

Total Friday: 60 min across 4 sessions
Weekend break. Resume Monday.

Next: Day 5 - Custom message types + subscriber

### Day 5 (Friday, Oct 16)
- [x] Created my_messages package with SensorReading.msg
- [x] Custom message: timestamp, sensor_name, value, confidence
- [x] Created SensorSubscriber node
- [x] Modified SensorPublisher to send SensorReading
- [x] Verified full pipeline: publisher -> /sensor/reading -> subscriber

Time: 60 minutes (total Friday across all sessions) ✓

Key Learnings:
- rosidl_default_generators auto-generates Python bindings from .msg
- Custom message types enforce data contracts
- Typed messages = safer, self-documenting interfaces
- Publisher and subscriber share message type, not code

Key Insight:
- Custom messages are the API contract of robot systems
- Decoupling maintained even with complex data types

## Week 1-2 ROS2 Fundamentals: COMPLETE

Days 1-5 summary:
- Day 1: Concepts + architecture
- Day 2: Pub/sub demo
- Day 3: Build system + workspace
- Day 4: Custom Python node
- Day 5: Custom message types + full pipeline

Next week: Gazebo URDF + simulation, sim latency analysis

## Week 3-4: Simulation + URDF

### Day 6 (Friday, Oct 16)
- [x] Created simple_quadruped.urdf (base + 4 legs, 8 joints)
- [x] Joint limits: hip +/-0.5 rad, calf -1.0 to +0.5 rad
- [x] Inertial properties (mass, moment of inertia)
- [x] Verified URDF structure via command line

Time: 30 minutes ✓

Key Learnings:
- URDF = XML describing robot structure
- Links = rigid bodies (inertial, visual, collision)
- Joints = connections (type, limits, axis)
- Geometry = cylinder, box, mesh
- Inertia = physics simulation accuracy
- 1 base + 4 legs = 9 links, 8 joints (hip + calf per leg)

Key Insight:
- URDF is the single source of truth for robot geometry
- Same model used for visualization, simulation, and control

Total Friday (Days 1-6): ~100 min

Next: Day 7 - Gazebo physics simulation

### Day 7 (Saturday, Oct 18)
- [x] Created simple.world (Bullet engine, 1kHz, gravity 9.81)
- [x] Setup model directory (~/.gazebo/models/simple_quadruped/)
- [x] Spawned quadruped 0.5m above ground plane
- [x] Verified gravity, collision, physics convergence

Time: 30 minutes ✓

Key Learnings:
- Gazebo = physics simulator (not just visualization)
- Bullet engine accurate for legged robots
- 1kHz timestep = good balance (fast enough, stable)
- Model directory: ~/.gazebo/models/ (standard location)
- gz topic -l shows all simulation data streams
- Wrench topics = real force/torque on each link

Key Insight:
- Simulation proves physics before touching real hardware
- Same URDF used for visualization and physics

## Week 1-2: COMPLETE

Days 1-7 summary:
- Days 1-3: ROS2 concepts, pub/sub, build system
- Days 4-5: Custom nodes, message types, full pipeline
- Days 6-7: URDF model, Gazebo physics simulation

Next: Days 8-10 (simulate motion, analyze latency)
Biweekly CP1 (Oct 26): Real Unitree sensor validation

## Week 3-4: Motion + Latency Analysis

### Day 8 (Sunday, Oct 19)
- [x] Created GazeboController node (JointTrajectory publisher)
- [x] 8 joints: hip + calf per leg, sinusoidal motion
- [x] Trotting gait: diagonal pairs in opposite phase
- [x] Verified message publishing at 10 Hz

Time: 20 minutes ✓

Key Learnings:
- JointTrajectory = standard ROS2 message for joint commands
- Trotting gait: diagonal legs move together (FL+RR, FR+RL)
- Hip amplitude 0.2 rad, calf 0.3 rad at 1 Hz
- setup.py entry point required for each new executable

Key Insight:
- Gait patterns = math (sine waves with phase offsets)
- Same controller works in simulation and real hardware

Next: Day 9 - Record rosbag, analyze latency

### Day 9 (Sunday, Oct 19)
- [x] Created WalkController (refined gait: 0.5 Hz, smaller amplitudes)
- [x] Added velocity command publisher (0.2 m/s forward)
- [x] Recorded day9_walk_motion.bag (30 seconds, 7-8 gait cycles)

Time: 20 minutes ✓

Key Learnings:
- Slower gait (0.5 Hz vs 1 Hz) = more stable motion
- Smaller amplitudes reduce jitter (hip 0.15, calf 0.25)
- rosbag record captures timestamped message streams
- Bag files enable offline analysis and replay

Key Insight:
- Record first, analyze later = reproducible experiments
- Same bag replays identically every time

Next: Day 10 - Playback rosbag, analyze latency

### Day 10 (Sunday, Oct 19)
- [x] Played back rosbag with --loop
- [x] Measured publish rate: 20 Hz (50 ms interval)
- [x] Measured latency: <5 ms (localhost simulation)
- [x] Estimated real hardware latency: 15-20 ms (Unitree WiFi)

Time: 20 minutes ✓

Key Learnings:
- Sim latency <5 ms, jitter <1 ms (ideal conditions)
- Real hardware expected: 15-20 ms, jitter +/-5 ms
- Bottleneck: wireless communication, not computation
- 15 ms gap acceptable for 2s gait cycle (0.5 Hz)

Key Insight:
- Sim-to-real gap is measurable and manageable
- Real robot walking feasible with current latency budget

## Week 1-2 Theory + Simulation: COMPLETE

Days 1-10 summary (225 min total):
- Days 1-3: ROS2 concepts, pub/sub, build system
- Days 4-5: Custom nodes, message types, full pipeline
- Days 6-7: URDF model, Gazebo physics simulation
- Days 8-10: Motion control, rosbag recording, latency analysis

Next: Biweekly Checkpoint 1 (Oct 26) - Real Unitree sensor validation

## Week 3-4: Hardware Research + Checkpoint Prep

### Day 11 (Tuesday, Oct 20)
- [x] Analyzed URDF vs real Unitree Go2 quadruped hardware
- [x] Base mass 10.0 kg matches real (within 20%)
- [x] Thigh/calf proportions realistic (0.3m + 0.2m)
- [x] Identified gap: hip range +/-0.5 rad vs real +/-0.8-1.0 rad

Time: 60 minutes ✓

URDF Validation:
- Base mass: 10.0 kg (matches real, within 20%)
- Leg masses: 1.0 kg thigh + 0.5 kg calf (accurate)
- Thigh/calf proportions: 0.3m + 0.2m (realistic)
- Hip range: +/-0.5 rad (real Go2: +/-0.8-1.0 rad) - 40-100% gap

Assessment: URDF is GOOD baseline for simulation
- Only significant gap: joint range limits
- After CP1 real data: refine limits
- Simulation ready for control algorithm testing

Next: Day 12 - Sensor data format + checkpoint prep

### Day 12 (Tuesday, Oct 20)
- [x] Created SENSOR_EXPECTATIONS.md (real sensor ranges)
- [x] Documented rosbag structure (SQLite3 + metadata.yaml)
- [x] Created analyze_rosbag.py template for CP1 analysis
- [x] Understood sensor message formats (IMU, JointState, foot force)

Time: 60 minutes ✓

Key Learnings:
- 50 Hz for IMU, joint state, foot force; 1 Hz for battery
- Quaternion orientation format for IMU
- Rosbag = SQLite3 database with timestamped messages
- CP1 plan: 45s standing + 45s walking, ~8 MB rosbag

Next: Day 13 - Rosbag analysis tools

### Day 13 (Wednesday, Oct 21)
- [x] Created SENSOR_EXAMPLES.md (real IMU/joint/force data examples)
- [x] Created inspect_rosbag.py (metadata + file inspection tool)
- [x] Practiced rosbag inspection workflow on Day 9 data
- [x] Documented expected CP1 output (6750+ messages, 3 topics)

Time: 60 minutes ✓

Key Learnings:
- Real IMU walking: pitch +/-3 deg, accel x +/-2.0 m/s^2
- Joint state: 12 joints, stance vs swing phase patterns
- Foot force: 0 (swing) to ~45N (stance) per foot
- metadata.yaml = topic list, message counts, duration

CP1 prep: 3/6 days complete
Next: Day 14 - Gait stability theory

### Day 14 (Friday, Oct 23)
- [x] Created GAIT_STABILITY.md (support polygon, SSM/DSM, frequency analysis)
- [x] Created STABILITY_CHECKLIST.md (pre-lab, during, post-lab steps)
- [x] Analyzed why 0.5 Hz is optimal for Go2 trotting
- [x] Defined success criteria for CP1

Time: 60 minutes ✓

Key Learnings:
- Support polygon: CoM must stay inside for stability
- SSM minimum 0.05m, DSM threshold 1.0 rad/s
- 0.5 Hz optimal: fast enough to walk, slow enough to control
- Instability detection: angular velocity, force asymmetry, joint error

CP1 prep: 4/6 days complete
Next: Day 15 - Latency analysis prep
Then: Day 16 - Safety review + dry run
CP1: Oct 26 - Real Unitree recording
