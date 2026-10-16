# Weekly Progress Log

Track learnings, blockers, experiments, and milestones week-by-week.

---

## Week 1-2: ROS2 Fundamentals

**Status:** In Progress  
**Target:** ROS2 environment, first sensor reader node  

### Tasks
- [ ] ROS2 Humble installation (lab machine, Ubuntu 22.04)
- [ ] Workspace setup + colcon build verification
- [ ] Clone Unitree SDK2 + ROS2 wrapper
- [ ] Create `unitree_control` package (Python)
- [ ] Implement sensor reader node (IMU, joint state, foot force)
- [ ] Test with synthetic data (before hardware connection)

### Learnings
- *To be filled*

### Blockers
- *None yet*

### Key Metrics
- ROS2 talker/listener test: ✓ (if working)
- Sensor reader node compiles: ⏳
- Synthetic publish rate: ⏳ Hz

---

## Week 3-4: Simulation + Unitree Integration

**Status:** Not Started  
**Target:** Gazebo environment + real hardware connection  

### Tasks
- [ ] URDF model for Unitree (load into Gazebo)
- [ ] Create Gazebo world with obstacles
- [ ] Connect real Unitree to ROS2 sensor reader
- [ ] Measure latency (real vs. publisher)
- [ ] Log sensor data to rosbag for analysis

### Learnings
- *To be filled*

### Blockers
- *To be filled*

### Key Metrics
- Gazebo simulation FPS: ⏳
- Real sensor latency: ⏳ ms
- Data recording stability: ⏳

---

## Week 5-6: Locomotion Control

**Status:** Not Started  
**Target:** Walk controller on Unitree  

### Tasks
- [ ] Study Unitree gait parameters (stride, height, speed)
- [ ] Implement basic PID balance controller
- [ ] Create walk command node (ROS2 service)
- [ ] Test on real Unitree (slow speeds first)
- [ ] Measure stability, energy consumption

### Learnings
- *To be filled*

### Blockers
- *To be filled*

### Key Metrics
- Walk speed achieved: ⏳ m/s
- Balance error: ⏳ degrees
- Power consumption: ⏳ W

---

## Week 7-8: Perception + Vision

**Status:** Not Started  
**Target:** Obstacle detection, camera pipeline  

### Tasks
- [ ] Setup RGB-D camera on Unitree or arm
- [ ] OpenCV obstacle detection (simple blob detection)
- [ ] YOLO lightweight model for object detection
- [ ] Deploy on RTX5090 for inference
- [ ] Arm reaches & grasps detected object (basic)

### Learnings
- *To be filled*

### Blockers
- *To be filled*

### Key Metrics
- Detection FPS: ⏳
- Inference latency: ⏳ ms
- Grasp success rate: ⏳ %

---

## Week 9-10: Imitation Learning

**Status:** Not Started  
**Target:** Learned policy on Unitree  

### Tasks
- [ ] Collect teleoperation demonstrations (manual control)
- [ ] PyTorch model training on RTX5090
- [ ] Evaluate policy in simulation
- [ ] Deploy to real robot
- [ ] Measure success rate vs. manual control

### Learnings
- *To be filled*

### Blockers
- *To be filled*

### Key Metrics
- Training data samples: ⏳
- Model accuracy: ⏳ %
- Real robot success rate: ⏳ %

---

## Week 11-12: Capstone + Finalization

**Status:** Not Started  
**Target:** Program plan + portfolio  

### Tasks
- [ ] Write capstone document (5-7 pages)
- [ ] Clean up GitHub repo + docs
- [ ] Record demo video (real Unitree executing learned task)
- [ ] Prepare presentation materials
- [ ] Final testing & documentation

### Learnings
- *To be filled*

### Blockers
- *To be filled*

### Key Deliverables
- Program plan: ⏳
- GitHub repo: ⏳ stars
- Demo video: ⏳ length

---

## Running Experiments

Document any standalone experiments here:

### Experiment: Sim-to-Real Latency
**Date:** TBD  
**Objective:** Measure gap between simulator and real robot response  
**Setup:** Gazebo simulator + real Unitree running same command  
**Result:** ⏳  
**Insight:** ⏳

---

## Resources & References

- [Unitree Go2 Spec Sheet](https://www.unitreerobotics.com/)
- [ROS2 Humble Docs](https://docs.ros.org/en/humble/)
- [Isaac Gym Examples](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs)

---

## Next Week Prep

*Update as you complete each week.*

