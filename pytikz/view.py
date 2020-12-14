class View:
    """Bundles a list of drawables with a common transformation."""

    def __init__(self, transformation=lambda vector: vector):
        self.transformation = transformation
        self.drawables = []

    def compose(self, transformation):
        """Compose the internal transformation with a new transformation."""
        transformation_original = self.transformation
        self.transformation = lambda vector: transformation(
            transformation_original(vector)
        )

    def append(self, drawable):
        """Appends a drawable to the internal list."""
        self.drawables.append(drawable)

    def __getitem__(self, k):
        """Returns the transformed version of the k-th drawable."""
        return self.drawables[k].copy().apply(self.transformation)

    def __iter__(self):
        """Iterates over the transformed drawables."""
        for k in len(self.drawables):
            yield self[k]
