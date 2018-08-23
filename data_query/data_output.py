#coding=utf-8
"""

author:k
date:2018.8.20
"""

import json


data_path = '1580_en_900_des.json'
train_path = 'query_train'
val_path = 'query_val'
test_path = 'query_test'


query_data = []
with open(data_path, 'r') as f:
    query_data = [json.loads(line) for line in f.readlines()]

query_train = query_data[0:2200]
query_val = query_data[2201:2400]
query_test = query_data[2401:]

with open(train_path, 'w') as f:
    for q in query_train:
        try:
            f.write(q['true_label'])
            f.write('\t')
            f.write(q['query'].encode('utf-8'))
            f.write('\n')
        except Exception as e:
            print e.message
            print q

with open(val_path, 'w') as f:
    for q in query_val:
        f.write(q['true_label'])
        f.write('\t')
        f.write(q['query'].encode('utf-8'))
        f.write('\n')

with open(test_path, 'w') as f:
    for q in query_test:
        f.write(q['true_label'])
        f.write('\t')
        f.write(q['query'].encode('utf-8'))
        f.write('\n')

