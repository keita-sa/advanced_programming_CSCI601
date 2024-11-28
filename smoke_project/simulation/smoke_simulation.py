import seaborn as sns
import matplotlib.pyplot as plt


def plot_smoke_simulation(smoke_data):
    """Plot simulation results for Smoke."""
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


def combined_plot_simulation(data):
    """Unified plot for general and Smoke-specific simulation results."""
    sns.set(style="whitegrid")
    fig, axs = plt.subplots(3, 3, figsize=(15, 12))  # 3x3 grid for flexibility
    fig.suptitle('Smoke Simulation - Unified Visualization', fontsize=16)

    # General plots
    sns.lineplot(x='step', y='x', data=data, ax=axs[0, 0], color='blue')
    axs[0, 0].set_title('x Position')
    axs[0, 0].set_xlabel('Step')
    axs[0, 0].set_ylabel('x')

    sns.lineplot(x='step', y='y', data=data, ax=axs[1, 0], color='green')
    axs[1, 0].set_title('y Position')
    axs[1, 0].set_xlabel('Step')
    axs[1, 0].set_ylabel('y')

    sns.lineplot(x='step', y='z', data=data, ax=axs[2, 0], color='red')
    axs[2, 0].set_title('z Position')
    axs[2, 0].set_xlabel('Step')
    axs[2, 0].set_ylabel('z')

    # Smoke-specific velocity plots
    sns.lineplot(x='step', y='vx', data=data, ax=axs[0, 1], color='purple')
    axs[0, 1].set_title('x Velocity')
    axs[0, 1].set_xlabel('Step')
    axs[0, 1].set_ylabel('vx')

    sns.lineplot(x='step', y='vy', data=data, ax=axs[1, 1], color='orange')
    axs[1, 1].set_title('y Velocity')
    axs[1, 1].set_xlabel('Step')
    axs[1, 1].set_ylabel('vy')

    sns.lineplot(x='step', y='vz', data=data, ax=axs[2, 1], color='brown')
    axs[2, 1].set_title('z Velocity')
    axs[2, 1].set_xlabel('Step')
    axs[2, 1].set_ylabel('vz')

    # Additional force plots
    sns.lineplot(x='step', y='fx', data=data, ax=axs[0, 2], color='cyan')
    axs[0, 2].set_title('x Force')
    axs[0, 2].set_xlabel('Step')
    axs[0, 2].set_ylabel('fx')

    sns.lineplot(x='step', y='fy', data=data, ax=axs[1, 2], color='magenta')
    axs[1, 2].set_title('y Force')
    axs[1, 2].set_xlabel('Step')
    axs[1, 2].set_ylabel('fy')

    sns.lineplot(x='step', y='fz', data=data, ax=axs[2, 2], color='grey')
    axs[2, 2].set_title('z Force')
    axs[2, 2].set_xlabel('Step')
    axs[2, 2].set_ylabel('fz')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
