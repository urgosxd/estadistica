import math

def cuart(lista=[]):
    cuartiles=[0,0,0]
    lista = sorted(lista)
    if len(lista)%2 ==0:
        middle=(len(lista)//2)-1
        print(middle)
        cuartiles[1]= (lista[middle]+ lista[middle+1])//2
        if middle%2==0:
            cuartiles[0]= lista[middle//2] + lista[(middle//2)+1]
            cuartiles[2]= lista[(middle*3)//2] + lista[(middle*3)//2]
        else:
            cuartiles[0]=lista[(middle//2)+1]
            cuartiles[2]=lista[((middle*3)//2)+1]
    else:
        middle=math.trunc(len(lista)/2)+1
        cuartiles[1]= lista[middle]
        if middle%2==0:
            cuartiles[0]=lista[middle//2]+lista[(middle//2)+1]
            cuartiles[2]= lista[(middle*3)//2] + lista[(middle*3)//2]
        else:
            cuartiles[0]=lista[(middle//2)+1]
            cuartiles[2]=lista[((middle*3)//2)+1]

    return lista,cuartiles


        
