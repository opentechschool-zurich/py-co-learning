import asyncio
import subprocess
import termios, fcntl, sys, os
import sys

class Terminating(Exception):
    pass

class Command:
    def __init__(self, cmd):
        self.cmd = cmd
        self.popen = None

    def execute(self):
        self.popen = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, universal_newlines=True)
        for stdout_line in iter(self.popen.stdout.readline, ""):
            yield stdout_line
        self.popen.stdout.close()
        return_code = self.popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, self.cmd)
    def stop(self):
        self.popen.terminate()

class Keyboard:
    def __init__(self):
        self.fd = None
        self.oldterm = None
        self.oldflags = None

    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.oldterm = termios.tcgetattr(self.fd)
        newattr = termios.tcgetattr(self.fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(self.fd, termios.TCSANOW, newattr)

        self.oldflags = fcntl.fcntl(self.fd, fcntl.F_GETFL)
        fcntl.fcntl(self.fd, fcntl.F_SETFL, self.oldflags | os.O_NONBLOCK)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.oldterm)
        fcntl.fcntl(self.fd, fcntl.F_SETFL, self.oldflags)

        self.fd = None
        self.oldterm = None
        self.oldflags = None

    def get_char(self):
        while True:
            c = sys.stdin.read(1)
            if not c:
                break
            yield c

async def read_key():
    with Keyboard() as keyboard:
        while True:
            # TODO: find out why it does not work without sleep
            await asyncio.sleep(1)
            try:
                for c in keyboard.get_char():
                    if c == 'c':
                          raise Terminating
            except IOError:
                pass

async def read_process():
    # cmd = Command(['ping', '192.168.178.1'])
    cmd = Command(['ping', '127.0.0.1'])
    # cmd = Command(['sleep', '5'])
    for output in cmd.execute():
        # TODO: find out why it does not work without sleep
        await asyncio.sleep(1)
        await print(output, end="")

    raise Terminating

async def main():
    gathering = asyncio.gather(
        read_key(),
        read_process()
    )
    try:
        await gathering
    except Terminating:
        for task in gathering._children:
            task.cancel()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

