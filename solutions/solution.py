def bold(text: str) -> str:
    BOLD = '\033[1m'
    END_BOLD = '\033[0m'
    return f"{BOLD}{text}{END_BOLD}"


class Exercise():
    """
    Exercises tips and solutions
    """
    def __init__(self, task, goal, hint, solution):
        self._task = task
        self._goal = goal
        self._hint = hint
        self._solution = solution

    def task(self):
        """
        Defines the task to achieve in order to complete the exercise
        Returns:

        """

        return f"{bold('Task: ')} {self._task}"

    def goal(self):
        """
        Defines the pedagogic goal of the exercise
        Returns:

        """
        return f"{bold('Goal: ')} {self._goal}"

    def hint(self):
        """
        Tips to help resolve the exercise
        Returns:

        """
        return f"{bold('Hint: ')} {self._hint}"

    def solution(self):
        """
        Exercise solution
        Returns:

        """
        return f"{bold('Solution: ')} {self._solution}"


exercise_1 = Exercise(
    task="Create an Adapter class which allows NewService instance to be compatible with client code."
         "When you're finished, client_code(new_service) return should be readable and understandable by a human being.",
    goal="Montrer que l'on peut faire de l'héritage multiple en Python Montrer qu'il faut que le nouveau"
         " service implémente l'interface de l'ancien service",
    hint="""""",
    solution="""
        # Object adapter: the adapter implements the interface of one object and wraps the other one.
        class ObjectAdapter(Client):
            def method(self, service):
                print(service.specific_request()[::-1])    
            
        new_service = NewService()
        object_adapter = ObjectAdapter()
        object_adapter.method(new_service)
        
        
        # Class adapter: the adapter inherits interfaces from both objects at the same time.
        class ClassAdapter(Client, NewService):
            def method(self):
                print(super().specific_request()[::-1])
        
        class_adapter = ClassAdapter()
        class_adapter.method()
    """
)

exercise_2 = Exercise(
    task="",
    goal="",
    hint="""""",
    solution="""
    class Adapter(Service, NewService):
        '''
        Adapter allows NewService instance to be compatible with client code.
        The client is now compatible with NewService instance through the Adapter.
        Adapter changes NewService interface so that it is understandable by client code.
        Adapter makes as if it was an Service instance.
        '''
        def request(self):
            new_service_req = self.specific_request()
            return new_service_req[::-1]
            
    adapter = Adapter()
    client_code(adapter)
    """
)

exercise_3 = Exercise(
    task="Create a new SectionSelector using numpy and an Adapter to plug it to the code. Can you draw the associated UML ?",
    goal="",
    hint="""""",
    solution="""
        import numpy as np
        def to_polyline(numpy_poly):
            '''
            numpy_poly: tuple(np.ndarray, np.ndarray)
            '''
            return polyline.Polyline(
                    [vertex.Vertex(x, y) for x, y in list(zip(*numpy_poly))]
            )
        
        
        class NewSectionSelector():
            def __init__(self, limit, placement):
                self.limit = limit
                self.placement = placement
        
            def new_filter(self):
                return [poly for poly in self.placement if poly[1].max() < self.limit]
        
        
        class Adapter(PolylinePlotter, NewSectionSelector):
            def __init__(self, placement, limit):
                self.placement = np.array([poly.to_numpy() for poly in placement])  # Adapter for input interface. Object conversion is made as quick as possible
                self.limit = limit
                
            def filter(self):
                section = self.new_filter()
                return [to_polyline(numpy_poly) for numpy_poly in section] # Adapter for output interface. Object conversion is made as late as possible
        
        adapter = Adapter(placement=placement, limit=50)
        adapter.filter()
        plotter.plot_polylines(section, title="Section")
        """
)
