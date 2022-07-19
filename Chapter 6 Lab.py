# This program adds golf records to the golf.txt file for the Springhill Amateur Golf Club
#Chapter 6 Lab
#Jeremy Bargy
#3/9/20

def checkFile():    #define check file funtion. validates there is a file to read, creates file if none founf
    try:
        # Open the file.
        infile = open('golf.txt', 'r')

        # Read the file's contents.
        contents = infile.read()

        # Close the file.
        infile.close()
    except IOError:
        print('\nAn error occurred trying to read the file.')
        print('Please select option A to input data to file.\n')
        golf_file = open('golf.txt', 'a')

def welcome():  #define welcome function

    beginSequence= 'y'       #str
    
    print('\n\t\t\t\tHello Students!\n\t\t\t\t---------------')
    print('Thank you for taking the time to use this program.')
    print('The program was made by Jeremy Bargy.')
    print('Last update March 2020')

    #Display description of program
    print('\n\t\t\t\tInstructions\n\t\t\t\t------------')
    print('The program being used is designed to help the Springhill Amateur Golf Club track their players scores and the overall skill of the players at their course.\n')
    print('With this information, Springhill can identify the actions needed to improve their golf course and see the skill level of their players.\n')
    print('Players with this information can identify the areas they need to improve at and what parts of their game they excel at.\n\n\n')

    #loop until user had read instructions
    beginSequence = input('Begin program?\n Please enter Y for yes\n')
    while not(beginSequence == 'Y' or beginSequence == 'y') or beginSequence=='' or beginSequence== ' ':
        print('Error: please read the instructions and enter "Y" for yes to begin: \n')
        beginSequence= input('Begin program? \n')

def getName():      #define get name function
    # Get golf input
    userName = input('Please enter in your name: \n')
    #validate sting
    while not(userName.isalpha()) or userName == ' ' or userName == '' :
        print('Error: incorrect input:')
        userName =input('Please your first name: \n')
    return userName


def getScore():     #define get score function
    userScore = input('Please enter in your score: \n')
    #validate integer
    while not(userScore.isdigit()) or int(userScore) >=130 or int(userScore)<= 60 or int(userScore) == ' ' or int(userScore)=='':
        print('Error: incorrect input: ')
        userScore = (input('Please enter the test score you have earned. Please use a numeric value and does not exceed 130 and not a value lower than 60: \n'))
    userScore = int(userScore)
    return userScore
    
def main():     #define main function
    menuOption = ""
 
    welcome()

    #Program menu for user to pick purchase options
    while menuOption != "C" and menuOption != "c":

        menuOption = input("\nSelect A to input name and score.\nSelect B to see all the players scores and average score for the club.\nSelect C to end the program.\n")

        #validates the entry. The user has to pick a menu option  
        while menuOption != "A" and menuOption != "a" and menuOption != "B" and menuOption != "b" and menuOption != "C" and menuOption != "c":
            print("Error: Please enter option A, B,or C.\n")
            menuOption = input("Select A to input name and score.\nSelect B to see all the players scores and average for the club.\nSelect C to end the program.\n")

        if menuOption =="A" or menuOption =="a":
            #loop variable
            another = 'y'
            
            # Open golf.txt file to append
            golf_file = open('golf.txt', 'a')

            # Add records to the file.
            while another == 'y' or another == 'Y':
            
                # Get golf input
                userName = getName()
                userScore = getScore()
                             
                # Append the data to the file.
                golf_file.write(userName +'\n')
                golf_file.write(str(userScore) + '\n')

                # Determine whether the user wants to add
                # another record to the file.
                print('Is there another user?')
                another = input('Y = yes, anything else = no: \n')
                #validate input
                while another !='Y' and another !='y' and another!='N' and another !='n':
                    print('Error: please enter Y for yes, anything else for no.')
                    another = input('Y = yes, anything else = no: \n')
                
            # Close the file.
            golf_file.close()
            
        elif menuOption == "B" or menuOption == "b":
            #call check file function
            checkFile()
            #initialize variables
            total = 0
            count = 0
            average = 0

            #opens file with name of "groceryList.txt"
            fileName = open("golf.txt","r")

            #read the username
            userName = fileName.readline()
            #accumulate scores and number of scores and average
            while userName != '':
               userScore = int(fileName.readline())
               total +=userScore
               count +=1
               average= total//count
               #display names and scores
               userName = userName.rstrip('\n')
               print(userName)
               print(userScore)

               userName = fileName.readline()

            # close file  
            fileName.close()
            #display average score
            print('\nThe average for the club is: ' + str(average))

            if average == 0:
                print('Please go to option A to input data.\n')
                
            
        else: 
            print('Thanks for using our program!')
            #end program if menu option c is selected

#call main
main()
