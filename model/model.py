import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.artists = []

        self.list_role = []
        self._nodes = []
        self._edges = []
        self.id_map = {}

        self.load_role()

    def classifica(self):
        pass

    def load_role(self):
        self.list_role = DAO.get_all_role()
        print(self.list_role)

    def get_all_categories(self):
        return DAO.get_all_categories()

    def load_artist(self, role):
        self.artist = DAO.get_artist(role)

    def build_graph(self, role: str):  # ricevo forna e anni
        self.G.clear()
        print(role)
        self.load_artist(role)
        for p in self.artist:  # per ogni stato nella lista
            self._nodes.append(p)  # lo aggiungo alla lista dei nodi
        self.G.add_nodes_from(self._nodes)  # aggiungo i nodi al grafo
        self.id_map = {}
        for n in self._nodes:  # per ogni nodo
            self.id_map[n.id] = n  # lo aggiungo al dizionario id_map con chiave l'id e valore il nodo
        tmp_edges = DAO.get_all_weighted_neigh(role)  # chiamo funz e passo forma e anni
        self._edges.clear()
        for e in tmp_edges:  # per ogni arco pesato
            self._edges.append((self.id_map[e[0]], self.id_map[e[1]], e[2]))
        # id_map[e[0]] è il primo nodo, e vado a prenderlo dentro id_map
        # id_map[e[1]] è il secondo nodo, e vado a prenderlo dentro id_map
        # e[2] è il peso dell'arco che unisce i due nodi
        self.G.add_weighted_edges_from(self._edges)