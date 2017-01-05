require 'decisiontree'

attributes = ['Temperature']
training = [
  [36.6, 'healthy'],
  [37, 'sick'],
  [38, 'sick'],
  [36.7, 'healthy'],
  [40, 'sick'],
  [50, 'really sick'],
]

# Instantiate the tree, and train it based on the data (set default to '1')
dec_tree = DecisionTree::ID3Tree.new(attributes, training, 'sick', :continuous)
dec_tree.train

test = [37, 'sick']
decision = dec_tree.predict(test)
puts "Predicted: #{decision} ... True decision: #{test.last}"

# => Predicted: sick ... True decision: sick

# Specify type ("discrete" or "continuous") in the training data
labels = ["hunger", "color"]
training = [
        [8, "red", "angry"],
        [6, "red", "angry"],
        [7, "red", "angry"],
        [7, "blue", "not angry"],
        [2, "red", "not angry"],
        [3, "blue", "not angry"],
        [2, "blue", "not angry"],
        [1, "red", "not angry"]
]

dec_tree = DecisionTree::ID3Tree.new(labels, training, "not angry", color: :discrete, hunger: :continuous)
dec_tree.train

test = [7, "red", "angry"]
decision = dec_tree.predict(test)
puts "Predicted: #{decision} ... True decision: #{test.last}"

# => Predicted: angry ... True decision: angry
