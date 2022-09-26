from js import alert
# import networkx as nx
# import matplotlib.pyplot as plt


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.nos = ['GMS', 'BVB', 'CCI', 'BAT', 'SOD', 'RAO', 'CWB', 'JOI', 'UDI', 'POJ', 'IJU', 'JTC', 'DIQ', 'MCZ',
                    'ERM', 'FLB', 'TUR', 'BPS', 'IDO', 'CCM', 'BSS', 'SDU', 'CMT', 'MEA', 'PTQ', 'QCP', 'VCP', 'LDB',
                    'PMW', 'CGB', 'RIA', 'MGF', 'CZB', 'PNZ', 'GRU', 'MII', 'JLS', 'NAT', 'NVT', 'SLZ', 'FOR', 'ARS',
                    'AJU', 'CGR', 'CFB', 'JPA', 'LCB', 'IOS', 'CGH', 'ATM', 'VOT', 'GUJ', 'BYO', 'THE', 'MCP', 'SSA',
                    'GYN', 'AAI', 'GIG', 'QAC', 'CZS', 'PIV', 'SMT', 'POA', 'FLN', 'SNZ', 'IGU', 'RDC', 'OYK', 'CNF',
                    'TUZ', 'OAL', 'JDO', 'MAO', 'ALQ', 'XAP', 'FEJ', 'REC', 'OTT', 'QCN', 'PLU', 'JRN', 'BEL', 'DNO',
                    'FRC', 'PHI', 'SSO', 'BSB', 'CPV', 'TRQ', 'VIX']

        self.grafo = [['GRU', 'GIG', 336.78], ['GRU', 'BSB', 854.83], ['GRU', 'SSA', 1452.09], ['GRU', 'CNF', 496.44], ['GRU', 'CWB', 359.08], ['GRU', 'POA', 865.54], ['BSB', 'SSA', 1084.7], ['GIG', 'SSA', 1217.85], ['GIG', 'VCP', 398.39], ['BSB', 'VCP', 797.96], ['BSB', 'CNF', 590.87], ['GIG', 'CNF', 362.0], ['GRU', 'FOR', 2346.48], ['GRU', 'REC', 2100.71], ['GRU', 'BEL', 2461.92], ['GRU', 'CGB', 1329.47], ['GRU', 'MAO', 2697.33], ['BSB', 'CGH', 872.56], ['GIG', 'CGH', 359.65], ['GRU', 'SDU', 343.33], ['SSA', 'VCP', 1458.25], ['SSA', 'CNF', 959.52], ['VCP', 'CNF', 498.75], ['BSB', 'CWB', 1081.89], ['GIG', 'CWB', 672.68], ['GIG', 'POA', 1121.96], ['BSB', 'POA', 1605.19], ['SSA', 'CGH', 1480.29], ['GIG', 'FOR', 2176.41], ['BSB', 'FOR', 1691.61], ['BSB', 'REC', 1653.95], ['GIG', 'REC', 1859.12], ['BSB', 'BEL', 1612.28], ['GIG', 'BEL', 2448.79], ['CNF', 'CGH', 524.33], ['GRU', 'GYN', 809.02], ['GRU', 'FLN', 514.96], ['SSA', 'CWB', 1805.51], ['BSB', 'CGB', 877.31], ['GIG', 'CGB', 1566.44], ['VCP', 'CWB', 348.4], ['CNF', 'CWB', 846.16], ['GIG', 'MAO', 2847.43], ['BSB', 'MAO', 1948.52], ['VCP', 'POA', 874.38], ['CNF', 'POA', 1361.97], ['GRU', 'RAO', 288.68], ['CGH', 'CWB', 331.11], ['BSB', 'SDU', 928.19], ['CGH', 'POA', 837.71], ['CWB', 'POA', 533.94], ['GRU', 'CGR', 907.44], ['SSA', 'REC', 648.62], ['SSA', 'FOR', 1015.68], ['VCP', 'FOR', 2329.89], ['VCP', 'REC', 2106.18], ['GRU', 'VIX', 729.58], ['GRU', 'SLZ', 2330.82], ['GRU', 'NAT', 2295.82], ['CNF', 'BEL', 2087.05], ['CNF', 'REC', 1607.64], ['CNF', 'FOR', 1858.33], ['GRU', 'UDI', 537.73], ['VCP', 'CGB', 1247.0], ['CNF', 'CGB', 1360.01], ['VCP', 'MAO', 2619.88], ['CNF', 'MAO', 2539.39], ['GRU', 'AJU', 1705.55], ['GRU', 'MCZ', 1919.87], ['GRU', 'PLU', 476.2], ['SSA', 'SDU', 1224.0], ['CGH', 'CGB', 1328.53], ['VCP', 'SDU', 406.73], ['CNF', 'SDU', 374.86], ['GIG', 'GYN', 928.32], ['BSB', 'GYN', 162.63], [
            'GIG', 'FLN', 758.99], ['BSB', 'FLN', 1313.77], ['GRU', 'IGU', 845.32], ['CGH', 'SDU', 365.58], ['GRU', 'LDB', 475.4], ['GRU', 'JPA', 2189.84], ['GRU', 'THE', 2080.31], ['GRU', 'BPS', 1095.97], ['BSB', 'RAO', 585.86], ['GIG', 'RAO', 502.39], ['CWB', 'SDU', 675.51], ['BEL', 'MAO', 1299.01], ['FOR', 'MAO', 2389.59], ['POA', 'SDU', 1119.97], ['GRU', 'MGF', 564.98], ['BSB', 'CGR', 877.44], ['GIG', 'CGR', 1208.48], ['GIG', 'VIX', 417.71], ['BSB', 'SLZ', 1531.18], ['GIG', 'SLZ', 2251.27], ['BSB', 'VIX', 942.83], ['GIG', 'NAT', 2074.62], ['BSB', 'NAT', 1769.97], ['GRU', 'IOS', 1236.02], ['PLU', 'BEL', 2112.04], ['PLU', 'LDB', 836.98], ['PLU', 'REC', 1626.06], ['PLU', 'CFB', 392.79], ['PLU', 'SNZ', 343.43], ['PLU', 'JOI', 864.7], ['PLU', 'JTC', 588.57], ['MAO', 'REC', 2836.34], ['IOS', 'ARS', 1421.01], ['IOS', 'SMT', 1816.04], ['IOS', 'BYO', 1973.84], ['IOS', 'CPV', 906.09], ['SMT', 'FLB', 1515.37], ['SNZ', 'POJ', 554.33], ['POJ', 'ATM', 1825.46], ['PIV', 'JRN', 1664.2], ['PHI', 'VIX', 2043.29], ['SNZ', 'REC', 1895.21], ['OYK', 'JDO', 1857.03], ['MCP', 'FEJ', 2322.03], ['TUR', 'MGF', 2203.5], ['CMT', 'DIQ', 2058.02], ['MCP', 'THE', 1077.93], ['CZS', 'QCN', 3334.34], ['TRQ', 'BSS', 2724.5], ['MEA', 'OAL', 2412.26], ['GMS', 'OTT', 1766.13], ['TUZ', 'LCB', 1299.38], ['PTQ', 'UDI', 1955.47], ['NVT', 'JLS', 757.39], ['JLS', 'REC', 2156.83], ['GUJ', 'BSS', 1699.8], ['AAI', 'OAL', 1591.58], ['DNO', 'QCP', 1276.58], ['DNO', 'IJU', 2001.97], ['IJU', 'SSO', 1126.71], ['SSO', 'XAP', 951.73], ['XAP', 'CWB', 390.1], ['PNZ', 'FLB', 393.04], ['QAC', 'ALQ', 807.99], ['QAC', 'BVB', 3285.33], ['BVB', 'MII', 3019.72], ['MII', 'SOD', 287.43], ['VOT', 'ERM', 832.7], ['ERM', 'SOD', 667.77], ['BAT', 'FRC', 126.07], ['BAT', 'RIA', 1136.57], ['PMW', 'GRU', 1475.09], ['IDO', 'REC', 1766.23], ['CCM', 'CZB', 408.65], ['CCI', 'CZB', 224.5], ['RIA', 'RDC', 2441.25], ['RDC', 'JRN', 967.57]]

    def adicionar_aresta(self, inicio, fim, peso):
        self.grafo.append([inicio, fim, peso])

    def mostrar_todos_aeroportos(self, distancia, origem):
        distancias = ""
        for chave, valor in distancia.items():
            if valor != float("Inf") and valor != 0:
                distancias += f'{origem} ---> {chave}: {valor:.2f} Km\n'
        return distancias

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
                return self.mostrar_todos_aeroportos(distancia, origem)
            elif distancia[final] == float("Inf"):
                return 'Sem conexão entre os aeroportos!'
            else:
                return f'{origem} ---> {final} : {distancia[final]:.2f} Km'
        else:
            return 'Parâmetros inválidos!'


