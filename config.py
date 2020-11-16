# import configargparse
# parser = configargparse.ArgumentParser(allow_abbrev=False)

##########
### All Constants
### Used in other scripts

TRAINING_DATA_FILE = "data/dow_30_2009_2020.csv"

TRAINED_MODEL_DIR = "trained_models"

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
