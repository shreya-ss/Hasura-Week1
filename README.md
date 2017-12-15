# Hasura-Week1
The following tasks will have to be demonstrated by the repective programs:
 
1) hello-world.py - A simple hello-world at ​ http://localhost:8080/​ that displays a simple string like "Hello World - Shreya"
 
2) authors.py - Adds a route, for e.g. ​ http://localhost:8080/authors​ , which: 
a) fetches a list of authors from a request to 
https://jsonplaceholder.typicode.com/users 
b) fetches a list of posts from a request to 
https://jsonplaceholder.typicode.com/posts 
c) Respond with ​ only​ a list of authors and the count of their posts (a newline for each author). 
 
3) set-cookie.py - Sets a simple cookie (​ if it has not already been set ) ​ at http://localhost:8080/setcookie​ with the following values: name=<your-first-name>​ and ​ age=<your-age>​ . 
 
4) get-cookie.py - Fetches the set cookie with ​ http://localhost:8080/getcookies​ and display the stored key-values in it. 
 
5) deny-requests.py - Deny requests to your ​ http://localhost:8080/robots.txt​ page. 
 
6) send-html.py - Render an HTML page at ​ http://localhost:8080/html​ . 
 
7) send-data.py - A text box at ​ http://localhost:8080/input​ which sends the data as ​ POST​ to an endpoint. This endpoint logs the received input to stdout​ .

templates - A folder contains the html pages that serve the requests by the client.

To run the programs on a local ubuntu machine with pyhton3 installed, the following steps need to be followed:
1) Change directory to the directory containing all the given files and folders in repository using cd command.
2) Create a vrtual environment for the programs to run using the following commands:
   $ virtualenv folder_name     # folder_name can be any name of your choice
   Ex: 
   $ virtualenv venv
3) Activate this environment using the following command:
   $ source venv/bin/activate   # here venv is the folder name that is created above
4) Import the flask module in this virtual environment using the command:
   (venv) $ import flask
5) Now run any of the desired programs using the given command:
   (venv) $ python3 program_name.py
6) The program is now successfully running on your local server. To view it, open your browser and type                
   http://localhost:8080/ along with the desired path according to the programs given above. 
   For example: 
   (venv) $ pyhton3 send-html.py
   runs the request at the URL given below
   http://localhost:8080/html
   
