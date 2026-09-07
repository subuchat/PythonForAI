import matplotlib
import matplotlib.pyplot as plt

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

def main():
    # Uncomment whichever function you want to run
    #plot_x_y2_graph()
    bar_plot_example()

if __name__ == "__main__":
    main()