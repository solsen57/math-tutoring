import cmath
def main():
    print('Given quadratic ax^2 + bx +c...')
    a = float(input('Please input a: '))
    b = float(input('Please input b: '))
    c = float(input('Please input c: '))


    #discriminant
    d = (b**2) - (4*a*c)

    #check the discriminant
    def check_dis(a):
        if a == 'y' or a == 'yes':
            print('Great! Give it another go!')
            dis = float(input('What did you get for the discriminant? '))
            dis_check(dis)
        elif a == 'n' or a == 'no':
            print('Okay! Moving on!')
            
    def dis_check(x):
        if x == d:
            print('Great job!')
        else:
            ans = input('Would you like to try again? (y/n) ').lower()
            check_dis(ans)

    dis = float(input('What did you get for the discriminant? '))
    dis_check(dis)

    #number of roots
    if d>0:
        print('The discriminant is {0}, so there are 2 real roots'.format(d))
    elif d == 0:
        print('The discriminant is 0, so there is 1 real root')
        print('Simply input the same root for both root prompts')
    elif d < 0:
        print('The discriminant is {0}, so there are no real roots'.format(d))
        print('For the rest of the calculations, simply ignore the complex element, i, and proceed as normal.')

    #roots
    rt1 = (-b-cmath.sqrt(d))/(2*a)
    rt2 = (-b+cmath.sqrt(d))/(2*a)
    rt1_no_i = rt1.real + rt1.imag
    rt2_no_i = rt2.real + rt2.imag
    rt1_round = round(rt1_no_i, 2)
    rt2_round = round(rt2_no_i, 2)
    #print(rt1, rt2)
    #print(rt1_no_i, rt2_no_i)

    #root check
    #want to implement same idea as discriminant check
    def check_root1(a):
        if a == 'y' or a == 'yes':
            print('Great! Give it another go!')
            root1 = float(input('What did you get for your first real root, rounded 2 decimal places? '))
            root1_check(root1)
        elif a == 'n' or a == 'no':
            print('Okay! Moving on!')
            print('The first root is {0}'.format(rt1_round))

    def root1_check(x):
        if x <= rt1_round+0.3 and x >= rt1_round-0.3:
            print('Great! The first root is {0}'.format(rt1_round))
        else:
            ans = input('Would you like to try again? (y/n) ').lower()
            check_root1(ans)

    root1 = float(input('What did you get for your first real root, rounded 2 decimal places? '))
    root1_check(root1)

    def check_root2(a):
        if a == 'y' or a == 'yes':
            print('Great! Give it another go!')
            root2 = float(input('What did you get for your second real root, rounded 2 decimal places? '))
            root2_check(root2)
        elif a == 'n' or a == 'no':
            print('Okay! Moving on!')
            print('The second root is {0}'.format(rt2_round))

    def root2_check(x):
        if x <= rt2_round+0.3 and x >= rt2_round-0.3:
            print('Great! The second root is {0}'.format(rt2_round))
        else:
            ans = input('Would you like to try again? (y/n) ').lower()
            check_root2(ans)

    root2 = float(input('What did you get for your second real root, rounded 2 decimal places? '))
    root2_check(root2)

    #find the vertex
    #find value between 2 roots
    ver_x = (rt1_round+rt2_round)/2
    def check_ver_x(a):
        if a == 'y' or a == 'yes':
            print('Great! Give it another go!')
            x_check = float(input('What is the value between your two roots? '))
            ver_x_check(x_check)
        elif a == 'n' or a == 'no':
            print('Okay! Moving on!')
            print('The x-coordinate of the vertex is {0}'.format(ver_x))

    def ver_x_check(x):
        if x <= ver_x+0.3 and x >= ver_x-0.3:
            print('Nice work! The x-coordinate of the vertex is {0}'.format(ver_x))
        else:
            ans = input('Would you like to try again? (y/n) ').lower()
            check_ver_x(ans)
            
    x_check = float(input('What is the value between your two roots? '))
    ver_x_check(x_check)

    #find y coordinate
    ver_y = a*(ver_x**2) + b*ver_x +c

    def check_ver_y(a):
        if a == 'y' or a == 'yes':
            print('Great! Give it another go!')
            y_check = float(input('What is the y-value when you calculate the equation with the previous answer? '))
            ver_y_check(y_check)
        elif a == 'n' or a == 'no':
            print('Okay! Moving on!')
            print('The y-coordinate of the vertex is {0}'.format(ver_y))

    def ver_y_check(y):   
        if y <= ver_y+0.3 and y >= ver_y-0.3:
            print('Nice work! The y-coordinate of the vertex is {0}'.format(ver_y))
        else:
            ans = input('Would you like to try again? (y/n) ').lower()
            check_ver_y(ans)
        
    y_check = float(input('What is the y-value when you calculate the equation with the previous answer? '))
    ver_y_check(y_check)

    print('So we now have the coordinates we can create our graph from! We have our x-intercepts, y-intercept, and the vertex!')
    if d>0:
        print('Our x-intercepts are: ({0},0.0) and ({1},0.0)'.format(rt1_round, rt2_round))
    elif d<0:
        print('Our x-intercepts do not exist')
    elif d==0:
        print('Our x-intercept is: ({0}, 0.0)'.format(rt1_round))
    print('Our y-intercept is: (0.0,{0})'.format(c))
    print('Our vertex is: ({0}, {1})'.format(ver_x, round(ver_y, 2)))
    
    reset = input('Do you have another problem? (y/n) ').lower()
    if reset == 'y' or reset == 'yes':
        main()
    else:
        print('Okay!')

main()
    


