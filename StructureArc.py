"""Created on Thu Feb 18 19:57:50 2021@author: abdoumahamadouzakariyaou"""import data1 as PiscinePatinoireCampus import data2 as PoisyParcDesGlaisinsimport networkximport matplotlib.pyplot as pltclass Graphe():    def __init__(self, graph_dict=None):        if graph_dict == None:            graph_dict = {}        self.__graph_dict = graph_dict      # Fonction retournant tous les chemins entre deux noeuds     def find_all_paths(self, start_node, end_node, path=[]):        graph = self.__graph_dict         path = path + [start_node]        if start_node == end_node:            return [path]        if start_node not in graph:            return []        paths = []        for node in graph[start_node]:            if node not in path:                extended_paths = self.find_all_paths(node, end_node, path)                for p in extended_paths:                     paths.append(p)        return paths                    """  C'est la premiere structure qui ne permettait pas d'avoir un fastest  class BUS():        def __init__(self,Numeroligne,direction,listeArret=[]):        self.Numeroligne=Numeroligne        self.direction=direction        self.listeArret=listeArret    def getdirection(self):        return self.direction    def getNumeroligne(self):        return self.Numeroligne    def getlisteArrect(self):        arret=[]        name1 = PiscinePatinoireCampus.regular_path.split(" N ")        name2 = PoisyParcDesGlaisins.regular_path.split(" N ")        if self.direction==PiscinePatinoireCampus:            if self.Numeroligne==2:                name1=name1[::-1]            for a in name1:                arret.append(a)        if self.direction==PoisyParcDesGlaisins:            if self.Numeroligne==2:                name2=name2[::-1]            for a in name2:                arret.append(a)         return arret    def setdirection(direction):        self.direction=direction    def setNumero(Numero):        self.Numeroligne=Numero    def setlisteArret(Nouvelleliste):        self.listeArret=Nouvellelisteprint("---------testclass Bus-----------------")a=BUS(1,PiscinePatinoireCampus)b=a.getlisteArrect()print(b)print("--------------------------")"""