import numpy as np
import rasterio
import matplotlib.pyplot as plt
from pylandsat import Scene

# Access data
scene = Scene('data/LE07_L1TP_205050_19991104_20170216_01_T1')
print(scene.available_bands())
print(scene.product_id)
print(scene.sensor)
print(scene.date)

# Access MTL metadata
print(scene.mtl['IMAGE_ATTRIBUTES']['CLOUD_COVER_LAND'])

# Quality band
plt.imshow(scene.quality.read())

# Access band data
nir = scene.nir.read(1)
red = scene.red.read(1)
ndvi = (nir + red) / (nir - red)

# Access band metadata
print(scene.nir.bname)
print(scene.nir.fname)
print(scene.nir.profile)
print(scene.nir.width, scene.nir.height)
print(scene.nir.crs)

# Use reflectance values instead of DN
nir = scene.nir.to_reflectance()

# ..or brightness temperature
tirs = scene.tirs.to_brightness_temperature()

# Save file to disk
with rasterio.open('temperature.tif', 'w', **scene.tirs.profile) as dst:
    dst.write(tirs, 1)