import pandas as pd
import math
def R_(obj):
    return obj.max() - obj.min()

def K_(total):
    k = math.log(total,10)*3.32 + 1
    return int(round(k,0))
def A_(dat1,dat2):
    k = dat1/dat2
    if isinstance(k,int):
        return dat1//dat2
    else:
        return round(k,0)
