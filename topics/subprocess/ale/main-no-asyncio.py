import subprocess
import termios, fcntl, sys, os

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

class CommandTerminated(Exception):
    pass

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

def main():
    # cmd = Command(['ping', '192.168.178.1'])
    cmd = Command(['ping', '127.0.0.1'])
    # cmd = Command(['sleep', '5'])

    with Keyboard() as keyboard:
        for output in cmd.execute():
            print(output, end="")
            try:
                for c in keyboard.get_char():
                    if c == 'c':
                        cmd.stop()
                        raise CommandTerminated
            except CommandTerminated:
                break
            except IOError:
                pass

if __name__ == "__main__":
    main()
