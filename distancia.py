def adjacent ( A, B, C ):
    return A < B < C or A > B > C
 
#array = map(int, raw_input().split())
array = [ 0, 3, 3, 7, 5, 3, 11, 1 ]
#num_test = input()
for r in xrange( len(array) ):
	P, Q = ( int(P) for P in raw_input().split() )
	for i, h in enumerate( array ):
		if i != P and i != Q:
			if adjacent ( array[P], h, array[Q] ):
				print "The indexs have no adjacent values-> index", i
				break;
	else:
		print "Indices " + str(P) + " and " + str(Q), "have adjacent values"