# from autokeras.classifier import ImageClassifier
import autokeras as ak
from keras.datasets import mnist

clf = ak.ImageClassifier(verbose=True, augment=False)

if __name__ == '__main__':
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(x_train.shape + (1,))
    x_test = x_test.reshape(x_test.shape + (1,))

    # clf = ImageClassifier(verbose=True, augment=False)
    clf.fit(x_train, y_train, time_limit=12 * 60 * 60)
    clf.final_fit(x_train, y_train, x_test, y_test, retrain=True)
    y = clf.evaluate(x_test, y_test)
    print(y * 100)
