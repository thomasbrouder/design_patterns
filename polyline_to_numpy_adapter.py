"""
    Context: You have a legacy code where polylines are today's tekyntools objects.
    You already know that your polyline data structure will evolve towards numpy arrays.
    You need to create a brand new module. You choose to use numpy instead of current polylines
    so that you're code would as close as possible from your future polyline implementation.
    Goal: Create a new SectionSelector using numpy and an Adapter to plug it to the code.
    Can you draw the associated UML ?
"""

from tekyntools.geometryObjects import geometric_form, vertex, polyline
import matplotlib.pyplot as plt


class SectionSelector():
    def __init__(self, limit, placement):
        self.limit = limit
        self.placement = placement

    def filter(self):
        return [poly for poly in self.placement if max(poly.y_coords) < self.limit]


def plot_polylines(polylines):
    for poly in polylines:
        plt.plot(poly.x_coords, poly.y_coords)
    plt.show()


def to_polyline(numpy_poly):
    return polyline.Polyline(
            [vertex.Vertex(x, y) for x, y in list(zip(*numpy_poly))]
    )


class NewSectionSelector():
    def __init__(self, limit, placement):
        self.limit = limit
        self.placement = placement

    def new_filter(self):
        return [poly for poly in self.placement if poly[1].max() < self.limit]


class Adapter(SectionSelector, NewSectionSelector):
    def filter(self):
        self.placement = [poly.to_numpy() for poly in self.placement]
        section = self.new_filter()
        return [to_polyline(numpy_poly) for numpy_poly in section]


if __name__ == '__main__':
    placement = [
        geometric_form.create_rectangle(height=20, width=200),
        geometric_form.create_rectangle(origin=vertex.Vertex(0, 21), height=20, width=50),
        geometric_form.create_rectangle(origin=vertex.Vertex(51, 21), height=50, width=10),
        geometric_form.create_rectangle(origin=vertex.Vertex(62, 21), height=50, width=30),
    ]

    plot_polylines(placement)

    # Main code
    section_selector = SectionSelector(placement=placement, limit=50)
    section = section_selector.filter()
    plot_polylines(section)

    # Adapter code
    # Rappel: polyline.to_numpy()

    new_section_selector = Adapter(placement=placement, limit=50)
    new_section = new_section_selector.filter()

    plot_polylines(new_section)
