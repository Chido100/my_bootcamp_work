# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

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
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
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
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    ''' Function to register a new user '''
    def reg_user():
        
        '''Add a new user to the user.txt file'''
        # - Request input of a new username
        new_username = input("New Username: ")

        # Check if the username already exists in user.txt
        if new_username in username_password.keys():
            print("Username already exists. Please enter a different username.")
            return
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

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")

    
    

    ''' Function for adding new tasks '''
    def add_task():
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            return
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

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
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            


    def view_mine():
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''

        print("Tasks:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task['title']}")

        print("Type the task number to select a task, or -1 to return to the main menu.")

        task_num = input("Enter task number: ")
        if task_num == '-1':
            return

        try:
            task_index = int(task_num) - 1
            selected_task = task_list[task_index]
            print(f"Selected Task: {selected_task['title']}")
            
            if selected_task['completed']:
                print("This task is already completed and cannot be edited.")
                return

            print("1. Mark as Complete")
            print("2. Edit Task")
            
            option = input("Enter option: ")

            if option == '1':
                # Mark the task as complete
                task_list[task_index]['completed'] = True
                print("Task marked as complete.")
            elif option == '2':
                # Edit the task
                print("Edit Task:")
                print("1. Edit Assigned User")
                print("2. Edit Due Date")

                edit_option = input("Enter option: ")

                if edit_option == '1':
                    new_username = input("Enter new username: ")
                    if new_username not in username_password:
                        print("Username does not exist.")
                        return
                    task_list[task_index]['username'] = new_username
                    print("Assigned user updated successfully.")
                elif edit_option == '2':
                    new_due_date = input("Enter new due date (YYYY-MM-DD): ")
                    try:
                        new_due_date = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                        task_list[task_index]['due_date'] = new_due_date
                        print("Due date updated successfully.")
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD.")

        except (ValueError, IndexError):
            print("Invalid task number.")

        
    def generate_reports():
        ''' Generates reports '''

        # Total number of tasks
        total_tasks = len(task_list)
        # Number of completed tasks
        completed_tasks = sum(1 for task in task_list if task['completed'])
        # Number of incomplete tasks
        incomplete_tasks = total_tasks - completed_tasks
        # Number of overdue tasks
        overdue_tasks = sum(1 for task in task_list if not task['completed'] and 'due_date' in task and task['due_date'] < datetime.now())
        # Percentage of incomplete tasks
        percentage_incomplete = (incomplete_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        # Percentage of overdue tasks
        percentage_overdue = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0

        # Write task overview to task_overview.txt
        with open("task_overview.txt", "w") as task_file:
            task_file.write(f"Total number of tasks: {total_tasks}\n")
            task_file.write(f"Number of completed tasks: {completed_tasks}\n")
            task_file.write(f"Number of incomplete tasks: {incomplete_tasks}\n")
            task_file.write(f"Number of overdue tasks: {overdue_tasks}\n")
            task_file.write(f"Percentage of incomplete tasks: {percentage_incomplete:.2f}%\n")
            task_file.write(f"Percentage of overdue tasks: {percentage_overdue:.2f}%\n")

        # Total number of users
        total_users = len(username_password)
        # Write user overview to user_overview.txt
        with open("user_overview.txt", "w") as user_file:
            user_file.write(f"Total number of users: {total_users}\n")
            for user, password in username_password.items():
                user_tasks = [task for task in task_list if task['username'] == user]
                total_user_tasks = len(user_tasks)
                completed_user_tasks = sum(1 for task in user_tasks if task['completed'])
                percentage_user_complete = (completed_user_tasks / total_user_tasks) * 100 if total_user_tasks > 0 else 0
                user_file.write(f"\nUser: {user}\n")
                user_file.write(f"Total number of tasks assigned: {total_user_tasks}\n")
                user_file.write(f"Percentage of tasks completed: {percentage_user_complete:.2f}%\n")

        print("Reports generated successfully.")


    def display_statistics():
        ''' Display statistics so that the reports generated are read from tasks.txt and user.txt '''

        # Check if tasks.txt and user.txt exist
        if not os.path.exists("tasks.txt") or not os.path.exists("user.txt"):
            print("Generating reports...")
            generate_reports()
        
        # Read task data from tasks.txt
        with open("tasks.txt", "r") as task_file:
            task_data = task_file.readlines()

        # Read user data from user.txt
        with open("user.txt", "r") as user_file:
            user_data = user_file.readlines()

        # Calculate statistics
        total_users = len(user_data)
        total_tasks = len(task_data)
        completed_tasks = sum(1 for task in task_data if task.strip().split(";")[-1] == "Yes")
        incomplete_tasks = total_tasks - completed_tasks

        print("Statistics:")
        print(f"Total number of users: {total_users}")
        print(f"Total number of tasks: {total_tasks}")
        print(f"Total number of completed tasks: {completed_tasks}")
        print(f"Total number of incomplete tasks: {incomplete_tasks}")

        # Calculate and display additional statistics from reports
        generate_reports()


    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()
    
    elif menu == 'gr':
        generate_reports()
    
    elif menu == 'ds':
        display_statistics()


    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
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
        
                
    










