class Structure:
    def __init__(self):
        self.blocks = {}

    def set_block(self, x, y, z, block):
        self.blocks[(x, y, z)] = block

    def get_block(self, x, y, z):
        return self.blocks.get((x, y, z))