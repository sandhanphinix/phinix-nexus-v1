import pandas as pd

from load.write_data import WriteData
from validators.run_validator import RunValidator

class WriteCsv(WriteData):
    """
    Write CSV class using abstract write data class.
    """

    def __init__(
            self,
            file_path: str,
    ) -> None:
        super().__init__(file_path=file_path)
    
    @RunValidator.validate_instance_method(check="write_dataframe")
    def write_file(
            self,
            output: pd.DataFrame,
            **kwargs
    ) -> None:
        output.to_csv(self.file_path, index=False, **kwargs)