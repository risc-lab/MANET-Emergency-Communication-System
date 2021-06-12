import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
import random
from Graph import Graph

if __name__ == '__main__':
    # Input Handling

    n = input().split()
    node = [input().split() for i in range(int(n[1]))]

    g = Graph(int(n[0]))
    map = {}
    R = 50

    for d in node:
        g.addEdge(int(d[0]), int(d[1]), int(d[2]))
        map[int(d[0])] = [divmod(ele, R + 1) for ele in random.sample(range((R + 1) * (R + 1)), 1)][0]
        map[int(d[1])] = [divmod(ele, R + 1) for ele in random.sample(range((R + 1) * (R + 1)), 1)][0]

    print(map)

    mst = g.Update_DLT()
    connected = g.connectedComponents()
    print(mst)
    print(connected)

    # Visualizing Part

    if len(connected) == 1:

        colors = {}
        colorlist = ['r', 'g', 'b', 'c', 'm', 'y', 'brown', 'lime', 'orange', 'violet', 'pink', 'aqua', 'greenyellow']

        fig, axes = plt.subplots(figsize=(12, 8))
        plt.subplots_adjust(left=0.102)

        g = nx.Graph()

        for d in node:
            if int(d[0]) in connected[0] and int(d[1]) in connected[0]:
                g.add_edge(int(d[0]), int(d[1]), weight=int(d[2]))
                colors[int(d[0])] = 'silver'
                colors[int(d[1])] = 'silver'

        ps = []
        edgeList = [(u, v) for (u, v, d) in g.edges(data=True)]
        pos = nx.spring_layout(g)
        ps.append(pos)
        values = [colors.get(node, 0.25) for node in g.nodes()]
        nx.draw_networkx_nodes(g, pos, node_size=400, node_color=values)

        nx.draw_networkx_edges(g, pos, edgeList, width=2)

        nx.draw_networkx_labels(g, pos, font_size=10, font_family='sans-serif')

        edge_labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=8, label_pos=0.4)

        DLT = []
        text = plt.text(0.5, -0.1, "", size=10, ha="center",
                        transform=axes.transAxes)

        l = []
        index = 0


        def update(num):
            # print(num)
            global l, index
            if num != 0:
                if (mst[num - 1][0], mst[num - 1][1]) in g.edges():
                    DLT.append(map[mst[num - 1][0]])
                    DLT.append(map[mst[num - 1][1]])
                    if colors[mst[num - 1][0]] != 'silver' and colors[mst[num - 1][1]] == 'silver':
                        colors[mst[num - 1][1]] = colors[mst[num - 1][0]]
                    elif colors[mst[num - 1][1]] != 'silver' and colors[mst[num - 1][0]] == 'silver':
                        colors[mst[num - 1][0]] = colors[mst[num - 1][1]]
                    elif colors[mst[num - 1][0]] == 'silver' and colors[mst[num - 1][1]] == 'silver':
                        colors[mst[num - 1][0]] = colorlist[index % len(colorlist)]
                        colors[mst[num - 1][1]] = colorlist[index % len(colorlist)]
                        index = index + 1
                    elif colors[mst[num - 1][0]] != 'silver' and colors[mst[num - 1][1]] != 'silver':
                        c0 = 0
                        c1 = 0
                        color0 = colors[mst[num - 1][0]]
                        color1 = colors[mst[num - 1][1]]
                        for key, val in colors.items():
                            if val == color0:
                                c0 = c0 + 1
                        for key, val in colors.items():
                            if val == color1:
                                c1 = c1 + 1
                        if c0 > c1:
                            for key, val in colors.items():
                                if val == color1:
                                    colors[key] = color0
                        else:
                            for key, val in colors.items():
                                if val == color0:
                                    colors[key] = color1
                    values = [colors.get(node, 0.25) for node in g.nodes()]
                    l = list(set(DLT))
                    nx.draw_networkx_edges(g, pos, edgelist=[(mst[num - 1][0], mst[num - 1][1])], width=5,
                                           edge_color='r')
                    nx.draw_networkx_nodes(g, pos, node_size=400, node_color=values)
                    # print(DLT)
            if num == len(mst):
                text.set_text(f"DLT: {l}")


        ani = animation.FuncAnimation(fig, update, frames=len(mst) + 1, interval=1000, repeat=False)

        manager = plt.get_current_fig_manager()
        plt.show()

    else:
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 8))
        ax = axes.flatten()
        plt.subplots_adjust(wspace=0.4)

        colors0 = {}
        colors1 = {}
        colorlist = ['r', 'g', 'b', 'c', 'm', 'y', 'brown', 'lime', 'orange', 'violet', 'pink', 'aqua', 'greenyellow']

        whole_graph = nx.Graph()
        g = nx.Graph()
        g1 = nx.Graph()

        for d in node:
            whole_graph.add_edge(int(d[0]), int(d[1]), weight=int(d[2]))

        for d in node:
            if int(d[0]) in connected[0] and int(d[1]) in connected[0]:
                g.add_edge(int(d[0]), int(d[1]), weight=int(d[2]))
                colors0[int(d[0])] = 'silver'
                colors0[int(d[1])] = 'silver'
        for d in node:
            if int(d[0]) in connected[1] and int(d[1]) in connected[1]:
                g1.add_edge(int(d[0]), int(d[1]), weight=int(d[2]))
                colors1[int(d[0])] = 'silver'
                colors1[int(d[1])] = 'silver'
            # for u in range(int(n[1])):
        gs = [g, g1]
        ps = []
        for i in range(len(gs)):
            edgeList = [(u, v) for (u, v, d) in gs[i].edges(data=True)]
            if i == 0:
                values = [colors0.get(node, 0.25) for node in gs[i].nodes()]
            else:
                values = [colors1.get(node, 0.25) for node in gs[i].nodes()]
            pos = nx.circular_layout(gs[i])
            ps.append(pos)
            nx.draw_networkx_nodes(gs[i], pos, node_size=700, ax=ax[i], node_color=values)

            nx.draw_networkx_edges(gs[i], pos, edgeList, width=2, ax=ax[i])

            nx.draw_networkx_labels(gs[i], pos, font_size=10, font_family='sans-serif', ax=ax[i])

            edge_labels = nx.get_edge_attributes(gs[i], 'weight')
            nx.draw_networkx_edge_labels(gs[i], pos, edge_labels=edge_labels, font_size=9, ax=ax[i], label_pos=0.3)

        DLT = []
        DLT1 = []
        text = plt.text(0.5, -0.1, "", size=11, ha="center",
                        transform=ax[0].transAxes, wrap=True)
        text._get_wrap_line_width = lambda: 500.
        text1 = plt.text(0.5, -0.1, "", size=11, ha="center",
                         transform=ax[1].transAxes, wrap=True)
        text1._get_wrap_line_width = lambda: 500.

        l1 = []
        index = 0


        def update(num):
            # print(num)

            global l1, index
            if num != 0:
                if (mst[num - 1][0], mst[num - 1][1]) in gs[0].edges():
                    DLT.append(map[mst[num - 1][0]])
                    DLT.append(map[mst[num - 1][1]])
                    if colors0[mst[num - 1][0]] != 'silver' and colors0[mst[num - 1][1]] == 'silver':
                        colors0[mst[num - 1][1]] = colors0[mst[num - 1][0]]
                    elif colors0[mst[num - 1][1]] != 'silver' and colors0[mst[num - 1][0]] == 'silver':
                        colors0[mst[num - 1][0]] = colors0[mst[num - 1][1]]
                    elif colors0[mst[num - 1][0]] == 'silver' and colors0[mst[num - 1][1]] == 'silver':
                        colors0[mst[num - 1][0]] = colorlist[index % len(colorlist)]
                        colors0[mst[num - 1][1]] = colorlist[index % len(colorlist)]
                        index = index + 1
                    elif colors0[mst[num - 1][0]] != 'silver' and colors0[mst[num - 1][1]] != 'silver':
                        c0 = 0
                        c1 = 0
                        color0 = colors0[mst[num - 1][0]]
                        color1 = colors0[mst[num - 1][1]]
                        for key, val in colors0.items():
                            if val == color0:
                                c0 = c0 + 1
                        for key, val in colors0.items():
                            if val == color1:
                                c1 = c1 + 1
                        if c0 > c1:
                            for key, val in colors0.items():
                                if val == color1:
                                    colors0[key] = color0
                        else:
                            for key, val in colors0.items():
                                if val == color0:
                                    colors0[key] = color1
                    values = [colors0.get(node, 0.25) for node in gs[0].nodes()]
                    l1 = list(set(DLT))
                    nx.draw_networkx_nodes(gs[0], ps[0], node_size=700, ax=ax[0], node_color=values)
                    nx.draw_networkx_edges(gs[0], ps[0], edgelist=[(mst[num - 1][0], mst[num - 1][1])], width=5,
                                           edge_color='r', ax=ax[0])
                    # print(DLT)
            if num == len(mst):
                text.set_text(f"DLT: {l1}")


        l = []
        index1 = 0


        def update1(num):
            # print(num)

            global l, index1
            if num != 0:
                if (mst[num - 1][0], mst[num - 1][1]) in gs[1].edges():
                    DLT1.append(map[mst[num - 1][0]])
                    DLT1.append(map[mst[num - 1][1]])
                    if colors1[mst[num - 1][0]] != 'silver' and colors1[mst[num - 1][1]] == 'silver':
                        colors1[mst[num - 1][1]] = colors1[mst[num - 1][0]]
                    elif colors1[mst[num - 1][1]] != 'silver' and colors1[mst[num - 1][0]] == 'silver':
                        colors1[mst[num - 1][0]] = colors1[mst[num - 1][1]]
                    elif colors1[mst[num - 1][0]] == 'silver' and colors1[mst[num - 1][1]] == 'silver':
                        colors1[mst[num - 1][0]] = colorlist[index1 % len(colorlist)]
                        colors1[mst[num - 1][1]] = colorlist[index1 % len(colorlist)]
                        index1 = index1 + 1
                    elif colors1[mst[num - 1][0]] != 'silver' and colors1[mst[num - 1][1]] != 'silver':
                        c0 = 0
                        c1 = 0
                        color0 = colors1[mst[num - 1][0]]
                        color1 = colors1[mst[num - 1][1]]
                        for key, val in colors1.items():
                            if val == color0:
                                c0 = c0 + 1
                        for key, val in colors1.items():
                            if val == color1:
                                c1 = c1 + 1
                        if c0 > c1:
                            for key, val in colors1.items():
                                if val == color1:
                                    colors1[key] = color0
                        else:
                            for key, val in colors1.items():
                                if val == color0:
                                    colors1[key] = color1
                    values = [colors1.get(node, 0.25) for node in gs[1].nodes()]
                    l = list(set(DLT1))
                    nx.draw_networkx_nodes(gs[1], ps[1], node_size=700, ax=ax[1], node_color=values)
                    nx.draw_networkx_edges(gs[1], ps[1], edgelist=[(mst[num - 1][0], mst[num - 1][1])], width=5,
                                           edge_color='r', ax=ax[1])
            if num == len(mst):
                text1.set_text(f"DLT: {l}")


        ani = animation.FuncAnimation(fig, update, frames=len(mst) + 1, interval=1000, repeat=False)
        ani1 = animation.FuncAnimation(fig, update1, frames=len(mst) + 1, interval=1000, repeat=False)
        plt.show()
