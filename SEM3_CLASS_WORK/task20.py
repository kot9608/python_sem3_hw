# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит


d = [{"V": "S001"}, {"VI": "S001"}, {"V": "S002"}, {"VII": "S005"},
{"V": "S009"}, {"VI": "S005"}, {"VIII": "S007"}]
new_set = set()
for i in d:
  for k in i.values():
    new_set.add(k)
print(new_set)


#print(set((list(k.values())[0]) for k in d))