import matplotlib.pyplot as plt

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