import re
import subprocess

class Wifi:

    def __init__(self):
        pass

    @property
    def networks(self):
        process = subprocess.run(['iwlist', 'scan'], 
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                universal_newlines=True)
        results = re.findall(r'ESSID:\".*\"', process.stdout)
        networks = []
        for result in results:
            result = result.replace("ESSID:\"", "")[:-2]
            if result not in networks:
                networks += [result]
        return networks

    @property
    def current_network(self):
        process = subprocess.run(['iwgetid'],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                universal_newlines=True)

        match = re.search(r'ESSID:\"(.*)\"', process.stdout)
        try:
            return match.group(1)
        except IndexError:
            return ""

    def connect(self, essid, password):
        pass

