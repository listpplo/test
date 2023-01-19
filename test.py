# Setting the random seed 
tf.random.set_seed(42)

#1. creating the model using TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1)   # Dense function gives the number of neurons in the layer

])

#2. compiling the model
model.compile(loss =tf.keras.losses.mae,    # mae  --> Mean absolute error
              optimizer = tf.keras.optimizers.SGD(),
              metrics = ["mae"])

#3. Fit the model

model.fit(tf.expand_dims(X,axis = -1),Y, epochs = 10)
