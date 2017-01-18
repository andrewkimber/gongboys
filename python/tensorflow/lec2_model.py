import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

train = False

mnist = input_data.read_data_sets("MNIST data/", one_hot=True)

# tensor sizes
INPUT_SIZE = 784
HIDDEN1_SIZE = 150
CLASSES = 10

x = tf.placeholder(tf.float32, shape=[None, INPUT_SIZE], name='x')
y_ = tf.placeholder(tf.float32, shape=[None, CLASSES], name='y_')

W_h1 = tf.Variable(tf.truncated_normal(shape=[INPUT_SIZE, HIDDEN1_SIZE]), dtype=tf.float32, name='W_h1')
b_h1 = tf.Variable(tf.zeros(shape=[HIDDEN1_SIZE]), dtype=tf.float32, name='b_h1')

W_o = tf.Variable(tf.truncated_normal(shape=[HIDDEN1_SIZE, CLASSES]), dtype=tf.float32, name='W_o')
b_o = tf.Variable(tf.zeros(shape=[CLASSES]), dtype=tf.float32, name='b_o')


param_list = [W_h1, b_h1, W_o, b_o]
saver = tf.train.Saver(param_list)

hidden1 = tf.sigmoid(tf.matmul(x, W_h1) + b_h1)
y = tf.nn.softmax(tf.matmul(hidden1, W_o) + b_o)

if train:
    # cost function
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

    rate = 1
    train_step = tf.train.GradientDescentOptimizer(rate).minimize(cross_entropy)

    init = tf.global_variables_initializer()

    sess = tf.Session()
    sess.run(init)

    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        _, loss = sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y_: batch_ys})
        if i % 100 == 0:
            saver.save(sess, './mnist_cnn.ckpt')
            print loss

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

else:
    sess = tf.Session()
    saver.restore(sess, './mnist_cnn.ckpt')
    result = sess.run(tf.argmax(y, 1), feed_dict={x: mnist.test.images})
    print(result)
    print sess.run(tf.argmax(y_, 1), feed_dict={y_: mnist.test.labels})

