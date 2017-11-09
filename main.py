"""

This is the main interface for Data Whisperer

"""

import numpy as np
import pandas as pd

from whisper.util import parse_arguments
from whisper.model import VizClassifier

def main(args):
    args = parse_arguments(args)

    # loader loads dataset
    df = pd.read_csv(filepath_or_buffer=args.filepath)

    # processing of dataset
    X = np.zeros(shape=(5, 5))
    y = np.zeros(shape=(5, 2))

    # train classifiers
    m = VizClassifier()
    m.train(X=X, y=y)

    d = DialogueManager()

    is_incomplete = True
    while is_incomplete:

        is_unknown_plot = True
        if is_unknown_plot:
            y_hat = m.predict(X)
            viz_type = VizClassifier.get_viz_type(y_hat)

    # display visualization
    print('hi')

if __name__ == '__main__':
    main()
