import ee 

ee.Authenticate()
ee.Initialize()

image = ee.Image('LANDSAT/LE07/C01/T1_SR/LE07_044034_19990707')

print(type(image))