# aserial
Simple Python serial

#### Installation
This tool uses pipenv. First install the dependencies from Pipfile:

```pipenv install```

To activate pipenv shell:

```pipenv shell```

#### Sender
Use Sender to send fake measurements through serial port

```sudo python sender.py "/dev/ttyUSB0"```


#### Receiver
Use Receiver to recieve measurements from serial port

```sudo python receiver.py "/dev/ttyUSB1"```
