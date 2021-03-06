# -*- coding: cp936 -*-

# ---------------------------------------------------------------------------
# LjTp.py
# Created on: 2015-01-06 15:43:16.00000
#   (generated by ArcGIS/ModelBuilder)
# Description:
'''
新建数据库
遍历工作空间里的shp文件
以shp文件名新建数据集，并向该数据集导入这个shp
对数据集创建拓扑                CreateTopology_management
向拓扑结构添加数据集里的shp      AddFeatureClassToTopology_management
向拓扑结构添加拓扑规则           AddRuleToTopology_management
验证拓扑                       ValidateTopology_management
'''
# ---------------------------------------------------------------------------

# Set the necessary product code
import arceditor
# Import arcpy module
import arcpy,os

arcpy.env.workspace = r"D:\0_PROJECTS\3_QingHai_MaDuo_Project\MaDuoNewBorderTask0107\data"

#坐标系
Coordinate_System = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;.001;.001;IsHighPrecision"

#数据库路径
GDB_Dir = r"D:\0_PROJECTS\3_QingHai_MaDuo_Project\MaDuoNewBorderTask0107\Result"
#数据库名称
File_GDB_Name = "MD_TP.gdb"
Geodatabase = os.path.join(GDB_Dir,File_GDB_Name)
print Geodatabase

#新建数据库
arcpy.CreateFileGDB_management(GDB_Dir, File_GDB_Name, "CURRENT")
print "start"

fcs = arcpy.ListFeatureClasses("*","All","")
for fc in fcs:
        out_dataset_path = Geodatabase
        out_name = str(fc[:-4])   #数据集名称
        print u"数据集名称:" + str(out_name)
        #创建数据集
        arcpy.CreateFeatureDataset_management(out_dataset_path, out_name, Coordinate_System)

        #向数据集导入shp
        in_features = fc  #导入的shp名称
        out_path = os.path.join(Geodatabase,out_name)   #shp导入的数据集位置
        print u"shp导入的数据集位置:" + str(out_path)
        out_name = str(fc[:-4]) + "_ToPo"    #导入后shp的名称
        print u"导入后shp的名称:" + str(out_name)
        arcpy.FeatureClassToFeatureClass_conversion (in_features, out_path, out_name)


        # Process: Create Topology
        Topo_name = str(fc[:-4]) + "_ToPology" #拓扑结构的名称
        print u"拓扑结构的名称:" + str(Topo_name)
        arcpy.CreateTopology_management(out_path, Topo_name, "")   #zhiduo_tp  拓扑结构

        # Process: Add Feature Class To Topology
        Topology = os.path.join(out_path,Topo_name)  # 拓扑结构的路径
        print u"拓扑结构的路径:" + str(Topology)
        ToPoShp = os.path.join(out_path,out_name)    # 要做拓扑的数据集里的shp
        print u"要做拓扑的数据集里的shp:" + str(ToPoShp)
        arcpy.AddFeatureClassToTopology_management(Topology, ToPoShp, "1", "1")

        # Process: Add Rule To Topology
        arcpy.AddRuleToTopology_management(Topology, "Must Not Have Gaps (Area)", ToPoShp, "", "", "")
        print u"正在添加 Must Not Have Gaps 规则"
        arcpy.AddRuleToTopology_management(Topology, "Must Not Overlap (Area)", ToPoShp, "", "", "")
        print u"正在添加 Must Not Overlap 规则"

        # Process: Validate Topology
        arcpy.ValidateTopology_management(Topology, "Full_Extent")

print "finish"


