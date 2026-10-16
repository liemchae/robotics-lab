# GitHub Setup Guide

Push this repo to GitHub for portfolio visibility.

---

## 1. Create Repository on GitHub

1. Go to github.com/new
2. Name: `robotics-lab`
3. Description: "Humanoid control stack + learning on Unitree with NVIDIA RTX5090"
4. Visibility: **Public** (show employers)
5. **Do NOT** initialize with README (we have one)
6. Click "Create"

---

## 2. Push Local Repo

```bash
cd /Users/LCHAEHY/argus_agent/Work/robotics-lab

# Initialize git (if not already done)
git init

# Add all files
git add .

# First commit
git commit -m "Initial ROS2 project structure: sensor reader, Unitree integration skeleton

- ROS2 Humble workspace setup
- Unitree sensor reader node (IMU, joint state, foot force)
- Configuration files for Unitree H1/Go2
- Weekly progress tracking
- Documentation: ROS2 setup, API reference, weekly log

Week 1-2 milestone: Establish sensor acquisition pipeline
"

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/robotics-lab.git

# Rename branch to main (if needed)
git branch -M main

# Push
git push -u origin main
```

---

## 3. Update README with GitHub Link

```bash
# Edit README.md
# Add near top:
**GitHub:** [github.com/YOUR_USERNAME/robotics-lab](https://github.com/YOUR_USERNAME/robotics-lab)
```

---

## 4. GitHub Best Practices

### Commit Format (for PM credibility)
```
<type>(<scope>): <subject>

<body>

Relates to: <issue or milestone>
```

Types:
- `feat` — New feature (e.g., new ROS2 node)
- `fix` — Bug fix
- `docs` — Documentation
- `refactor` — Code cleanup
- `test` — Testing
- `chore` — Setup, config

### Weekly Commit Cadence
After each 1-hour session, commit progress:
```bash
git add .
git commit -m "Week 1 Day 3: Sensor reader improvements

- Added joint encoder publishing
- Fixed IMU orientation quaternion
- Tested with synthetic data at 50 Hz
"
git push
```

---

## 5. In Job Applications

**Use this format in cover letter/application:**

> "I'm building a hands-on robotics portfolio while preparing for this role. I've established a GitHub repository demonstrating real robot control on Unitree humanoid with NVIDIA RTX5090. By Week 12, I'll have deployed a learned policy on hardware and written a comprehensive program plan.
> 
> Repository: [github.com/...robotics-lab](...)
> 
> This shows:
> - System architecture thinking (ROS2, simulation, hardware integration)
> - Software engineering discipline (reproducible builds, documentation)
> - Hardware-software coupling understanding (sim-to-real transfer)
> - Manufacturing readiness (cost, scaling, supply chain)"

---

## 6. Link to Application

When applying to Tesla/Google/Boston Dynamics:

1. Include GitHub link in resume
2. In cover letter, highlight 2-3 specific learnings from each phase
3. By Week 12, link demo video as well

---

## Commit History Example (12-Week Arc)

```
Week 1-2:  feat(sensor): Unitree IMU and joint state integration
           docs: ROS2 setup guide, Unitree API reference

Week 3-4:  feat(simulation): Gazebo environment and URDF loader
           fix(sensor): Latency reduction in sensor publisher

Week 5-6:  feat(control): Walk controller with PID balance
           test: Hardware validation on real Unitree

Week 7-8:  feat(perception): RGB-D obstacle detection
           feat(arm): Robotic arm reach-and-grasp basics

Week 9-10: feat(learning): Imitation learning framework
           feat(training): Policy training on RTX5090 with Isaac Gym

Week 11-12: docs(capstone): Program plan for production deployment
            docs: Final learnings and architectural decisions
```

---

## Resources

- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub README Best Practices](https://github.com/matiassingers/awesome-readme)

