# Robotics Lab: Humanoid Control & Perception Pipeline

**Goal:** Build production-grade robotics control stack on Unitree humanoid + robotic arm, with hands-on deployment on NVIDIA RTX5090 hardware.

**Portfolio project for:** Robotics Technical Program Manager (Tesla Optimus), AI Robotics Product Manager (Google), Principal Product Manager - Atlas Logistics (Boston Dynamics).

---

## Lab Equipment

- **GPU:** NVIDIA RTX5090 (simulation + training)
- **Robots:** Unitree Go2 / H1 humanoid, robotic arm (6-DOF)
- **Simulation:** Isaac Gym + Gazebo
- **Framework:** ROS2 Humble (LTS)

---

## Project Phases (90 Days)

### Phase 1: ROS2 Fundamentals + Simulation (Weeks 1-4)
- [x] ROS2 environment setup
- [ ] Unitree sensor integration (IMU, joint encoders)
- [ ] Gazebo simulation environment
- [ ] Sim-to-real latency analysis

### Phase 2: Robot Control + Perception (Weeks 5-8)
- [ ] Locomotion controller (walk, balance, gait patterns)
- [ ] Vision pipeline (RGB-D sensor, obstacle detection)
- [ ] Sim-to-real transfer (policy execution on hardware)
- [ ] Performance benchmarking

### Phase 3: Learning Algorithms + Capstone (Weeks 9-12)
- [ ] Imitation learning framework (PyTorch + Isaac Gym)
- [ ] Policy training & evaluation
- [ ] Program plan: "Humanoid Control Stack for Production"
- [ ] Portfolio: code + demo video + documentation

---

## Directory Structure

```
robotics-lab/
├─ ros2_ws/              # ROS2 workspace
│  ├─ src/
│  │  ├─ unitree_control/      # Unitree walking, balance
│  │  ├─ perception_pipeline/  # Vision + sensor fusion
│  │  └─ shared_msgs/          # Custom ROS messages
│  ├─ build/
│  ├─ install/
│  └─ README.md
│
├─ sim/                   # Simulation environments
│  ├─ isaac_env/         # Isaac Gym training
│  ├─ gazebo_models/     # URDF + SDF models
│  └─ README.md
│
├─ learning/             # ML algorithms
│  ├─ imitation_learning/
│  ├─ checkpoints/       # Trained policies
│  └─ README.md
│
├─ docs/                 # Documentation
│  ├─ ROS2_SETUP.md
│  ├─ UNITREE_API.md
│  ├─ CAPSTONE_PLAN.md
│  ├─ LEARNINGS.md
│  └─ WEEKLY_LOG.md
│
└─ README.md (this file)
```

---

## Quick Start

### Prerequisites
- Ubuntu 22.04 (lab machine with RTX5090)
- Docker (optional, recommended)
- Git

### Setup (Week 1)

```bash
# Clone & navigate
git clone <this-repo>
cd robotics-lab

# Follow ROS2 setup guide
cat docs/ROS2_SETUP.md

# Build workspace
cd ros2_ws
colcon build --symlink-install
source install/setup.bash

# Verify installation
ros2 topic list
```

### First Milestone: Read Unitree Sensors
```bash
cd ros2_ws/src/unitree_control
# Implementation in Week 1-2, see docs/UNITREE_API.md
```

---

## Key Resources

- [ROS2 Humble Docs](https://docs.ros.org/en/humble/)
- [Unitree Go2 SDK](https://github.com/unitreerobotics/unitree_sdk2)
- [Isaac Gym Docs](https://docs.nvidia.com/isaac/isaac_gym/)
- [MuJoCo Docs](https://mujoco.readthedocs.io/)

---

## Documentation

- **[ROS2_SETUP.md](docs/ROS2_SETUP.md)** — Installation & environment
- **[UNITREE_API.md](docs/UNITREE_API.md)** — Sensor + actuator interfaces
- **[SIMULATION.md](docs/SIMULATION.md)** — Gazebo + Isaac Gym setup
- **[LEARNINGS.md](docs/LEARNINGS.md)** — Weekly insights & blockers
- **[CAPSTONE_PLAN.md](docs/CAPSTONE_PLAN.md)** — Final program plan

---

## Weekly Progress

See **[WEEKLY_LOG.md](docs/WEEKLY_LOG.md)** for detailed week-by-week updates, experiments, and results.

---

## Application Portfolio

This repo demonstrates:
1. **Hands-on robotics:** Real robot control, sim-to-real transfer, sensor integration
2. **Software engineering:** Clean ROS2 architecture, reproducible builds, documentation
3. **Systems thinking:** Understanding hardware constraints, manufacturing readiness, cross-functional dependencies
4. **Technical depth:** Perception, control algorithms, training pipelines

**Use in job applications:**
- Link to GitHub repo
- Highlight capstone program plan
- Share demo video (real Unitree executing learned behavior)

---

## Author

Chaehyuen Liem  
Product Manager, Speech & Navigation @ Mercedes-Benz  
Pursuing: Robotics PM roles (Tesla Optimus, Google, Boston Dynamics)

---

## License

MIT (for reusability)

