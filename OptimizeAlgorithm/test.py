popolation = [
    {
        'id': 1,
        'value': [1, 2, 3, 4],
        'late': 0
    },
    {
        'id': 2,
        'value': [1, 2, 4, 3],
        'late': 3
    },
    {
        'id': 3,
        'value': [1, 2, 3, 4],
        'late': 1
    },
    {
        'id': 4,
        'value': [1, 2, 4, 3],
        'late': 3
    },
]

popolation.sort(key=lambda x: x['late'])
d ={}

for p in popolation:
    d[p['late']] = p
    # print(d)
popolation = d.values()

print(popolation)
       

