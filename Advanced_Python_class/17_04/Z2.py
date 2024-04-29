class chart():
    def __init__(self, height_1:int, height_2:int, height_3:int):
        self.height_1 = height_1
        self.height_2 = height_2
        self.height_3 = height_3

    def print_chart(self):
        print("-"*self.height_1)
        print("-"*self.height_2)
        print("-"*self.height_3)



def draw_chart():
    height_1 = input("Type the height of the first bar.\nRequirements: integer, height_1 != height_2, >0, <20.\n")
    height_3 = input("Type the height of the second bar.\nRequirements: integer, >0, <20.\n")

    try:
        height_1 = int(height_1)
        height_3 = int(height_3)
        height_2 = int(round((height_1 + height_3) / 2, 0))

    except ValueError:
        print("Invalid input - please enter integers.")
        draw_chart()

    if height_1 != height_3 and height_1 > 0 and height_3 > 0 and height_1 < 20 and height_3 < 20:
        user_chart = chart(height_1, height_2, height_3)
        user_chart.print_chart()
    else:
        print("Invalid input. Try again.")
        draw_chart()

draw_chart()