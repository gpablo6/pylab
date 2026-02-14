"""
Week 1 - Hello World video

To run this code using poetry you can do `poetry run python src/hello_world.py`
from the root of the project.
"""

# Import the required libraries
import tensorflow as tf
import numpy as np

# Model definition. Basic NN with 1 layer and 1 neuron
model = tf.keras.Sequential([
    # Define the input shape
    tf.keras.Input(shape=(1,)),
    # Add a Dense layer with 1 neuron
    tf.keras.layers.Dense(units=1)
])

if __name__ == "__main__":
    # Compile the model`
    model.compile(
        optimizer='sgd',
        loss='mean_squared_error'
    )

    # Create sample test data
    xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
    ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

    # Train the model
    model.fit(xs, ys, epochs=500)

    # Predict a sample value
    result = model.predict(np.array([10.0]))

    # Print the result
    print(f"Prediction for 10.0: {result}")

    # NOTE: The result is not exactly 19.0 because the model is not perfectly
    # fitted, but it is close enough.
