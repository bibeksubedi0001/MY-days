import geopandas as gpd
import rasterio
from rasterio.features import rasterize
from rasterio.transform import from_bounds

# Load the shapefile using geopandas
shapefile_path = r"C:\Users\Bibek\Documents\ArcGIS\Data For GIS Training\Nepal Adm\Country Level 1\Level_1.shp"
nepal = gpd.read_file(shapefile_path)

# Set the resolution of the raster (e.g., 0.01 degree per pixel)
pixel_size = 0.01

# Calculate the bounds of the shapefile (xmin, ymin, xmax, ymax)
minx, miny, maxx, maxy = nepal.total_bounds

# Define the transform (affine transformation) and calculate the width and height
transform = from_bounds(minx, miny, maxx, maxy, int((maxx - minx) / pixel_size), int((maxy - miny) / pixel_size))

# Set raster dimensions
out_shape = (int((maxy - miny) / pixel_size), int((maxx - minx) / pixel_size))

# Rasterize the geometries
raster = rasterize(
    [(geom, 1) for geom in nepal.geometry],  # Convert geometries to raster format
    out_shape=out_shape,
    transform=transform,
    fill=0,  # Value for pixels not covered by the geometries
    dtype='uint8'
)

# Write the raster to a file using rasterio
with rasterio.open(
    "nepal_raster.tif",
    "w",
    driver="GTiff",
    height=raster.shape[0],
    width=raster.shape[1],
    count=1,
    dtype=raster.dtype,
    crs=nepal.crs,
    transform=transform,
) as dst:
    dst.write(raster, 1)

print("Raster file saved as 'nepal_raster.tif'")
with rasterio.open(
    r"C:\Users\Bibek\Documents\ArcGIS\Data For GIS Training\Nepal Adm\Country Level 1\nepal_raster.tif",  # Specify the full file path
    "w",
    driver="GTiff",
    height=raster.shape[0],
    width=raster.shape[1],
    count=1,
    dtype=raster.dtype,
    crs=nepal.crs,
    transform=transform,
) as dst:
    dst.write(raster, 1)