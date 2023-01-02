import os
from tkinter.filedialog import askdirectory

print("Hi there! I'm a program written to help you create folders for your classes :)")
print("Type 'q' at any time to quit")

while True:
    print("\nOpening a file window so you can click on the main folder..."
          "\n\tThis is usually a folder where you store each course.")

    main_path = askdirectory()  # show an "Open" dialog box and return the path to the selected file
    print("Creating folder system in: " + main_path)

    main_name = input("Type the name of the folder to create: ")

    if main_name == 'q':
        break
    else:
        # Make the main/parent directory using the main_name variable and attach it at the end of the main_path
        os.makedirs(main_path + "/" + main_name)
        print('Folder ' + main_name + ' created :)')

        # Asking the user if they would like a formula sheet folder
        form_sheet = input('Would you like a folder for a formula sheet? y/n ')

    if form_sheet == 'q':
        break
    else:
        if form_sheet == 'y':
            form_sheet_path = main_path + '/' + main_name + '/' + 'formula_sheet'
            os.makedirs(form_sheet_path)
            print('Formula sheet folder created!')
        else:
            print('No formula sheet folder created, continuing program...')

    # Asking the user if they would like a homework folder
    homework = input('Would you like a folder for homework? y/n ')

    if homework == 'q':
        break
    else:
        if homework == 'y':
            hw_num = int(input('How many homework folders would you like? '))
            hw_path = main_path + '/' + main_name + '/' + 'homework'
            os.makedirs(hw_path)
            print('Formula sheet folder created!\nNow creating a sub-folder for each homework...')

            # i = 1
            for i in range(1, hw_num + 1):
                hw_path_2 = main_path + '/' + main_name + '/' + 'homework' + '/' + 'hw_' + str(i)
                os.makedirs(hw_path_2)
        else:
            print('No homework folder created, continuing program...')

    # Asking the user if they would like a labs folder
    labs = input('Would you like a folder for labs? y/n ')

    if labs == 'q':
        break
    else:
        if labs == 'y':
            lab_num = int(input('How many lab folders would you like? '))
            lab_path = main_path + '/' + main_name + '/' + 'labs'
            os.makedirs(lab_path)
            print('Labs folder created!\nNow creating a sub-folder for each lab...')

            for i in range(1, lab_num + 1):
                lab_path_2 = main_path + '/' + main_name + '/' + 'labs' + '/' + 'lab_' + str(i)
                os.makedirs(lab_path_2)
        else:
            print('No labs folder created, continuing program...')

print('All done!')
