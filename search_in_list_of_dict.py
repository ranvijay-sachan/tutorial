>>> dicts = [
...     { "name": "Tom", "age": 10 },
...     { "name": "Mark", "age": 5 },
...     { "name": "Pam", "age": 7 },
...     { "name": "Dick", "age": 12 }
... ]

>>> next(item for item in dicts if item["name"] == "Pam")
{'age': 7, 'name': 'Pam'}
