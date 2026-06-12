# Task 1: Exploring and Visualizing the Iris Dataset

## Objective
Load, inspect, and visualize the Iris dataset to understand
data trends, feature distributions, and relationships between
measurements across three flower species.

## Dataset
- **Name:** Iris Dataset
- **File:** `Iris.csv` (uploaded manually via Google Colab)
- **Loaded with:** `iris = pd.read_csv('Iris.csv')`
- **Size:** 150 rows × 6 columns
- **Columns:** Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species
- **Classes:** Iris-setosa, Iris-versicolor, Iris-virginica (50 samples each)
- **Missing values:** None — all 150 entries are complete

## Libraries Used
| Library | Purpose |
|---------|---------|
| `pandas` | Loading, inspecting, and summarizing the dataset |
| `seaborn` | Creating scatter plots, histograms, and box plots |
| `matplotlib` | Rendering and customizing all charts |

## Steps Performed
1. Uploaded `Iris.csv` using `google.colab.files.upload()` and loaded with pandas
2. Inspected dataset shape — confirmed 150 rows and 6 columns using `.shape`
3. Listed column names using `.columns`
4. Previewed first 5 rows using `.head(5)`
5. Checked data types and missing values using `.info()` and `.isnull().sum()`
6. Generated summary statistics using `.describe()`
7. Created a **scatter plot** — PetalLengthCm vs PetalWidthCm, colored by Species
8. Created **histograms** — distribution of all 4 features with KDE curves, in a 2×2 grid
9. Created **box plots** — all 4 features grouped by Species, in a 2×2 grid

## Key Results and Findings
- **No missing values** found across all 6 columns
- **Petal dimensions are strongly correlated** — petal length increases as petal
  width increases, visible clearly in the scatter plot
- **Iris-setosa is linearly separable** from the other two species based on
  petal measurements alone
- **Sepal measurements overlap** more between species, making them weaker
  separators than petal measurements
- **Petal length** has the widest range (1.0 cm to 6.9 cm) and highest
  standard deviation (1.76), indicating the most variation across species
- **SepalWidthCm** shows the most overlap between species in histograms —
  distributions of all three species cluster around similar values
- Box plots confirm **Iris-setosa has notably smaller petals** compared to
  Iris-versicolor and Iris-virginica

## Files
| File | Description |
|------|-------------|
| `Iris_Analysis.ipynb` | Main notebook with all code, outputs, and charts |
| `Iris.csv` | Raw dataset uploaded to Colab session |

## How to Run
1. Open `Iris_Analysis.ipynb` in [Google Colab](https://colab.research.google.com)
2. Upload `Iris.csv` when prompted by the file upload cell
3. Run all cells top to bottom — Runtime → Run all
