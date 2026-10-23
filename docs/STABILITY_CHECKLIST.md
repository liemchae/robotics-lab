# CP1 Stability Checklist

## Pre-Lab Prep
- [ ] Understand support polygon concept
- [ ] Know SSM/DSM limits (0.05m static, 1.0 rad/s dynamic)
- [ ] Review SENSOR_EXAMPLES.md expected values
- [ ] Verify analyze_rosbag.py and inspect_rosbag.py work
- [ ] Prepare recording commands (see rosbag_structure.txt)

## During CP1 (Oct 26)

### Standing Test (45 seconds)
- [ ] Robot powered on, standing still
- [ ] Start rosbag recording
- [ ] Verify IMU accel z ~9.81 m/s^2
- [ ] Verify foot force ~equal on all 4 feet
- [ ] Verify angular velocity ~0 rad/s
- [ ] Stop recording

### Walking Test (45 seconds)
- [ ] Start rosbag recording
- [ ] Command trotting gait (0.5 Hz, 0.2 m/s)
- [ ] Observe diagonal pair pattern (FL+RR, FR+RL)
- [ ] Verify robot maintains balance
- [ ] Stop recording

### Quick Checks During Test
- IMU pitch stays within +/-5 degrees
- No foot force sensor reads 0 during stance phase
- Joint positions follow expected sinusoidal pattern

## Post-Lab Analysis
- [ ] Run inspect_rosbag.py on recording
- [ ] Run analyze_rosbag.py on .db3 file
- [ ] Verify message counts (~4500 per topic for 90s)
- [ ] Check diagonal phase pattern in joint states
- [ ] Compute latency statistics
- [ ] Compare real values to SENSOR_EXAMPLES.md expectations

## Success Criteria
- [ ] Balanced standing: foot force variance < 20%
- [ ] Trotting gait: 0.5 Hz with diagonal pairs visible
- [ ] Body sway: < 0.5 rad/s angular velocity
- [ ] Sensor rates: 50 Hz confirmed for IMU/joints/force
- [ ] Rosbag: complete 90s recording without drops
