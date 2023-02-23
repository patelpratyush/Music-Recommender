"""
Name: Pratyush Patel 
Name: Nicholas Russo
Name: Yanran Jia
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Group Name: NPJ Python Pros
"""
'''
Get Recommendation to made with the extra credit
'''
#Overview
'''
Pratyush's functions:
Putting it all together and testing the functionality
The user should be prompted for their name
The menu and input taken from the user

Julie's functions
e - Enter preferences
r - Get recommendations
p - Show most popular artists

Nicholas' functions
h - How popular is the most popular [artist]
m - Which user has the most likes
q - Save and quit
'''

#Defines file to use
prefName = "musicrecplus.txt" 

#Functions Defined Below

######################################################################################################

def loadUsers(fileName):
    '''Creates and prints a dictionary of artists liked by specific users from text file, fileName'''
    open(fileName,"a")
    file = open(fileName, "r")
    userDict = {}
    for line in file:
        [username,artists] = line.strip().split(":")
        artistList = artists.split(",")
        artistList.sort()
        userDict[username] = artistList
    file.close()
    return userDict

######################################################################################################

def getUserInfo(userDict):
    '''Takes a dictionary of users and their preferences & If user not yet created, asks for preferences and add to dictionary
    If user already exists, prints menu'''
    nameInput = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    nameInput = nameInput.title() #Brings to title case
    if not(nameInput in userDict): #If first-time user
        userDict[nameInput] = getPreferences(nameInput, userDict)
    while True:
        optionLetter = input("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\nd - Delete preferences\ns - Show preferences\n")
        if(optionLetter == "e"): #Enter preferences (By now, preferences would've been entered previously; enables changing preferences)
          getPreferences(nameInput,userDict)
        elif  (optionLetter == "r"): #Get recommendations
          getRecommendations(nameInput,userDict)   
        elif(optionLetter == "p"): #Show the 3 most popular artists
          showPopularArtists(userDict,False)  #Why call False?       
        elif(optionLetter == "h"):#How popular is the most popular artist? - # of likes
          howPopular(userDict)       
        elif(optionLetter == "m"):#Which user likes the most artists?
          mostUserLikes(userDict)
        elif(optionLetter == "q"): #Save and Quit
          save(prefName,userDict) #saves
          break #quits
        elif(optionLetter == "d"): #Delete preferences # Extra Credit
            deletePreferences(nameInput, userDict)
        elif(optionLetter == "s"): #Show saved preferences #Extra Credit
            showPreferences(nameInput, userDict)
    return userDict


######################################################################################################

def getPreferences(userName, userMap): # e - allows user to enter preferences
    ''' Returns a list of the uesr's preferred artists. If the system already knows about the user, it gets the preferences out of the userMap
        dictionary and then asks the user if they have additional preferences.  If the user is new, it simply asks the user for their preferences. '''
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before. \nYour music preferences include:") #Updated to use \n
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you \nlike, or just press Enter")
        newPref = input("to see your recommendations: ") 
    else:
        prefs = []
        print("I see that you are a new user. \nPlease enter the name of an artist or band")
        newPref = input("that you like: " )
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you \nlike, or just press Enter")
        newPref = input("to see your menu: ")
        
    # Always keep the lists in sorted order for ease of comparison
    prefs.sort()
    return prefs

######################################################################################################

def getRecommendations(userName,userDict):
    '''Returns recommendations for user, userName'''
    #Works if there is only one user in the system - prints a custom error message

    curBest=["",0]
    for key in userDict:
        if not(key[-1]=="$"):
            val = checkSimilarity(userDict[userName],userDict[key],0)
            if (val>curBest[1] and not(userDict[key] == userDict[userName])):
                curBest=[key,val]
    reccomendations=[]
    if not(curBest[0]==""):
        for item in userDict[curBest[0]]:
            if not(item in userDict[userName]):
                reccomendations+=[item]
    if not(reccomendations==[]):
        for i in reccomendations:
            print(i)
    else:
        print("No recommendations available at this time.")
            
def checkSimilarity(userPreferences, preferencesToCompare, similarityCounterl):
    '''Returns amount of similar artists between two users preferences'''
    if (userPreferences==[] or preferencesToCompare==[]):
        return similarityCounterl
    elif userPreferences[0]==preferencesToCompare[0]:
        return checkSimilarity(userPreferences[1:],preferencesToCompare[1:],similarityCounterl+1)
    elif userPreferences[0]<preferencesToCompare[0]:
        return checkSimilarity(userPreferences[1:],preferencesToCompare,similarityCounterl)
    else:
        return checkSimilarity(userPreferences,preferencesToCompare[1:],similarityCounterl)

######################################################################################################

