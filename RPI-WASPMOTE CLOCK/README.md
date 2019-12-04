WAPMOTE CLOCK ANALYSIS

Waspmote has  an inbuilt Real Time Clock, which keeps it informed of the time.
In that way, it is possible and easy to set an alarm each time we want to wake it up 
to take a measure from the field. 

More information about the set up of the RTC of waspmote 
in Libelium's guide -> http://www.libelium.com/downloads/documentation/waspmote-rtc-programming_guide.pdf



RASPBERRY PI CLOCK ANALYSIS

While the Pi is connected to a network it sets its clock correctly using NTP. 
Without a network connection the system time and date will almost certainly be wrong. 
This is a problem for our project because we are performing  time sensitive operations.
This can be solved using a Real Time Clock (RTC) module. 
This will use a small coin cell battery to keep the time for the Pi even if it is turned off. 
When the Pi reboots it can set it’s own internal clock using the time held in by the RTC.
