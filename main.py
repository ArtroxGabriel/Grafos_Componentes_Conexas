def dfs(ListaADJ, vertice, Visitados, Componentes):# Funcao de DFS
  Visitados.add(vertice)  # Adiciona o vertice na lista de visitados
  Componentes.add(vertice) # Adiciona o vertice na lista de componentes
  for N in ListaADJ[vertice]: # Para cada vizinho do vertice
    if N not in Visitados: 
      DFS(ListaADJ, N, Visitados, Componentes) 


def procurarconexas(ListaADJ): # Funcao que procura as componentes conexas
    VerticesVisitados = set()  # percorrera a lista e vera quem tem conexões
    Compenentes = []           # adicionando numa lista de componentes 
    for Vertice in ListaADJ:
        if Vertice not in VerticesVisitados:
            component = set()
            dfs(ListaADJ, Vertice, VerticesVisitados, component)  # chama a funcao de DFS
            Compenentes.append(component)
    return Compenentes  # retorna a lista de componentes

trash = input()  # trash: variavel descartavel
trash = input()  # ira pegar 1,2 e 4 linha junto ao "n=10"
trash, NumIndices = input().split("n=") #Pegar o numero de indices
NumIndices = int(NumIndices)
trash = input()

ListaADJ = {} # criando Lista de adjacencia
for aux in range(1, NumIndices+1):
  ListaADJ[aux] = [aux]


status = True
while status: # Pegar os valores de entrada
  try:        # das arestas, e lista-os com quem tem conexões, resumindo: um grafo
    aux1, aux2 = input().split(" ")
    ListaADJ[int(aux1)].append(int(aux2))
    ListaADJ[int(aux2)].append(int(aux1))
  except EOFError:
    status = False


saida = procurarconexas(ListaADJ)  

for aux in range(len(saida)): #SAIDA do programa
  print(" ".join(map(str, sorted(saida[aux]))))
