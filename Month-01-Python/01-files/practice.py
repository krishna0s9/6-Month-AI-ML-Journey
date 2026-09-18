with open('Month-01-Python/01-files/diva.jpeg', 'rb') as rf:
 with open('Month-01-Python/01-files/diva_copy.jpeg', 'wb') as wf:
  chunk_size = 4098
  rf_chunk= rf.read(chunk_size)
  while len(rf_chunk) > 0:
    wf.write(rf_chunk)
    rf_chunk= rf.read(chunk_size)