# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
import copy
from datetime import datetime, date


#=================================Function Definitions================================
def reg_user(users_in):
    '''Add a new user to the user.txt file'''
    #Variables for input validation
    is_reg_successful = False
    # - Request input of a new username
    new_username = input("New Username: ")
    if new_username in users_in: #Returns to input request when duplicate username detected
        print("Username already in use. Please try another")
        return is_reg_successful
    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password      
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
        is_reg_successful = True
    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

    return is_reg_successful

def add_task():
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
    is_name_valid = False
    while not is_name_valid: #New while loop to maintain flow of program within scope of adding new task
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
        else:
            is_name_valid = True

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break #Breaks while loop when input successful
        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

    for t in task_list:
        disp_str = str('-'* 40)
        disp_str += f"\nTask: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"\nTask Description: \n {t['description']}\n"
        disp_str += str('-' * 40)

        print(disp_str)

def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
    i = 1 #index set to 1 because this is how normal people count
    for t in task_list:
        if t['username'] == curr_user:
            t['index'] = int(i) #Adds task number to dict for user selection
            disp_str = str('-'* 40)
            disp_str += f"\nTask #{t['index']}: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Completion status: \t{t['completed']}"
            disp_str += f"\nTask Description: \n {t['description']}\n"
            disp_str += str('-' * 40)

            print(disp_str)

        i += 1
    task_edited = False
    while True:
        task_to_edit = input('''Enter the number of the task you wish to edit (-1 to return to main menu)
        Task # ''')

        if task_to_edit == "-1":
            if task_edited: 
                write_tasks_to_file()
            return #Exits view_mine func at user request
        
        try:
            task_to_edit = int(task_to_edit)
        except:
            print("\nInvalid input. Please enter an integer value.")
            continue #Reutrns to head of while loop to ask user for a task
        
        for t in task_list:
            task_found = False
            if t['index'] == task_to_edit:
                task_found = True
                if t ['completed'] == False:#Limits editing to completed tasks
                    t = edit_task(task_list[int(t['index']) - 1]) #Calls edit function and assigns any changes user makes
                task_edited =True
                break #limits cycles for loop takes to execute if task found
        
        if not task_found:
            print(f"\nTask #{task_to_edit} not found.")

def generate_reports():
    '''Outputs two reports to text files. Overall report for task manager, and per user report
    '''
    task_overview()
    user_overview()

    return

def edit_task(edit_task_in):
    '''Allows a user to edit the completion status or due date of a task.
    '''
    edit_task_out = copy.deepcopy(edit_task_in) #deep copy of task in to preserve before editing

    while True:
        edit_type = input(f'''\nEditing Task #{edit_task_in['index']}.
            Enter 'Yes' to mark the task complete.
            Enter 'Date' to change the due date of the task.
            Enter 'User' to reassign the task.
            Enter -1 to return to previous menu
            ''' )
        
        if edit_type == 'Yes':
            edit_task_out['completed'] = True
            break
        
        elif edit_type == 'Date':
            while True:
                try:
                    task_due_date = input("Due date of task (YYYY-MM-DD): ")
                    due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                    edit_task_out['due_date'] = due_date_time
                    break

                except ValueError:
                    print("Invalid datetime format. Please use the format specified")
            break

        elif edit_type == 'User':
            while True:
                task_username = input("Name of person assigned to task: ")
                if task_username not in username_password.keys():
                    print("User does not exist. Please enter a valid username")
                    continue #prevents assignment of task before valid user is entered
                
                edit_task_out['username'] = task_username
                break
            break
        
        elif edit_type == '-1':
            break

    return edit_task_out

def write_tasks_to_file():
    '''Writes current task_list to output file
    '''
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))

