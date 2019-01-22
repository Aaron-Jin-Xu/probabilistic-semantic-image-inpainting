import os
import sys
import numpy as np
from PIL import Image
import data.celeba_data as celeba_data
import data.church_outdoor_data as church_outdoor_data
import data.binarized_mnist_data as binarized_mnist_data


class DataSet(object):
    pass

class CelebA(DataSet):

    def __init__(self, data_dir, batch_size, img_size, rng=np.random.RandomState(None)):
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.img_size = img_size
        self.rng = rng

    def train(self, shuffle=True, limit=-1):
        return celeba_data.DataLoader(self.data_dir, 'train', self.batch_size,
                rng=self.rng, shuffle=shuffle, size=self.img_size, limit=limit)

    def test(self, shuffle=False, limit=-1):
        return celeba_data.DataLoader(self.data_dir, 'valid', self.batch_size,
                rng=self.rng, shuffle=shuffle, size=self.img_size, limit=limit)

class ChurchOutdoor(DataSet):

    def __init__(self, data_dir, batch_size, img_size, rng=np.random.RandomState(None)):
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.img_size = img_size
        self.rng = rng

    def train(self, shuffle=True, limit=-1):
        return church_outdoor_data.DataLoader(self.data_dir, 'train', self.batch_size,
                rng=self.rng, shuffle=shuffle, size=self.img_size, limit=limit)

    def test(self, shuffle=False, limit=-1):
        return church_outdoor_data.DataLoader(self.data_dir, 'valid', self.batch_size,
                rng=self.rng, shuffle=shuffle, size=self.img_size, limit=limit)


class BinarizedMNIST(DataSet):

    def __init__(self, data_dir, batch_size, img_size, rng=np.random.RandomState(None)):
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.img_size = img_size
        self.rng = rng

    def train(self, shuffle=True, limit=-1):
        return binarized_mnist_data.DataLoader(self.data_dir, 'train', self.batch_size,
                rng=self.rng, shuffle=shuffle, size=self.img_size, limit=limit)

    def test(self, shuffle=False, limit=-1):
        return binarized_mnist_data.DataLoader(self.data_dir, 'valid', self.batch_size,
                rng=self.rng, shuffle=shuffle, size=self.img_size, limit=limit)
