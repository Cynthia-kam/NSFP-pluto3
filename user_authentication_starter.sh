#!/bin/bash
## to be updated to match your settings
PROJECT_HOME="."
credentials_file="$PROJECT_HOME/data/credentials.txt"
logged_in_file="$PROJECT_HOME/data/.logged_in"

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
    if grep -q "^$username:" "$credentials_file"; then
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
    # if check_existing_username $username; then
    if check_existing_username $username; then
        echo "User already exists"
        return 1
    fi

    #TODO: if it exists, safely fails from the function.
    
    ## retrieve the role. Defaults to "normal" if the 4th argument is not passed
    role=${4:-"normal"}

    ## check if the role is valid. Should be either normal, salesperson, or admin
    if [[ "$role" != "normal" ]] && [[ "$role" != "salesperson" ]] && [[ "$role" != "admin" ]]; then
        echo "User role invalid"
        return 1
    fi

    ## first generate a salt
    salt=`generate_salt`
    ## then hash the password with the salt
    hashed_pwd=`hash_password $password $salt`
    ## append the line in the specified format to the credentials file (see below)
    ## username:hash:salt:fullname:role:is_logged_in
    echo "$username:$hashed_pwd:$salt:$fullname:$role:0" >> "$credentials_file"
}

# register_credentials "cyn" "password" "Cynthia Abijuru"

# Function to verify credentials
verify_credentials() {
    ## arg1 is username
    ## arg2 is password
    username=$1
    password=$2
    ## retrieve the stored hash, and the salt from the credentials file
    # if there is no line, then return 1 and output "Invalid username"
    stored_hash=`grep "^$username" "$credentials_file" | cut -d':' -f2`
    if [[ -z "$stored_hash" ]] || ! check_existing_username "$username"; then
        echo "Invalid username"
        return 1
    fi
    echo "$stored_hash"
    ## compute the hash based on the provided password
    stored_salt=`grep "^$username" "$credentials_file" | cut -d':' -f3`
    hashed_pwd=`hash_password "$password" "$stored_salt"`
    echo "$hashed_pwd"
    ## compare to the stored hash
    ### if the hashes match, update the credentials file, override the .logged_in file with the
    ### username of the logged in user
    login_status=`grep "^$username" "$credentials_file" | cut -d':' -f6`
    if [[ "$stored_hash" == "$hashed_pwd" ]]; then
        echo "$username" > "$logged_in_file"
        login_status="1"
        echo "$login_status"
        
        echo "Login successful"
    ### else, print "invalid password" and fail.
    else
        echo "Invalid password"
        exit 1
    fi
}

verify_credentials "jdoe" "password"

# logout() {
#     #TODO: check that the .logged_in file is not empty
#     # if the file exists and is not empty, read its content to retrieve the username
#     # of the currently logged in user

#     # then delete the existing .logged_in file and update the credentials file by changing the last field to 0
# }

## Create the menu for the application
# at the start, we need an option to login, self-register (role defaults to normal)
# and exit the application.

# After the user is logged in, display a menu for logging out.
# if the user is also an admin, add an option to create an account using the 
# provided functions.

# Main script execution starts here
echo "Welcome to the authentication system."

#### BONUS
#1. Implement a function to delete an account from the file