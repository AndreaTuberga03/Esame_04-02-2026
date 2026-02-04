import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        pass

    def handle_classifica(self, e):
        pass

    def popola_dd(self):
        list_role1 = self._model.list_role
        for role in list_role1:
            print(role)
            self._view.dd_ruolo.options.append(ft.dropdown.Option(role))

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        selected_role = int(self._view.dd_ruolo.value)
        # Controllo che abbia un valore
        if selected_role is None:
            self._view.show_alert("Ruolo Invalida")
            return
        # Pulisce area risultato
        self._view.lista_visualizzazione_1.controls.clear()
        # Costruisce grafo con i parametri selezionati
        self._model.build_graph(selected_role)
        # Mostra info grafo
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(
                f"Numero di vertici: {self._model.get_num_of_nodes()} "
                f"Numero di archi: {self._model.get_num_of_edges()}"
            )
        )
        # Mostra somma pesi per nodo
        for node_info in self._model.get_sum_weight_per_node():
            self._view.lista_visualizzazione_1.controls.append(
                ft.Text(f"Nodo {node_info[0]}, somma pesi su archi = {node_info[1]}")
            )
        self._view.update()