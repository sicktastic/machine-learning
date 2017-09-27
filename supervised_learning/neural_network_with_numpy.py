from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs
        random.seed(1)

        # We model a single neuron, with 3 input connections and 1 output connection.
        # We assign random weights to a 3 x 1 matrix, with values in the range -1 to 1
        # and mean

if __name__ == '__main__':

    # Initialize a single neuron nueral network
    neural_network = NeuralNetwork()

    print('Random starting synaptic weights:')
    print neural_network.synaptic_weights

    # The training set.  We have 4 examples, each consisting of 3 input values
    # and 1 output value.

    training_set_inputs = array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    # Training the neural network using a training set.
    #Do it 10,000 times and make small adustments each time
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print("New synaptic weights after taining")
    print neural_network.think(array([1,0,0]))
