"""
Let's get acquainted with the ** operator used to pass a varying number of keyword arguments into a function. **kwargs collects all possible extra values in a dictionary with keywords as keys.
By convention, people use special names for this kind of arguments: *args for positional arguments and **kwargs for keyword arguments, but you can call them whatever you want. The main thing is that a single asterisk * matches a value by position and a double asterisk ** associates a value with a name, or keyword.
So, **kwargs differs from *args in that you will need to assign keywords.
Example of usage:
def capital(**kwargs):
    for key, value in kwargs.items():
        print(value, "is the capital city of", key)


capital(Canada="Ottawa", Estonia="Tallinn", Venezuela="Caracas", Finland="Helsinki")
There are two unpacking operators in Python: a single asterisk * unpacks elements of an iterable object and a double asterisk ** works with dictionaries. Let's try to get key-value pairs from a dictionary and pass them as keyword arguments using a double asterisk **:

def say_bye(**names):
    for name in names:
        print("Au revoir,", name)
        print("See you on", names[name]["next appointment"])
        print()


humans = {"Laura": {"next appointment": "Tuesday"},
          "Robin": {"next appointment": "Friday"}}

say_bye(**humans)

# Au revoir, Laura
# See you on Tuesday
#
# Au revoir, Robin
# See you on Friday
"""
#TASK1
"""
Joe defined a dictionary listing his favorite artists, their albums, and the song from each of the albums. It looks as follows:

tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
                      "On the Other Side": "Samara"},
          "Cure": {"Disintegration": "Lovesong",
                   "Wish": "Friday I'm in love"}}
Joe's tastes can change, though.

Your task is to define a tracklist() function that would take several keyword arguments representing musicians and dictionaries with albums and songs as values. For the example above, the call of this function will look as follows:

tracklist(Woodkid={"The Golden Age": "Run Boy Run",
                   "On the Other Side": "Samara"},
          Cure={"Disintegration": "Lovesong",
                "Wish": "Friday I'm in love"})
"""
#SOLUTION
"""

"""