import os
import arcpy

# The workspace
ws = r"YOUR_WORKSPACE"
outfile = os.path.join(ws,"outdata","envelope.shp")

# WGS84 Bounds
outSR = arcpy.SpatialReference(4326)
coordinates = [-180,-90,180, 90]

LowerLeft = arcpy.Point(coordinates[0],coordinates[1])
LowerRight = arcpy.Point(coordinates[2],coordinates[1])
UpperLeft = arcpy.Point(coordinates[0],coordinates[3])
UpperRight = arcpy.Point(coordinates[2],coordinates[3])

# We create an array of Points
array = arcpy.Array()
array.add(LowerLeft)
array.add(LowerRight)
array.add(UpperRight)
array.add(UpperLeft)
array.add(LowerLeft)

# We create the Polygon
polygon = arcpy.Polygon(array)

# We save the result to the current workspace
arcpy.CopyFeatures_management(polygon, outfile)

# We define the output SR
arcpy.DefineProjection_management(outfile, outSR)