#%%
import os

#%%
class PARAM:
    """

    Args:
        cParam ([type]): [description]
    """

    def __init__(self):
        # @ PJT Root Path
        self.pjtRoot = os.path.join(os.getcwd())

        # @ Data TypeB
        self.dataType1 = "Data/TypeB"
        self.dataRype1Naem = "외부지표_vFFF.csv"
        self.type1Dtype = {"ITEM": str, "CATEGORY_SEGMENT1": str}

        # @ Data TypeA
        self.dataType2 = "Data/TypeA"

        return None


# %%
#
