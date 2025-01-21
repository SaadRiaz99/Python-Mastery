# Generator Pipelines

def read_data():
    for i in range(100):
        yield {'id': i, 'value': i * 10, 'active': i % 3 == 0}

def filter_active(records):
    for r in records:
        if r['active']:
            yield r

def transform(records):
    for r in records:
        r['value'] = r['value'] * 2
        yield r

def take(n, records):
    for i, r in enumerate(records):
        if i >= n:
            break
        yield r

# Pipeline
pipeline = take(5, transform(filter_active(read_data())))
for item in pipeline:
    print(item)

