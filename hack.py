import subprocess
import os, sys

correct_file = './Files/correct.cpp'

# files to compare with `correct file` output
files = [
    './Files/wrong1.cpp',
    # './Files/wrong2.cpp',
    # './Files/wrong3.cpp',
    # './Files/wrong4.cpp',
]

io_files = {
    "input_file" : "./Files/in.txt",
    "output_file" : "./Files/out.txt",
    "wa_file": "./Files/wa.txt",
    "testcase_file" : "./testcase.cpp",
    "validator_file": "./validator.cpp",
}

# clear files
with open(io_files["input_file"], "w") as file:
    file.write("")
with open(io_files["output_file"], "w") as file:
    file.write("")
with open(io_files["wa_file"], "w") as file:
    file.write("")

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

# run(execute) file and return the output
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
def Format(out):
    out = out.split('\n')
    res = ""
    for o in out:
        o = o.strip()
        if(o != "" and o != "\n"):
            res += o + "\n"
    return res.strip()

# color text on terminal 

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
# Compile(io_files["validator_file"])

# compile all java and c++ file
Compile(correct_file)
for f in files:
    Compile(f)

print()
test_case = 1
while(True):
    try:
        Print("yellow", f"Case # {test_case} : ", end = '')

        # generate test case
        std_input = Run(io_files["testcase_file"]).stdout.strip()

        # testcase validator
        # Run(io_files["validator_file"], std_input)

        # store all outputs
        std_output = Format(Run(correct_file, std_input).stdout)
        outputs = []
        for f in files:
            outputs.append(Format(Run(f, std_input).stdout))

        # check
        ok = True
        for out in outputs:
            if out != std_output:
                ok = False
                break

        if(not ok):
            Print("red", "Wrong Answer")

            # print input & output
            Print("cyan", "Input")
            print(std_input)

            Print("cyan", "\nOutput")
            print(std_output)

            # print all outputs
            for i in range(len(files)):
                Print("cyan", f"\n{files[i]}")
                print(outputs[i])

            # print diffrent files
            Print("yellow", "\nMismatched files")
            for i in range(len(files)):
                if(outputs[i] != std_output):
                    Print("cyan", files[i])

            # store input & output
            with open(io_files["input_file"], "w") as file:
                file.write(std_input)

            with open(io_files["output_file"], "w") as file:
                file.write(std_output)

            # special log
            if(len(files) == 1):
                log = "# Testcase\n" + std_input
                log += "\n\n# Participant\n" + outputs[0]
                log += "\n\n# Expected\n" + std_output
                log += "\n\n" +  "-" * 50 + "\n"

                with open(io_files["wa_file"], "a") as file:
                    file.write(log)

            Print("purple", "\nPress 1 to stop : ", end = '')
            brk = int(input())
            if(brk == 1):
                break
        else:
            Print("green", "Accepted")
            if(test_case <= 5):
                print("Input")
                print(std_input)
                print("\nOutput")
                print(std_output)
                for i in range(len(files)):
                    print(f"\n{files[i]}")
                    print(outputs[i])

        test_case += 1

    except KeyboardInterrupt:
        Print("red", "\nFinished")
        sys.exit(0)