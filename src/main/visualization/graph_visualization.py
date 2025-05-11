from manim import *
from manim import config

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.main.algorithms.dijkstra import dijkstra
from src.main.algorithms.shortest_path import get_shortest_path

config["pixel_height"] = 1080
config["pixel_width"] = 1920
config["frame_rate"] = 60


class GraphVisualization(Scene):
    def __init__(self, graph, start, end, **kwargs):
        super().__init__(**kwargs)
        self.graph = graph
        self.start = start
        self.end = end

    def construct(self):
        edges = self.graph.get_edges_list()
        edges_weight = [(u, v, self.graph.get_edge_weight(u, v)) for u, v in
                        edges]
        vertices = self.graph.get_vertices_list()

        manim_graph = Graph(
            vertices,
            edges,
            layout="spring",
            layout_scale=3,
            labels=True,
            vertex_config={v: {"fill_color": BLUE} for v in vertices},
        )

        self.play(Create(manim_graph))

        edge_weights = {}
        for u, v, weight in edges_weight:
            edge = manim_graph.edges.get((u, v), manim_graph.edges.get((v, u)))
            if edge:
                edge_center = edge.get_center()
                weight_label = Text(str(weight), font_size=24,
                                    fill_color=PINK).move_to(
                    edge_center
                )
                edge_weights[(u, v)] = weight_label
                self.add(weight_label)

        self.visualize_start_and_end(manim_graph)
        self.visualize_algorithm(manim_graph, self.start, self.end)
        self.wait(3)

    def visualize_start_and_end(self, manim_graph):
        self.play(manim_graph[self.start].animate.set_fill(ORANGE), run_time=1)
        self.play(manim_graph[self.end].animate.set_fill(RED), run_time=1)


    def visualize_algorithm(self, manim_graph, start, end):
        distances, previous = dijkstra(self.graph, start)
        path = get_shortest_path(previous, start, end)
        algorithm_name = "Алгоритм Дейкстры"

        title = Text(algorithm_name, font_size=36, color=WHITE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            edge = manim_graph.edges.get((u, v), manim_graph.edges.get((v, u)))
            if edge:
                self.play(edge.animate.set_color(YELLOW), run_time=1)

        self.play(FadeOut(title))

def create_video(graph, representation_type, start_vertex, end_vertex):
    scene = GraphVisualization(
        graph=graph,
        start=start_vertex,
        end=end_vertex
    )
    scene.render()
    print(f"Видео для {representation_type} создано!")