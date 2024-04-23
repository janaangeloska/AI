import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB


# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'], 
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'], 
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    
    data = dataset
    classifier = GaussianNB()

    train_raw = data[:int(0.85 * len(data))]
    test_raw = data[int(0.85 * len(data)):]

    train = []
    for r in train_raw:
        red = [float(el) for el in r[:-1]]
        red.append(int(r[-1]))
        train.append(red)

    test = []
    for r in test_raw:
        red = [float(el) for el in r[:-1]]
        red.append(int(r[-1]))
        test.append(red)

    train_X = [redici[:-1] for redici in train]
    train_Y = [redici[-1] for redici in train]
    test_X = [redici[:-1] for redici in test]
    test_Y = [redici[-1] for redici in test]

    classifier.fit(train_X, train_Y)

    counter = 0

    for vlezz, klasaa in zip(test_X, test_Y):
        new_klasaa = classifier.predict([vlezz])[0]
        if new_klasaa == klasaa:
            counter += 1

    accurate = counter / len(test)

    vlez = input()
    vlez = vlez.split(' ')
    vlez = [float(element) for element in vlez]
    vlez_klasa = classifier.predict([vlez])[0]
    vlez_klasa_prob = classifier.predict_proba([vlez])
    print(accurate)
    print(int(vlez_klasa))
    print(vlez_klasa_prob)

    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    submit_classifier(classifier)
    
    # povtoren import na kraj / ne ja otstranuvajte ovaa linija
    from submission_script import *
