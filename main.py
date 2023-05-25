from requests import get as get_request
from time import sleep
import RPi.GPIO as GPIO

def main(url:str) -> None:
    
    while True:
        response = get_request(url=url)
        
        led1_status = bool(response.json()['status_1'])
        led2_status = bool(response.json()['status_2'])
        
        GPIO.output(38, led1_status)
        GPIO.output(40, led2_status)
        
        sleep(0.25)
    
if __name__ == '__main__':
    from tomli import load as load_toml
    
    with open("settings.toml", mode="rb") as fp:
        config:dict = load_toml(fp)
    fp.close()

    IP_SERVER:str = config['server']['ip']
    PORT_SERVER:int = config['server']['port']
    API_ENDPOINT: str = config['server']['endopoint']
    
    URL = f"http://{IP_SERVER}:{PORT_SERVER}{API_ENDPOINT}"
    
    GPIO.setmode(GPIO.Board)
    GPIO.setwarnings(False)
    GPIO.setup(38, GPIO.OUT)
    GPIO.setup(40, GPIO.OUT)
    
    main(url=URL)