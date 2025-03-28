from manim import *

class ParticleMotion(Scene):
    def construct(self):
        # Define the functions
        def a(t):
            return 0.3 * t + 2.4

        def v(t):
            return 0.15 * t**2 + 2.4 * t - 12

        def x(t):
            return 0.05 * t**3 + 1.2 * t**2 - 12 * t + 4.6

        # Time when particle is at rest
        t_rest = 4

        # Axes
        axes = Axes(
            x_range=(-5, 25, 1),
            y_range=(-25, 10, 1),
            x_axis_config={"numbers_to_include": [-5, 0, 4, 25]},
            y_axis_config={"numbers_to_include": [-25, 0, 4.6, 10]},
        )
        axes.add_coordinate_labels()
        self.play(Create(axes))

        # Graphs
        a_graph = axes.plot(a, x_range=(-5, 25), color=RED)
        v_graph = axes.plot(v, x_range=(-5, 25), color=GREEN)
        x_graph = axes.plot(x, x_range=(-5, 25), color=BLUE)

        a_label = axes.get_graph_label(a_graph, "a(t)", x_val=20)
        v_label = axes.get_graph_label(v_graph, "v(t)", x_val=20)
        x_label = axes.get_graph_label(x_graph, "x(t)", x_val=20)

        self.play(
            Create(a_graph),
            Create(v_graph),
            Create(x_graph),
            Create(a_label),
            Create(v_label),
            Create(x_label),
        )
        self.wait(2)

        # Particle animation
        particle = Dot(axes.coords_to_point(4.6, 0), color=YELLOW)
        particle_label = MathTex("Particle").next_to(particle, UP)
        self.play(Create(particle), Create(particle_label))

        # Follow the position
        def update_particle(obj):
            current_t = self.get_time()  # Manim's time
            if current_t < 25:
                new_pos = axes.coords_to_point(x(current_t), 0)
                obj.move_to(new_pos)

        particle.add_updater(update_particle)
        self.play(MoveAlongPath(particle,Line(start=axes.coords_to_point(4.6, 0),end=axes.coords_to_point(x(25), 0))), run_time=25, rate_func=linear)
        particle.remove_updater(update_particle) # Stop updating

        # Mark the point where the particle stops
        rest_point = Dot(axes.coords_to_point(x(t_rest), 0), color=PURPLE)
        rest_label = MathTex(f"Rest at t={t_rest}s, x={x(t_rest):.2f}m").next_to(rest_point, DOWN)
        self.play(Create(rest_point), Create(rest_label))

        self.wait(5)