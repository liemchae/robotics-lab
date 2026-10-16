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
