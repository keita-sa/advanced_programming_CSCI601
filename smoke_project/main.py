# from smoke import Smoke
# from simulation import run_simulation
# from visualization import plot_simulation

from smoke.smoke import Smoke
from simulation.simulation import run_simulation
from analysis.cleaning import clean_data
from analysis.preprocessing import preprocess_data
# from smoke_project.visualization.visualization import plot_simulation

from visualization.visualization import plot_simulation

# from analysis.analysis import analyze_data
# from visualization.visualization import visualize_data


if __name__ == "__main__":
    # Create and run simulation
    # average_smoke = Smoke()
    # steps = 100
    # smoke_data = run_simulation(average_smoke, steps)

    average_smoke = Smoke()
    steps = 100
    raw_data = run_simulation(average_smoke, steps)

    cleaned_data = clean_data(raw_data)
    processed_data = preprocess_data(cleaned_data)

    # Analyze and visualize results
    print("Processed Data Overview:")
    print(processed_data.describe())
    plot_simulation(processed_data)
    # analyze_data(processed_data)
    # visualize_data(processed_data)