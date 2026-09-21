#Problem 3.a function
def add_user(sn, username, fullname):
    """
Write a function add_user(sn, username, fullname) that adds to the social network stored in
dictionary sn a new user with the given username and full name. The new user has initially no friend
links. The function returns True if the user was added successfully and False, otherwise, i.e. if the user
existed before."""

    #if statement to check if user is in the social network
    if username in sn:
        #returning false to indicate user already exist
        return False
    #else statement to show that the user does not exist and needs to be added
    else:
        #add new user into the system using username and full name, no friends added at this time
        sn[username] = (fullname, [])
        #returning true statement to show that user was added into the social network
        return True

#Problem 3b. function
def add_friend(sn, user1, user2):
    """
Write a function add_friend(sn, user1, user2) that takes a dictionary sn with a social network and
adds a mutual friend link between users user1 and user2. The function returns True if success, and
False otherwise, e.g. when at least one the user names given are not found in sn."""

    #checking sn to see if users are in social network
    if user1 not in sn or user2 not in sn:
        return False

    #adding user2 to user 1 after check that it doesnt already exist
    if user2 not in sn[user1][1]:
        sn[user1][1].append(user2)

    #adding user1 to user 1 after check that it doesnt already exist
    if user1 not in sn[user2][1]:
        sn[user2][1].append(user1)

    #returning true to indicate the addition was a success
    return True

#Problem 3c function
def get_friends(sn, user1, distance):

    """Write a function get_friends(sn, user1, distance) that takes a dictionary sn with a social network, a
username in argument user1, and a positive integer in argument distance and that returns a list with all
friends of user1 at link distance 1, 2, …, distance.
Friends at distance=1 of a user are the users in its immediate list of friends:
"""
    #Checking to see if the user is in the social network
    if user1 not in sn:
        return []

    #variables to store and keep track of users friends and what friends have been reviewed/looked at 
    reviewed = [user1]
    friends = []
    current = sn[user1][1]

    #loop initiatated to start iterating through the friends list using ths distance
    for i in range(distance):

        #list to store the friend to be reviewed at the next distance
        next_friend_level = []

        #second loop to go by specific user
        for user in current:

            #if statement to make sure we do not go into a cycle
            if user not in reviewed:

                friends.append(user)
                reviewed.append(user)

                #loop for looking at this users friends
                for friend in sn[user][1]:

                    #if statement to see if this user has been looked at already
                    if friend not in reviewed:
                        next_friend_level. append(friend)

        #moving over to the next distancce level of friends
        current = next_friend_level
    
    return friends
#Problem 3d function
def save_network(filename, sn):
    """
Write a function save_network(filename, sn) that saves a social network dictionary to a .CSV file.
The function takes as parameter the file name and the dictionary. Let your function throw relevant
exceptions, e.g. FileNotFoundError."""

    try:
        #open file to commence writting of social network
        output_file = open(filename, "w")

        #loop to go through the users from the social network into the cvs file
        for user in sn:
            #printing the user, username, and friends information
            print(user, sn[user][0], ",".join(sn[user][1]), sep=",", file=output_file)

        #closing the file to save the changes we made
        output_file.close()

    #error for not finding file
    except FileNotFoundError:
        print("File not found")
        raise

    #error for not being able to write to file
    except PermissionError:
        print("Error writing to file. Review permissions")
        raise

    #error for file provided not exisitng
    except FileExistsError:
        print("File does not exist")
        raise

#Problem 3e function
def load_network(filename):
    """
Write a function load_network(filename) that reads a social network from a .CSV file saved with
save_network(…) and that returns the dictionary object. Let your function throw relevant exceptions.
"""
    try:
        #opening filename to read
        input_file = open(filename, "r")

        #creating empty dictionary object to store social network info from cvs file
        social_network = {}

        #loop to add items from cvs into empty dictionary
        for line in input_file:
            #clean the information from commas and \n
            new_line = line.rstrip("\n")
            sn_info = new_line.split(",")

            #separate the info for dictionary
            username = sn_info[0]
            user = sn_info[1]
            friends = sn_info[2:]            

            #adding info into dictionary
            social_network[username] = (user, friends )

        #closing the file to save changes
        input_file.close()

        #returning dictionary
        return social_network

    #error when file does not exist
    except FileExistsError:
        print("File does not exist")
        raise
    #error when file is not found
    except FileNotFoundError:
        print("Unable to locate file")
        raise
    #error when reading/parsing through file
    except Exception:
        print("Error reading or parsing file.")
        raise

#Problem 3f function
def main():    
#dictionary for testing all the functions for problem 3.
    sn = {
        'alice': ('Alice Smith', ['maria']),
        'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
        'joe': ('Joseph Adams', ['maria', 'eve']),
        'eve': ('Evelyn Cooper', ['joe']),
        'david': ('David Benson', ['maria'])}

#testing output for problem 3a
    print(add_user(sn, 'alice', 'Alice Smith'))

#testing output for problem 3b
    print(add_friend(sn, 'Billy', 'Tommy')) #false case
    print(add_friend(sn, 'alice', 'timmy')) #one true on false case
    print(add_friend(sn, 'alice', 'maria')) #true case

#testing output for problem 3c
    print(get_friends(sn, 'alice', 2)) #true case
    print(get_friends(sn, 'tommy', 2)) #false case

#testing output for problem 3d
    test_file = "h2_cvs_testfile.csv"
    print(save_network(test_file, sn))

#testing output for problem 3e
    print(load_network(test_file))

#Problem 3g test if function extra credit
def testif(b, testname, msgOK="", msgFailed=""):

    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)

    return b

#Problem 3g testing function extra credit
def test():

    #dictionary for testing all the functions for problem 3
    sn = {
        'alice': ('Alice Smith', ['maria']),
        'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
        'joe': ('Joseph Adams', ['maria', 'eve']),
        'eve': ('Evelyn Cooper', ['joe']),
        'david': ('David Benson', ['maria'])
    }

    #testing output for problem 3a true case
    testif(
        add_user(sn, "timmy", "Timmy Jones") == True,
        "added new user"
    )
    #testing output for problem 3a false case
    testif(
        add_user(sn, "timmy", "Timmy Jones") == False,
        "existing user, addition not needed"
    )

    #testing output for problem 3b true case
    testif(
        add_friend(sn, "alice", "timmy") == True,
        "valid users - added friends"
    )
    #testing output for problem 3b false case
    testif(
        add_friend(sn, "alice", "billy") == False,
        "invalid user - no friends added"
    )

    #testing output for problem 3c true case
    friends = get_friends(sn, "alice", 1)
    print(get_friends(sn, "alice", 1))
    testif(
        get_friends(sn, "alice", 1) == ["maria", "timmy"],
        "friends @ distance 1"
    )
    #testing output for problem 3c false case
    friends = get_friends(sn, "billy", 1)
    print(get_friends(sn, "billy", 1))
    testif(
        get_friends(sn, "billy", 1) == [],
        "No friends - invalid user"
    )

    #testing output for problem 3d and ef
    test_file = "h2_cvs_testfile.csv"

    save_network(test_file, sn)

    loaded_network = load_network(test_file)

    testif(
        loaded_network == sn,
        "save_network and load_network"
    )

#if __name__ == "__main__":
    #main()

#testing for problem 3g extra credit
test()




      