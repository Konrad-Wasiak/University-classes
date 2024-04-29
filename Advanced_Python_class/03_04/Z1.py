class pyramid():
    def __init__(self, height, brick_char, type):
        self.height = height
        self.brick_char = brick_char
        self.type = type
        if type == "vertical":
            self.first_row_elements_number = height*2 - 1

    def build_pyramid(self):
        if self.type == "vertical":
            for level in range(self.height):
                print(" " * (self.height-level) + self.brick_char * (self.first_row_elements_number - 2 * (self.height-level-1)))
        elif self.type == "horizontal":
            for char_num in range(1, self.height+1):
                print(self.brick_char * char_num)
            for char_num in range(1, self.height+1):
                print(self.brick_char * (self.height-char_num))
        else:
            print("Typo in the 'type' parameter.")


    def build_pyramid_down_on_the_upside(self):
        if self.type == "vertical":
            for level in range(self.height):
                print(" " * level + self.brick_char * (self.first_row_elements_number - 2 * level))
        elif self.type == "horizontal":
            print("Yet to be implemented.")
        else:
            print("Typo in the type argument.")

my_pyramid = pyramid(6, "(=^.^=)", "horizontal")
my_pyramid.build_pyramid()