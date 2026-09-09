# Libraries -----------------------------------------------------------------------

import itertools
import tempfile
from datetime import datetime
from pathlib import Path
import pandas as pd
import statsmodels.api as sm


# Function -----------------------------------------------------------------------


def excel_view(self, folder=None, filename_prefix="temp"):
    """Save the DataFrame as a CSV in the system temp folder.

    Usage:
        data.excel_view()
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    target_folder = Path(folder) if folder is not None else Path(tempfile.gettempdir())
    target_folder.mkdir(parents=True, exist_ok=True)

    file_name = f"{timestamp}_{filename_prefix}.csv"
    file_path = target_folder / file_name
    self.to_csv(file_path, index=False)
    return str(file_path)


pd.DataFrame.excel_view = excel_view


# This function performs best subset regression on the given dataset. 
# It evaluates all possible combinations of predictor variables and computes various statistics for each model, including RSS, R², Adjusted R², Mallows' Cp, AIC, and BIC.

def best_subset_regression(X, y):
    
    results = []

    # Full model for Mallows' Cp
    X_full = sm.add_constant(X)
    full_model = sm.OLS(y, X_full).fit()
    
    mse_full = full_model.ssr / full_model.df_resid
    n = len(y)

    # All possible combinations
    for k in range(1, len(X.columns) + 1):

        for variables in itertools.combinations(X.columns, k):

            X_temp = sm.add_constant(X[list(variables)])
            model = sm.OLS(y, X_temp).fit()

            rss = model.ssr
            r2 = model.rsquared
            adj_r2 = model.rsquared_adj
            aic = model.aic
            bic = model.bic

            # Number of parameters including intercept
            p = k + 1

            # Mallows' Cp
            cp = (rss / mse_full) - (n - 2 * p)

            results.append({
                "Variables": ", ".join(variables),
                "RSS": rss,
                "R2": r2,
                "Adj R2": adj_r2,
                "Cp": cp,
                "AIC": aic,
                "BIC": bic
            })

    return pd.DataFrame(results)
