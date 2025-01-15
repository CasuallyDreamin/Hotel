from ds import hashtable
ht = hashtable()

ht.add(10, "hi")
ht.add(12, "bye")
ht.add(13, "gg")
ht.add(4, "bee")
ht.add(5, "bee")
ht.add(6, "bee")
ht.add(9, "bee")
ht.add(10, "ten")
ht.table.show_all()
print(ht.table.size)
print(ht.get_by_key(10))