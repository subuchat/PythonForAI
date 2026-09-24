import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_x_y2_graph():

    print(f"Matplotlib version: {matplotlib.__version__}")

    x = range(-10, 11)
    y = [value**2 for value in x]

    plt.plot(x,y)
    #plt.plot(x, y , label="y = x²", color='blue', linewidth=2)
    plt.xlabel("x axis")
    plt.ylabel("y = x²",color='red')
    plt.title("Plot of y = x²")
    plt.grid(True)
    plt.show()

def bar_plot_example():
    x1 = ['A', 'B', 'C', 'D']
    x2 = ['E', 'F', 'G', 'H']
    y1 = [10, 20, 15, 25]
    y2 = [12, 18, 22, 28]

    plt.bar(x1, y1, label="Series 1", color='orange')
    plt.bar(x2, y2, label="Series 2", color='blue')
    plt.plot()

    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.title("Bar Plot Example")
    plt.legend()
    plt.show()

def scatter_plot_example_matplotlib():
    # Generate dummy data
    np.random.seed(42)
    x = np.random.rand(50) * 10
    y = x * 2 + np.random.randn(50) * 2

    # --- MATPLOTLIB APPROACH ---
    plt.figure(figsize=(5, 4))
    plt.scatter(x, y, color="blue", alpha=0.7)
    plt.title("Matplotlib Basic Scatter")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()

def scatter_plot_example_seaborn():
    # Generate dummy data
    np.random.seed(42)
    x = np.random.rand(50) * 10
    y = x * 2 + np.random.randn(50) * 2

    # --- SEABORN APPROACH ---
    plt.figure(figsize=(5, 4))
    sns.scatterplot(x=x, y=y, color="green", alpha=0.7)
    plt.title("Seaborn Basic Scatter")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()

def scatter_plot_example_dataframe():
    # Load a built-in dataset as a Pandas DataFrame
    df = sns.load_dataset("tips")
    #print(df.head())
    #print(df.info())
    # --- SEABORN APPROACH (Recommended for DataFrames) ---
    # Seaborn automatically handles colors (hue) and builds the legend for you
    '''
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", palette="Set1")
    plt.title("Seaborn: Automatically Grouped by Time")
    plt.show()
    '''
    
    # --- MATPLOTLIB APPROACH ---
    # In Matplotlib, you have to manually loop over categories to get a legend
    plt.figure(figsize=(6, 4))
    for time_category, group in df.groupby("time"):
        print(f"Time Category: {time_category}, Number of Points: {len(group)}")
        plt.scatter(group["total_bill"], group["tip"], label=time_category, alpha=0.7)
    #plt.scatter(x = df["total_bill"], y = df["tip"], color="gray", alpha=0.5, label="All Data")
    #plt.scatter(df[df["time"] == "Lunch"]["total_bill"], df[df["time"] == "Lunch"]["tip"], label="Lunch", color="blue", alpha=0.7)
    #plt.scatter(df[df["time"] == "Dinner"]["total_bill"], df[df["time"] == "Dinner"]["tip"], label="Dinner", color="orange", alpha=0.7)
    #plt.title("Matplotlib: Manually Grouped by Time")   
    plt.xlabel("Total Bill")
    plt.ylabel("Tip")  
    plt.legend(title="Time of Day")
    plt.show()

    '''
    # --- PANDAS APPROACH ---

    df.plot(kind="scatter", x="total_bill", y="tip", c="time", colormap="viridis", alpha=0.7, title="Pandas DataFrame Scatter Plot")
    plt.xlabel("Total Bill")
    plt.ylabel("Tip")
    plt.show()
    '''

def main():
    # Uncomment whichever function you want to run
    #plot_x_y2_graph()
    #bar_plot_example()
    #scatter_plot_example_matplotlib()
    #scatter_plot_example_seaborn()
    scatter_plot_example_dataframe()

if __name__ == "__main__":
    main()