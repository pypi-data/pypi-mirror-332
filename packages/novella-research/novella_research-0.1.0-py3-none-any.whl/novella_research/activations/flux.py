import tensorflow as tf
from tensorflow import keras
from keras.layers import Layer


class flux(Layer):
    def __init__(self, activation, **kwargs):
        super(flux, self).__init__(**kwargs)
        self.activation = activation

    def build(self, input_shape):
        self.W = self.add_weight(
            shape=(1,)
        )

        self.b = self.add_weight(
            shape=(1,)
        )

    def call(self, inputs):
        return keras.activations.get(self.activation)((self.W * inputs) + self.b)
