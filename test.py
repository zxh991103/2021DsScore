





def changescore(io, sid,num, score):
    import pandas as pd
    s1 = pd.read_excel(io=io, header=0,index_col='sid')

    import numpy as np
    if str(num) not in s1.columns:
        s1[str(num)] = np.nan
    stlist=s1.index.tolist()
    res=""
    pf=False
    for i in range(len(stlist)):
        if sid==stlist[i]:
            s1.iloc[i,num] = score
            res=res+s1.iloc[i,0]+" "+str(stlist[i])+" "+"ex"+str(num)+" "+str(score)+" points"
            pf=True
            break
    

    s1.to_excel(io)
    if pf:
        return res
    else:
        return "No this sid"

