# Readme
A quick and dirty method to get an alert if a given website has updated.

Requirements.
* hashlib
* urllib
* notify_run

The push notification is done using this library called notify_run, an amazing library (https://github.com/notify-run/notify.run/tree/master/py_client).
Just follow the instructions in the website https://notify.run/ and you are good to go. 

Also,this is a quick and dirty method. For better performance its better to parse the text and hash only certain headers, but thats for futher update.
