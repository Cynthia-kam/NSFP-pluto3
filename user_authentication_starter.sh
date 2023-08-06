#! /bin/bash

# program options
MENU=("Login" "Register" "Logout" "Close the program")
ROLES=("admin" "normal" "salesperson")
ADMIN_OPTIONS=("Register Others" "Delete Account")

PROJECT_HOME="."
credentials_file="$PROJECT_HOME/data/credentials.txt"

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

check_existing_username() {
    username=$1
    ## verify if a username is already included in the credentials file
    grep "^$username" $credentials_file
}

## function to add new credentials to the file
register_credentials() {
    # arg1 is the username
    # arg2 is the password
    # arg3 is the fullname of the user
    # arg4 (optional) is the role. Defaults to "normal"

    username=${1:?"Username is required"}
    username="${username,,}"
    password=${2:?"Password is required"}
    fullname=${3:?"Fullname is required"}
    role=${4:-"normal"}
    role="${role,,}"
    ## call the function to check if the username exists
    res=$(check_existing_username $username)
    #TODO: if it exists, safely fails from the function.
    if [[ -n "$res" ]]; then
        echo "username already exist"
        return 1
    fi
    ## retrieve the role. Defaults to "normal" if the 4th argument is not passed

    ## check if the role is valid. Should be either normal, salesperson, or admin
    if [[ ! " ${ROLES[@]} " =~ " ${role} " ]]; then
        echo "Invalid role"
        return 1
    fi

    ## first generate a salt
    salt=$(generate_salt)
    ## then hash the password with the salt
    hashed_pwd=$(hash_password $password $salt)
    ## append the line in the specified format to the credentials file (see below)
    ## username:hash:salt:fullname:role:is_logged_in

    echo "$username:$hashed_pwd:$salt:$fullname:$role:0" >>$credentials_file
    echo "Registration Successful. You can now log in"
}

# Function to verify credentials
verify_credentials() {
    ## arg1 is username
    ## arg2 is password
    username=$1
    username=${username,,}
    password=$2
    ## retrieve the stored hash, and the salt from the credentials file
    # if there is no line, then return 1 and output "Invalid username"
    is_username_empty=$(grep "^$username" $credentials_file)
    if [[ -z "$is_username_empty" ]]; then
        echo "Invalid username"
        return 1
    fi

    stored_hash=$(echo "$is_username_empty" | cut -d: -f2)
    salt=$(echo "$is_username_empty" | cut -d: -f3)
    fullname=$(echo "$is_username_empty" | cut -d: -f4)
    role=$(echo "$is_username_empty" | cut -d: -f5)

    ## compute the hash based on the provided password
    computed_hash=$(hash_password $password $salt)

    ## compare to the stored hash
    if [[ "$stored_hash" != "$computed_hash" ]]; then
        echo "Invalid password"
        return 1
    else
        # update credentials file
        # ToDo 1: update is_logined field in credentials file

        # update the .logged_in file
        echo "$username" >".logged_in"
        echo "Welcome $fullname! You have successfully logged in as ${role^}"
        if [[ "$role" == "admin" ]]; then
            admin_options
        fi
        return 0
    fi
    ### if the hashes match, update the credentials file, override the .logged_in file with the
    ### username of the logged in user

    ### else, print "invalid password" and fail.
}

logout() {
    #TODO: check that the .logged_in file is not empty
    # if the file exists and is not empty, read its content to retrieve the username
    # of the currently logged in user

    if [[ -f ".logged_in" && -n $(cat ".logged_in") ]]; then
        username=$(cat ".logged_in")
        # ToDo 2: update is_logged_in field in credentials file

        # delete .logged_in
        rm ".logged_in"
        echo "Logged out"
    else
        echo "You are not logged in"
    fi

    # then delete the existing .logged_in file and update the credentials file by changing the last field to 0
}

login() {
    echo "===== Login ====="
    read -p 'Username: ' user
    read -rs -p 'Password: ' pass
    echo

    # verify credentials
    verify_credentials $user $pass
}

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

# takes a username as an argument
# checks if the username exists
# if it does, delete the account
# else, print "Account does not exist"
delete_account() {
    username=$1
    username=${username,,}

    is_username=$(grep "^$username" $credentials_file)

    if [[ -z "$is_username_empty" ]]; then
        echo "Account does not exist"
        return 1
    else
        echo "Deleting account..."
        sed -i "/^$username/d" $credentials_file
    fi

}

# display self registration menu
display_registration_menu() {
    echo "===== User Registration ====="
    read -p "Username: " username
    read -rs -p "Password: " password
    echo # print new line
    read -rs -p "Confirm password: " confirm_password
    echo # print new line

    # Verification
    if [[ $password != $confirm_password ]]; then
        echo "Passwords do not match"
        display_registration_menu
    fi

    read -p "Fullname: " fullname
    # read -p "Enter role (admin/normal/salesperson): " role
    echo

    # register user
    # register_credentials $username $password "$fullname" $role
    register_credentials $username $password "$fullname"
}

admin_options() {
    echo "===== What would you like to do ====="

    for ((i = 0; i < ${#ADMIN_OPTIONS[@]}; i++)); do
        echo "$(expr $i + 1). ${ADMIN_OPTIONS[$i]}"
    done

    # PROMT USER FOR CHOICE
    read -p "Enter your choice: " CHOICE
    case $CHOICE in
    1)
        read -p "Username: " username
        read -rs -p "Password: " password
        echo # print new line
        read -rs -p "Confirm password: " confirm_password
        echo # print new line

        # Password Confirmation
        if [[ $password != $confirm_password ]]; then
            echo "Passwords do not match"
            return 1
        fi

        read -p "Fullname: " fullname
        read -p "Enter role (admin/normal/salesperson): " role
        echo

        # register user
        register_credentials $username $password "$fullname" $role
        ;;
    2)
        read -p "Username: " username
        delete_account $username
        ;;
    *)
        echo "Invalid Selection"
        ;;
    esac
}

# display welcome menu
echo "Please select an option: "
for ((i = 0; i < ${#MENU[@]}; i++)); do
    echo "$(expr $i + 1). ${MENU[$i]}"
done

# PROMT USER FOR CHOICE
read -p "Enter your choice: " CHOICE
case $CHOICE in
1)
    login
    ;;
2)
    display_registration_menu
    ;;
3)
    logout
    ;;
4)
    exit
    ;;
*)
    echo "Invalid Selection"
    ;;
esac