grafo = Graph(93)


def calcular_distancia(*ags, **kags):
    div_main_distancias = Element("div-main-distancias")

    input_aeroportoOrigem = Element("input_aeroportoOrigem")
    aeroportoOrigem = input_aeroportoOrigem.element.value
    input_aeroportoChegada = Element("input_aeroportoChegada")
    aeroportoChegada = input_aeroportoChegada.element.value

    valor = grafo.bellman_ford(aeroportoOrigem, aeroportoChegada)
    if valor == "Parâmetros inválidos!":
        alert("Ops, parâmetros inválidos!")
    elif valor == "Sem conexão entre os aeroportos!":
        alert("Ops, parece que esses aeroportos não possuem conexão entre si :(")
    else:
        div_main_distancias.element.innerText = ""
        div_main_distancias.element.innerText += f"{valor}\n"

    input_aeroportoOrigem.element.value = ""
    input_aeroportoChegada.element.value = ""


# Para plotar o grafo

# G = nx.DiGraph()
# def mostrar_grafo():
#     for i in grafo.grafo:
#         G.add_edge(i[0], i[1])

#     pos = nx.spring_layout(G)
#     nx.draw_networkx_nodes(G, pos, node_size=600, node_color="plam")
#     nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='grey')
#     nx.draw_networkx_labels(G, pos)
#     plt.show()
# mostrar_grafo()
