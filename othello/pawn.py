class pawn():
    def __init__(self, color):
        self.color = color

    def reverse_pawn(self):
        if self.color == 'o':
            self.color = '*'
        elif self.color == '*':
            self.color = 'o'
