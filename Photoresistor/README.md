Raspberry Pi Requirements:

For this project i worked on a Raspberry Pi 3 model b+

We need to install:

-python3, in order to run the python script -> sudo apt-get install python3

-GPIO, in order to gain access to the RPi's GPIO pins -> sudo apt-get install RPi.GPIO

For the sensor installation we need:

-Raspberry Pi x 1
-1x LDR(light dependent resistor)
-1x Breadboard
-1x 1µf capacitor
-3x(or more) Jumper Wires

**NOTE:LDRs are slow acting and non-linear.They are not well suited to accurate measurement of light intensity,but 
better employed for light detection.**

Building the circuit:

1)Connect pin #1 (3v3) to the positive rail on the breadboard.
(If the breadboard doesn't have positive rail, connect the wire directly to the left side of the LDR)

2)Connect pin #6 (ground) to the ground rail on the breadboard.
(If the breadboard doesn't have negative rail,connect the wire directly after the negative pin of the capasitor)

3)Place the LDR sensor onto the board and have a wire go from one end to the positive rail.

4)On the other side of the LDR sensor place a wire leading back to the Raspberry Pi. Hook this to pin #7.

5)Place the capacitor from the wire to the negative rail on the breadboard. Make sure you have the negative 
pin of the capacitor in the negative rail.
 
Run the script using the command : python light_sensor.py

How it works:

The sensor will essentially charge a 1µF capacitor while measuring the amount of time needed until it 
is fully charged. This charging time is what will be measured, and use it as an approximation 
for the brightness in the area of the sensor. In the absence of light, there will be very little current flowing, 
and thus the capacitor will take longer to charge. On the other hand, 
the presence of light, there is more current flowing, and the capacitor charges quickly.
After this we will have measured the value of the LDR resistance,so we can use it to calculate the light in lux with 
the equation below:

lux = 10000 / [(R[Ω]/100)^(4/3)]

*R[Ω] is the resistance of the LDR


Illuminance (lux)	Surfaces illuminated by

0.0001   	  >      Moonless, overcast night sky (starlight)
0.002	       >         Moonless clear night sky with airglow
0.05–0.3	    >    Full moon on a clear night
3.4	         >       Dark limit of civil twilight under a clear sky
20–50	        >        Public areas with dark surroundings
50	           >     Family living room lights
80	           >     Office building hallway/toilet lighting
100	          >      Very dark overcast day
150	          >      Train station platforms
320–500	       >         Office lighting
400	           >     Sunrise or sunset on a clear day.
1000	           >     Overcast day-typical TV studio lighting
10,000–25,000	   >     Full daylight (not direct sun)
32,000–100,000	   >     Direct sunlight


