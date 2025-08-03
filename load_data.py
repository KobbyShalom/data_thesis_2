# LOAD PROCESSED DATA FOR P-MEDIAN ANALYSIS

import pickle
import numpy as np
import rasterio
import geopandas as gpd

print("=== LOADING PROCESSED DATA ===")

# Load raster data
with rasterio.open("processed_data/population_1km_utm.tif") as src:
    pop_data_utm = src.read(1)
    pop_transform = src.transform
    pop_crs = src.crs

with rasterio.open("processed_data/malaria_1km_utm.tif") as src:
    malaria_data_utm = src.read(1)

# Load vector data  
hospitals_utm = gpd.read_file("processed_data/hospitals_utm.geojson")
regions_utm = gpd.read_file("processed_data/regions_utm.geojson")
districts_utm = gpd.read_file("processed_data/districts_utm.geojson")

# Load grid parameters
with open("processed_data/grid_parameters.pkl", "rb") as f:
    grid_params = pickle.load(f)

# Load summary
with open("processed_data/data_summary.pkl", "rb") as f:
    data_summary = pickle.load(f)

print("✅ All data loaded successfully!")
print(f"Population grid: {pop_data_utm.shape}")
print(f"Malaria grid: {malaria_data_utm.shape}") 
print(f"Hospitals: {len(hospitals_utm)} facilities")
print(f"CRS: {pop_crs}")
