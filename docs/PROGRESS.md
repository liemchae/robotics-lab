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
