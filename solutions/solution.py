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
    task="Create an Adapter class which allows NewService instance to be compatible with client code.",
    goal="Montrer que l'on peut faire de l'héritage multiple en Python Montrer qu'il faut que le nouveau"
         " service implémente l'interface de l'ancien service",
    hint="""""",
    solution="""
    class Adapter(NewService):
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
                
        new_section_selector = Adapter(placement=placement, limit=50)
        new_section = new_section_selector.filter()
        
        plot_polylines(new_section, "new_section")
        """
)
