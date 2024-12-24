# Mandelbrot Set Visualization and Zoom Animation

## 1. 功能

此 Python 程式生成曼德布羅集合的視覺化圖像，並提供縮放動畫功能，允許使用者互動式地探索集合的不同區域。主要功能包括：

- **靜態視覺化**：顯示曼德布羅集合的初始全貌。
- **縮放動畫**：動畫化地展示縮放進入集合的特定區域。
- **互動式導航**：在動畫過程中，使用者可以透過方向鍵動態調整縮放中心，探索集合的不同部分。

## 2. 使用方式

1. **安裝依賴**：
   - 程式需要以下 Python 函式庫：
     - `numpy`：用於數值計算。
     - `matplotlib`：用於繪圖和動畫。
   - 使用 pip 安裝所需的函式庫：
     ```bash
     pip install numpy matplotlib
     ```

2. **執行程式**：
   - 在終端機或 IDE 中運行 `mandelbrot.py`：
     ```bash
     python mandelbrot.py
     ```

3. **互動控制**：
   - 在縮放動畫過程中，使用 **方向鍵**（上、下、左、右）動態調整縮放中心，探索集合的不同區域。

## 3. 程式架構

程式主要包含以下函式：

- **`mandelbrot(c, max_iter)`**：
  - 計算複數平面中每個點 `c` 的曼德布羅集合，返回在達到最大迭代次數前，點是否逃逸的次數。

- **`generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)`**：
  - 生成覆蓋指定範圍的複數網格，並計算每個點的曼德布羅集合。

- **`animate_zoom(xmin, xmax, ymin, ymax, zoom_center, zoom_levels, width, height, max_iter)`**：
  - 創建縮放動畫，生成連續的畫面，展示縮放進入集合的過程。

- **`on_key(event, zoom_center, ax, width, height, max_iter, zoom_levels, frames, final_frame)`**：
  - 處理使用者的鍵盤輸入，允許在動畫過程中動態調整縮放中心。

## 4. 開發過程

開發過程始於理解曼德布羅集合的數學原理，以及如何使用 Python 進行科學計算和視覺化。最初，使用 `numpy` 和 `matplotlib` 生成靜態的曼德布羅集合圖像。接著，實現了縮放動畫功能，通過迭代調整圖像邊界，逐步縮放進入集合的不同區域。

為了增強互動性，利用 `matplotlib` 的鍵盤事件處理功能，允許使用者在動畫過程中使用方向鍵動態調整縮放中心。整個過程中，逐步完善了視覺化效果和使用者體驗。

## 5. 參考資料來源

- **曼德布羅集合**：
  - 曼德布羅集合的數學理論參考了以下線上資源：
    - [維基百科：曼德布羅集合](https://zh.wikipedia.org/wiki/曼德布羅集合)

- **Python 函式庫**：
  - 以下是相關函式庫的官方文件：
    - [NumPy 文件](https://numpy.org/doc/)
    - [Matplotlib 文件](https://matplotlib.org/stable/contents.html)

- **ChatGPT**：
  - 在開發過程中，部分實現細節和程式結構的設計得到了 ChatGPT 的協助。

## 6. 程式修改或增強的內容

原始實現僅提供了靜態的曼德布羅集合視覺化。以下是所做的修改和增強：

1. **縮放動畫**：
   - 修改程式以創建動態的縮放效果，通過調整圖像邊界，逐步縮放進入集合的不同區域。

2. **互動式縮放**：
   - 新增互動功能，允許使用者在動畫過程中使用方向鍵動態調整縮放中心，探索集合的不同部分。

3. **改進的繪圖**：
   - 優化視覺化效果，設置適當的軸範圍，並添加標籤和標題，以提升使用者體驗。

這些修改和增強使程式從靜態視覺化轉變為動態且具有互動性的曼德布羅集合探索工具。
