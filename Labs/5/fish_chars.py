import os

from sklearn.ensemble import RandomForestClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]


if __name__ == '__main__':
    # Vashiot kod tuka
    data = dataset
    col_index = int(input())
    n = int(input())
    kriteria = input()
    new_record = input()
    new_record = new_record.split(" ")
    split_index_from = col_index + 1
    classifier = RandomForestClassifier(n_estimators=n, criterion=kriteria, random_state=0)

    data = [row[:col_index] + row[split_index_from:] for row in data]
    new_record = new_record[:col_index] + new_record[split_index_from:]

    train = data[:int(0.85 * len(data))]
    test = data[int(0.85 * len(data)):]

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

    vlez_klasa = classifier.predict([new_record])[0]
    vlez_klasa_prob = classifier.predict_proba([new_record])[0]

    print(f'Accuracy: {accurate}')
    print(vlez_klasa)
    print(vlez_klasa_prob)

    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    submit_classifier(classifier)
