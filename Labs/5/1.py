import os

from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier


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
    # Vashiot kod tuka
    data = dataset
    x = int(input())
    kriteria = input()
    encoder = OrdinalEncoder()
    classifier = DecisionTreeClassifier(criterion=kriteria, random_state=0)

    encoder.fit([redici[:-1] for redici in data])

    train = data[int((100 - x) / 100 * len(data)):]
    test = data[:int((100 - x) / 100 * len(data))]

    train_X = [redici[:-1] for redici in train]
    train_Y = [redici[-1] for redici in train]
    test_X = [redici[:-1] for redici in test]
    test_Y = [redici[-1] for redici in test]

    train_x_transf = encoder.transform(train_X)
    test_x_transf = encoder.transform(test_X)

    classifier.fit(train_x_transf, train_Y)

    depth = classifier.get_depth()
    nr_leaves = classifier.get_n_leaves()
    acurr = accuracy_score(test_Y, classifier.predict(test_x_transf))
    feat = list(classifier.feature_importances_)

    print(f'Depth: {depth}')
    print(f'Number of leaves: {nr_leaves}')
    print(f'Accuracy: {acurr}')
    print(f'Most important feature: {feat.index(max(feat))}')
    print(f'Least important feature: {feat.index(min(feat))}')

    train_X = train_x_transf
    test_X = test_x_transf

    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    submit_classifier(classifier)
    
    # submit na encoderot
    submit_encoder(encoder)
