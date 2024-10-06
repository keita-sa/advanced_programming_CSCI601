import numpy as np
import pandas as pd
import seaborn as sns
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

def plot_simulation_seaborn(smoke_data):
    """Plot simulation results using Seaborn for Smoke."""
    sns.set(style="whitegrid")
    fig, axs = plt.subplots(3, 2, figsize=(12, 10))
    fig.suptitle('Smoke Simulation - Position and Velocity', fontsize=16)

    # Position plots
    sns.lineplot(x='step', y='x', data=smoke_data, ax=axs[0, 0], color='blue')
    axs[0, 0].set_title('x Position')
    axs[0, 0].set_xlabel('Step')
    axs[0, 0].set_ylabel('x')

    sns.lineplot(x='step', y='y', data=smoke_data, ax=axs[1, 0], color='green')
    axs[1, 0].set_title('y Position')
    axs[1, 0].set_xlabel('Step')
    axs[1, 0].set_ylabel('y')

    sns.lineplot(x='step', y='z', data=smoke_data, ax=axs[2, 0], color='red')
    axs[2, 0].set_title('z Position')
    axs[2, 0].set_xlabel('Step')
    axs[2, 0].set_ylabel('z')

    # Velocity plots
    sns.lineplot(x='step', y='vx', data=smoke_data, ax=axs[0, 1], color='purple')
    axs[0, 1].set_title('x Velocity')
    axs[0, 1].set_xlabel('Step')
    axs[0, 1].set_ylabel('vx')

    sns.lineplot(x='step', y='vy', data=smoke_data, ax=axs[1, 1], color='orange')
    axs[1, 1].set_title('y Velocity')
    axs[1, 1].set_xlabel('Step')
    axs[1, 1].set_ylabel('vy')

    sns.lineplot(x='step', y='vz', data=smoke_data, ax=axs[2, 1], color='brown')
    axs[2, 1].set_title('z Velocity')
    axs[2, 1].set_xlabel('Step')
    axs[2, 1].set_ylabel('vz')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

# Create objects for Smoke
average_smoke = Smoke()

# Run the simulation for 100 steps
steps = 100
smoke_data = run_simulation(average_smoke, steps)

# Analyze the results
print("Smoke Data Overview:")
print(smoke_data.describe())

# Plot simulation using seaborn
plot_simulation_seaborn(smoke_data)
