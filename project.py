import numpy as np
import pandas as pd

np.random.seed(123)

class Fruid(object):
    def __init__(self):
        self.con = 1.0
        self.x, self.y, self.z = 2.0, 0.0, 0.0  # Initial positions
        self.vx, self.vy, self.vz = 0.05, 0.0, -0.1  # Initial velocities
        self.fx, self.fy, self.fz = 0.0, 0.0, 0.0  # Forces acting on the object
        self.mass = 1.0  # Assuming unit mass for Fruid
        self.dt = 0.1  # Time step for the simulation

    def eval_force(self):
        """Random force for Fruid object."""
        self.fx = np.random.randn()
        self.fy = np.random.randn()
        self.fz = np.random.randn()

    def update_position(self):
        """Update position based on velocity and forces."""
        ax = self.fx / self.mass
        ay = self.fy / self.mass
        az = self.fz / self.mass

        # Update velocities
        self.vx += ax * self.dt
        self.vy += ay * self.dt
        self.vz += az * self.dt

        # Update positions
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt
        self.z += self.vz * self.dt

class HeavySmoke(Fruid):
    def __init__(self):
        super().__init__()
        self.mass = 1.0  # Mass of the HeavySmoke object
        self.g_const = [0.0, 0.0, -9.8]  # Gravitational constant

    def eval_force(self):
        """Force for HeavySmoke object including gravity."""
        self.fx = np.random.randn() + self.mass * self.g_const[0]
        self.fy = np.random.randn() + self.mass * self.g_const[1]
        self.fz = np.random.randn() + self.mass * self.g_const[2]

def run_simulation(obj, steps):
    """Run simulation for a given object and number of time steps."""
    data = {
        'step': [],
        'x': [], 'y': [], 'z': [],
        'vx': [], 'vy': [], 'vz': [],
        'fx': [], 'fy': [], 'fz': []
    }

    for step in range(steps):
        obj.eval_force()
        obj.update_position()

        # Logging data at each step
        data['step'].append(step)
        data['x'].append(obj.x)
        data['y'].append(obj.y)
        data['z'].append(obj.z)
        data['vx'].append(obj.vx)
        data['vy'].append(obj.vy)
        data['vz'].append(obj.vz)
        data['fx'].append(obj.fx)
        data['fy'].append(obj.fy)
        data['fz'].append(obj.fz)

    return pd.DataFrame(data)

# Create objects for Fruid and HeavySmoke
average_fruid = Fruid()
heavy_smoke = HeavySmoke()

# Run the simulation for 100 steps
steps = 100
fruid_data = run_simulation(average_fruid, steps)
heavy_smoke_data = run_simulation(heavy_smoke, steps)

# Analyze the results
print("Fruid Data Overview:")
print(fruid_data.describe())

print("\nHeavySmoke Data Overview:")
print(heavy_smoke_data.describe())
