class Card:
    def __init__(self, parent, row, column):
        self.parent = parent
        self.row = row
        self.column = column
        self.face_up = False
        self.matched = False
        self.button = tk.Button(parent, text="", command=lambda: self.flip_card(), height=3, width=6)
        self.button.grid(row=row, column=column)

    def flip_card(self):
        if not self.face_up and not self.matched:
            self.face_up = True
            if random.random() < 0.5:
                self.button.config(text="A")
            else:
                self.button.config(text="B")