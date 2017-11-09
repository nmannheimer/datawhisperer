"""



"""

class Model(object):
    def train(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

class VizClassifier(Model):
    valid_chart_types = ['bar', 'pie']

    def __init__(self):
        self.weights = None

    def train(self, X, y):
        self.weights = 100

    def predict(self, X):
        return [1, 0]

    @staticmethod
    def get_viz_type(predicted_vector):
        return VizClassifier.valid_chart_types[predicted_vector.index(1)]


