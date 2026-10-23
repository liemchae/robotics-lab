# Gait Stability Fundamentals

## Support Polygon
- Area defined by ground contact points (feet on ground)
- Center of Mass (CoM) must stay inside polygon for static stability
- Trotting: 2 feet on ground = line (not polygon) = dynamically stable only

## Trotting Gait Pattern
- Cycle: 2.0 seconds (0.5 Hz)
- Phase 1 (0-1.0s): FL + RR swing, FR + RL stance
- Phase 2 (1.0-2.0s): FR + RL swing, FL + RR stance
- Diagonal pairs move together (natural quadruped pattern)

## Why 0.5 Hz?
| Frequency | Speed | Stability | Notes |
|-----------|-------|-----------|-------|
| 0.2 Hz | Very slow | High | Too slow for practical use |
| 0.5 Hz | 0.2 m/s | Good | Optimal for learning + control |
| 1.0 Hz | 0.5 m/s | Moderate | Requires faster feedback |
| 2.0 Hz | 1.0 m/s | Low | Near gallop, hard to control |

## Stability Margins

### Static Stability Margin (SSM)
- Distance from CoM projection to nearest edge of support polygon
- Minimum: 0.05m (diagonal stance for Go2)
- Below 0.03m: risk of tipping

### Dynamic Stability Margin (DSM)
- Accounts for angular velocity and momentum
- Angular velocity threshold: 1.0 rad/s
- Above threshold: corrective action needed

## Control Requirements
- Feedback loop: <50 ms (20 Hz minimum)
- Foot force sensing: detect stance vs swing
- IMU: track body orientation and angular velocity
- Joint encoders: know leg positions for CoM estimation

## Detecting Instability
1. CoM projection outside support polygon
2. Angular velocity > 1.0 rad/s sustained
3. Foot force asymmetry > 50% between diagonal pairs
4. Joint position error > 0.1 rad from target
