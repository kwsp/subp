from subprocess import Popen, PIPE


# input to Popen is a list: ["executable", "flags", "arguments", ...]
proc = Popen(["python3", "echo.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)

while proc.poll() is None:  # while process has not exited

    inp = input()  # take user input, or put formatted data (e.g. weather) here

    # communicate's argument is passed to stdin, and the return values are stdout and stderr
    outs, errs = proc.communicate(
        inp.encode()
    )  # send data to the stdin of the running process

    print(outs.decode())  # Get output of the running program if desired.
