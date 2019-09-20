import argparse

from src import *
from src import yolo


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=_valid_model, default=MODEL_DEFAULT)
    return parser.parse_args()


def _valid_model(s):
    if type(s) is str and s in MODEL_LIST:
        return s
    else:
        msg = f'Model has to be one of: {MODEL_LIST}'
        raise argparse.ArgumentTypeError(msg)


if __name__ == '__main__':
    args = _parse_args()
    yolo.run(model_name=args.model)
