# overall reuired libraries
import os
import pandas as pd
from datetime import datetime
from pathlib import Path
import shutil

#===============================================================================
# 1. Create project folders
# ==============================================================================

# Required libraries:
import os

def create_project_folders(
    dirs=("input", "output", "scripts", "temp")
):
    
    for d in dirs:
        
        if not os.path.exists(d):
            print(f"Creating directory: {d}")
        
        os.makedirs(d, exist_ok=True)
# --------------------------------------------------------------------------------

# ================================================================================
# 2. View a DataFrame in Excel or CSV format
# ==============================================================================

# Required libraries:
import os
import pandas as pd
from datetime import datetime

def excel_view(df, format="csv"):
    
    df = pd.DataFrame(df)

    if format not in ["csv", "xlsx"]:
        raise ValueError(
            "format must be either 'csv' or 'xlsx'"
        )

    dir_path = os.path.join(
        os.getcwd(),
        "temp"
    )

    os.makedirs(
        dir_path,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    file = os.path.join(
        dir_path,
        f"{timestamp}_temp.{format}"
    )

    if format == "csv":
        df.to_csv(file, index=False)

    elif format == "xlsx":
        df.to_excel(file, index=False)

    os.startfile(
        os.path.abspath(file)
    )
#------------------------------------------------------------------------------

#==============================================================================
# 3. Delete folders
# ==============================================================================

# Required libraries:
from pathlib import Path
import shutil

def delete_folder(
    path="temp",
    force=True
):

    paths = (
        [path]
        if isinstance(path, str)
        else path
    )

    results = []

    for p in paths:

        folder = Path(p)

        if not folder.exists():
            print(f"Not available: {p}")
            results.append(False)
            continue

        try:

            if folder.is_dir():
                shutil.rmtree(folder)

            elif force:
                folder.unlink()

            print(f"Deleted: {p}")
            results.append(True)

        except Exception:
            results.append(False)

    return results
# --------------------------------------------------------------------------------

# ==============================================================================
# 4. Trim spaces from all columns
# ==============================================================================

# Required libraries:
import pandas as pd

def trimmed_data(data):

    if not isinstance(
        data,
        pd.DataFrame
    ):
        raise TypeError(
            "`data` must be a pandas DataFrame."
        )

    numeric_var = data.select_dtypes(
        include="number"
    ).columns

    categorical_var = data.select_dtypes(
        include="category"
    ).columns

    trim_data = data.astype(str).apply(
        lambda col: col.str.strip()
    )

    for col in numeric_var:

        trim_data[col] = pd.to_numeric(
            trim_data[col],
            errors="coerce"
        )

    for col in categorical_var:

        trim_data[col] = (
            trim_data[col]
            .astype("category")
        )

    return trim_data
# ------------------------------------------------------------------------------------------