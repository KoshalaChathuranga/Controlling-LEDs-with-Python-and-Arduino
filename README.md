#Controlling LEDs with Python and Arduino

This project demonstrates how to control LEDs connected to an Arduino board using a Python GUI application. The Python code uses PyQt5 for the GUI and communicates with the Arduino board over a serial connection.
Requirements
Hardware:

    Arduino board
    LEDs (connected to digital pins 14 to 19 on the Arduino board)
    Resistors (if necessary, for current limiting)

Software:

    Python 3.x
    PyQt5 library
    Arduino IDE

Setup

    Upload Arduino Code:
        Connect your Arduino board to your computer.
        Open the Arduino IDE and upload the provided Arduino code (arduino_code.ino) to your Arduino board.
        This code sets up the digital pins 14 to 19 as outputs and listens for commands over the serial port to turn on/off LEDs connected to those pins.

    Install Python Dependencies:
        Make sure you have Python 3.x installed on your computer.
        Install the PyQt5 library using pip:

        pip install PyQt5

Usage

    Run Python Script:
        Open a terminal or command prompt.
        Navigate to the directory containing the Python script (gui_control.py).
        Run the Python script:

        python gui_control.py

        This will launch the GUI application.

    Interact with the GUI:
        The GUI application will display buttons labeled B1 to B6.
        Each button corresponds to an LED connected to the Arduino board.
        Clicking a button will turn on the LED connected to the corresponding pin and turn off the previously selected LED.

    Close the Application:
        Close the GUI application window to exit the program.
        This will send a signal to the Arduino board to turn off all LEDs and close the serial connection.

Notes

    Make sure the Arduino board is connected to the correct serial port (e.g., COM4 on Windows) specified in the Python code (MyWindow class constructor).
    Adjust the pin numbers in both the Python and Arduino code if you connect the LEDs to different pins on the Arduino board.
    Ensure that the baud rate in the Arduino code (Serial.begin(9600)) matches the baud rate in the Python code (9600).
    Handle the hardware components with care, ensuring correct wiring and appropriate use of resistors to prevent damage to the components.
