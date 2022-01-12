import subprocess
from color_print import cprint

# Compile cpp, c, java file
def compile(file_path):

    lang = file_path.split(".")[-1]
    file = ".".join(file_path.split(".")[:-1])
    
    if(lang == "cpp" or lang == "c"):
        cmd = "g++ -std=c++17 -DONLINE_JUDGE \"{}\" -o \"{}.exe\"".format(file_path, file)
    elif(lang == "java"):
        cmd = "javac \"{}\"".format(file_path)
    else:
        return -1
    
    # print(cmd)
    print('\nCompiling ', end = '')
    cprint(file_path, clr = "purple")

    subprocess.run(cmd, check = True, shell = True)
    print('Compilation done')

# Run file and return output
def run(file_path, std_input = None):

    lang = file_path.split(".")[-1]
    file = ".".join(file_path.split(".")[:-1])

    if(lang == "cpp" or lang == "c"):
        cmd = "\"{}.exe\"".format(file)
    elif(lang == "java"):
        cmd = "java Main"
    elif(lang == "py"):
        cmd = "python \"{}\"".format(file_path)
    else:
        return -1
        
    # print(cmd)
    return subprocess.run(cmd, input = std_input, capture_output = True, shell = True, text = True, check = True)