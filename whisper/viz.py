"""



"""

import matplotlib.pyplot as plt

class Vizualization(object):
    def plot(self):
        raise NotImplementedError

class BarVizualization(Vizualization):
    def plot(self, *args, **kwargs):
        plt.bar(*args, **kwargs)
        plt.show()

class PieVizualization(Vizualization):
    def plot(self):
        pass

