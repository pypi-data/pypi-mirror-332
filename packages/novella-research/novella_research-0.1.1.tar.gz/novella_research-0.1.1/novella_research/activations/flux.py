import tensorflow as tf
from tensorflow import keras
from keras.layers import Layer


class flux(Layer):
    def __init__(self, activation, **kwargs):
        super(flux, self).__init__(**kwargs)
        self.activation = activation

    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(1,)
        )

        self.b = self.add_weight(
            shape=(1,)
        )

    def call(self, inputs):
        if self.activation == 'none':
            return (self.w * inputs) + self.b
        else:
            activation_function = keras.activations.get(self.activation)
            return activation_function(self.w * activation_function(inputs) + self.b)
