# @Bob Booth - https://www.esri.com/arcgis-blog/products/arcgis-desktop/defense/determining-a-z-factor-for-scaling-linear-elevation-units-to-match-geographic-coordinate-values/
# Determining a Z-factor for scaling linear elevation units to match geographic coordinate values
import arcpy
import math

dataset = r"IN_RASTER_DATASET"

desc = arcpy.Describe(dataset)
extent = desc.Extent
spatial_ref = desc.spatialReference

if spatial_ref.type == "Geographic":
    left,bottom,right,top= [extent.XMin,extent.YMin,extent.XMax,extent.YMax]
    
    if (top > bottom):
        height = (top - bottom)
        mid = (height/2) + bottom
    elif (top < bottom):
        height = bottom - top
        mid = (height/2) + top
    else:
        mid = top
    
    spatial_reference = desc.SpatialReference
    semi_major_axis = spatial_reference.semiMajorAxis
    
    a = 1.0
    b = ((2.0 * math.pi * float(semi_major_axis))/360.0)
    c = math.cos(math.radians(mid))
    zfactor = abs(a/(b * c))
    
    print("%06f" % zfactor)