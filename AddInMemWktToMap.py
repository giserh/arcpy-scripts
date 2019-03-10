''' Run this code from within Arcgis Desktop '''

import arcpy

# Create a new Geometry object from WKT.
wkt_point = arcpy.FromWKT("POINT (0 0)")

# Add the new Geometry to Map
arcpy.CopyFeatures_management(wkt_point, r"in_memory\wkt_point")