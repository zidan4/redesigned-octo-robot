def receive_from(connection):

  buffer = ""
  # We set a 2 second timeout; depending on your
  # target, this may need to be adjusted
  connection.settimeout(2)
  try:
  # keep reading into the buffer until
  # there's no more data
  # or we time out
    while True:
      data = connection.recv(4096)
      if not data:
      break
      buffer += data
  except:
  pass
  return buffer
