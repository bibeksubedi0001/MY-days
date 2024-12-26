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