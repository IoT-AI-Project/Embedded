Reolink Go Analysis

1)CAPABILITIES

•	4G Connectivity: It connects to 4G LTE wireless network, enabling it to roam free in locations with limited or no Wi-Fi. 

•	Waterproof

•	Siren: An alarm (built-in Siren) will sound automatically when motion is detected.

•	Rechargeable Battery: Long-running rechargeable battery extends battery life

•	Solar Charging: It can connect to Reolink Solar Panel for constant solar charging and non-stop power supply.

•	1080p Full HD: It provides true 1080p (1920*1080) Full HD with 130° wide viewing angle.

•	Cloud Storage: Save motion-triggered recordings securely in the Reolink Cloud and never miss important details.

•	operates on 4G-LTE and 3G networks.

-----------------------------------------------------------------------------------------

2)PLACEMENT

- The viewing angle of Reolink Go is diagonal 130° and horizontal 110° vertical. Μake sure that the monitoring area is well within its field of view.

- The ideal viewing distance is 2-10 meters). To achieve a better viewing experience, it's advised not to place the camera too far away or too high (suggested mounting height: 2-3 meter) from the designated monitoring area.

•	Do not install the camera facing any objects with bright lights, like sunshine.

-----------------------------------------------------------------------------------------

3)APP INSTALLATION

Install the SIM card and power it up, then you may start the initial setup via the Reolink App when you hear the voice "Network connection succeeded".

1) Tap on the icon in the top right corner to start configuration.

2) Scan the QR code on the back of the camera. If the phone doesn't respond, please click on the Enter button below the scan window and then type in the 16-digits characters under the QR code of the camera.

3) Create the login password and click Next to continue.

4) Name the camera, then click the button Next to enter the next page.

5) Read the tips and click Use now to finish the Initialization.

-----------------------------------------------------------------------------------------

4)FTP INSTALLATION

a) Raspberry Pi Set up

- Install Pure-FTPd -> sudo apt install pure-ftpd
------------------------------------------------------------------
- Create a new user group named ftpgroup and a new user named ftpuser for FTP users, and make sure this "user" has no login privilege and no home directory

-> sudo groupadd ftpgroup

-> sudo useradd ftpuser -g ftpgroup -s /sbin/nologin -d /dev/null

--------------------------------------------------------------------
- Make a new directory named FTP for this user

-> sudo mkdir /home/pi/FTP

-> sudo chown -R ftpuser:ftpgroup /home/pi/FTP

---------------------------------------------------------------------

- Create a virtual user named upload, mapping the virtual user to ftpuser and ftpgroup, setting home directory /home/pi/FTP, and record password of the user in database:

-> sudo pure-pw useradd upload -u ftpuser -g ftpgroup -d /home/pi/FTP -m

- set up a virtual user database -> sudo pure-pw mkdb

-----------------------------------------------------------------------------------------------
- Define an authentication method by making a link of file /etc/pure-ftpd/conf/PureDB

-> sudo ln -s /etc/pure-ftpd/conf/PureDB /etc/pure-ftpd/auth/60puredb

For extra configuration:

The administrator only needs to define the necessary settings by making files with option names, like ChrootEveryone, and typing yes, then storing in the directory /etc/pure-ftpd/conf, if all FTP users are to be locked in their FTP home directory (/home/pi/FTP). Here are some recommended settings:


-> sudo nano /etc/pure-ftpd/conf/ChrootEveryone

Type yes, and press Ctrl + X, Y, and Enter.

Likewise,

Make a file named NoAnonymous and type yes;

Make a file named AnonymousCantUpload and type yes;

Make a file named AnonymousCanCreateDirs and type no;

Make a file named DisplayDotFiles and type no;

Make a file named DontResolve and type yes;

Make a file named ProhibitDotFilesRead and type yes;

Make a file named ProhibitDotFilesWrite and type yes;

Make a file named FSCharset and typeUTF-8;

Finally:

-> sudo service pure-ftpd restart


b) Reolink Go set up

Step 1. Launch Reolink App, log into your device and click Device Settings.

Step 2. Go to More-> FTP UPload page, enable FTP Upload option and then click FTP Settings to enter this page.

Step 3. Complete the information required and click Sure to save all the settings.

•	Server Address: Type in the address of your FTP server and FTP Port. The default FTP Port for Reolink products is 21.

•	User Name and Password: Enter the User Name and Password of your FTP server. If there is no username and password required, please enable Anonymous FTP.

•	Upload Directory: Set an upload directory for device video recording. You may also leave it blank.

•	Maximum File Length: you can enter the file length here.

•	File Type: Choose to upload both video and picture or picture only.

•	FTP Postpone: Set the record time limit after a motion is detected. This option is only available when File Type is Video and FTP Schedule is Motion.

•	Transfer Mode: divided into Auto, PORT, and PASV three parts. We suggest you choose the Auto option.




