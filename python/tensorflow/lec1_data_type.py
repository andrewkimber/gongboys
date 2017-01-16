import tensorflow as tf

ph = tf.placeholder(dtype=tf.float32, shape=[3, 3])
# variable needs initialization. Weight data are mostly seeded in variable data type.
var = tf.Variable([1, 2, 3, 4, 5], dtype=tf.float32)
# literally constant data type. doesn't require initialization.
const = tf.constant([10, 20, 30, 40, 50], dtype=tf.float32)

image = [[1, 2, 3, 4, 5],
         [5, 4, 3, 2, 1]]
label = [10, 20, 30, 40, 50]

ph_image = tf.placeholder(dtype=tf.float32)
ph_label = tf.placeholder(dtype=tf.float32)

feed_dict = {ph_image: image, ph_label: label}

result_tensor = ph_image + ph_label

sess = tf.Session()
result = sess.run(result_tensor, feed_dict=feed_dict)
print result
