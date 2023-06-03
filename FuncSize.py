### Estructura que guarda la cantidad de variables locales y temporales que usa una funcion al momento de ser invocada ###
class FuncSize:
    def __init__(self, CLint, CLfloat, CLstring, CLchar, CLbool, CTint, CTfloat, CTstring, CTchar, CTbool, CTpointers):
        # Locales
        self.CLint = CLint
        self.CLfloat = CLfloat
        self.CLstring = CLstring
        self.CLchar = CLchar
        self.CLbool = CLbool

        # Temporales
        self.CTint = CTint
        self.CTfloat = CTfloat
        self.CTstring = CTstring
        self.CTchar = CTchar
        self.CTbool = CTbool

        # Apuntadores de arreglos
        self.CTpointers = CTpointers

    def returnElements(self):
        return f'{self.CLint},{self.CLfloat},{self.CLstring},{self.CLchar},{self.CLbool},{self.CTint},{self.CTfloat},{self.CTstring},{self.CTchar},{self.CTbool},{self.CTpointers}'