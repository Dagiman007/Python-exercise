def gen_records(path):
    with open(path) as handle:
        record = {}
        for line in handle:
            if line == '\n':
                yield record
                record = {}
                continue
            key, value = line.strip('\n').split(': ', 1)
            record[key] = value


for record in gen_records(r'C:\Users\DagiMan\Desktop\Python Programming - CBT Nuggets\Exercise\Articles.txt'):
    print('{} had {} requests in the past hour'.format(record['article'], record['requests']))
