# import configargparse
# parser = configargparse.ArgumentParser(allow_abbrev=False)

##########
### All Constants
### Used in other scripts

TRAINING_DATA_FILE = "data/dow_30_2009_2020.csv"

TRAINED_MODEL_DIR = "trained_models"
TURBULENCE_DATA = "data/dow30_turbulence_index.csv"

TESTING_DATA_FILE = "test.csv"

# shares normalization factor
# 100 shares per trade
HMAX_NORMALIZE = 100
# initial amount of money we have in our account
INITIAL_ACCOUNT_BALANCE=1000000
# total number of stocks in our portfolio
STOCK_DIM = 30
# transaction fee: 1/1000 reasonable percentage
TRANSACTION_FEE_PERCENT = 0.001

# TODO: Get rid of turbulence threshold
# turbulence index: 120 reasonable threshold
TURBULENCE_THRESHOLD = 120
# Normalization factor: (not used)
#MAX_ACCOUNT_BALANCE = 2147483647
#MAX_NUM_SHARES = 2147483647
#MAX_CLOSE_PRICE = 5000
