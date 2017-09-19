import input_data
import tensorflow as tf

NUM_CLASS = 10
IMAGE_SIZE = 28
IMAGE_PIXEL = IMAGE_SIZE * IMAGE_SIZE

mnist = input_data.read_data_sets("/MNIST/",one_hot=True)
sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32, [None,IMAGE_PIXEL])
W = tf.Variable(tf.zeros([IMAGE_PIXEL,NUM_CLASS]))
b = tf.Variable(tf.zeros([NUM_CLASS]))
y = tf.nn.softmax(tf.matmul(x,W) + b )

y_ = tf.placeholder(tf.float32, [None,NUM_CLASS])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

tf.initialize_all_variables().run()
for i in range(1000):
  batch_xs,batch_ys = mnist.train.next_batch(100)
  train_step.run({x:batch_xs, y_:batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(accuracy.eval({x:mnist.test.images, y_:mnist.test.labels}))

