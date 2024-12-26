# Import essential libraries
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, mean_squared_error, r2_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras import layers, models
import dask_geopandas as dgpd
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

# ------------------- Simulating GeoSpatial Data for Various Topics -------------------
np.random.seed(42)

# Generate dummy geospatial data
n_samples = 2000  # Increase the size for large dataset simulation
data = {
    'Latitude': np.random.uniform(-90, 90, n_samples),
    'Longitude': np.random.uniform(-180, 180, n_samples),
    'Elevation': np.random.uniform(0, 3000, n_samples),
    'Soil_Type': np.random.choice([0, 1, 2], n_samples),  # 0: Sandy, 1: Clay, 2: Silt
    'Flood_Risk': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),  # 0: Low, 1: High
    'Traffic_Volume': np.random.uniform(50, 2000, n_samples),
    'Water_Quality': np.random.uniform(6.5, 8.5, n_samples)  # pH levels
}

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=[Point(xy) for xy in zip(data['Longitude'], data['Latitude'])])

# ------------------- Topic: Data Preprocessing -------------------
print("Cleaning and Preprocessing Data")

# Fill missing values (none in this case, but a placeholder)
gdf = gdf.fillna(gdf.mean())

# Encoding categorical data
gdf['Soil_Type_Encoded'] = gdf['Soil_Type']

# Splitting data into train-test sets
X = gdf[['Latitude', 'Longitude', 'Elevation', 'Soil_Type_Encoded']]
y = gdf['Flood_Risk']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------------- Topic: Building Machine Learning Models -------------------
print("Training Machine Learning Models")

# Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
print(f"Random Forest Accuracy: {rf_accuracy:.2f}")

# Support Vector Machine
svm_model = SVC(kernel='rbf', random_state=42)
svm_model.fit(X_train, y_train)
svm_predictions = svm_model.predict(X_test)
svm_accuracy = accuracy_score(y_test, svm_predictions)
print(f"SVM Accuracy: {svm_accuracy:.2f}")

# ------------------- Topic: Visualization -------------------
print("Visualizing Results")

# Actual vs Predicted Flood Risk
gdf_test = gdf.iloc[X_test.index]
gdf_test['Predicted_Risk'] = rf_predictions

fig, ax = plt.subplots(1, 2, figsize=(15, 8))

# Actual Flood Risk
gdf_test.plot(column='Flood_Risk', cmap='coolwarm', legend=True, ax=ax[0])
ax[0].set_title('Actual Flood Risk')

# Predicted Flood Risk
gdf_test.plot(column='Predicted_Risk', cmap='coolwarm', legend=True, ax=ax[1])
ax[1].set_title('Predicted Flood Risk')

plt.tight_layout()
plt.show()

# ------------------- Topic: Deep Learning with TensorFlow -------------------
print("Building a TensorFlow Model for Flood Risk Prediction")

# Normalizing Data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# TensorFlow Model
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the Model
history = model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the Model
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f"TensorFlow Model Accuracy: {accuracy:.2f}")

# ------------------- Topic: Working with Large Datasets -------------------
print("Using Dask for Large Datasets")

# Convert GeoDataFrame to Dask GeoDataFrame
dask_gdf = dgpd.from_geopandas(gdf, npartitions=4)
dask_gdf['Elevation_Scaled'] = dask_gdf['Elevation'] / 1000
dask_gdf = dask_gdf.compute()
print(dask_gdf.head())

# ------------------- Topic: Clustering -------------------
print("Performing K-Means Clustering")

kmeans = KMeans(n_clusters=3, random_state=42)
dask_gdf['Cluster'] = kmeans.fit_predict(dask_gdf[['Latitude', 'Longitude']])

plt.scatter(dask_gdf['Longitude'], dask_gdf['Latitude'], c=dask_gdf['Cluster'], cmap='viridis', alpha=0.5)
plt.title('K-Means Clustering')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

print("Script Execution Completed.")