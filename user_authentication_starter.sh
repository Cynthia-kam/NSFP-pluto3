#!/bin/bash
## to be updated to match your settings
PROJECT_HOME="."
credentials_file="./credentials.txt"
logged_in="./Logged_in.txt"

# Function to prompt for credentials
get_credentials() {
    read -p 'Username: ' user
    read -rs -p 'Password: ' pass
    echo
}

generate_salt() {
    openssl rand -hex 8
    return 0
}

## function for hashing
hash_password() {
    # arg1 is the password
    # arg2 is the salt
    password=$1
    salt=$2
    # we are using the sha256 hash for this.
    echo -n "${password}${salt}" | sha256sum | awk '{print $1}'
    return 0
}

check_existing_username(){
    username=$1
    ## verify if a username is already included in the credentials file
    if grep -q "^${username}:" "$credentials_file"; then
        return 0  
    else
        return 1  
    fi
}

## function to add new credentials to the file
register_credentials() {
    # arg1 is the username
    # arg2 is the password
    # arg3 is the fullname of the user
    # arg4 (optional) is the role. Defaults to "normal"

    username=$1
    password=$2
    fullname=$3
    ## call the function to check if the username exists
    check_existing_username $username
    #TODO: if it exists, safely fails from the function.
     if check_existing_username "$username"; then
        echo "Username already exists. Registration failed."
        return 1
    fi
    
    ## retrieve the role. Defaults to "normal" if the 4th argument is not passed
    role=${4:-"normal"}
    ## check if the role is valid. Should be either normal, salesperson, or admin

    ## first generate a salt
    salt=`generate_salt`
    ## then hash the password with the salt
    hashed_pwd=`hash_password $password $salt`
    ## append the line in the specified format to the credentials file (see below)
    echo "${username}:${hashed_pwd}:${salt}:${fullname}:${role}:0" >> "$credentials_file"
            echo "Registration successful for user: $username"
            return 0
        
    ## username:hash:salt:fullname:role:is_logged_in
}

# Function to verify credentials
verify_credentials() {
    ## arg1 is username
    ## arg2 is password
    username=$1
    password=$2
    ## retrieve the stored hash, and the salt from the credentials file
    stored_hash=$(grep "^$username:" credentials.txt | cut -d ':' -f 2)
    stored_salt=$(grep "^$username:" credentials.txt | cut -d ':' -f 3)
    # if there is no line, then return 1 and output "Invalid username"
      if [ -z "$stored_hash" ] || [ -z "$stored_salt" ]; then
        echo "Invalid username"
        return 1
    fi
    ## compute the hash based on the provided password
     computed_hash=$(echo -n "$password$stored_salt" | sha256sum | awk '{print $1}')
    ## compare to the stored hash
     if [ "$computed_hash" = "$stored_hash" ]; then
     echo "$username" >> "$logged_in"
     sed -i "/^$username:.*:0$/ s/0$/1/" credentials.txt
     echo "Login successful for user:$username"
     else
     echo "invalid credentials"
     fi
    ### if the hashes match, update the credentials file, override the .logged_in file with the
    ### username of the logged in user

    ### else, print "invalid password" and fail.
}

logout_fun() {
#     #TODO: check that the .logged_in file is not empty
    if [ -f "$logged_in" ]; then
       
#     # if the file exists and is not empty, read its content to retrieve the username
#     # of the currently logged in user
        if grep -q "." "$logged_in"; then
#     # then delete the existing .logged_in file and update the credentials file by changing the last field to 0
# deleting the content of file instead
         > "$logged_in" 
           sed -i "/^$username:.*:1$/ s/1$/0/" credentials.txt
        fi
    fi
}

## Create the menu for the application
# at the start, we need an option to login, self-register (role defaults to normal)
# and exit the application.

# After the user is logged in, display a menu for logging out.
# if the user is also an admin, add an option to create an account using the 
# provided functions.

# Main script execution starts here
echo "Welcome to the authentication system."
while true; do
    echo "Select an option:"
    echo "1. Login"
    echo "2. Register"
    echo "3. Logout"
    echo "4. Close the program"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            # Call the login function
            echo "======Login======"
            # ... (call the function for login)
            get_credentials
            verify_credentials "$user" "$pass"
            ;;
        2)
            # Call the register function
            echo "======Register======"
            # ... (call the function for register)
            get_credentials
            read -p 'Fullname: ' fullname
            register_credentials "$user" "$pass" "$fullname"
            ;;
        3)
            # Call the logout function
            echo " Logging out..."
            logout_fun
            sleep 5
            # ... (call the function for logout)
            ;;
        4)
            echo "EXiting the program. bye bye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please select a valid option (1-4)."
            ;;
    esac
done

#### BONUS
#1. Implement a function to delete an account from the file