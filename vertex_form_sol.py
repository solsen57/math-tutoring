#build quadratic equation from vertex and point
import numpy as np
import math

#f(x) = a*(x-h)**2 + k
#axis of symmetry: x = -(b/2a)
def main():
	def vert_find():
		h = float(input('What is the x-coordinate of the vertex? '))
		k = float(input('What is the y-coordinate of the vertex? '))
		x = float(input('What is the x-coordinate of your reference point? '))
		y = float(input('What is the y-coordinate of your reference point? '))
		a = ((y-k)/((x-h)**2))
		if h >= 0 and k >= 0:
			print('The vertex form is f(x) = ' + str(a) + '(x-' + str(h) + ')^2 + ' + str(k))
		elif h >=0 and k < 0:
			print('The vertex form is f(x) = ' + str(a) + '(x-' + str(h) + ')^2 ' + str(k))
		elif h < 0 and k < 0:
			print('The vertex form is f(x) = ' + str(a) + '(x+' + str(abs(h)) + ')^2 ' + str(k))
		return h,k,a,x,y
		
	def ver_to_quad(h,k,a,x,y):
		b = -h * 2 * a
		c = y - (a*(x**2)) - (b*x)
		return h,k,a,b,c
		
	def quad_to_ver(a,b,c):
		h = -(b/(2*a))
		k = -a*(h**2)+c
		return h,k,a,b,c
		
	def quad_form(a,b,c):
		d = (b**2)-4*a*c
		if d > 0:
			x1 = round((-b - math.sqrt(d))/(2*a),2)
			x2 = round((-b + math.sqrt(d))/(2*a),2)
		elif d == 0:
			x1 = round((-b)/(2*a),2)
			x2 = None
		elif d < 0:
			x1 = None
			x2 = None
		return x1,x2
	
#WHY IS VERTEX A NOT ROUNDING?!?!?!?!	
	def print_block(h,k,a,b,c):
		a = round(a,2)
		#b and c are positive
		if b>0 and c>=0:
			print('The standard form is y = {0}x^2 + {1}x + {2}'.format(a,b,c))
			if h>=0 and k>=0:
				print('The vertex form is f(x) = {0}(x-{1})^2 + {2}'.format(round(a,2),h,k))
			elif h>=0 and k<0:
				print('The vertex form is f(x) = {0}(x-{1})^2 {2}'.format(round(a,2),h,k))
			elif h<0 and k>=0:
				print('The vertex form is f(x) = {0}(x+{1})^2 + {2}'.format(round(a,2),abs(h),k))
			elif h<0 and k<0:
				print('The vertex form is f(x) = {0}(x+{1})^2 {2}'.format(round(a,2),abs(h),k))
		#b is negative and c is positive
		elif b<0 and c>=0:
			print('The standard form is y = {0}x^2 {1}x + {2}'.format(a,b,c))
			if h>=0 and k>=0:
				print('The vertex form is f(x) = {0}(x-{1})^2 + {2}'.format(round(a,2),h,k))
			elif h>=0 and k<0:
				print('The vertex form is f(x) = {0}(x-{1})^2 {2}'.format(round(a,2),h,k))
			elif h<0 and k>=0:
				print('The vertex form is f(x) = {0}(x+{1})^2 + {2}'.format(round(a,2),abs(h),k))
			elif h<0 and k<0:
				print('The vertex form is f(x) = {0}(x+{1})^2 {2}'.format(round(a,2),abs(h),k))
		#b and c are negative
		elif b<0 and c<0:
			print('The standard form is y = {0}x^2 {1}x {2}'.format(a,b,c))
			if h>=0 and k>=0:
				print('The vertex form is f(x) = {0}(x-{1})^2 + {2}'.format(round(a,2),h,k))
			elif h>=0 and k<0:
				print('The vertex form is f(x) = {0}(x-{1})^2 {2}'.format(round(a,2),h,k))
			elif h<0 and k>=0:
				print('The vertex form is f(x) = {0}(x+{1})^2 + {2}'.format(round(a,2),abs(h),k))
			elif h<0 and k<0:
				print('The vertex form is f(x) = {0}(x+{1})^2 {2}'.format(round(a,2),abs(h),k))
		#b is zero
		elif b==0:
			print('The standard form is y = {0}x^2 + {1}'.format(a,c))
			if h>=0 and k>=0:
				print('The vertex form is f(x) = {0}(x-{1})^2 + {2}'.format(round(a,2),h,k))
			elif h>=0 and k<0:
				print('The vertex form is f(x) = {0}(x-{1})^2 {2}'.format(round(a,2),h,k))
			elif h<0 and k>=0:
				print('The vertex form is f(x) = {0}(x+{1})^2 + {2}'.format(round(a,2),abs(h),k))
			elif h<0 and k<0:
				print('The vertex form is f(x) = {0}(x+{1})^2 {2}'.format(round(a,2),abs(h),k))
		return 0
	
	def descrip(h,k,a,b,c,rt1,rt2):
		if rt1 != None and rt2 != None:
			print('The roots are {0} and {1}'.format(round(rt1,2),round(rt2,2)))
		elif rt1 != None and rt2 == None:
			print('The root is {0}'.format(round(rt1,2)))
		elif rt1 == None and rt2 == None:
			print('There are no real roots')
		print('The y-intercept is (0.0, {0})'.format(c))
		print('The vertex is ({0}, {1})'.format(h,k))
		print('The axis of symmetry is x = {0}'.format(h))
		return 0
		
	def type_of_eq():
		print('What kind of equation are you starting with?')
		eq = int(input('Type 1 if your equation looks like ax^2 + bx + c\nType 2 if your equation looks like a(x-h)^2 + k\nType here: '))
		if eq == 1:
			print('Given the equation is ax^2 + bx +c...')
			a = float(input('What is a? '))
			b = float(input('What is b? '))
			c = float(input('What is c? '))
			h,k,a,b,c = quad_to_ver(a,b,c)
			rt1,rt2 = quad_form(a,b,c)
			h = round(h,2)
			k = round(k,2)
			b = round(b,2)
			c = round(c,2)
			print_block(h,k,a,b,c)
			descrip(h,k,a,b,c,rt1,rt2)
		elif eq == 2:
			print('Given the equation is a(x-h)^2 + k...')
			mult = input('Do you know what a is? (y/n) ').lower()
			if mult == 'y' or mult == 'yes':
				h = float(input('What is h? '))
				k = float(input('What is k? '))
				a = float(input('What is a? '))
				x = float(input('What is the x-coordinate of your reference point? '))
				y = float(input('What is the y-coordinate of your reference point? '))
				h,k,a,b,c = ver_to_quad(h,k,a,x,y)
				rt1,rt2=quad_form(a,b,c)
				h = round(h,2)
				k = round(k,2)
				b = round(b,2)
				c = round(c,2)
				print_block(h,k,a,b,c)
				descrip(h,k,a,b,c,rt1,rt2)
			elif mult == 'n' or mult == 'no':
				h,k,a,x,y = vert_find()
				h,k,a,b,c = ver_to_quad(h,k,a,x,y)
				rt1,rt2=quad_form(a,b,c)
				h = round(h,2)
				k = round(k,2)
				b = round(b,2)
				c = round(c,2)
				print_block(h,k,a,b,c)
				descrip(h,k,a,b,c,rt1,rt2)
	
	type_of_eq()
	
	reset = input('Would you like to do another problem? (y/n) ').lower()
	if reset == 'y' or reset == 'yes':
		main()
	else:
		print('Okay!')
	
main()
