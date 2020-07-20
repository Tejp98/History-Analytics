# Fun Little Projects :
This repository included various small projects. Description about each project is given below.


## 1. Number of Google Searches:


-Wrote a little script ( NumberOfGoogleSearches.py ) to find out total number of google searches i have done in my lifetime.

-Google Takeout data is required.

-It is done using Beautiful Soup package which is used to parse HTML files.

In case you want to use this script, follow the step given below.

### Process to get Google Takeout data:

a. Google Search "Google takeout", click on the first link and navigate to the location shown in the image below, by logging in to your Google account.

![](images/Takeout1.png)

b. Check the box shown in the above image and continue to next step.

![](images/Takeout2.png)

c. Click Create Export as shown in the image above. Once the export is created Google will send you an email and you can download the .zip file. On unzipping the file you will find a folder called Takeout. 

d. Navigate to Takeout/MyActivity/Search, you will find a MyActivity.html, this MyActivity.html file is used in NumberOfGoogleSearches.py program. Give appropriate path for that file in the program or copy it in the same directory as program.
