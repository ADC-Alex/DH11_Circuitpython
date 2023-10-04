# DH11_Circuitpython
Temperature and Humidity sensor using RaspberryPi Pico HW 
This project was developed using CircuitPython to record temperature and humidity using a DHT11 sensor with a Raspberry Pi Pico and display the data on an LCD1602 module.
To interface a Raspberry Pi Pico with an LCD1602 module using CircuitPython, you can use the "CircuitPython_CharLCD" library. Make sure you have the library installed on your Pico. 
You can install it using the Adafruit CircuitPython bundle or by manually downloading the library from the Adafruit CircuitPython library repository.
You'll also need the adafruit_dht library for the DHT11 sensor. Make sure you have this library installed on your Pico.

![IMG_2414](https://github.com/ADC-Alex/DH11_Circuitpython/assets/144302937/afa67b1a-6216-437d-b50e-9e6b68699da2)

Make sure your connections are correct, and adjust the GPIO pins in the code if needed to match your physical connections. 
This code will continuously display temperature and humidity readings on the LCD1602 module while handling errors gracefully.
