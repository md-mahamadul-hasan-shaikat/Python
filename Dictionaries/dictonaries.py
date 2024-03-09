
stuentId = {
    "101" : "MHS 1",
    "102" : "MHS 2",
    "103" : "MHS 3",
    "104" : "MHS 4",
    "105" : "MHS 5",
}

#print(stuentId["101"])

#print(stuentId.get('103'))

print(stuentId.get('106', 'Not a valid key'))