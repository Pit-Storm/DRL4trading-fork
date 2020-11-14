# Set TF Loglevel
import os
import logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.get_logger().setLevel(logging.ERROR)

# common library
import pandas as pd
import numpy as np
import time
from stable_baselines.common.vec_env import DummyVecEnv

# preprocessor
from preprocessing.preprocessors import *
# config
from config.config import *
# model
from model.models import *


def run_model() -> None:
    """Train the model."""

    # read and preprocess data
    # TODO: Read in own Data
    data = preprocess_data()
    data = add_turbulence(data)

    # 2015/10/01 is the date that validation starts
    # 2016/01/01 is the date that real trading starts
    # unique_trade_date needs to start from 2015/10/01 for validation purpose
    # TODO: this has to be a datetime range which all the dates except the first half (minus 3 months)
    unique_trade_date = data[(data.datadate > 20151001)&(data.datadate <= 20200707)].datadate.unique()

    # rebalance_window is the number of months (=Number/21) to retrain the model
    # validation_window is the numeber of months (=Number/21) to validate the model and select for trading
    # TODO: set this as a datetime element which counts the number of days.
    rebalance_window = 63
    validation_window = 63
    
    ## Ensemble Strategy
    run_ensemble_strategy(df=data, 
                          unique_trade_date= unique_trade_date,
                          rebalance_window = rebalance_window,
                          validation_window=validation_window)

    #_logger.info(f"saving model version: {_version}")

if __name__ == "__main__":
    run_model()
