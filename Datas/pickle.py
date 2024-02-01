import pickle as pk

data_dict = {
    'books': 12,
    'articles': 100,
    'subjects': [
        'math',
        'programing',
        'python'
    ]
}

with open('reading.pk', 'wb') as f:
    pk.dump(data_dict,f)
    
with open('reading.pk', 'rb') as f:
    data = pk.load(f)