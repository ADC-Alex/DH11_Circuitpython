import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd
import time
import Adafruit_DHT

# Define LCD pin configuration
lcd_rs = digitalio.DigitalInOut(board.GP0)  # Register Select (RS) pin
lcd_en = digitalio.DigitalInOut(board.GP1)  # Enable (E) pin
lcd_d4 = digitalio.DigitalInOut(board.GP4)  # Data pin D4
lcd_d5 = digitalio.DigitalInOut(board.GP5)  # Data pin D5
lcd_d6 = digitalio.DigitalInOut(board.GP6)  # Data pin D6
lcd_d7 = digitalio.DigitalInOut(board.GP7)  # Data pin D7

# Set the LCD dimensions (16x2)
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD object
lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# Initialize the DHT11 sensor
dht = Adafruit_DHT.DHT11(board.GP3)  # DHT11 sensor connected to GP3

while True:
    try:
        # Read temperature and humidity from the DHT11 sensor
        temperature_celsius = dht.temperature
        humidity_percent = dht.humidity

        # Display the temperature and humidity on the LCD
        lcd.message = f"Temp: {temperature_celsius:.1f} C\nHumidity: {humidity_percent:.1f}%"

    except Exception as e:
        # Handle any errors reading from the DHT11 sensor
        lcd.message = "Error reading DHT11"

    # Wait for a few seconds before the next reading
    time.sleep(2)
