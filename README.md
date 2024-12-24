# Mandelbrot Set Visualization and Interactive Zoom

## 1. Program Features (5 points)
This program calculates and visualizes the famous **Mandelbrot Set**, providing dynamic zoom functionality to allow users to explore its intricate structure. Key features include:

- **Static Mandelbrot Set Generation:** Displays an initial view of the entire set.
- **Dynamic Zoom Animation:** Gradually zooms into a specified center point, revealing details.
- **Interactive View Adjustment:** Adjust the zoom center in real-time using arrow keys.

---

## 2. Usage (5 points)

### 2.1 Run the Program
```bash
python mandelbrot_zoom.py
```

### 2.2 Controls
- The initial Mandelbrot Set view will be displayed.
- A dynamic zoom animation will start automatically.
- After zooming, use **arrow keys** (`↑`, `↓`, `←`, `→`) to shift the zoom center.
- The view will update dynamically.

---

## 3. Program Structure (5 points)

- **mandelbrot(c, max_iter):** Calculates the divergence time for the Mandelbrot set.
- **generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):** Generates a Mandelbrot image based on the given range and resolution.
- **animate_zoom(...):** Animates zooming into a specified center point.
- **on_key(...):** Handles user keyboard inputs to update the zoom center.
- **Main Execution:** Controls the overall program flow.

---

## 4. Development Process (5 points)

- **Initial Phase:** Implemented basic static Mandelbrot set visualization.
- **Second Phase:** Added dynamic zoom functionality with smooth transitions.
- **Final Phase:** Introduced interactive view adjustment using keyboard controls.
- Optimized performance and ensured smooth user experience.

---

## 5. References (5 points)

- **Matplotlib Documentation:** https://matplotlib.org
- **NumPy Documentation:** https://numpy.org
- Used **ChatGPT** for program logic design and debugging.

---

## 6. Modifications and Enhancements (10 points)

### 6.1 Base Features from References
- Static Mandelbrot set visualization.
- Basic zoom functionality.

### 6.2 Custom Modifications and Enhancements
- **Dynamic Zoom Animation:** Added smooth frame-by-frame zoom transitions.
- **Interactive Controls:** Enabled zoom center adjustment using **arrow keys**.
- **Performance Optimization:** Improved real-time rendering efficiency.
- **View Range Display:** Added titles showing the current zoom center and level.

This version supports both static image generation and interactive exploration, making the Mandelbrot Set visualization intuitive and flexible.

---

Feel free to suggest improvements or further optimizations!

**Developer:** [Your Name]
**Version:** 1.0
**Date:** [Insert Date]

