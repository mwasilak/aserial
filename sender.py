import asyncio
import aioserial
from datetime import datetime
import sys


class Sender:

    def __init__(self, port):
        self.counter = 1
        self.aioserial_instance = aioserial.AioSerial(port)
        self.loop = asyncio.get_event_loop()
        try:
            self.loop.run_until_complete(self.send_measurements())
        finally:
            self.loop.run_until_complete(self.loop.shutdown_asyncgens())  # Python 3.6 only
            self.loop.close()

    async def send_measurements(self):
        while True:
            await self.aioserial_instance.write_async(str(self.counter).encode() + b"\n")
            print("{}: {}".format(datetime.now(), self.counter))
            self.counter += 1

            # Wait before next iteration:
            await asyncio.sleep(5)


if __name__ == '__main__':
    serial_port = sys.argv[1]
    sender = Sender(serial_port)