def showPopularArtists(userDict,amountpopular):
    '''Prints the 3 most popular artists. If less than 3 artists are saved, it prints all of them.'''
    artistDict={}
    
    for key in userDict:
        if not(key[-1]=="$"):
            for item in userDict[key]:
                if item in artistDict:
                    artistDict[item]+=1
                else:
                    artistDict[item]=1
    popArtistLst=[["",0],["",0],["",0]]

    artistDict = list(sorted(artistDict.items(), key = lambda artistDict:artistDict[1]))

    if len(artistDict) == 0:
        print("Sorry, no artists found.")
    else:
        print(artistDict[-1][0])
        if len(artistDict) == 2:
            print(artistDict[-2][0])
        elif len(artistDict) >= 3:
            print(artistDict[-2][0])
            print(artistDict[-3][0])

######################################################################################################

def howPopular(userDict): # h - How popular is the most popular artist?
    '''print the number of likes the most popular artist received'''

    userDict = removePrivate(userDict) #OK to remove private users from the dictionary here since we don't need to return userDict.  
    numx = {} #Initializes dictionary to store artists and their respective like counts
    for values in userDict.values():    #Iterates through the artists
        for n in range (len(values)):
            if values[n] in numx:
                numx[values[n]] = numx[values[n]]+1 #Add to counter if the artist is found
            else:
                numx[values[n]] = 1   
    if numx == {}:
        print('Sorry, no artists found')    
    else:
        sortednumx = list(sorted(numx.items(),key = lambda numx:numx[1]))
        print (sortednumx [-1][1])  #Prints the final value


def removePrivate(userDict):
    '''Returns the userDict after removing users who requested that their preferences be private.'''
    for key in userDict.copy(): #.copy() is needed since the dictionary length changes as it is iterated through; otherwise it yields an error.
        if key[-1] == "$":
            userDict.pop(key)   #Deletes the entire dictionary entry if its key (username) has a $ (private)
    return userDict

######################################################################################################

def mostUserLikes(userDict): # m - which user likes the most artists?
    '''Prints the full name(s) of the user(s) who like(s) the most artists.'''
    userDict = removePrivate(userDict) #Remove private users from the dictionary

    L = [] #Initializes a list to which we'll add name - (# of likes) pairs.

    for key in userDict: #Iterate through userDict.
        L.append([ len(userDict[key]), key])

    L = sorted(L) #Sorts list from users with fewest likes to users with most likes.  

    while L[0][0] < L[-1][0]: #Disregard users with fewer likes than the user with the most
        L = L[1:]

    for i in range(len(L)): #Print all users with the highest number of likes
        print(L[i][1])

######################################################################################################

def save(prefName, userDict): # q - Saves user dictionary to file
    '''Saves the updated dictionary to file.'''
    sortedUserDict = sorted(userDict) #Sort the userDict (will return a list)
    dictForFile = {} #Initialize a new dictionary so we can copy the sorted dictionary to it (since the sorted dictionary was a list)

    for i in sortedUserDict: #Copy the sorted userDict (which is a list) to the new dictionary
        dictForFile[i] = userDict[i]
        
    #Open the database
    finalFile = open(prefName, "w") 

    for key in dictForFile: #For every user in the sorted dictionary
        userWithPreferences = str(key) + ":" + ",".join(dictForFile[key]) + "\n" #Formats the final file with : and , to separate users and their preferences.
        finalFile.write(userWithPreferences) #Writes one line to the file (of a user and their preferences)

    finalFile.close()

######################################################################################################

################# Extra Credit ##################

def deletePreferences(userName, userDict):
    '''Allows users to delete previously-saved preferences.'''
    if not userDict[userName]:
        print("No saved preferences were found.")
        return 

    else:
        userPreferences = userDict[userName]
        print("Your music preferences include:")
        for artist in userPreferences: #Reprints saved preferences
            print(artist)
        print("Please enter an artist or band that you")
        prefToRemove = input("would like to remove: ").strip().title() #So it matches with the saved preference

    while prefToRemove != "":
        userDict[userName].remove(prefToRemove) #Removes the entered preference
        print(prefToRemove, "was removed from your preferences. Your saved preferences are now:")
        for artist in userDict[userName]:  #Reprints their saved preferences
            print(artist)
        print("Please enter another artist or band that would\nlike to remove, or press enter")
        prefToRemove = input("to see your menu: ")
    return userPreferences

################# Extra Credit ##################

def showPreferences(userName, userDict):
    '''Prints the user's saved preferences.'''
    if not userDict[userName]:
        print("No saved preferences were found.")
        return

    else:
        userPreferences = userDict[userName]
        print("Your music preferences include:")
        for artist in userPreferences: #Reprints saved preferences
            print(artist)
            
######################################################################################################

##Startup Commands

def main():
    '''Loads users from the appropriate file, then starts the program.'''
    getUserInfo(loadUsers(prefName))

if __name__=="__main__":
    main() #Starts the program
