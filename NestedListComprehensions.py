rooms = [[{'age': 14, 'hobby': 'horses', 'name': 'A'}, 
          {'age': 12, 'hobby': 'piano', 'name': 'B'}, 
          {'age': 9, 'hobby': 'chess', 'name': 'C'}], 
        [{'age': 15, 'hobby': 'programming', 'name': 'D'}, 
         {'age': 17, 'hobby': 'driving', 'name': 'E'}], 
        [{'age': 45, 'hobby': 'writing', 'name': 'F'}, 
         {'age': 43, 'hobby': 'chess', 'name': 'G'}]]

per = [person['name'] 
    for room in rooms
    for person in room
    if person['hobby'] == 'chess']

for p in per:
    print(p, end = ' ')
