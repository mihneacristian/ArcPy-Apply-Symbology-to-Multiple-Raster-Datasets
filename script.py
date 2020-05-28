import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame

'''Create new Group'''
groupName = "New Group Layer"
allLayers = arcpy.mapping.ListLayers(mxd, groupName, df) [0]
for layer in allLayers: 
    arcpy.ApplySymbologyFromLayer_management(layer, "RASTER_NAME_+_EXTENSION")
