import os
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    data = dataset
    encoder = OrdinalEncoder()
    classifier = CategoricalNB()
    
    encoder.fit([redici[:-1] for redici in data])
    
    train = data[:int(0.75 * len(data))]
    test = data[int(0.75 * len(data)):]
    train_X = [redici[:-1] for redici in train]
    train_Y = [redici[-1] for redici in train]
    test_X = [redici[:-1] for redici in test]
    test_Y = [redici[-1] for redici in test]
    train_x_transf = encoder.transform(train_X)
    test_x_transf = encoder.transform(test_X)
    classifier.fit(train_x_transf, train_Y)

    counter = 0

    for vlezz, klasaa in zip(test_x_transf, test_Y):
        new_klasaa = classifier.predict([vlezz])[0]
        if new_klasaa == klasaa:
            counter += 1

    accurate = counter / len(test)

    vlez = input()
    vlez = vlez.split(' ')
    enc = encoder.transform([vlez])
    vlez_klasa = classifier.predict(enc)[0]
    vlez_klasa_prob = classifier.predict_proba(enc)
    print(accurate)
    print(vlez_klasa)
    print(vlez_klasa_prob)

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    train_X = train_x_transf
    test_X = test_x_transf
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # # submit na encoderot
    submit_encoder(encoder)

    # # povtoren import na kraj / ne ja otstranuvajte ovaa linija
    from submission_script import *


