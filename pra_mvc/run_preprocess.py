# run_preprocess.py
import random
import argparse

from convert import PreprocessControler

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='demo coding about to explain my work and to learn.')
    parser.add_argument('-log', '--is_log', action="store_true", help='set -log if you want to run.') 
    parser.add_argument('-std', '--is_standard', action="store_true", help='set -std if you want to run.') 
    parser.add_argument('-mm', '--is_minmax', action="store_true", help='set -mm if you want to run.')
    args = parser.parse_args()

    # Set datas below under code.
    # But it should be better to set data pass at parser.
    datas = []
    for _ in range(100):
        x = [random.random() for _ in range(2)]
        datas.append({"poss": x, "y": random.random()})

    ctrl = PreprocessControler(
        args.is_log,
        args.is_standard,
        args.is_minmax,
        datas,
    )
    ctrl.show_init_msg()
    ctrl.run_preprocess()
