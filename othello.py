from typing import List


numDisck=32
BIANCO=1
NERO=-1
#Da A a H e da 1 a 8
class Posizione:
    lettera=None #colonna
    numero=-1 #riga

    def __init__(self, colonna:str, riga:int):
        self.lettera=int.from_bytes(bytes(colonna,'utf-8')) 
        if self.lettera>=65 and self.lettera<=72: 
            self.lettera=self.lettera%65
        else: 
            self.lettera=None
        self.numero=riga
        if self.numero<0 or self.numero>7: 
            self.numero=None
    
    def __str__(self):
        return f"({self.lettera}, {self.numero})"
    
    def indexPosizione(self):
        return 8*self.numero+self.lettera

class Pedina:
    posizione=None
    colore=0

    def __init__(self, pos:Posizione, col:int):
        if pos!=None:
            self.posizione=pos
        else: raise Exception("Posizione==None")
        if col==-1 or col==1:
            self.colore=col
        else: self.colore=0 #raise Exception("Colore!=1 and Colore!=1") 
    
    def __str__(self):
        return f"({self.posizione}, {self.colore})"

class ListaPedine:
    pedina=None
    next=None 
    prev=None 

    def __init__(self,p:Pedina,n:Pedina):
        self.pedina=p 
        self.next=n 
        if(n!=None):
            n.prev=self 
    
    def __str__(self):
        return self.pedina.__str__()+", "+str(id(self.next)) 

class Giocatore:
    headLista=None

    def __init__(self):
        pass

    def __str__(self):
        stringa=""
        lista=self.headLista
        while(lista is not None):
            stringa+="-"+lista.pedina.__str__()
            #stringa+="-"+lista.__str__()+"\n"
            lista=lista.next 
        return stringa

    def addPedina(self,pedina:Pedina):
        #print("Giocatore-"+str(id(self.headLista)))
        #print(pedina)
        self.headLista=ListaPedine(pedina,self.headLista)
        #print("Giocatore-"+str(id(self.headLista)))
    
    def removePedina(self,pedina:Pedina)->Pedina:
        retPedina=None
        lista=self.headLista
        while(lista is not None): 
            if(lista.pedina.posizione.indexPosizione()==pedina.posizione.indexPosizione()): 
                retPedina=lista.pedina
                if(lista.prev is None):
                    self.headLista=lista.next
                elif(lista.next is None):
                    lista.prev.next=lista.next
                else:
                    lista.next.prev=lista.prev
                    lista.prev.next=lista.next
            lista=lista.next
        return retPedina

class Tabellone:
    celle=[]

    def __init__(self): 
        for colonna in ["A","B","C","D","E","F","G","H"]:
            for riga in range(8):
                self.celle.append(Pedina(Posizione(colonna,riga),0))
    
    def __str__(self):
        stringa=""
        for i in range(len(self.celle)):
            stringa=stringa+str(self.celle[i])
            if(i!=0 and (i+1)%8==0):
                stringa=stringa+"\n"
        return stringa 
    
    def addPedina(self, pos:Posizione, colGiocatore:int):
        print(pos)
        for pedina in self.celle:
            if pedina.posizione.indexPosizione()==pos.indexPosizione():
                pedina.colore=colGiocatore

def posizioniDisponibili(pedineGiocatore:List[Pedina])->List[int]:
    for pedina in pedineGiocatore:
        print(pedina)

def main(): 
    tabellone=Tabellone()  
    tabellone.addPedina(Posizione("D",3),BIANCO)
    tabellone.addPedina(Posizione("E",4),BIANCO)
    tabellone.addPedina(Posizione("D",4),NERO)
    tabellone.addPedina(Posizione("E",3),NERO) 
    print("Tabellone")
    print(tabellone)

def unused():
    print("Hello World!")
    print(int.from_bytes(bytes("A",'utf-8'))%65)
    print(int.from_bytes(bytes("H",'utf-8'))%65) 

    posizione=Posizione("A",0)
    print(posizione) 
    #tabellone.addPedina(Pedina(Posizione("D",3),BIANCO))
    #tabellone.aggiungiPedina(Pedina(Posizione("E",4),BIANCO))
    #tabellone.aggiungiPedina(Pedina(Posizione("D",4),NERO))
    #tabellone.aggiungiPedina(Pedina(Posizione("E",3),NERO)) 

    tabellone2=Giocatore()
    tabellone2.addPedina(Pedina(Posizione("D",3),BIANCO))
    tabellone2.addPedina(Pedina(Posizione("E",4),BIANCO))
    tabellone2.addPedina(Pedina(Posizione("D",4),NERO))
    tabellone2.addPedina(Pedina(Posizione("E",3),NERO))
    print("Tabellone")
    print(tabellone2)

    giocatoreB=Giocatore() 
    giocatoreB.addPedina(Pedina(Posizione("D",3),BIANCO))
    giocatoreB.addPedina(Pedina(Posizione("E",4),BIANCO))
    print("Giocatore Bianco")
    print(giocatoreB)
    
    giocatoreN=Giocatore() 
    giocatoreN.addPedina(Pedina(Posizione("D",4),NERO))
    giocatoreN.addPedina(Pedina(Posizione("E",3),NERO))
    print("Giocatore Nero")
    print(giocatoreN)
    print("Giocatore Nero removePedina")
    print(giocatoreN.removePedina(Pedina(Posizione("D",4),NERO)))
    print("Giocatore Nero")
    print(giocatoreN)   

if __name__ == "__main__":
    main()

