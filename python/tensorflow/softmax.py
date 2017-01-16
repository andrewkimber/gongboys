import tensorflow as tf
import numpy as np

x_data = np.transpose([[1., 1., 1., 1., 1., 1., 1., 1.],
                       [2., 3., 3., 5., 7., 2., 6., 7.],
                       [1., 2., 4., 5., 5., 5., 6., 7.]])
y_data = np.transpose([[0, 0, 0, 0, 0, 0, 1, 1],
                       [0, 0, 0, 1, 1, 1, 0, 0],
                       [1, 1, 1, 0, 0, 0, 0, 0]])

X = tf.placeholder("float", [None, 3])
Y = tf.placeholder("float", [None, 3])

W = tf.Variable(tf.zeros([3, 3]))

hypothesis = tf.nn.softmax(tf.matmul(X, W))

learning_rate = 0.01

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), reduction_indices=1))

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in xrange(2001):
    sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
    if step % 200 == 0:
        print step, sess.run(cost, feed_dict={X: x_data, Y: y_data})
        print sess.run(W)
