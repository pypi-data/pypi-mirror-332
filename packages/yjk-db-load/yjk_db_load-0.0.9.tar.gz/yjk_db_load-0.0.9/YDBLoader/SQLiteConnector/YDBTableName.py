from enum import Enum
ID = "ID"
STD_FLR_ID = "StdFlrID"
JOINT_ID = "JtID"
SECTION_ID = "SectID"
ECC_X = "EccX"
ECC_Y = "EccY"
ROTATION = "Rotation"


class YDBTableName():
    JOINT_TABLE_NAME = "tblJoint"
    JOINT_TABLE_USEFUL_COLUMNS = [ID,"X","Y",STD_FLR_ID]

    COLUMN_SECTION_TABLE_NAME = "tblColSect"
    COLUMN_SECTION_TABLE_USEFUL_COLUMNS = [ID,"Mat","Kind","ShapeVal"]

    COLUMN_TABLE_NAME = "tblColSeg"
    COLUMN_TABLE_USEFUL_COLUMNS = [ID,JOINT_ID,SECTION_ID,ECC_X,ECC_Y,ROTATION]


    RESULT_PERIOD_TABLE = "calEigenInf"
    RESULT_PERIOD_USEFUL_COLUMNS = ["ModuleID","EigenNo","Period","Angle","CoeffInf","mInf"]

