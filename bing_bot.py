from splinter import Browser
import random
from time import sleep

try:
    f = open('keywords.txt', 'r')
except:
    print("There appears to not be a keywords.txt file in the current directory, please check and rerun")
else:
    keywords = f.readlines()
    f.close()

num_of_searches = input("Enter the number of searches you'd like to do (default is 400): ")
try: 
    num_of_searches = int(num_of_searches)
except:
    print("input error, try again")
    num_of_searches = input("Enter the number of searches you'd like to do (default is 400): ")

with Browser() as browser:
    iterations = 0
    for i in range (0,num_of_searches):
        randint = random.randint(0,len(keywords))
        randkeyword = keywords[randint]
        randtime = random.randint(45,300)
        print("Searching: "+str(randkeyword))
        url = "https://www.bing.com/search?q="+str(randkeyword)
        browser.visit(url)
        print("Waiting "+str(randtime)+" before searching again (time is random between 45 and 300 seconds)")
        sleep(randtime)

        iterations += 1

print("Finished")
print("Searched "+str(iterations)+" times")