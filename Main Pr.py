def main():
    create_database()
    print("Welcome to the Educational Quiz App!")
    username = login()
    if username:
        user_menu(username)
    else:
        print("Exiting the program.")

if __name__ == "__main__":
    main()
