import tensorflow as tf

x_data = [[1., 1., 1., 1., 1.,1.],
          [2., 3., 3., 5., 7.,2.],
          [1., 2., 4., 5., 5.,5.]]
y_data = [0,0,0,1,1,1]

X=tf.placeholder(tf.float32)
Y=tf.placeholder(tf.float32)

W = tf.Variable(tf.random_uniform([1, 3], -1.0, 1.0))

h= tf.matmul(W, x_data)

hypothesis = tf.sigmoid(h)

cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y)*tf.log(1-hypothesis))

a = tf.Variable(0.1)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in xrange(2001):
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    if step % 20 == 0:
        print step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W)
