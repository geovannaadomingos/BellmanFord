# Initializing the Graph Class
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = ['GRU', 'GIG', 'BSB', 'SSA', 'VCP', 'CNF', 'FOR', 'BEL', 'POA', 'CGB', 'MAO', 'SDU', 'CWB', 'GYN', 'RAO', 'FLN', 'VIX', 'UDI', 'AJU', 'MCZ', 'NAT', 'IGU', 'JPA', 'REC', 'SLZ', 'CGH', 'THE', 'BPS', 'MGF', 'PLU', 'IOS', 'LDB', 'CFB', 'SNZ', 'JOI', 'JTC', 'FLB', 'BYO', 'CPV', 'ARS', 'SMT', 'POJ', 'ATM', 'PHI', 'JRN',
                      'PIV', 'SSCI', 'CMT', 'CZS', 'MCP', 'MEA', 'TUZ', 'PTQ', 'LCB', 'OAL', 'QCN', 'GUJ', 'FEJ', 'JDO', 'JLS', 'NVT', 'TUR', 'DIQ', 'GMS', 'BSS', 'OTT', 'AAI', 'DNO', 'IJU', 'XAP', 'SSO', 'PNZ', 'QAR', 'ALQ', 'QAC', 'BVB', 'MII', 'SOD', 'VOT', 'QRE', 'ERM', 'FRC', 'BAT', 'PMW', 'IDO', 'NTM', 'CZB', 'CCM', 'RDC', 'CCI', 'RIA']

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def print(self):
        print(self.graph)

    # Implementing Bellman-Ford's Algorithm

    def bellmanFord(self, src):
        dist = {i: float("Inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.V-1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative cycle")
                return

        print("Distance of Vertex from Source")
        for key, value in dist.items():
            print('  ' + key, ' :    ', value)


grafo = Graph(93)

try:
    distancias = open("database.txt", "r")

    with distancias:
        for line in distancias:
            origem, destino, distancia = line.split()

            grafo.add_edge(origem, destino, float(distancia))

except FileNotFoundError as msg:
    print(msg)

grafo.bellmanFord("GRU")

# grafo.print()
