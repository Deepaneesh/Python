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

# ==============================================================================
# 5. Get the latest data file based on date in filename
# ==============================================================================

from pathlib import Path
import pandas as pd
import re


def get_latest_data(path, name=None, ext=None):

    path = Path(path)

    # Get files
    files = [
        file for file in path.iterdir()
        if file.is_file()
    ]

    if len(files) == 0:
        raise ValueError(
            "No files found in the specified path."
        )

    # If only one file exists
    if len(files) == 1:

        latest_file = files[0]

    else:

        file_names = [file.name for file in files]

        # Split filename
        split_data = [
            file_name.split(" - ", 1)
            for file_name in file_names
        ]

        # Dates
        dates = [
            x[0] if len(x) > 0 else None
            for x in split_data
        ]

        # Dataset names
        dataset_names = [
            x[1] if len(x) > 1 else ""
            for x in split_data
        ]

        # Remove extensions
        dataset_names_clean = [
            re.sub(r"\..*$", "", x)
            for x in dataset_names
        ]

        # Convert dates
        dates = pd.to_datetime(
            dates,
            format="%d-%m-%Y",
            errors="coerce"
        )

        # Filter by name
        if name is not None:

            idx = [
                bool(
                    re.search(
                        name,
                        dataset_name,
                        re.IGNORECASE
                    )
                )
                for dataset_name in dataset_names_clean
            ]

            files = [
                file
                for file, keep in zip(files, idx)
                if keep
            ]

            dates = dates[idx]

        # Filter by extension
        if ext is not None:

            ext = ext.lstrip(".")

            idx = [
                file.suffix.lower() == f".{ext.lower()}"
                for file in files
            ]

            files = [
                file
                for file, keep in zip(files, idx)
                if keep
            ]

            dates = dates[idx]

        # No files after filtering
        if len(files) == 0:
            raise ValueError(
                "No files found matching criteria"
            )

        # Latest date
        max_date = dates.max()

        latest_files = [
            file
            for file, date in zip(files, dates)
            if date == max_date
        ]

        # Multiple latest files
        if len(latest_files) > 1:

            print(
                "Multiple files found with the latest date:"
            )

            print(
                "\n".join(str(file) for file in latest_files)
            )

            raise ValueError(
                "Please specify 'name' or 'ext' to narrow down."
            )

        latest_file = latest_files[0]

    print(f"Loading: {latest_file}")

    return str(latest_file)

# ==============================================================================

# =============================================================================
#  6. Save file with today's date in filename
# ==============================================================================

from pathlib import Path
from datetime import date


def save_with_date(path, filename):

    # Create directory if it doesn't exist
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)

    # Today's date
    today = date.today().strftime("%d-%m-%Y")

    # Create new filename
    new_name = f"{today} - {filename}"

    print(f"Saving file as: {new_name}")

    # Return complete file path
    return str(path / new_name)

# =============================================================================
