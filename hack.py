import subprocess
import os, sys

no_users = 2
files = [ # first file Expected output
    './Files/correct.cpp',
    './Files/wrong1.cpp',
    './Files/wrong2.cpp',
    './Files/wrong3.cpp',
    './Files/wrong4.cpp',
]

io_files = {
    "input_file" : "./Files/in.txt",
    "wa_file": "./Files/wa.txt",
    "testcase_file" : "./testcase.cpp",
    "validator": "./validator.cpp",
}

# compile cpp, c, java file
def Compile(file_path):
    lang = file_path.split(".")[-1]
    if(lang == "cpp" or lang == "c"):
        cmd = "g++ -std=c++17 -DONLINE_JUDGE {} -o {}.exe".format(file_path, file_path)
    elif(lang == "java"):
        cmd = "javac {}".format(file_path)
    else:
        return -1

    print('\nCompiling ', end = '')
    Print("purple", file_path)
    
    subprocess.run(cmd, check = True, shell = True)
    print('Compilation done')

# Run file and return output
def Run(file_path, std_input = None):
    lang = file_path.split(".")[-1]
    if(lang == "cpp" or lang == "c"):
        cmd = "\"{}.exe\"".format(file_path)
    elif(lang == "java"):
        cmd = "java Main"
    elif(lang == "py"):
        cmd = "python \"{}\"".format(file_path)
    else:
        return -1

    return subprocess.run(cmd, input = std_input, capture_output = True, shell = True, text = True, check = True)

# remove extra spaces and new lines
def format(out):
    out = out.split('\n')
    res = ""
    for o in out:
        o = o.strip()
        if(o != "" and o != "\n"):
            res += o + "\n"
    return res.strip()

# color text on terminal ----------------------------------------------------

import colorama
from colorama import Fore, Back, Style
colorama.init()

clr_list = {
    "red" : Fore.RED,
    "yellow" : Fore.YELLOW,
    "green" : Fore.GREEN,
    "cyan" : Fore.CYAN,
    "blue" : Fore.BLUE,
    "purple" : Fore.MAGENTA
}

def setColor(clr):
    global clr_list
    print(Style.BRIGHT + clr_list[clr], end = '')

def resetColor():
    print(Style.RESET_ALL, end = '')

# print with color, first argument is color name
def Print(*args, **kwargs):
    resetColor()
    if len(args):
        clr = args[0]
        args = args[1::]
        setColor(clr)
    print(*args, **kwargs)
    resetColor()

# ---------------------------------------------------------------------------

# compile test case file
Compile(io_files["testcase_file"])
# Compile(io_files["validator"])

# compile all java and c++ file
for i in range(no_users):
    Compile(files[i])

with open(io_files["wa_file"], "w") as file:
    file.write("")

print(f"\ntotal users : {no_users}")
test_case = 1
while(True):
    try:
        Print("yellow", f"Case # {test_case} : ", end = '')

        # generate test case
        Input = Run(io_files["testcase_file"]).stdout.strip()
        # print(f'\n{Input}')

        # uncomment for testcase validator
        # Run(io_files["validator"], Input)

        # store all outputs
        Outputs = []
        for i in range(no_users):
            Outputs.append(format(Run(files[i], Input).stdout))

        # check
        if(len(set(Outputs)) != 1):

            Print("red", "Wrong Answer")
            Print("cyan", "Input")
            print(Input)

            for i in range(no_users):
                Print("cyan", f"\n{files[i]}")
                print(Outputs[i])

            Print("yellow", "\nDiffrent files:")

            for i in range(no_users):
                if(Outputs[i] != Outputs[0]):
                    Print("cyan", files[i])

            # store input in file
            with open(io_files["input_file"], "w") as file:
                file.write(Input)

            if(no_users == 2):
                Input += "\n\n# Participant\n" + Outputs[1]
                Input += "\n\n# Expected\n" + Outputs[0]
                Input += "\n\n" +  "-" * 50 + "\n"

                with open(io_files["wa_file"], "a") as file:
                    file.write("# TestCase\n" + Input)

            Print("purple", "\nBreak (0/1) : ", end = '')
            brk = int(input())
            if(brk == 1):
                break
        else:
            Print("green", "Accepted")
            if(test_case <= 5):
                print(Input)
                for out in Outputs:
                    print('\n', out, sep = '')
        test_case += 1

    except KeyboardInterrupt:
        Print("red", "\nFinished")
        sys.exit(0)