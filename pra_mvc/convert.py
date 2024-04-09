from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np


@dataclass
class PoointCloud:
    poss: Tuple[float, float]  # x_center, y_center
    y: float
    ...


@dataclass
class PreprocessExecution:
    datas: List[Dict[str, any]]  # "poss": [x_center, y_center] each is float, "y": scaler as float
    # datas: List["PoointCloud"]  # This is better than above.

    def get_poss_norm(self):
        x_min, y_min = np.inf, np.inf
        x_max, y_max = -np.inf, -np.inf
        for data in self.datas:
            poss = data["poss"]
            x_min = min(x_min, poss[0])
            x_max = max(x_max, poss[0])
            y_min = min(y_min, poss[1])
            y_max = max(y_max, poss[1])
        self.poss_describe = {
            "x_min": x_min,
            "x_max": x_max,
            "y_min": y_min,
            "y_max": y_max,
        }
        return

    def poss_norm(self):
        def calc(poss, _min, _max):
            return (poss - _min) / (_max - _min)
        for data in self.datas:
            data["poss"][0] = calc(data["poss"][0], self.poss_describe["x_min"], self.poss_describe["x_max"])
            data["poss"][1] = calc(data["poss"][1], self.poss_describe["y_min"], self.poss_describe["y_max"])
        return            

    # TODO hirose
    def get_grand_truth_desctibe(self):
        return

    def log10_transformer(self):
        return

    def minmax_transformer(self):
        return

    def standard_transformer(self):
        return


@dataclass
class PreprocessControler:
    is_log: bool
    is_standard: bool
    is_minmax: bool
    datas: List[Dict[str, any]]
    pre_exe: "PreprocessExecution" = None

    def show_init_msg(self):
        msg = f"""
        is_standard: {self.is_standard}
        is_minmax: {self.is_minmax}
        is_log: {self.is_log}
        """
        print(msg)
        ans = input("check values. Start preprocess? [y/n]")
        if ans != "y":
            exit()
        return
    
    def run_preprocess(self):
        self.pre_exe = PreprocessExecution(self.datas)
        self.pre_exe.poss_norm()

        if self.is_log:
            self.pre_exe.log10_transformer()
        self.pre_exe.get_grand_truth_desctibe()
        if self.is_minmax:
            self.pre_exe.minmax_transformer()
        if self.is_standard():
            self.pre_exe.standard_transformer()
        print("finishe.")
        return


@dataclass
class Geometry:
    x_min: float
    x_max: float
    y_min: float
    y_max: float

    @property
    def get_s(self):
        return (self.x_max - self.x_min) * (self.y_max - self.y_min)

    @staticmethod
    def print_hoge():
        print("hoge")
        return


if __name__ == "__main__":
    geo = Geometry(0, 1, 2, 4)
    print(f"面積：{geo.get_s}")  # if use @property, you can access geo.get_s not geo.get_s().
