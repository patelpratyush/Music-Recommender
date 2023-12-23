# Music Recommendation System

This is a simple music recommendation system implemented in Python. The system allows users to input their music preferences, get recommendations based on similarities with other users, and perform various other actions.

## Table of Contents

- [File Structure](#file-structure)
- [Functions](#functions)
- [How to Use](#how-to-use)
- [Extra Features](#extra-features)
- [Startup Commands](#startup-commands)

## File Structure

- `musicrecplus.py`: The main Python script containing the music recommendation system.
- `musicrecplus.txt`: The text file used to store user preferences.

## Functions

The program includes the following functions:

- `loadUsers(fileName)`: Loads user preferences from a text file.
- `getUserInfo(userDict)`: Allows users to enter preferences, get recommendations, and perform other actions.
- `getPreferences(userName, userMap)`: Allows users to enter their music preferences.
- `getRecommendations(userName, userDict)`: Provides music recommendations for a given user.
- `showPopularArtists(userDict, amountpopular)`: Displays the three most popular artists among users.
- `howPopular(userDict)`: Shows the number of likes the most popular artist received.
- `mostUserLikes(userDict)`: Prints the user(s) who like the most artists.
- `save(prefName, userDict)`: Saves the user dictionary to a file.
- `deletePreferences(userName, userDict)`: Allows users to delete previously saved preferences.
- `showPreferences(userName, userDict)`: Prints the user's saved preferences.

## How to Use

1. Run the program using the command `python musicrecplus.py`.
2. Enter your name to start using the system.
3. Choose options (e, r, p, h, m, q, d, s) to perform various actions.

## Extra Features

- The program allows users to delete and view their saved preferences.
- Private preferences can be set by appending a `$` symbol to the username.

## Startup Commands

To run the program, use the following command:

```bash
python musicrecplus.py