def task_overview():
    '''Produces reporting file for task_overview.txt
    '''
    with open("task_overview.txt", 'w') as task_report:    
        output_string = ""

        output_string += str('*' * 50)
        output_string += "\nTask Overview\n"
        #Total tasks
        output_string += f"\nTotal Tasks: {len(task_list)}\n"
        #Total completed
        completion_count = 0
        incompletion_count = 0
        for task in task_list:
            if task['completed']:
                completion_count += 1
            else:
                incompletion_count +=1
        
        output_string += f"\nCompleted tasks: {completion_count}"
        #Total uncompleted
        output_string += f"\nTasks incomplete: {incompletion_count}"

        #Percentage incomplete
        percentage_incomplete = incompletion_count / len(task_list) * 100

        output_string += f"\n{percentage_incomplete}% of tasks remain incomplete\n"
        #Total overdue
        tasks_overdue = 0
        for task in task_list:
            if task_overdue(task):
                tasks_overdue += 1
        
        output_string += f"\nThere are currently {tasks_overdue} which are overdue. "
        #Percentage overdue
        percentage_overdue = tasks_overdue / incompletion_count * 100

        output_string += f"{percentage_overdue}% of incomplete tasks.\n"

        output_string += str('*' * 50)

        task_report.write(output_string)

def user_overview():
    '''Produces reporting file for user_overview.txt
    '''
    output_string = str('*' * 50) + "\nUser Overview\n" + str('*' * 50)
    #Users registered
    num_users = len(username_password.keys())

    output_string += f"\nUsers registered: {num_users}"

    #Total tasks generated and tracked
    num_tasks = len(task_list)

    output_string += f"\nTotal tasks: {len(task_list)}\n"

    with open('user_overview.txt', 'w') as ouput_file: #flush output buffer and ensure output file exists
        ouput_file.write(output_string)

    #for users:
    for user in username_password.keys():
        #reset output buffer to limit memory usage in case of large user numbers
        output_string = "" 
        
        output_string += str('*' * 50) + f"\nUser: {user}"

        tasks_assigned = 0
        percentage_tasks = 0.0

        #Total tasks assigned
        for task in task_list:
            if task['username'] == user:
                tasks_assigned += 1
        
        output_string += f"\nTotal tasks for {user}: {tasks_assigned}"

        #Percentage of Total assigned
        percentage_tasks = tasks_assigned / num_tasks * 100

        output_string += f" ({percentage_tasks} of total tasks)."
        #Percentage assigned completed and incomplete
        completion_count = 0
        incompletion_count = 0

        for task in task_list:
            if task['username'] == user and task['completed']:
                completion_count += 1
            elif task['username'] == user and not task['completed']:
                incompletion_count +=1
        
        percentage_complete = completion_count / tasks_assigned * 100
        percentage_incomplete = incompletion_count / tasks_assigned * 100

        output_string += f"\n{user} has completed {percentage_complete}% of their tasks."
        output_string+= f"\n{percentage_incomplete}% remain incomplete"
        
        #Percentage overdue
        overdue_count = 0
        for task in task_list:
            if task['username'] == user and not task['completed']:
                if task_overdue(task):
                    overdue_count +=1
        
        percentage_overdue = overdue_count / incompletion_count * 100 

        output_string += f" (of which {percentage_overdue}% are overdue.)\n"

        output_string += str('*' * 50)

        with open('user_overview.txt', 'a') as ouput_file: #flush output buffer to limit memory usage
            ouput_file.write(output_string)

def task_overdue(task_in):
    '''Helper function for report generation. Checks for overdue tasks.
    '''
    if not task_in['completed']:
        curr_date = datetime.today()
        due_date = task_in['due_date']
        if curr_date < due_date:
            return True
        else:
            return False
#=================================Main Thread=======================================================

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        while not reg_user(username_password.keys()): 
            continue #If user registration fails, will stay in loop until successful
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'gr':
        generate_reports()
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        # TODO - Edit so ds reads from tasks.txt
        '''Reading from file here is unnecessary.
        At all points where display stats is called the value stored in file is identical to value stored in RAM.
        Reading from file only adds pointless I/O ops.
        Login sequence initialises users file.
        App opening initialises tasks file.
        '''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)
        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")