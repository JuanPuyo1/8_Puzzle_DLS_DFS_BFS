#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Busquedas.py Es una API que se podra utilizar en diferentes proyectos que este en la misma ruta de esta
#con el fin de poder acceder a los metodos de construcción de las estructuras de datos usados en las 
#busquedas de solución informadas y no informadas

# Definición de la clase Tree (Árbol) para la contruccion de la estructura de un arbol de orden N

class Tree:
    def __init__(self, label, state, children=None):
        self.label = label
        self.state = state
        if children is not None:
            self.children  = children
        else:
            self.children=[]

    def __str__(self):
        return (str(self.label)+" "+str(self.state))
    
# Para la función de recorrido "pre-order" basta procesar el nodo visitado antes de recorrer recursivamente sus hijos, que luego serán procesados
    def preorder(self):
        if self is None: 
            return
        
        print(self)
        if len(self.children)>0:
            for child in self.children: 
                child.preorder()
        return

# Similarmente, el recorrido "post-order" se consigue explorando recursivamente los hijos de cada nodo visitado antes de procesarlo
    def postorder(self):
        if self is None: 
            return
        
        if len(self.children)>0:
            for child in self.children: 
                child.postorder()
        print(self.label)
        return
    
# El recorrido por niveles es análogo a los métodos en profundidad
    def levelorder(self):
        visit_queue=[]
        visit_queue.append(self)
 
        while (len(visit_queue)>0):
            print (visit_queue[0].data)
            node=visit_queue.pop(0) 
            if len(node.children)>0:
                for child in node.children:
                    visit_queue.append(child)
        return
    
# Definiremos la clase (State) para el manejo de estados que es nacesaria en la clase (Tree)
class State:
    def __init__(self, parent, cost=0, is_goal=False):
        self.parent = parent
        self.cost = cost
        self.is_goal  = is_goal
    
    def __str__(self):
        return str(self.cost)+" "+str(self.parent)+" "+str(self.is_goal)

# Definición de la clase StateGraph (Grafo) para construir la estructura de un grafo no dirigido
class StateGraph:
    def __init__(self,data=None,node_content=None):
        if data is None:
            self.data=[]
        else:
            self.data=data
        if node_content is None:
            self.node_content=[]
        else:
            self.node_content=node_content

    def getNodes(self):
        keys=list(self.data.keys())

        node_content=[]
        for key in keys:
            node_content.append(key)
        return node_content
    
    def getEdges(self):
        edge_names=[]
        for node in self.data:
            for next_node in self.data[node]:
                if (node,next_node) not in edge_names:
                    edge_names.append((node, next_node))
        return edge_names  
    
    
    def buscarClave(self,data,clave):
        claves = data.keys()
        a = 0
        for i in claves:
            if(clave == i):
                a = a+1
        if(a!=0):
            return True
        else:
            return False
        
    def agregarVertice(self,data,vertice):
        if (data == None):
            data[vertice] = []
        else:
            vali = StateGraph.buscarClave(self,data,vertice)
            if(vali):
                print("El vertice ya esta agregado")
            else:
                data[vertice] = []
            
    def agregarArista(self,data,clave,vertice,peso):
        vali = StateGraph.buscarClave(self,data,clave) 
        a =0
        if(vali == True):
            lista = data[clave]
            if(len(lista) > 0):
                for i in lista:
                    for j in i:
                        if(j != vertice):
                            a = a + 1
                            lista.append((vertice,peso))
                            return True
                    break
            else:
                lista.append((vertice,peso))
                return True
        else:
            print("No se encuentra la clave")
            
    def conversion(self,conver):
        
        if conver is not None:
            conversion = []
            for i in conver:
                #print(i[1][1])        
                #print(i[0])
                #print(i[1][0])
                a = (i[1][1],i[0],i[1][0])
                conversion.append(a)
            t = set(conversion)
            
            return t
        else:
            print("No hay contenido en el grafo")
        
        
    def conversion2(self, vertices, conver):
        from pprint import pprint
        dic = {}
        for i in vertices:
            dic[i]={}
            
        print(dic)
        
        #print(i[0]) clave
        #print(i[1][1]) peso
        #print(i[1][0]) union
        
        for i in conver:
            print(i)
            print(i[0])
            print(i[1][0])
            print(i[1][1])
            dic[i[0]][i[1][0]]=i[1][1]
            print("--------------------------------------------------------------------------")
            pprint(dic)
            print("*******-------------------------------------------------------------------")
        
    
    def union(self,vertices,aristas):
        dic = {'vertices':vertices,'aristas':aristas}
        return dic

