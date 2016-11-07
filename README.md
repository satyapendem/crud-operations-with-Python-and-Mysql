# Crud-Operations-with-Python-and-Mysql
This is a basic example for Flask-python and Mysql. Basically this repository contains the run.py which will contains the all the crud operation functions and it will throws the HTML files based on the events. 
#Requirements

 1.python 2.7.11 <br />
   a. Download python from python.org.<br>
   b.tar -xzf Python-2.7.11.tgz <br>
   c. cd Python-2.7.11<br>
   d. use the following commands "./configure"<br>
   e. After successfull configure use "make"<br>
   f. After successfull make use "sudo make install"<br>
 2. flask<br>
   a. sudo apt-get install virtualenv<br>
   b. sudo pip install virtualenv(sudo apt-get install python-virtualenv)<br>
   c. sudo pip install flask<br>
 3. mysql Database(sudo apt-get install mysql-server)<br>
 4. pymysql(sudo pip install pymysql)<br>

The CRUD operations are performed with Flask and mysql with simple Sql queries. It contains the INSERT,DELETE,UPDATE,SELECT
operations in simple Flask Program.

The all HTML files are present in the "Templates" Directory.

when ever user opens the Browser and enters "localhost:5000" then the main function will execute and it throw "index.html" page which will contains main links. 
![alt tag](https://github.com/satyapendem/crud-operations-with-Python-and-Mysql/blob/master/ScreenShots/x.png)

The first operation is "Insert". By clicking the insert then the "createForm" function will execute and will throw "insert.html" which contains name,latitude,longitude textfields.

![alt tag](https://github.com/satyapendem/crud-operations-with-Python-and-Mysql/blob/master/ScreenShots/insert.png)
After that "insert" function will be executed the form values are loaded to python script and the values are stored in mysql
database. If it was success the it will dispay the name for the user as shown below.
![alt tag](https://github.com/satyapendem/crud-operations-with-Python-and-Mysql/blob/master/ScreenShots/insert1.png)

If you click the "showdetails" link then "select" function will be executed and will throw a "show.html" for which will contains the values retrived from database.
![alt tag](https://github.com/satyapendem/crud-operations-with-Python-and-Mysql/blob/master/ScreenShots/show.png)

The user can update the values in the table based on ID by clicking the "update" in index.html. By clicking update "update"
function will be executed and it will throw a html form which will take ID as input.

![alt tag](https://github.com/satyapendem/crud-operations-with-Python-and-Mysql/blob/master/ScreenShots/update.png)
After entering ID and submiting it goto "update_details" form and it will throw HTML page with textfileds and data from the 
database as shown below image.
![alt tag](https://github.com/satyapendem/crud-operations-with-Python-and-Mysql/blob/master/ScreenShots/update1.png)
After successfull update it will display the nameof the user who updated the details as shown below.
![alt tag](https://github.com/satyapendem/crud-operations-with-Python-and-Mysql/blob/master/ScreenShots/update2.png)

The user can delete the details based on ID just like update. As shown beow
![alt tag](https://github.com/satyapendem/crud-operations-with-Python-and-Mysql/blob/master/ScreenShots/delete.png)
![alt tag](https://github.com/satyapendem/crud-operations-with-Python-and-Mysql/blob/master/ScreenShots/delete1.png)

The showJson will display data in the form of JSON. If anyone want insert the into some other Database it will be very helpfull.
![alt tag](https://github.com/satyapendem/crud-operations-with-Python-and-Mysql/blob/master/ScreenShots/json.png)

                                                Thank You








