import RPi.GPIO as GPIO
import argparse

GPIO.setmode(GPIO.BCM)

def set_power(
        port: int,
        on: bool
):
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, on)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int, help="Which port to output on")
    parser.add_argument("on", type=bool, help="True for turning power on, false for off")
    args = parser.parse_args()

    set_power(args.port, args.on)