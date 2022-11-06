# storage
names = []
idx = []


# establish connection
key = '';
comm = smartwaiver.Smartwaiver(key)

# signed waivers
overview = comm.get_waiver_summaries()
print("Waivers:\n")

# list waiver info
for i in overview:
  print(i.waiver_id + ': ' + i.title)
  
  
