# ML_Max-MSP_Python

By Ramin Akhavijou
ramin.akhavijou@gmail.com
www.akhavijou.com

This patch facilitates the transfer of data between Max/MSP and Python for machine learning purposes using UDP. The UDP protocol is utilized to send and receive data in both Python and Max/MSP. Given Python's extensive machine learning libraries, the data is sent to Python for processing and subsequently returned to Max/MSP for result generation or further processing.
The patch serves an educational purpose, and the accompanying code is designed to test the connections between these two code environments. However, the provided code is a straightforward machine learning model. It predicts the next notes using a supervised regression method in machine learning.

I have seperated patches for a better understanding and facilitating changing the codes for user. To run the patches and receive data in Python do the following:
1) open up the Max patch UDP_MAX_ML for sending intended data (the default is sending sensors' data or sending key slider notes)
2) open Python script UDP_MAX_receiver and run the script
3) interact with Max patch; all data during interaction will be sent to Python and saved in a file
4) run Python script ML_Pattern5 that starts processing ML on the recevied data from Max and it will save the data in a new file
5) run Python script UDP-send to send the new data back to Max/MSP
6) you now have a new data (your interacted data + added predicted data) in Max/MSP
   
