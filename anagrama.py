

def  solution(A):
	if len(A) == 1:
		return 1

	b = 0
	for v in A:		
		b = b^ 1 << ord(v) - ord('a')
	valor =   (b & (b - 1))
	if valor == 0:
		return 1
	else: 
		return 0




print solution("codility")		