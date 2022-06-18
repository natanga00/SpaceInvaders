class Phase:
    def __init__(self, quantity_of_levels = 4, points_per_level = [25, 80, 150, 200]):
        self.phases = []
        self.current_phase = 1
        self.quantity_of_levels = quantity_of_levels
        self.points_per_level = points_per_level

        self.setup_phases()
    def setup_phases(self):
        if len(self.points_per_level) != self.quantity_of_levels:
            raise Exception("A configuração de fases está incorreta, ajustar a relação de fases com a pontuação")

        for phase in range(self.quantity_of_levels):
            self.phases.append(self.points_per_level[phase])

    def change_phase(self, score):
        if(not self.quantity_of_levels == self.current_phase):

            if score > self.phases[self.current_phase]:
                self.current_phase += 1

            if self.current_phase == self.quantity_of_levels:
                return False
            
            return True
        
        return False