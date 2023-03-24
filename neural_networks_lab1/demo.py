import numpy as np
from matplotlib import pyplot as plt
import main
import utils
import random

if __name__ == '__main__':
    #training
    x_train, y_train = utils.load_data('dataset/train/')
    #changing the number of layers
    layers = 2
    model = main.build_model(layers, x_train.shape)
    print(model.summary())
    print("Number of layers:", layers)
    res = model(x_train)
    print(res)
    model.compile(optimizer='adam', loss='binary_crossentropy',
                  metrics=['accuracy'])
    H = model.fit(x_train, y_train, batch_size=10, epochs=100, validation_split=0.2)
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0, 100), H.history["loss"], label="train_loss")
    plt.plot(np.arange(0, 100), H.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, 100), H.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, 100), H.history["val_accuracy"], label="val_acc")
    plt.title("Training Loss and Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend()
    plt.show()

    #testing
    x_test, y_test = utils.load_data('dataset/test/')
    y_pred = model.predict(x_test, batch_size=10)
    print(y_pred)
    for i in range(16):
        ax = plt.subplot(4, 4, i + 1)
        c = 83
        j = i + c
        plt.imshow(x_test[j])
        plt.title(main.normalize_prediction(y_pred[i]))
        plt.axis("off")
    plt.show()
