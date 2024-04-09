
from dataclasses import dataclass
from preprocess_execution import PreprocessExecution


@dataclass
class PreprocessController:
    is_minmax_x: bool
    is_std_y: bool
    is_log_z: bool
    exe: "PreprocessExecution"

    def run(self):
        self.exe.get_desc_dict()
        if self.is_minmax_x:
            self.exe.minmax()
        if self.is_std_y:
            self.exe.std()
