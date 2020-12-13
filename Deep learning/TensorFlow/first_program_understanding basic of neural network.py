import math

import matplotlib.pyplot as plt
import numpy as np
import scipy.special
from sklearn.datasets import make_blobs


class NeuralNetwork:
    def __init__(self, inputnodes, hiddenodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddenodes
        self.onodes = outputnodes
        self.lrate = learningrate
        # self.wih=np.random.rand(3,3)-.5 #weight between input and hidden layet
        self.wih = np.random.normal(0, pow(self.hnodes, -0.5), (self.hnodes,
                                                                self.inodes))  # this will also give random weight but its according to formula (weight =1/sqrt(number of incoming links).
        # pow(self.hnodes, -0.5)=standard deviation
        # (self.hnodes, self.inodes)=size of matrix
        # self.who = np.random.rand(3, 3) - .5 #weight between hidden and output layer
        self.who = np.random.normal(0, pow(self.onodes, -0.5), (self.onodes,
                                                                self.hnodes))  # this will also give random weight but its according to formula (weight =1/sqrt(number of incoming links).
        self.activation_function = lambda x: scipy.special.expit(x)
        # self.activation_function =lambda x: np.maximum(x, 0)

        pass

    def train(self, input_list, target_list):
        input_array = np.array(input_list, ndmin=2).T  # here we need transpose matrix
        target_array = np.array(target_list, ndmin=2).T  # here we need transpose matrix
        # print "target array", target_array
        # hidden layer procession
        hidden_input = np.dot(self.wih, input_array)
        hidden_output = self.activation_function(hidden_input)
        # final layer processing
        final_input = np.dot(self.who, hidden_output)
        final_output = self.activation_function(final_input)

        print("final output array", final_output)
        output_error1 = (target_array - final_output) * (target_array - final_output)
        math.sqrt(output_error1)
        output_error = output_error1
        # print "the outut error is" , output_error
        # print "the accuracy is ", np.sum(output_error)
        hidden_error = np.dot(self.who.T, output_error)

        # now calculating final weight  changes
        delta_weight = self.lrate * np.dot((output_error * final_output * (1 - final_output)),
                                           np.transpose(hidden_output))
        self.who += delta_weight
        # print "the delta weight is ",delta_weight
        self.wih += self.lrate * np.dot((hidden_error * hidden_output * (1 - hidden_output)), np.transpose(input_array))
        pass

    # THIS is consider as testing functions
    def test(self, input_list):
        input_array = np.array(input_list, ndmin=2).T  # here we need transpose matrix
        hidden_input = np.dot(self.wih, input_array)
        hidden_output = self.activation_function(hidden_input)

        final_input = np.dot(self.who, hidden_output)
        final_output = self.activation_function(final_input)
        return final_output
        pass


input_nodes = 2
hidden_node = 3
output_node = 1
learning_rate = 0.003
epoch = 3

myneural = NeuralNetwork(inputnodes=input_nodes, hiddenodes=hidden_node, outputnodes=output_node,
                         learningrate=learning_rate)

data_blobs = make_blobs(n_samples=50, n_features=2, centers=4, random_state=75)

print(data_blobs)
feature = data_blobs[0]
labels = data_blobs[1]
plt.scatter(feature[:, 0], feature[:, 1], c=labels)

print("prev weight wih /n:", myneural.wih)
print
print("prev weight who /n:", myneural.who)
# print myneural.query([-.6,.5,-.8])

#
# # data_file = open("mnist_train_100.csv", 'r')
# data_file = open("mnist_train.csv", 'r')
# data_list = data_file .readlines()
# data_file .close()
# target = [.01]

# print data_list[1]
count = 0
new_data = np.arange(0, 12, 2)
x = new_data
# y=-x
for looper in range(epoch):
    for record in feature:
        # all_values = record.split(',')
        # scaled_input = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        # targets = target * 10
        # targets[int(all_values[0])] = 0.99
        scaled_input = record
        targets = labels[count]
        myneural.train(scaled_input, targets)
        if count == 49:
            break
        count = count + 1
        y = (x * myneural.wih[0, 0]) / myneural.wih[0, 1]
        y1 = (x * myneural.wih[1, 0]) / myneural.wih[1, 1]
        y2 = (x * myneural.wih[2, 0]) / myneural.wih[2, 1]
        y1 = (x * myneural.wih[1, 0]) / myneural.wih[1, 1]
        print(x, y)
        plt.scatter(feature[:, 0], feature[:, 1], c=labels)
        plt.plot(x, y)
        plt.plot(x, y1)
        plt.plot(x, y2)
        plt.show()

print("final weight wih /n:", myneural.wih)
print
print("final weight who /n:", myneural.who)
# print myneural.query([-.6,.5,-.8])


'''data_file = open("mnist_test_10.csv", 'r')
data_list = data_file .readlines()
data_file .close()

right_predict_flag=0
status_list=[]
for myrecord in data_list:
    all_values = myrecord.split(',')
    label_val=int(all_values[0])
    print ("the corrent value was ",label_val)
    scaled_input = (np.asfarray(all_values[1:]) / 255.0 * 0.99) +0.01
    mydata= (myneural.test(scaled_input))
    # print mydata
    # print mydata.astype(float)
    # print np.max(mydata)
    predicted_value= np.argmax(mydata)
    print ("the predicted value is ", predicted_value)
    if (label_val== predicted_value):
        right_predict_flag+=1
        status_list.append(1)
    else:
        status_list.append(0)
    #for showing image
    # image_array = np.asfarray(scaled_input.reshape(28, 28))
    # plt.imshow(image_array, cmap='Greys', interpolation='None')
    # plt.show()


print status_list

print ("the accuracy is ", float(float (right_predict_flag)/float(len(status_list))))'''
