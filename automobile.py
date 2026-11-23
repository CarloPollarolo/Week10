

class Automobile:
    def __init__(self, t, m, c):
        self._targa = t
        self._modello = m
        self.colore = c

    def __str__(self):
        print(self._targa)

    # Serve questo metodo per poter usare Automobile come nodo di un grafo
    def __hash__(self):
        return hash(self._targa)