import arcpy
import os
import sys
class ToolValidator(object):
  """Class for validating a tool's parameter values and controlling
  the behavior of the tool's dialog."""

  def __init__(self):
    """Setup arcpy and the list of tool parameters."""
    self.params = arcpy.GetParameterInfo()
    self.current_path = sys.argv[0]
    self.sdefile = os.path.join(self.current_path, "vector.sde")
    self.project = os.path.join(self.sdefile, 'SDE.PROJECT')
    self.fields = ['PRODUCT_TY', 'LOCATION', 'PRJ_ID', 'PRO_YEAR', 'RESOLUTION', 'PRJ_NAME']

  def initializeParameters(self):
    """Refine the properties of a tool's parameters.  This method is
    called when the tool is opened."""
    cur = arcpy.da.SearchCursor(self.project, self.fields)
    self.prj_list = []
    for row in cur:
        self.prj_id_name = row[2] + "--" + row[5]
        self.prj_list.append(self.prj_id_name)
    self.params[0].filter.list = self.prj_list
    return

  def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""
    return

  def updateMessages(self):
    """Modify the messages created by internal validation for each tool
    parameter.  This method is called after internal validation."""
    return