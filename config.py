"""
Central configuration for the fan array project notebooks.

Import this at the top of each notebook instead of hardcoding paths:

    from config import DATA_DIR, data_path

    df = pd.read_excel(data_path("z=2,r=0.xlsx"))

Set FAN_ARRAY_DATA_DIR as an environment variable to point at wherever you've
downloaded the raw data from the project's Google Drive folder, or just edit
DATA_DIR below directly. This is the local-Jupyter equivalent of the
Colab `/content/...` paths used in the original notebooks.
"""

import os
from pathlib import Path

# --- Data location -----------------------------------------------------
# Override by setting the FAN_ARRAY_DATA_DIR environment variable, e.g.:
#   export FAN_ARRAY_DATA_DIR=/path/to/downloaded/drive/folder
# Otherwise defaults to a local ./data folder next to this file.
DATA_DIR = Path(os.environ.get("FAN_ARRAY_DATA_DIR", Path(__file__).parent / "data"))

# --- Known raw data filenames -------------------------------------------
# Fill in / extend these as you confirm exact filenames from the Drive folder.
SENSOR_VOLTAGE_FILES = {
    # (z, r): filename
    (1, 0): "z=1,r=0.xlsx",
    (2, 0): "z=2,r=0.xlsx",
    (2, 1): "z=2,r=1.xlsx",
}

FAN_LOG_FILE = "fan_log.csv"


def data_path(filename: str) -> Path:
    """Return the full path to a raw data file inside DATA_DIR.

    Raises a clear error if the file doesn't exist, instead of failing
    deep inside pandas with a confusing traceback.
    """
    path = DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(
            f"Expected data file not found: {path}\n"
            f"Download it from the project's Google Drive folder and place it in "
            f"{DATA_DIR}, or set FAN_ARRAY_DATA_DIR to point at your data location."
        )
    return path


def ensure_data_dir() -> None:
    """Create DATA_DIR if it doesn't exist yet (does not download anything)."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
