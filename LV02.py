
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

# Import geometry conversion extension methods
clr.ImportExtensions(Revit.GeometryConversion)

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from System.Collections.Generic import *

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

#Uncomment the line below to enable the first input
source_component_id = UnwrapElement(IN[0]).Id


# Collect all used wall types
all_walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()
used_types = set( [w.GetTypeId() for w in all_walls] )


# "Start" the transaction
TransactionManager.Instance.EnsureInTransaction(doc)

out = []
spacing = UnitUtils.ConvertToInternalUnits(1000, UnitTypeId.Millimeters)
for n, wall_type_id in enumerate(used_types):
    # copy/paste source element
    move = XYZ(spacing*(n+1), 0, 0)
    new_elem = ElementTransformUtils.CopyElement(doc, source_component_id, move)[0]
    new_elem = doc.GetElement(new_elem) # get the actual element
    
    # edit Type Component parameter
    par = new_elem.get_Parameter(BuiltInParameter.LEGEND_COMPONENT)
    par.Set(wall_type_id)
    
    # Collect new elements
    out.append(new_elem)

# "End" the transaction
TransactionManager.Instance.TransactionTaskDone()

#Uncomment the line below to output an object
OUT = out
