import os, sys, subprocess
import winsound
from color_print import cprint
from compile_run import compile, run

path = {
    "incorrect_files": [
        "./Files/wrong1.cpp",
        # "./Files/wrong2.cpp",
        # "./Files/wrong3.cpp",
        # "./Files/wrong4.cpp",
        # "../1.cpp",
        # "../2.cpp",
    ],
    "correct_file": "./Files/correct.cpp",
    "in_file": "./Files/in.txt",
    "out_file": "./Files/out.txt",
    "wa_file": "./Files/wa.txt",
    "testcase_file": "./testcase.cpp",
    "validator_file": "./validator.cpp",
}

# remove extra spaces and new lines
def adjust(out):
    out = out.split('\n')
    res = ""
    for o in out:
        o = o.strip()
        if(o != "" and o != "\n"):
            res += o + "\n"
    return res.strip()

def process():
    test_case = 1
    while(True):
        try:
            cprint(f"Case # {test_case} : ", end = '', clr = "yellow")

            # generate test case
            std_input = run(path["testcase_file"]).stdout.strip()

            # testcase validator
            # run(path["validator_file"], std_input)

            # store all outputs
            std_output = adjust(run(path["correct_file"], std_input).stdout)
            outputs = []
            for file in path["incorrect_files"]:
                outputs.append(adjust(run(file, std_input).stdout))

            # check
            ok = True
            for out in outputs:
                if out != std_output:
                    ok = False
                    break

            if(not ok):
                cprint("Wrong Answer", clr = "red")

                # print input
                cprint("Input", clr = "cyan")
                print(std_input)

                # print output
                cprint("\nOutput", clr = "cyan")
                print(std_output)

                # print all outputs
                for i in range(len(path["incorrect_files"])):
                    cprint(f'\n{path["incorrect_files"][i]}', clr = "cyan")
                    print(outputs[i])

                # print diffrent files
                cprint("\nMismatched files", clr = "yellow")
                for i in range(len(path["incorrect_files"])):
                    if(outputs[i] != std_output):
                        cprint(path["incorrect_files"][i], clr = "cyan")

                # store input in 'in.txt'
                with open(path["in_file"], "w") as file:
                    file.write(std_input)

                # store output in 'out.txt'
                with open(path["out_file"], "w") as file:
                    file.write(std_output)

                # store expected and actual output in 'wa.txt'
                if(len(path["incorrect_files"]) == 1):
                    log = "# TestCase\n" + std_input + "\n"
                    log += "\n# Participant\n" + outputs[0] + "\n"
                    log += "\n# Expected\n" + std_output + "\n"
                    log += "\n" +  "-" * 50 + "\n"

                    with open(path["wa_file"], "a") as file:
                        file.write(log)

                # break?
                winsound.Beep(2500, 1000)
                cprint("\nPress 1 to stop : ", end = '', clr = "purple")
                brk = int(input())
                if(brk == 1):
                    break
            else:
                cprint("Accepted", clr = "green")
                if(test_case <= 5):
                    print("Input")
                    print(std_input)

                    print("\nOutput")
                    print(std_output)
                    
                    for i in range(len(path["incorrect_files"])):
                        print(f'\n{path["incorrect_files"][i]}')
                        print(outputs[i])

            test_case += 1

        except KeyboardInterrupt:
            cprint("\nFinished", clr = "red")
            sys.exit(0)

if __name__ == "__main__":
    print(path["incorrect_files"])

    # compile test case file
    compile(path["testcase_file"])

    # compile validator file
    # compile(path["validator_file"])

    # compile all java and c++ file
    compile(path["correct_file"])
    for file in path["incorrect_files"]:
        compile(file)

    # clear in.txt
    with open(path["in_file"], "w") as file:
        file.write("")

    # clear out.txt
    with open(path["out_file"], "w") as file:
        file.write("")

    # clear wa.txt
    with open(path["wa_file"], "w") as file:
        file.write("")

    print()
    process()