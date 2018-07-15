# -*- coding: cp936 -*-

# ---------------------------------------------------------------------------
# daochu.py
# Created on: 2015-01-09 13:56:05.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 将数据库里的数据集里的要素转出来，转成shp
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy,os


# Local variables:
arcpy.env.workspace = r"G:\maduo_2.gdb"
gdb = r"G:\maduo_2.gdb"
fds = arcpy.ListDatasets("*","All")
print fds
Result_Topo = r"G:\d2shp"

print "start"
for fd in fds:
        print fd
        fd_path = os.path.join(gdb,fd)
        #arcpy.env.workspace = fd_path
        arcpy.env.workspace = gdb + "\\" + fd
        fcs = arcpy.ListFeatureClasses("*","All")
        for fc in fcs:
                print "fc" + str(fc)

                Input_Features = fc
                outname = str(fcs)
                Output_Folder = Result_Topo

                # Process: Feature Class To Shapefile (multiple)
                arcpy.FeatureClassToShapefile_conversion(Input_Features, Output_Folder)
                print ""

#rename
arcpy.env.workspace = Result_Topo
Fcs = arcpy.ListFeatureClasses("*","All")
for Fc in  Fcs:
        out_data = str(Fc[:-9])
        arcpy.Rename_management(Fc, out_data)

                
print "finish"

