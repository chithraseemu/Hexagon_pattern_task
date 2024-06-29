import matplotlib.pyplot as plt
import numpy as np

def hexagon(x_center, y_center, size):
    angle = np.linspace(0, 2 * np.pi, 6, endpoint=False)
    x_hexagon = x_center + size * np.cos(angle)
    y_hexagon = y_center + size * np.sin(angle)
    return x_hexagon, y_hexagon

def plot_hex_grid(rows, cols, size=1):
    plt.figure(figsize=(cols, rows))
    for row in range(rows):
        for col in range(cols):
            x_offset = col * 1.5 * size
            y_offset = row * np.sqrt(3) * size + (col % 2) * (np.sqrt(3) * size / 2)
            x_hexagon, y_hexagon = hexagon(x_offset, y_offset, size)
            plt.fill(x_hexagon, y_hexagon, edgecolor='black', facecolor='none')
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.show()

def main():
    rows = int(input("Enter number of rows for first grid: "))
    cols = int(input("Enter number of columns for first grid: "))


    plot_hex_grid(rows, cols)

if __name__ == "__main__":
    main()
