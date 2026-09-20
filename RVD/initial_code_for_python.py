# ─────────────────────────────────────
# Setup
# ─────────────────────────────────────

# Cleaning the Environment ================================

%reset -sf

# =========================================================

# Loading Libraries ======================================
import gc
import random
import numpy as np
import pandas as pd

# Garbage collection
gc.collect()

# Reproducibility
random.seed(123)
np.random.seed(123)

# Display numbers without scientific notation
np.set_printoptions(suppress=True)
pd.set_option("display.float_format", "{:.6f}".format)