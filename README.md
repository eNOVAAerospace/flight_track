# flight_track

> Project realized by Antoine Rovini, student at Epitech Technology, Promo 2025.

In this program, Airlabs's API is used to retrieve flight data around the globe. Here is a tutorial to help you to use
it.

We have two programs that aren't merged, so we will do use them separately.

Bear in mind that this program isn't automated yet, so you will have to do it manually, and that the usage of this
program is limite to 1000 use per month.

> To install dependencies, you will have to click on the "install_all_packages.exe" file. It will install all the needed
> dependencies for the program to work.

-------------

## How to : use the program 'main.py'

On the dump, you will see a file and a folder. the program is contained in the main.py file and the library in the
folder, so don't delete or modify anything. you will have to keep this configuration so the program can work.

![img.png](library/readme/azertyhgcx.png)

Now we will click on the "wrap_planes.exe" file. It will open a command prompt.

![img.png](library/readme/dcvbjhgv.png)

As you can see, it will ask you to choose if you want to automate the process or not. If you choose to automate it, you
will have to type "0" for yes, otherwise, type "1" for no. Let's choose "0" for now, we will follow up step by step the
process.

![img_1.png](library/readme/gvbnj,.png)

Now, it asks to enter the number of requests you want to make. There is no maximum, but keep in mind the limits of the
API. We will type "2" for now, asking then 2 data retrieval.

![img_2.png](library/readme/fvbj,l.png)

Now, it asks to enter the number of seconds between each request. This is to avoid being blocked by the API. As you can
see, it asks to provide the time in seconds, it is to be accurate in the time calculation between each request. We will
type "10" for ten second. It will do 1 request each 10 seconds and permit us to see what it does.

![img_3.png](library/readme/aqsxcvghjk.png)

As you see, the data retrieval has started. It will take some time, depending on the number of requests you asked. It
will close automatically once all the requests are done.

This command applies itself in Windows, Linux, and Mac.

![img_4.png](library/readme/aqwxcvbn.png)


Those are the new files. One of them is a JSON file and the other CSV, it won't interest us, so we can remove them if we
want to. The file with the 'excel_' prefixe is the one that interest us and has the data with the correct format for
usage. Note that if you chose to make multiple requests, there will be multiple files, each one will have the exact time
it was done.

------------

## How to : use the program 'list_planes.py'

On the dump, you will see a file named 'list_planes.py'. as for the previous program, the library/ folder mustn't be
touched, modified, or moved.


![img.png](library/readme/rfcvhytf.png)

You will have to keep this configuration so the program can work. Now, we'll take the exact same command prompt, and
type in the following command:
> **python list_planes.py**
> 
> ![img.png](library/readme/ascvbhg.png)

It will ask you to provide the file name that was created. Here, the name of our file is
'tab_2023-06-09_17_02_48_flight.csv'. The naming is quite simple : 'tab' is meant for the CSV version of the file, the
numbers have the format YYYY-MM-DD_HH_MM_SS (Year, Month, Day, Hour, Minute, Second), and flight.
So actually our current file is : tab_2023-06-15_15-59-12_flight.csv

Let's continue by entering the name of the file.
After pressing enter, you will have the following display : 

![img_1.png](library/readme/aqwxcvbn,.png)

on this display we see in the pormpt 'plane number #1 Lat: 49.98      Lng: 62.86'. This is subject to be removed in the
long run, but it attests that data has been written. The data will be written in the filename with the 'sorted_' prefix.
You will see it in your file explorer.

![img.png](library/readme/ergx.png)

For notice, the 'coordinates.txt' file is read by the program to filter the requested zone using 4 point, two lat and
two lng point, as shown in the file:

![img.png](library/readme/asdvbn.png)

It is mandatory to keep the same format as it won't be functional otherwise.