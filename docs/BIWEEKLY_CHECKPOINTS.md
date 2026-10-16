# Biweekly Lab Checkpoints

**Schedule:** Every 2 weeks (typically weekends)  
**Duration:** 2 hours per checkpoint  
**Location:** Robotics lab with Unitree + RTX5090  
**Goal:** Validate theory, gather real data, iterate

All checkpoints produce GitHub commits + hardware data logs.

---

## CHECKPOINT 1: Week 2 (End of ROS2 Fundamentals)

**Focus:** Sensor integration validation  
**Theory Prerequisite:** DAILY_THEORY_PATH.md Days 1-5

### Pre-Lab Checklist (Home, 30 min before)

- [ ] Review: docs/UNITREE_API.md (sensor topics, baud rate)
- [ ] Verify: `/dev/ttyUSB0` detection (check USB connection)
- [ ] Test: `ros2 --version` + talker/listener running locally
- [ ] Prepare: Empty directory for data logs

### Lab Session (2 hours)

**0:00-0:30 | Setup & Connection**
```bash
# Connect real Unitree
ls -la /dev/ttyUSB*

# Start sensor reader node
ros2 run unitree_control sensor_reader

# Monitor in separate terminal
ros2 topic list
ros2 topic echo /unitree/imu
ros2 topic echo /unitree/joint_state
```

**0:30-1:15 | Data Collection & Validation**

Record 45 seconds of sensor data:
```bash
ros2 bag record /unitree/imu /unitree/joint_state /unitree/foot_force -o cp1_sensor_data

# Meanwhile, move Unitree slowly (manual control or gentle walk)
# Capture: real motion → real sensor readings
```

**1:15-1:45 | Analysis**

Playback & inspect:
```bash
ros2 bag play cp1_sensor_data

# Terminal 1: Visualize data
ros2 topic echo /unitree/imu --field linear_acceleration.z

# Terminal 2: Measure frequency
ros2 topic hz /unitree/imu
```

Document findings:
- IMU publish rate: ___ Hz (expected: ~50 Hz)
- Joint state latency: ___ ms
- Foot force sensitivity: ___ N per step
- Any data corruption/gaps: YES/NO

**1:45-2:00 | Commit & Return**

```bash
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab

git add docs/BIWEEKLY_CHECKPOINTS.md CHECKPOINT_1_NOTES.md

git commit -m "checkpoint(1): ROS2 sensor integration validated

Lab Session Week 2:
- Connected real Unitree Go2 via /dev/ttyUSB0
- Verified sensor reader node publishing:
  * IMU: 50 Hz, <5ms latency
  * Joint state: 50 Hz
  * Foot force: 4 channels, pressure readings
- Recorded 45s rosbag of walking motion
- Analyzed publish rates + data quality

Findings:
- Sensor data clean, no corruption
- All topics publishing at expected rates
- Ready for Gazebo comparison (next checkpoint)

Files: cp1_sensor_data.bag (stored in lab)
"

git push
```

---

## CHECKPOINT 2: Week 4 (End of Gazebo + Simulation)

**Focus:** Sim-to-real comparison, latency analysis  
**Theory Prerequisite:** DAILY_THEORY_PATH.md Days 6-15

### Lab Session (2 hours)

**0:00-0:30 | Setup Simulation + Hardware**

Terminal 1: Gazebo simulator
```bash
gazebo ~/ros2_ws_learning/src/unitree_models/worlds/simple.world
```

Terminal 2: Real Unitree
```bash
ros2 run unitree_control sensor_reader
```

Terminal 3: Monitor both
```bash
# Subscribe to both sim and real topics
ros2 topic list | grep -E "gazebo|unitree"
```

**0:30-1:15 | Comparative Test**

In simulator:
```bash
# Send joint commands
ros2 topic pub /gazebo/joint_cmd trajectory_msgs/JointTrajectory \
  "{joint_names: [FL_hip, FL_thigh], ...}"
```

In reality:
```bash
# Send same commands to real Unitree
ros2 topic pub /unitree/cmd_vel geometry_msgs/Twist \
  "{linear: {x: 0.1}, angular: {z: 0.0}}"
```

Record both:
```bash
ros2 bag record \
  /gazebo/joint_state \
  /unitree/joint_state \
  -o cp2_sim_vs_real
```

**1:15-1:45 | Analysis**

Compare timing:
```bash
# Latency: command → execution
# Accuracy: expected vs. measured joint angle
# Energy: power draw in sim vs. battery consumption
```

Document:
- Sim latency: ___ ms
- Real latency: ___ ms
- Divergence: ___ % (after 30 seconds)
- Limiting factors: ___

**1:45-2:00 | Commit**

```bash
git commit -m "checkpoint(2): Sim-to-real latency analysis

Week 4 Lab Session:
- Ran Gazebo simulator alongside real Unitree
- Executed identical joint commands on both
- Recorded parallel rosbags for comparison

Latency Measurements:
- Sim: ~5ms (deterministic, 1kHz physics)
- Real: ~15ms (wireless + hardware)
- Gap: 10ms (expected, acceptable for walking)

Divergence after 30s: <2% (position error)

Insights:
- Wireless latency is bottleneck (not computation)
- Can use sim for planning, real hardware for validation
- 10ms latency acceptable for 2 Hz gait controller

Next: Test walk controller on real hardware (checkpoint 3)
"

git push
```

---

## CHECKPOINT 3: Week 6 (End of Control Systems)

**Focus:** Walk controller deployment + performance  
**Theory Prerequisite:** DAILY_THEORY_PATH.md Days 16-30

### Lab Session (2 hours)

**0:00-0:30 | Safe Mode Testing**

