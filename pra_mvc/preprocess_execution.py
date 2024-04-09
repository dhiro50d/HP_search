

from dataclasses import dataclass
from typing import List, Tuple
from sklearn.preprocessing import MinMaxScaler

@dataclass
class PreprocessExecution:
    datas: List[Tuple[float, float]]

    def get_desc_dict(self):
        MinMaxScaler
        return

    def minmax(self):
        return
    
    def std(self):
        return

    def log(self):
        return
