import tensorflow as tf
import matplotlib.pyplot as plt

X = [1., 2., 3.]
Y = [1., 2., 3.]

W = tf.placeholder(tf.float32)

hypothesis = tf.mul(X, W)

cost = tf.reduce_mean(tf.pow(hypothesis - Y, 2))

init = tf.global_variables_initializer()

W_val = []
cost_val = []

sess = tf.Session()
sess.run(init)
for i in range(-30, 50):
    cost_i = sess.run(cost, feed_dict={W: i * 0.1})
    print i * 0.1, cost_i
    W_val.append(i * 0.1)
    cost_val.append(cost_i)

plt.plot(W_val, cost_val, 'ro')
plt.ylabel('Cost')
plt.xlabel('W')
plt.show()