Start slow:
```bash
# Gazebo: test controller at low speeds (sim only)
ros2 run unitree_control walk_controller --speed 0.1 --gazebo

# Verify stability before hardware
# Expected: steady walking at ~0.1 m/s
```

**0:30-1:15 | Real Unitree Deployment**

Once verified in sim:
```bash
# Real hardware (SAFETY FIRST: use harness/padded area)
ros2 run unitree_control walk_controller --speed 0.2 --hardware

# Monitor:
ros2 topic echo /unitree/imu  # Stability metric
ros2 topic echo /unitree/foot_force  # Contact detection
```

Record performance:
```bash
ros2 bag record /unitree/imu /unitree/joint_state /unitree/foot_force \
  -o cp3_walk_controller

# Duration: 60 seconds of steady walking
```

**1:15-1:45 | Performance Analysis**

Measure:
- Speed achieved: ___ m/s
- Stability (roll/pitch): ___ degrees variance
- Energy (battery drop): ___ % per minute
- Success rate: ___ (falls/recoveries)

**1:45-2:00 | Commit**

```bash
git commit -m "checkpoint(3): Walk controller deployed on hardware

Week 6 Lab Session:
- Implemented PID-based gait controller (local ROS2 node)
- Tested in Gazebo (stable at 0.1-0.5 m/s)
- Deployed on real Unitree (harness-supported)
- Recorded 60s walking motion + sensor data

Performance:
- Commanded: 0.2 m/s
- Achieved: 0.18 m/s (90% efficiency)
- Stability: roll ±2°, pitch ±3° (excellent)
- Battery consumption: 2% per minute
- No falls, smooth gait transition

Controller Parameters:
- PID gains: Kp=10, Ki=0.1, Kd=2
- Target height: 0.45m
- Stride frequency: 2.0 Hz

Next: Vision pipeline + obstacle avoidance
"

git push
```

---

## CHECKPOINT 4: Week 8 (End of Perception)

**Focus:** Vision pipeline + arm control  
**Theory Prerequisite:** DAILY_THEORY_PATH.md Days 31-45

### Lab Session (2 hours)

Record video + sensor fusion:
```bash
ros2 bag record \
  /camera/color/image_raw \
  /unitree/joint_state \
  /arm/joint_state \
  -o cp4_vision_arm_control
```

Measure:
- Detection FPS: ___ 
- Arm reach-to-grasp success: ___ %
- End-to-end latency: ___ ms

---

## CHECKPOINT 5: Week 10 (End of Learning)

**Focus:** Learned policy deployment  
**Theory Prerequisite:** DAILY_THEORY_PATH.md Days 46-55

### Lab Session (2 hours)

Deploy trained policy:
```bash
ros2 run unitree_control learned_policy_node
# Policy: trained on Week 9 with imitation learning

# Expected: Unitree executes learned behavior
# (e.g., navigate obstacle course, follow trajectory)
```

Record + analyze:
```bash
ros2 bag record ... -o cp5_learned_policy
```

Success metrics:
- Task completion rate: ___ %
- Energy efficiency vs. manual: ___ %
- Generalization: works on new obstacle layout: YES/NO

---

## CHECKPOINT 6: Week 12 (Capstone)

**Focus:** Demo video + final validation  
**Theory Prerequisite:** DAILY_THEORY_PATH.md Days 56-60 + capstone plan

### Lab Session (2 hours)

Film final demo:
```
1. Unitree standing ready
2. Controller starts, robot walks
3. Vision detects obstacle
4. Robot avoids, continues
5. Learned policy makes decision
6. Final pose/task completion
```

Resolution: 1080p, 30 fps, landscape  
Duration: 3-5 minutes  
Audio: None (just mechanical + motor sounds)

Commit to GitHub:
```bash
git commit -m "capstone(demo): Final portfolio video + deployment

Week 12 Lab Session:
- Filmed complete demo video (3 min, 1080p)
- Unitree executes full stack:
  * ROS2 sensor pipeline
  * Gazebo-validated controller
  * Vision-based obstacle avoidance
  * Learned policy from imitation

Demo: Autonomous walking → obstacle detection → avoidance → learned task

Portfolio Ready:
- GitHub: 60 commits (daily + checkpoints)
- Code: Full ROS2 stack (public repo)
- Video: Hardware demonstration
- Docs: Program plan + learnings

Ready for Optimus/Atlas/Google interviews
"

git push
```

Upload video to GitHub (LFS or linked):
```bash
git lfs install
git lfs track "*.mp4"
git add demo_week12_final.mp4
git commit -m "media: Final capstone demo video"
git push
```

---

## Data Storage

Store hardware data locally during lab visits:
```
robotics-lab/
├─ data/
│  ├─ cp1_sensor_data.bag
│  ├─ cp2_sim_vs_real.bag
│  ├─ cp3_walk_controller.bag
│  ├─ ...
│  └─ cp6_final_demo.mp4
```

(Mark `data/` in .gitignore to avoid huge repo)

---

## Checkpoint Commit Summary

After each 2-week lab visit:
```
checkpoint(N): [Focus area]

Week X Lab Session:
- What you tested
- Metrics achieved
- Key learnings
- Issues discovered + solutions
- Next steps

Files: cp{N}_*.bag (rosbag data)
"
```

---

## Progress Template

Update after each checkpoint:

```markdown
## Checkpoints Completed

- [ ] CP1 (Week 2): Sensor validation
- [ ] CP2 (Week 4): Sim-to-real latency
- [ ] CP3 (Week 6): Walk controller
- [ ] CP4 (Week 8): Vision + arm
- [ ] CP5 (Week 10): Learned policy
- [ ] CP6 (Week 12): Demo + capstone
```

