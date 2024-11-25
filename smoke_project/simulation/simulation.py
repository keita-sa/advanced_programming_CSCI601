import pandas as pd

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