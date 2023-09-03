from pydantic import BaseModel

class PatientRecord(BaseModel):
    Clump_Thickness:int
    Uniformity_of_Cell_Size:int
    Uniformity_of_Cell_Shape:int
    Marginal_Adhesion:int
    Single_Epithelial_Cell_Size:int
    Bare_Nuclei:int
    Bland_Chromatin:int
    Normal_Nucleoli:int
    Mitoses:int