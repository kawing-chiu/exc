import tensorflow as tf

n_epochs = 1

# use cmd `tensorboard --logdir <log_dir>` to show log
log_dir = '/tmp/test/linear_model'

# Model parameters
W = tf.Variable([.3], dtype=tf.float32, name='weight')
b = tf.Variable([-.3], dtype=tf.float32, name='offset')
# Model input and output
x = tf.placeholder(tf.float32, name='x')
linear_model = W*x + b
y = tf.placeholder(tf.float32, name='y')

# loss
loss = tf.reduce_sum(tf.square(linear_model - y), name='loss') # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss, name='minimize')

# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]
# training loop
init = tf.global_variables_initializer()
with tf.Session() as sess:
    writer = tf.summary.FileWriter(log_dir, sess.graph)
    sess.run(init) # reset values to wrong
    for i in range(n_epochs):
      sess.run(train, {x: x_train, y: y_train})
    
    # evaluate training accuracy
    curr_W, curr_b, curr_loss = sess.run(
        [W, b, loss], {x: x_train, y: y_train})
    print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))

print("Use 'tensorboard --logdir {}' to visualize".format(log_dir))

