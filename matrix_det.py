#find determinant of 2x2 and 3x3 and 4x4 matricies - straightforward
import numpy as np

def main():
	def row_col(a,b):
		c = a*b
		A = np.arange(c)
		A = A.reshape(a,b)
		return A
		
	def fill_entry(A):
		row = len(A)
		col = len(A[0])
		A = A.reshape(1, row*col)
		i = 0
		while i < (row*col):
			if i == 0:
				a = float(input('What is your first entry? '))
				A[0,i] = a
				i += 1
			elif 0 < i < (row*col)-1:
				b = float(input('What is your next entry? '))
				A[0,i] = b
				i += 1
			elif i == (row*col)-1:
				c = float(input('What is your final entry? '))
				A[0,i] = c
				i += 1
		A = A.reshape(row, col)
		return A
	
	def sq_check(a,b):
		if a == b and 1 < a < 5:
			return True
		else:
			return False
		
	def matrix_builder():
		r = int(input('How many rows are there? '))
		c = int(input('How many columns are there? '))
		ans = sq_check(r, c)
		if ans == True:
			M = row_col(r, c)
			fill_entry(M)
			print(M)
			return M
		else:
			return 'No'
	
	def matrix2_det(M):
		a = M[0,0]
		b = M[0,1]
		c = M[1,0]
		d = M[1,1]
		det = (a*d)-(b*c)
		#print('The determinant is ' + str(det))
		return det
		
	def matrix3_det(M):
		a = M[0,0]
		b = M[0,1]
		c = M[0,2]
		M1 = np.delete(M, 0, axis = 1)
		M1 = np.delete(M1, 0, axis = 0)
		M2 = np.delete(M, 1, axis = 1)
		M2 = np.delete(M2, 0, axis = 0)
		M3 = np.delete(M, 2, axis = 1)
		M3 = np.delete(M3, 0, axis = 0)
		det = a*(matrix2_det(M1)) - b*(matrix2_det(M2)) + c*(matrix2_det(M3))
		#print('The determinat is ' + str(det))
		return det
	
	def matrix4_det(M):
		a = M[0,0]
		b = M[0,1]
		c = M[0,2]
		d = M[0,3]
		M1 = np.delete(M, 0, axis = 1)
		M1 = np.delete(M1, 0, axis = 0)
		M2 = np.delete(M, 1, axis = 1)
		M2 = np.delete(M2, 0, axis = 0)
		M3 = np.delete(M, 2, axis = 1)
		M3 = np.delete(M3, 0, axis = 0)
		M4 = np.delete(M, 3, axis = 1)
		M4 = np.delete(M4, 0, axis = 0)
		det = a*(matrix3_det(M1)) - b*(matrix3_det(M2)) + c*(matrix3_det(M3)) - d*(matrix3_det(M4))
		#print(det)
		return det
	
	def determinant(M):
		n = len(M)
		if n == 2:
			d = matrix2_det(M)
			print('The determinant is ' + str(d))
		elif n == 3:
			d = matrix3_det(M)
			print('The determinant is ' + str(d))
		elif n == 4:
			d = matrix4_det(M)
			print('The determinant is ' + str(d))
			
	def all_together_det():
		X = matrix_builder()
		if X != 'No':
			determinant(X)
		else:
			print('Cannot do determinant calculation. Either matrix is not square or matrix dimension is too large.')
			
	all_together_det()
	
	reset = input('Is there another determinant you need? ').lower()
	if reset == 'y' or reset == 'yes':
		main()
	else:
		print('Okay')
		
main()
