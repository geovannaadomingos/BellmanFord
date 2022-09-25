class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = []
        self.nos = ['GMS', 'BVB', 'CCI', 'BAT', 'SOD', 'RAO', 'CWB', 'JOI', 'UDI', 'POJ', 'IJU', 'JTC', 'DIQ', 'MCZ',
                      'ERM', 'FLB', 'TUR', 'BPS', 'IDO', 'CCM', 'BSS', 'SDU', 'CMT', 'MEA', 'PTQ', 'QCP', 'VCP', 'LDB',
                      'PMW', 'CGB', 'RIA', 'MGF', 'CZB', 'PNZ', 'GRU', 'MII', 'JLS', 'NAT', 'NVT', 'SLZ', 'FOR', 'ARS',
                      'AJU', 'CGR', 'CFB', 'JPA', 'LCB', 'IOS', 'CGH', 'ATM', 'VOT', 'GUJ', 'BYO', 'THE', 'MCP', 'SSA',
                      'GYN', 'AAI', 'GIG', 'QAC', 'CZS', 'PIV', 'SMT', 'POA', 'FLN', 'SNZ', 'IGU', 'RDC', 'OYK', 'CNF',
                      'TUZ', 'OAL', 'JDO', 'MAO', 'ALQ', 'XAP', 'FEJ', 'REC', 'OTT', 'QCN', 'PLU', 'JRN', 'BEL', 'DNO',
                      'FRC', 'PHI', 'SSO', 'BSB', 'CPV', 'TRQ', 'VIX']

    def adicionar_aresta(self, inicio, fim, peso):
        self.grafo.append([inicio, fim, peso])

    def mostrar_todos_aeroportos(self, distancia, origem):
        for chave, valor in distancia.items():
            if valor != float("Inf") and valor != 0:
                print(origem + ' ---> ' + chave, ':', f'{valor:.2f} Km')

    def bellman_ford(self, inicio, final=''):
        if (inicio in self.nos) and ((final == '') or (final in self.nos)):
            origem = inicio
            distancia = {i: float("Inf") for i in self.nos}
            distancia[inicio] = 0
            for _ in range(self.vertices - 1):
                for inicio, fim, peso in self.grafo:
                    if distancia[inicio] != float("Inf") and distancia[inicio] + peso < distancia[fim]:
                        distancia[fim] = distancia[inicio] + peso
            for inicio, fim, peso in self.grafo:
                if distancia[inicio] != float("Inf") and distancia[inicio] + peso < distancia[fim]:
                    return
            if final == '':
                print("Distância em Km entre os aeroportos")
                self.mostrar_todos_aeroportos(distancia, origem)
            else:
                print(f'Distância em Km entre os aeroportos {origem} e {final}.')
                print(f'{origem} ---> {final} : {distancia[final]:.2f} Km')
        else:
            print('Parâmetros inválidos!')


grafo = Graph(93)

try:
    distancias = open("database.txt", "r")

    with distancias:
        for linha in distancias:
            origem, destino, distancia = linha.split()

            grafo.adicionar_aresta(origem, destino, float(distancia))

except FileNotFoundError as msg:
    print(msg)

grafo.bellman_ford("GRU")
