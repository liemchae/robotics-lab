# START HERE: Your 90-Day Robotics Portfolio

You have a fully scaffolded robotics learning project ready to deploy. **Spend 1 hour daily.**

---

## What You Have

```
robotics-lab/
├─ README.md                  # Project overview
├─ START_HERE.md             # This file
├─ GITHUB_SETUP.md           # Instructions to push to GitHub
├─ quick_start.sh            # Verify ROS2 installation
│
├─ ros2_ws/                  # ROS2 Humble workspace
│  └─ src/unitree_control/   # First package: sensor reader
│
├─ docs/
│  ├─ ROS2_SETUP.md         # Step-by-step ROS2 installation
│  ├─ UNITREE_API.md        # Unitree hardware + ROS2 interface
│  └─ WEEKLY_LOG.md         # Track progress week-by-week
```

**Scaffold:** Complete. Ready to build on.

---

## Today: Next 3 Hours

### Hour 1: Environment Setup (Now)

```bash
# Navigate to project
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab

# Read setup guide (20 min)
cat docs/ROS2_SETUP.md

# On lab machine (Ubuntu 22.04):
# Follow sections 1-5 (build, verify)
# Should take ~1 hour total

# Verify
ros2 --version
```

### Hour 2: First Code Review (In lab)

```bash
# On lab machine
cd robotics-lab/ros2_ws

# Build workspace
colcon build --symlink-install

# Test
ros2 run unitree_control sensor_reader

# Should print:
# [INFO] UnitreeSensorReader initialized
# [INFO] Publishing at 50 Hz
```

### Hour 3: GitHub Setup

```bash
# Initialize git (local machine)
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab
git init
git add .

git commit -m "Initial ROS2 project structure: sensor reader, Unitree integration skeleton

- ROS2 Humble workspace setup
- Unitree sensor reader node (IMU, joint state, foot force)
- Configuration files for Unitree H1/Go2
- Weekly progress tracking
- Documentation: ROS2 setup, API reference, weekly log

Week 1-2 milestone: Establish sensor acquisition pipeline
"

# Create GitHub repo (github.com/new)
# Then push:
git remote add origin https://github.com/YOUR_USERNAME/robotics-lab.git
git branch -M main
git push -u origin main

# Share link with me for tracking
```

---

## Week 1-2 Milestones

### Checklist

- [ ] ROS2 Humble installed & verified (talker/listener test works)
- [ ] `unitree_control` package builds without errors
- [ ] Sensor reader node runs, publishes IMU + joint state at 50 Hz
- [ ] Synthetic data validated (use `ros2 topic echo`)
- [ ] Connect to real Unitree hardware (if available)
- [ ] Log 60 seconds of sensor data to rosbag
- [ ] GitHub repo created & first commit pushed
- [ ] WEEKLY_LOG.md updated with learnings

### Commit Checklist
After each ~1-hour session:
```bash
git add .
git commit -m "Week 1 DayX: [specific improvement]

- What you did
- What you learned
- What's next
"
git push
```

---

## Portfolio Strategy

### By Week 4 (End of Phase 1)
- Simulation environment working (Gazebo URDF loaded)
- Real Unitree sensor data being published
- GitHub shows clean, documented code
- WEEKLY_LOG.md filled with learnings

### By Week 8 (End of Phase 2)
- Walk controller deployed on real hardware
- Vision pipeline processing camera frames
- Sim-to-real transfer analysis complete
- Commit history shows deliberate progress

### By Week 12 (Capstone)
- 5-7 page program plan: "Humanoid Control Stack for Production"
- GitHub repo with 12 weeks of commits
- Demo video: Unitree executing learned behavior
- Portfolio ready for Tesla/Google/Boston Dynamics applications

---

## Apply to Roles

**When to apply:**
- Week 4: Apply with Phase 1 complete (working ROS2 stack)
- Week 8: Re-apply with Phase 2 (hardware deployments)
- Week 12: Final push with capstone + demo video

**In cover letter:**

> "I'm actively building a robotics portfolio to deepen hands-on expertise. Over the past [X] weeks, I've:
> 
> - Built a ROS2 control stack for Unitree humanoid on NVIDIA RTX5090
> - Integrated real-time sensors (IMU, joint state, foot pressure)
> - Deployed locomotion controller on hardware
> - Implemented imitation learning with Isaac Gym
> 
> GitHub: [link]
> 
> This demonstrates:
> - Systems thinking (cross-functional dependencies)
> - Manufacturing readiness (sim-to-real transfer, latency analysis)
> - Software discipline (reproducible builds, documentation)
> - Hardware-software coupling understanding"

---

## Common Blockers & Solutions

### Issue: ROS2 build fails
**Solution:** `rosdep install --from-paths ros2_ws/src --ignore-src -r -y`

### Issue: Unitree not connecting
**Solution:** Check `/dev/ttyUSB0` exists. Update `config/unitree_config.yaml` port.

### Issue: Sensor latency too high
**Solution:** Document in WEEKLY_LOG.md. Investigate real vs sim timing.

### Issue: Low motivation mid-project
**Solution:** Commit to GitHub. Share progress. Celebrate small wins in WEEKLY_LOG.md.

---

## Resources

- **ROS2:** https://docs.ros.org/en/humble/
- **Unitree:** https://github.com/unitreerobotics
- **Isaac Gym:** https://docs.nvidia.com/isaac/isaac_gym/
- **Job posting keywords:** "humanoid robotics", "manufacturing automation", "sim-to-real"

---

## Timeline

```
Today → Week 2: ROS2 + sensor integration (GitHub commits)
Week 3 → Week 4: Simulation + Gazebo
Week 5 → Week 6: Locomotion controller on hardware
Week 7 → Week 8: Perception pipeline
Week 9 → Week 10: Imitation learning
Week 11 → Week 12: Capstone + demo video

Apply at Week 4, 8, 12
```

---

## Questions?

Refer to:
1. `docs/ROS2_SETUP.md` for environment
2. `docs/UNITREE_API.md` for hardware interface
3. `docs/WEEKLY_LOG.md` for progress tracking
4. `README.md` for project overview

---

**Start now. Commit daily. Apply with confidence.**

✓ Set 1-hour daily calendar block starting tomorrow
✓ Push first code to GitHub this week
✓ Update WEEKLY_LOG.md after each session

Good luck. Your portfolio will be exceptional.

