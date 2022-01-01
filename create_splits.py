import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger
from pathlib import Path


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # TODO: Implement function

    if not os.path.exists(source + "/train"):
        os.makedirs(source + "/train")

    if not os.path.exists(source + "/val"):
        os.makedirs(source + "/val")

    if not os.path.exists(source + "/test"):
        os.makedirs(source + "/test")

    result = glob.glob(source + "/*.tfrecord")

    random.shuffle(result)

    resultSize = len(result)
    startIdx = int(0.0*resultSize)
    endIdx = int(0.8*resultSize)
    print("train: ", startIdx," - ", endIdx)
    result_train = result[startIdx : endIdx]
    for path in result_train:
        lStr = path.split("/")
        os.symlink(path, source + "/train/" + lStr[-1])  

    startIdx = int(0.8*resultSize)
    endIdx = int(0.9*resultSize)
    print("val: ", startIdx," - ", endIdx)
    result_val = result[startIdx : endIdx]
    for path in result_val:
        lStr = path.split("/")
        os.symlink(path, source + "/val/" + lStr[-1])  

    startIdx = int(0.9*resultSize)
    endIdx = int(1.0*resultSize)
    print("test: ", startIdx," - ", endIdx)
    result_test = result[startIdx : endIdx]
    for path in result_test:
        lStr = path.split("/")
        os.symlink(path, source + "/test/" + lStr[-1])  


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)