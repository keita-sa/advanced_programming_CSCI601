import numpy as np

class Smoke:
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