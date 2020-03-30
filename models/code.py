class Code:
    def __init__(self, string):
        self.colors = string

    def get_array(self):
        """ Returns the colors string as an array
            :return: Array of colors
            """
        return [x.strip() for x in self.colors.split(',')]
