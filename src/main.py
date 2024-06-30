#Run this file
import funs

conn = funs.database_setup()
    
while True:
        print("\nInternship Application Tracker")
        print("1. Add new application")
        print("2. Update follow-up status (NOT IMPLEMENTED)")
        print("3. Delete application")
        print("4. View all applications")
        print("5. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            funs.add_application(conn)
        elif choice == '2':
             print("NOT IMPLEMENTED")
        elif choice == '3':
            funs.delete_application(conn)
        elif choice == '4':
            funs.view_applications(conn)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")