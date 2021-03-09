import math as mt
def Varianza(args):
    media = args.mean()
    suma=0
    for i in args:
        suma+=(i-media)**2
    return suma/(len(args)-1)
def Coeficiente(args):
    ll = Varianza(args)
    ll = round(ll,2)
    l = mt.sqrt(ll)
    l = round(l,2)
    return (l/args.mean())*100
