import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# HYPERPARAMETERS
IMAGE_SIZE = 28
PATCH_SIZE = 5
STRIDES = 1
POOL_SIZE = 2
CONV1_FEATS = 32
CONV2_FEATS = 64
FC_NEURONS = 1024
CLASSES = 10


# FUNCTIONS
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, STRIDES, STRIDES, 1], padding='SAME')


def max_pool(x):
    return tf.nn.max_pool(x, ksize=[1, POOL_SIZE, POOL_SIZE, 1], strides=[1, POOL_SIZE, POOL_SIZE, 1], padding='SAME')


# INPUT LOADING & RESHAPING
mnist = input_data.read_data_sets("MNIST data/", one_hot=True)

x = tf.placeholder(tf.float32, [None, IMAGE_SIZE * IMAGE_SIZE])
x_image = tf.reshape(x, [-1, IMAGE_SIZE, IMAGE_SIZE, 1])
y_ = tf.placeholder(tf.float32, [None, CLASSES])
keep_prob = tf.placeholder(tf.float32)

######
W_conv1 = weight_variable([PATCH_SIZE, PATCH_SIZE, 1, CONV1_FEATS])
b_conv1 = bias_variable([CONV1_FEATS])

W_conv2 = weight_variable([PATCH_SIZE, PATCH_SIZE, CONV1_FEATS, CONV2_FEATS])
b_conv2 = bias_variable([CONV2_FEATS])

W_fc1 = weight_variable([7*7*CONV2_FEATS, FC_NEURONS])
b_fc1 = bias_variable([FC_NEURONS])

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

######
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool(h_conv1)

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool(h_conv2)

h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2


sess = tf.Session()

#####
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_conv, y_))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
sess.run(tf.global_variables_initializer())
with sess.as_default():
    for i in range(2000):
        batch = mnist.train.next_batch(20)
        if i % 100 == 0:
            train_accuracy = accuracy.eval(feed_dict={
                x: batch[0], y_: batch[1], keep_prob: 1.0})
            print("step %d, training accuracy %g" % (i, train_accuracy))
        train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

    print("test accuracy %g" % accuracy.eval(feed_dict={
        x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))
