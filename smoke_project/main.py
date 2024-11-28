from analysis.cleaning import clean_data
from analysis.preprocessing import preprocess_data
from simulation.base_simulation import run_simulation
from simulation.smoke_simulation import plot_smoke_simulation, combined_plot_simulation
from smoke.smoke import Smoke

if __name__ == "__main__":
    # Create and run simulation
    average_smoke = Smoke()

    steps = 100
    raw_data = run_simulation(average_smoke, steps)

    cleaned_data = clean_data(raw_data)
    processed_data = preprocess_data(cleaned_data)

    # Analyze and visualize results
    print("Processed Data Overview:")
    print(processed_data.describe())

    # Unified visualization
    combined_plot_simulation(processed_data)
