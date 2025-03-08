Regression-Influential-Points-Identification-Python
## Influential Points Detection using Cook’s Distance & Leverage Cutoff
---
## 📌 Overview
This Python script identifies **influential data points** in regression models using:
- **Cook’s Distance**: Measures the impact of a data point on the regression model.
- **Leverage Values**: Detects outliers in the predictor space.
- **CSV Input Support**: Reads a CSV file containing Cook’s Distance and Leverage values.
- From the Cook's DIstance and Leverage Values using reference (i & ii) it estimates a threshold point which is used to determine the             infleuncial points.

The script is useful for **data scientists, statisticians, and machine learning engineers** working with regression models.
---
## ✅ Features
- ✔ Computes **Cook’s Distance** for each data point (Upcoming)  
- ✔ Calculates **Leverage values (Hat Matrix Diagonal)**  (Upcoming)
- ✔ Provides a **sample CSV file** to guide users for **CSV Input Support**
- ✔ **CSV Input Support**: Reads a CSV file containing Cook’s Distance and Leverage values
- ✔ Automatically determines **cutoff values** for Cook’s Distance and Leverage
- ✔ Identifies **only influential data points** based on statistical cut-offs  
- ✔ **Displays results in a formatted table** for clarity  
- ✔ Supports **custom visualization of influential points (Upcoming Feature)**  
---
## 🔹 How It Works (Current)
1. **Enter regression parameters** (number of predictors (p), data points (n), and independent variables (d)).
2. **Based on two references provided, the script automatically calculates cutoff values** for:
   - Cook’s Distance (Two Methods)
   - Leverage Points
3. **Reads Cook’s Distance and Leverage values from a CSV file**.
4. **Identifies and displays only influential points** in a structured table.
---
## 📌 FUll DETAILS
### Input CSV Format
The CSV file must have **three columns**:

| **Column Name**    | **Description**                          |
|--------------------|----------------------------------------|
| `Index`           | Row number of the data point           |
| `Cooks_Distance`  | Cook’s Distance value                  |
| `Leverage`        | Leverage value                         |

**Example CSV File (`data.csv`):**
```csv
Index,Cooks_Distance,Leverage
1,0.12,0.25
2,0.45,0.30
3,0.90,0.50
```
👉 **The script will automatically filter and display only influential points.**

---

## 🔧 Installation
Ensure you have **Python 3+** installed, then install the required dependencies using:
```bash
pip install pandas scipy
```
---
## 📌 How to Use
1. Run the script:
   ```bash
   python script.py
   ```
2. Enter the required regression parameters:
   - **P**: Number of predictors (including the intercept).
   - **n**: Number of data points.
   - **d**: Number of independent variables (excluding the intercept).
3. **Provide a CSV file** containing Cook’s Distance and Leverage values.
4. The script **automatically identifies and displays influential data points**.
---
## 📌 Example Output
```
 **Influential Data Points**
============================================================
Index     Cook’s Distance      Leverage         Status    
============================================================
3         0.90                0.50             Influential
5         1.10                0.45             Influential(i)
9         0.85                0.48             Influential(ii)
============================================================
```
✅ **If no influential points are found, the script will notify the user.**

---

## 📖 References
- (i) Kutner et al., 2004. *Applied Linear Statistical Models*  
- (ii) Fox, 2016. *Applied Regression Analysis and Generalized Linear Models*  

---
## 🚀 Upcoming Features
- **Computes Cook’s Distance** for each data point  
- **Compute Leverage values (Hat Matrix Diagonal)** for each data point
- **Visualization**: Plot influential points for better understanding.
- **Classification of High Cook’s Distance & High Leverage Points** (separately from influential points).
- **Batch Processing**: Analyze multiple datasets at once.
---
## 📌 Contributing
Contributions are welcome! If you’d like to improve this script, feel free to fork the repository and submit a pull request.
---
## 📌 License
This project is licensed under the **MIT License** – feel free to use and modify it.

```
