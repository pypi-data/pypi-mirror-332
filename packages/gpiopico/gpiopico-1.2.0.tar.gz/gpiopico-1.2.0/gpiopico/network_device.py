from utime import sleep
import network
import urequests
import ujson

class Network:
    """
        Use Only with raspberry pi pico w
    """
    def __init__(self, ssid, password) -> None:
        self.ip = self._connect(ssid, password)
        self._response = None
        self._format = 'json'

    def _connect(self, ssid:str, password:str)->str:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)
        while wlan.isconnected() == False:
            print('Waiting for connection..')
            sleep(1)
        ip = wlan.ifconfig()[0]
        print(f'Connected on ip -> {ip}')
        return ip
            

    def _format_return(self):
        if self._format == 'json':
            return self._response.json()
        elif self._format == 'text':
            return self._response.text
        return self._response

    def put(self, url:str, headers={}, params={}, body={}, format_response:str='json'):
        print(f'PUT {url} - body {body}')
        self._format = format_response
        self._response = urequests.put(url, headers=headers, json=body, headers=headers, params=params)
        return self._format_return()
    
    def delete(self, url:str, headers={}, params={}, body={}, format_response:str='json'):
        print(f'DELETE {url} - body {body}')
        self._format = format_response
        self._response = urequests.delete(url, headers=headers, json=body, headers=headers, params=params)
        return self._format_return()
    
    def get(self, url:str, headers={}, params={}, format_response:str='json'):
        print(f'Get {url}')
        self._format = format_response
        self._response = urequests.get(url, headers=headers, params=params)
        return self._format_return()

    def post(self, url:str, headers={}, params={}, body={}, format_response:str='json'):
        print(f'Post {url} - body {body}')
        self._format = format_response
        self._response = urequests.post(url, headers=headers, json=body, headers=headers, params=params)
        return self._format_return()
