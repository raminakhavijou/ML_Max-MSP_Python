# ML_Max-MSP_Python

By Ramin Akhavijou
ramin.akhavijou@gmail.com
www.akhavijou.com

This patch facilitates the transfer of data between Max/MSP and Python for machine learning purposes using UDP. The UDP protocol is utilized to send and receive data in both Python and Max/MSP. Given Python's extensive machine learning libraries, the data is sent to Python for processing and subsequently returned to Max/MSP for result generation or further processing.
The patch serves an educational purpose, and the accompanying code is designed to test the connections between these two code environments. However, the provided code is a straightforward machine learning model. It predicts the next notes using a supervised regression method in machine learning.

I've separated the patches to enhance understanding and facilitate code modification for users. To execute the patches and receive data in Python, follow these steps:

1) Open the Max patch named "UDP_MAX_ML" to send the intended data (by default, it sends sensor data or kslider notes).
2) Open the Python script "UDP_MAX_receiver" and run the script.
3) Interact with the Max patch; all data generated during interaction will be sent to Python and saved in a file.
4) Run the Python script "ML_Pattern5" to initiate machine learning processing on the received data from Max. The processed data will be saved in a new file.
5) Run the Python script "UDP-send" to send the updated data back to Max/MSP.
   
Now, you have a new dataset in Max/MSP, comprising your interacted data along with the added predicted data.
   
