import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to calculate Mandelbrot set
def mandelbrot(c, max_iter):
    z = np.zeros_like(c, dtype=complex)
    div_time = np.full(c.shape, max_iter, dtype=int)
    mask = np.ones(c.shape, dtype=bool)
    
    for i in range(max_iter):
        z[mask] = z[mask]**2 + c[mask]
        mask = np.abs(z) <= 2
        div_time[~mask & (div_time == max_iter)] = i
        
    return div_time

# Generate Mandelbrot set image
def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    return mandelbrot(C, max_iter)

# Animate Zoom
def animate_zoom(xmin, xmax, ymin, ymax, zoom_center, zoom_levels, width=800, height=800, max_iter=100):
    frames = []
    cx, cy = zoom_center
    
    # Create zoom animation frames
    for frame in range(zoom_levels):
        zoom_factor = 2 ** (frame / zoom_levels)
        x_range = (xmax - xmin) / zoom_factor
        y_range = (ymax - ymin) / zoom_factor
        current_xmin, current_xmax = cx - x_range / 2, cx + x_range / 2
        current_ymin, current_ymax = cy - y_range / 2, cy + y_range / 2
        
        image = generate_mandelbrot(current_xmin, current_xmax, current_ymin, current_ymax, width, height, max_iter)
        frames.append((image, current_xmin, current_xmax, current_ymin, current_ymax))
    
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis('off')
    img = ax.imshow(frames[0][0], cmap='hot', origin='lower', extent=(xmin, xmax, ymin, ymax))
    
    def update_frame(frame):
        img.set_data(frames[frame][0])
        img.set_extent((frames[frame][1], frames[frame][2], frames[frame][3], frames[frame][4]))
        ax.set_title(f'Zoom Level {frame + 1}')
    
    ani = animation.FuncAnimation(fig, update_frame, frames=len(frames), interval=200, repeat=False)
    plt.show(block=False)  # Non-blocking show for interaction
    return fig, ax, ani, frames[-1]  # Return the last frame for the final zoomed-in plot

# Handle Key Events for Interaction (in the zoomed-in plot)
def on_key(event, zoom_center, ax, width, height, max_iter, zoom_levels, frames, final_frame):
    step = 0.1
    cx, cy = zoom_center
    
    # Update zoom center based on arrow key presses
    if event.key == 'up':
        cy += step * (ax.get_ylim()[1] - ax.get_ylim()[0])
    elif event.key == 'down':
        cy -= step * (ax.get_ylim()[1] - ax.get_ylim()[0])
    elif event.key == 'left':
        cx -= step * (ax.get_xlim()[1] - ax.get_xlim()[0])
    elif event.key == 'right':
        cx += step * (ax.get_xlim()[1] - ax.get_xlim()[0])
    
    # Update the zoom center
    zoom_center = (cx, cy)
    
    # Generate the Mandelbrot set with updated zoom level
    zoom_factor = 2 ** (zoom_levels / zoom_levels)
    x_range = (final_frame[2] - final_frame[1]) / zoom_factor
    y_range = (final_frame[4] - final_frame[3]) / zoom_factor
    current_xmin, current_xmax = cx - x_range / 2, cx + x_range / 2
    current_ymin, current_ymax = cy - y_range / 2, cy + y_range / 2
    
    # Generate the new zoomed-in image
    image = generate_mandelbrot(current_xmin, current_xmax, current_ymin, current_ymax, width, height, max_iter)
    
    # Update the plot
    ax.clear()
    ax.imshow(image, extent=(current_xmin, current_xmax, current_ymin, current_ymax), cmap='hot', origin='lower')
    ax.set_title(f'Mandelbrot Set - Zoom Center: ({cx:.3f}, {cy:.3f})')
    ax.axis('off')
    plt.draw()

# Main Execution
if __name__ == '__main__':
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5
    width, height = 800, 800
    max_iter = 100
    
   # Initial Static Plot
    plt.figure(figsize=(10, 10))
    image = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(image, extent=(xmin, xmax, ymin, ymax), cmap='hot', origin='lower')
    plt.zcolorbar(label='Iterations')
    plt.title('Mandelbrot Set')
    plt.show()
    
    # Initial zoom center and number of zoom levels
    zoom_center = (-0.1, 0.9)
    zoom_levels = 20
    
    # Generate and animate the Mandelbrot zoom plot
    fig, ax, ani, final_frame = animate_zoom(xmin, xmax, ymin, ymax, zoom_center, zoom_levels, width, height, max_iter)
    
    # Enable Interactive Navigation
    print("Use the arrow keys to shift the zoom center in the zoomed-in plot.")
    fig.canvas.mpl_connect('key_press_event', lambda event: on_key(event, zoom_center, ax, width, height, max_iter, zoom_levels, final_frame, final_frame))
    
    # Make sure the plot remains interactive and doesn't block
    plt.show()