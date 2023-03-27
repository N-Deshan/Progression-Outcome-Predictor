# Date - 10/04/2022
# UoW Student ID - w1912794
# IIT student ID - 20210053
# I declare that my work does not contain any misconduct such as plagarism. 
# If there are any code examples taken will be referenced.
#==============================================================================================

# Importing sys function

import sys

# Initializing variables

c_pass = 0
c_defer = 0
c_fail = 0
tot = 0
credit = [0,20,40,60,80,100,120]
progress = []
trailer = []
retriever = []
excluded = []
global i        # Globalizing the variable i


def main():     # This function is to get the user inputs to choose which option to proceed
    
    print("Enter 1 to Student version\nEnter 2 to Staff version\nEnter 3 to Exit\n")
    u_input =input("Enter an Option :")
    if u_input == '1':
        print('Student version')
        version1()
    elif u_input == '2':
        print('Staff version with Histogram')
        version2()
    elif u_input == '3':
        print('End of the Program')
        sys.exit()      # Using imported sys function to exit the program

    elif u_input != '1' or u_input != '2' or u_input == '3':
        print('Invalid input')
        print()
        main()
        print()

def version1():     # This function is to get the user inputs only once...Student version
    i = 1
    print()
    for x in range(i):
        try:
            c_pass = int(input('Enter the credits at pass :'))
            if c_pass not in credit:
                print('Out of range')
                print()
                version1()
                continue
                break
                
            else:
                c_defer = int(input('Enter the credits at defer :'))
                if c_defer not in credit:
                    print('Out of range')
                    print()
                    version1()
                    continue
                    break
                else:
                    c_fail = int(input('Enter the credits at fail :'))
                    if c_fail not in credit:
                        print('Out of range')
                        print()
                        version1()
                        continue
                        break
        except ValueError:
            print('Integer required')
            print()
            version1()
            continue
            break

        tot = c_pass + c_defer + c_fail
        if tot != 120:
            print('Total incorrect')
            print()
            version1()
            continue
            print()
        else:
            if c_pass == 120:
                print('progress')
                print()
            elif c_pass == 100:
                print('progress (module trailer)')
                print()
            elif c_fail >= 0 and c_fail <= 60:
                print('Module retriever')
                print()
            elif c_fail >= 80:
                print('Excluded')
                print()
            else:
                print('Invalid input')
                print()
                version1()
                continue
            main()

                
def version2():     # This function is to input many number of user inputs....Staff version

    pro_count = 0
    trail_count = 0
    retri_count = 0
    exclu_count = 0
    print()
        
    for i in range(100):
        try:
            c_pass = int(input('Enter the credits at pass :'))
            if c_pass not in credit:
                print('Out of range')
                continue
                break
            
            else:
                c_defer = int(input('Enter the credits at defer :'))
                if c_defer not in credit:
                    print('Out of range')
                    continue
                    break
                else:
                    c_fail = int(input('Enter the credits at fail :'))
                    if c_fail not in credit:
                        print('Out of range')
                        continue
                        break
        except ValueError:
            print('Integer required')
            continue
            break

        tot = c_pass + c_defer + c_fail
        if tot != 120:
            print('Total incorrect')
            continue
            print()
        else:
            if c_pass == 120:
                print('progress')
                print()
                pro_count += 1
                progress.append('*')
            elif c_pass == 100:
                print('progress (module trailer)')
                print()
                trail_count += 1
                trailer.append('*')
            elif c_fail >= 0 and c_fail <= 60:
                print('Module retriever')
                print()
                retri_count += 1
                retriever.append('*')
            elif c_fail >= 80:
                print('Excluded')
                print()
                exclu_count += 1
                excluded.append('*')
            else:
                print('Invalid input')
                print()
            cont=str(input("Enter 'Y' or 'y' to proceed or 'Q' or 'q' to exit :"))
            print()
            if cont == 'Y' or cont == 'y':
                print ()
                continue
            elif cont == 'Q' or cont == 'q':
                break
            elif (cont != 'Y' and cont != 'y') or (cont != 'Q' and cont != 'q'):
                print('Invalid integer')
                continue            

    print('Horizontal histogram')    # Printing Horizontal Histogram
    print()
    print('progress ',len(progress),' :', len(progress)*' * ')
    print('Trailer  ',len(trailer),' :', len(trailer)*' * ')
    print('Retriever',len(retriever),' :', len(retriever)*' * ')
    print('Excluded ',len(excluded),' :', len(excluded)*' * ')
    print()
    print(len(trailer)+len(retriever)+len(progress)+len(excluded),'outcomes in total')
    print('='*70)
        
    print()
    print('vertical histogram')     # Printing Vertical Histogram
    print()

    print (' progress   '' trailer   '' retriever   '' excluded')

    for x in range(max(pro_count,trail_count,retri_count,exclu_count)):
        print("   {0}          {1}             {2}           {3}".format(
            '*' if x < pro_count else ' ',
            '*' if x < trail_count else ' ',
            '*' if x < retri_count else ' ',
            '*' if x < exclu_count else ' '))
    print()
    print(len(trailer)+len(retriever)+len(progress)+len(excluded),'outcomes in total')
    print('='*70)
    print()
    main()

# Calling out the functions

main()   
version1()
version2()

# I used Stack overflow website to get the help to print the stars in vertical Histogram Below is the link to that website
#https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
