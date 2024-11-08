import statistics

# Sample data sets for demonstration
data = [2, 3, 5, 7, 9, 11, 13, 15, 15, 17, 20, 25, 30]
grouped_data = [1, 2, 2, 4, 5, 6, 7, 8, 9, 10]
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Displaying datasets
print("Data:", data)
print("Grouped Data:", grouped_data)
print("Weights:", weights)

# 1. Harmonic Mean
try:
    harmonic_mean = statistics.harmonic_mean(data)
    print(f"Harmonic Mean: {harmonic_mean}")
except statistics.StatisticsError as e:
    print(f"Harmonic Mean Error: {e}")

# 2. Arithmetic Mean (Average)
mean = statistics.mean(data)
print(f"Mean: {mean}")

# 3. Weighted Mean
weighted_mean = sum(x * w for x, w in zip(data, weights)) / sum(weights)
print(f"Weighted Mean: {weighted_mean}")

# 4. Median and Variants
median = statistics.median(data)
print(f"Median: {median}")

median_grouped = statistics.median_grouped(grouped_data)
print(f"Median Grouped: {median_grouped}")

median_high = statistics.median_high(data)
print(f"Median High: {median_high}")

median_low = statistics.median_low(data)
print(f"Median Low: {median_low}")

# 5. Mode and Handling Multi-Modal Data
try:
    mode = statistics.mode(data)
    print(f"Mode: {mode}")
except statistics.StatisticsError as e:
    print(f"Mode Error: {e}")

# Handling potential multimodal data with multiple modes
from collections import Counter
data_count = Counter(data)
modes = [k for k, v in data_count.items() if v == max(data_count.values())]
print(f"Modes (handling multi-modal data): {modes}")

# 6. Standard Deviation and Variance
pstdev = statistics.pstdev(data)
print(f"Population Standard Deviation (pstdev): {pstdev}")

stdev = statistics.stdev(data)
print(f"Sample Standard Deviation (stdev): {stdev}")

pvariance = statistics.pvariance(data)
print(f"Population Variance (pvariance): {pvariance}")

variance = statistics.variance(data)
print(f"Sample Variance (variance): {variance}")

# 7. Custom Outlier Detection (e.g., using 1.5 IQR rule)
def detect_outliers(data):
    Q1 = statistics.median_low(data)
    Q3 = statistics.median_high(data)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return [x for x in data if x < lower_bound or x > upper_bound]

outliers = detect_outliers(data)
print(f"Outliers: {outliers}")

# 8. Central Tendency Summary
def central_tendency_summary(data):
    return {
        "Mean": statistics.mean(data),
        "Median": statistics.median(data),
        "Mode": statistics.mode(data) if len(modes) == 1 else "No unique mode",
        "Harmonic Mean": statistics.harmonic_mean(data) if all(x > 0 for x in data) else "N/A for zero/negative values"
    }

summary = central_tendency_summary(data)
print("\nCentral Tendency Summary:")
for k, v in summary.items():
    print(f"{k}: {v}")

# 9. Correlation between Data and Weights (if applicable)
if len(data) == len(weights):
    # Compute covariance for context
    mean_data = statistics.mean(data)
    mean_weights = statistics.mean(weights)
    covariance = sum((x - mean_data) * (w - mean_weights) for x, w in zip(data, weights)) / (len(data) - 1)
    print(f"Covariance between data and weights: {covariance}")

    # Pearson correlation coefficient
    stddev_data = statistics.stdev(data)
    stddev_weights = statistics.stdev(weights)
    correlation = covariance / (stddev_data * stddev_weights)
    print(f"Correlation (Pearson) between data and weights: {correlation}")

# 10. Displaying Quartiles and Additional Statistics
def quartiles(data):
    data_sorted = sorted(data)
    Q1 = statistics.median_low(data_sorted[:len(data_sorted)//2])
    Q2 = statistics.median(data_sorted)
    Q3 = statistics.median_high(data_sorted[len(data_sorted)//2:])
    return Q1, Q2, Q3

Q1, Q2, Q3 = quartiles(data)
print(f"\nQuartiles:\nQ1 (25th percentile): {Q1}\nQ2 (Median): {Q2}\nQ3 (75th percentile): {Q3}")

# Summary of calculated values
print("\nSummary of Statistics:")
print(f"Arithmetic Mean: {mean}")
print(f"Weighted Mean: {weighted_mean}")
print(f"Median: {median}")
print(f"Mode(s): {modes}")
print(f"Standard Deviation (Sample): {stdev}")
print(f"Variance (Sample): {variance}")
print(f"Population Standard Deviation: {pstdev}")
print(f"Population Variance: {pvariance}")
print(f"Outliers: {outliers}")
