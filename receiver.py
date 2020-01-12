import asyncio
import aioserial
from datetime import datetime


class Receiver:

    def __init__(self):
        self.counter = 1
        self.aioserial_instance = aioserial.AioSerial(port='/dev/ttyUSB1')
        self.loop = asyncio.get_event_loop()
        try:
            self.loop.run_until_complete(self.receive_measurements())
        finally:
            self.loop.run_until_complete(self.loop.shutdown_asyncgens())  # Python 3.6 only
            self.loop.close()

    async def receive_measurements(self):
        while True:
            result = (await self.aioserial_instance.readline_async()).decode(errors='ignore')
            print("{}: {}".format(datetime.now(), result))


if __name__ == '__main__':
    receiver = Receiver()
