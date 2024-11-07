import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(123)

class Smoke(object):
    def __init__(self):
        self.con = 1.0
        self.x, self.y, self.z = 2.0, 0.0, 0.0  # Initial positions
        self.vx, self.vy, self.vz = 0.05, 0.0, -0.1  # Initial velocities
        self.fx, self.fy, self.fz = 0.0, 0.0, 0.0  # Forces acting on the object
        self.mass = 1.0  # Assuming unit mass for Smoke
        self.dt = 0.1  # Time step for the simulation

    def eval_force(self):
        """Random force for Smoke object."""
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

def plot_simulation(smoke_data):
    """Plot simulation results for Smoke."""
    time = smoke_data['step']

    # Create a figure with multiple subplots
    fig, axs = plt.subplots(3, 2, figsize=(12, 10))
    fig.suptitle('Smoke Simulation - Position and Velocity', fontsize=16)

    # Plot position for Smoke
    axs[0, 0].plot(time, smoke_data['x'], label='x (Smoke)', color='blue')
    axs[0, 0].set_title('Smoke - x Position')
    axs[0, 0].set_xlabel('Step')
    axs[0, 0].set_ylabel('x')

    axs[1, 0].plot(time, smoke_data['y'], label='y (Smoke)', color='green')
    axs[1, 0].set_title('Smoke - y Position')
    axs[1, 0].set_xlabel('Step')
    axs[1, 0].set_ylabel('y')

    axs[2, 0].plot(time, smoke_data['z'], label='z (Smoke)', color='red')
    axs[2, 0].set_title('Smoke - z Position')
    axs[2, 0].set_xlabel('Step')
    axs[2, 0].set_ylabel('z')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

# Create objects for Smoke and HeavySmoke
average_smoke = Smoke()

# Run the simulation for 100 steps
steps = 100
smoke_data = run_simulation(average_smoke, steps)

# Analyze the results
print("Smoke Data Overview:")
print(smoke_data.describe())

plot_simulation(smoke_data)
