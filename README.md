# Robotics Lab: Humanoid Control & Perception Pipeline

**Goal:** Build production-grade robotics control stack on Unitree humanoid + robotic arm, with hands-on deployment on NVIDIA RTX5090 hardware.

**Portfolio project for:** Robotics Technical Program Manager (Tesla Optimus), AI Robotics Product Manager (Google), Principal Product Manager - Atlas Logistics (Boston Dynamics).

**GitHub:** https://github.com/liemchae/robotics-lab

---

## Lab Equipment

- **GPU:** NVIDIA RTX5090 (simulation + training)
- **Robots:** Unitree Go2 / H1 humanoid, robotic arm (6-DOF)
- **Simulation:** Isaac Gym + Gazebo
- **Framework:** ROS2 Humble (LTS)

---

## Learning Structure (90 Days)

### Daily Learning Path (Mon-Fri, 1 hr/day)

**No hardware required.** Theory + local simulation on your machine.

- **[DAILY_THEORY_PATH.md](docs/DAILY_THEORY_PATH.md)** — Complete 60-day curriculum
  - Week 1-2: ROS2 fundamentals (pub/sub, nodes, messages)
  - Week 3-4: Gazebo simulation (URDF, physics)
  - Week 5-8: Control systems (kinematics, walking)
  - Week 9-10: Machine learning (imitation learning)
  - Week 11-12: Capstone (program plan)
  
**Daily commits:** Show consistency + progress on GitHub

### Biweekly Lab Checkpoints (Every 2 weeks, 2 hrs/session)

**Hardware validation only.** Offline learning feeds into checkpoint milestones.

- **[BIWEEKLY_CHECKPOINTS.md](docs/BIWEEKLY_CHECKPOINTS.md)** — 6 lab sessions
  - CP1 (Week 2): Sensor integration validation
  - CP2 (Week 4): Sim-to-real latency analysis
  - CP3 (Week 6): Walk controller on hardware
  - CP4 (Week 8): Vision + arm control
  - CP5 (Week 10): Learned policy deployment
  - CP6 (Week 12): Demo video + capstone
  
**Checkpoint commits:** Prove real robot progress

---

## Quick Start

### 1. Daily Learning (Start Monday)

```bash
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab

# Read today's task
cat docs/DAILY_THEORY_PATH.md | grep "^### MON"

# (Follow instructions: read, code, test, commit)
```

### 2. First Lab Visit (Week 2 Weekend)

```bash
# Pre-lab: Prepare checklist (30 min from home)
cat docs/BIWEEKLY_CHECKPOINTS.md | grep "Pre-Lab Checklist" -A 5

# In lab: Execute checkpoint (2 hrs)
cat docs/BIWEEKLY_CHECKPOINTS.md | grep "^## CHECKPOINT 1" -A 50
```

### 3. GitHub Tracking

```bash
# After each daily session
git add .
git commit -m "day<N>(theory|impl|analysis): [specific learning]"
git push

# After each lab checkpoint
git commit -m "checkpoint(N): [focus area]"
git push
```

---

## Directory Structure

```
robotics-lab/
├─ docs/
│  ├─ DAILY_THEORY_PATH.md           # Mon-Fri learning (no hardware)
│  ├─ BIWEEKLY_CHECKPOINTS.md        # Lab validation milestones
│  ├─ ROS2_SETUP.md                  # Environment setup
│  ├─ UNITREE_API.md                 # Hardware reference
│  ├─ PROGRESS.md                    # Track completions
│  └─ LEARNINGS.md                   # Document insights
│
├─ ros2_ws/                          # ROS2 workspace
│  └─ src/
│     └─ unitree_control/            # Main package
│        ├─ unitree_control/
│        │  ├─ sensor_reader.py
│        │  ├─ simple_publisher.py
│        │  └─ sensor_subscriber.py
│        ├─ msg/                     # Custom messages
│        ├─ config/                  # Parameters
│        └─ launch/                  # Launch files
│
├─ sim/                              # Simulation (Weeks 3-4+)
│  ├─ isaac_env/
│  └─ gazebo_models/
│
├─ learning/                         # ML code (Weeks 9-10)
│  ├─ imitation_learning/
│  └─ checkpoints/
│
├─ data/                             # Hardware data (lab-generated)
│  └─ .gitignore                     # Exclude large rosbags
│
├─ README.md                         # This file
├─ START_HERE.md                     # Quickstart guide
└─ GITHUB_SETUP.md                   # Pushing to GitHub
```

---

## Progress Tracking

**Daily Progress:** See [PROGRESS.md](docs/PROGRESS.md)

| Phase | Week | Daily Tasks | Lab Checkpoint |
|-------|------|-------------|-----------------|
| **ROS2** | 1-2 | Concepts, pub/sub, messages | CP1: Sensor validation |
| **Simulation** | 3-4 | URDF, Gazebo, physics | CP2: Sim-to-real latency |
| **Control** | 5-6 | Kinematics, PID, walking | CP3: Walk controller |
| **Perception** | 7-8 | Vision, arm control | CP4: Vision + arm |
| **Learning** | 9-10 | Imitation learning, training | CP5: Learned policy |
| **Capstone** | 11-12 | Program plan, portfolio | CP6: Demo + validation |

---

## Application Timeline

- **Week 4:** Apply to Tesla/Google/Boston Dynamics (Phase 1 complete)
  - Include: GitHub link + DAILY_THEORY_PATH progress
  
- **Week 8:** Re-apply with hardware deployments (Phase 2 complete)
  - Include: CP1-CP3 results + latency analysis
  
- **Week 12:** Final push with capstone + demo (Phase 3 complete)
  - Include: GitHub (60+ commits), demo video, program plan

---

## Documentation

- **[START_HERE.md](START_HERE.md)** — 90-day overview + checklist
- **[DAILY_THEORY_PATH.md](docs/DAILY_THEORY_PATH.md)** — Day-by-day curriculum
- **[BIWEEKLY_CHECKPOINTS.md](docs/BIWEEKLY_CHECKPOINTS.md)** — Lab sessions
- **[ROS2_SETUP.md](docs/ROS2_SETUP.md)** — Environment installation
- **[UNITREE_API.md](docs/UNITREE_API.md)** — Hardware reference
- **[PROGRESS.md](docs/PROGRESS.md)** — Track completion
- **[LEARNINGS.md](docs/LEARNINGS.md)** — Document insights

---

## Key Resources

- [ROS2 Humble Docs](https://docs.ros.org/en/humble/)
- [Unitree Robotics](https://github.com/unitreerobotics)
- [Isaac Gym](https://docs.nvidia.com/isaac/isaac_gym/)
- [Gazebo](https://gazebosim.org/)

---

## Commit History

Example of expected GitHub history:

```
day1(theory): ROS2 architecture + local setup
day2(theory): Pub/sub message passing verified
day3(theory): Workspace + build system
day4(impl): First custom ROS2 publisher
day5(impl): Custom message types + subscriber
checkpoint(1): ROS2 sensor integration validated

day6(theory): URDF + Gazebo basics
day7(theory): Gazebo simulation environment
...
checkpoint(2): Sim-to-real latency analysis

...

checkpoint(6): Final demo video + capstone
```

60+ commits over 12 weeks = **visible, consistent learning arc**.

---

## Author

**Chaehyuen Liem**  
Product Manager, Speech & Navigation @ Mercedes-Benz  
Pursuing: Robotics PM roles (Tesla Optimus, Google, Boston Dynamics)

---

## License

MIT (for educational reuse)

