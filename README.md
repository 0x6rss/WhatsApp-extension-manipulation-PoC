# WhatsApp-extension-manipulation-PoC
Android malware (.apk) can be spread through a fake PDF document by manipulating the file extension in the WhatsApp application. PoC is available in this repo

### Step 1: First, create a free account at https://user.ultramsg.com/signup.php. We will use this to manage the API

### Step 2: Click the "Add Instance" button and create a new instance. <br>
![image](https://github.com/user-attachments/assets/56b60b25-e1ec-4913-9b6d-fdaa325b7762) <br>


### Step 3: Fill in the appropriate fields in wp.py with the generated API information and log in to your WhatsApp application using the QR code found under the instance information. <br>
![mJAWHAyz (1)](https://github.com/user-attachments/assets/64609edd-33d6-43a9-9d60-edb04fb96637) <br>

### Step 4: Enter the target number in the "enter number" field and upload your file to the server (this can be an ngrok or python server. If you are testing locally, you can use XAMPP).


### Step 5: Run the wp.py file and watch the message being sent.
```sh
python wp.py
