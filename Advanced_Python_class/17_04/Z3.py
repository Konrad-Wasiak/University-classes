class chart():
    def __init__(self, height_1:int, height_2:int, height_3:int):
        self.height_1 = height_1
        self.height_2 = height_2
        self.height_3 = height_3

    def print_chart(self):
        print("--+-+--+-+--+-+--")
        if self.height_1 > self.height_2:
            for i in range(1, self.height_1+1):
                if i <= self.height_2:
                    print("  | |  | |  | |")
                elif i >= self.height_3:
                    print("  | |       | |")
                else:
                    print("  | |")
        else:
            for i in range(1, self.height_2+1):
                if i <= self.height_1:
                    print("  | |  | |  | |")
                elif i >= self.height_3:
                    print("  | |       | |")
                else:
                    print("  | |")


def draw_chart():
    height_1 = input("Type the height of the first bar.\nRequirements: integer, height_1 != height_2, >0, <20.\n")
    height_2 = input("Type the height of the second bar.\nRequirements: integer, >0, <20.\n")

    try:
        height_1 = int(height_1)
        height_2 = int(height_2)
        height_3 = abs(height_1 - height_2)

    except ValueError:
        print("Invalid input - please enter integers.")
        draw_chart()

    if height_1 != height_2 and height_1 >= 0 and height_2 >= 0 and height_1 < 9 and height_2 < 9:
        user_chart = chart(height_1, height_2, height_3)
        user_chart.print_chart()
    else:
        print("Invalid input. Try again.")
        draw_chart()

draw_chart()
