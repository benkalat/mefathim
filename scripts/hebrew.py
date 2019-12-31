#!/home/mefath5/.local/bin/python3


import sys, codecs


# Note this line. It's the important one
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) 

print ("Content-Type: text/plain; charset=UTF-8\n")
try:

	print( 'ככה כותבים עברית בפייתון'  )

except BaseException as e:
    print('Failed to do something: ' + str(e))

