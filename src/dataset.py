import pathlib as Path
import pandas as pd


class Dataset:
    def __init__(self):
        self.reset()

    def read_raw_dataset() -> pd.DataFrame:
      dataset_path = Path().absolute() / "data"
      spambase = pd.read_table(dataset_path / "spambase.data")
      return spambase
