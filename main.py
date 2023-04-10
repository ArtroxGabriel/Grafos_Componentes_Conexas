
def DFS(ListaADJ, vertice, Visitados, Componentes):
  Visitados.add(vertice)
  Componentes.add(vertice)
  for N in ListaADJ[vertice]:
    if N not in Visitados:
      DFS(ListaADJ, N, Visitados, Componentes)


def ProcurarConexas(ListaADJ):
    VerticesVisitados = set()
    Compenentes = []
    for Vertice in ListaADJ:
        if Vertice not in VerticesVisitados:
            component = set()
            DFS(ListaADJ, Vertice, VerticesVisitados, component)
            Compenentes.append(component)
    return Compenentes

trash = input()  # trash: variavel descartavel
trash = input()
trash, NumIndices = input().split("n=")
NumIndices = int(NumIndices)
trash = input()

status = True
ListaADJ = {}
for aux in range(1, NumIndices+1):
  ListaADJ[aux] = [aux]

while status: #Pegar os valores de entrada
  try:
    aux1, aux2 = input().split(" ")
    ListaADJ[int(aux1)].append(int(aux2))
    ListaADJ[int(aux2)].append(int(aux1))
  except EOFError:
    status = False

saida = ProcurarConexas(ListaADJ)  

for aux in range(len(saida)): #SAIDA do programa
  print(" ".join(map(str, sorted(saida[aux]))))