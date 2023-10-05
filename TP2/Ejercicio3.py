cantidad = int(input("Ingrese la cantidad de notas a guardar: "))
notas = []


for i in range(cantidad):
    nota = float(input("Ingrese nota: "))
    notas.append(nota)


def NotaMax(notas):
    mAx = 0
    for nota in notas:
        if(nota > mAx):
            mAx = nota
    return (mAx)

def Pos(notas, mAx):
    pos = notas.index(mAx)
    return pos
                                    #mAx es out of scope asique la cite 2 veces.. arreglar?
print(NotaMax(notas), " " , Pos(notas, NotaMax(notas)))
        
        