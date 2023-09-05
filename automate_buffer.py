import arcpy

arcpy.env.workspace = r"D:\SEM_III\Programming_3\p3_automated_scripts\Practical_3_ProProject\03_Automating_Scripts_With_Lists.gdb"
fc_list = arcpy.ListFeatureClasses()

print(fc_list)

for fc in fc_list:
    desc_obj = arcpy.Describe(fc)
    shape_type = desc_obj.shapeType

    # add buffer point: 500 ft, polyline: 1000 ft, polygon: 600 ft

    if shape_type == "Point":
        buffer_distance = "500 feet"
    elif shape_type == "Polyline":
        buffer_distance = "1000 feet"
    elif shape_type == "Polygon":
        buffer_distance = "600 feet"

    Output_buffer =fc + "_Buffer"
    arcpy.analysis.Buffer(fc,Output_buffer, buffer_distance)

print("process complete")


