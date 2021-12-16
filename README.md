# Stress Testing using Python

[What is stress testing ?](https://ali-ibrahim137.github.io/competitive/programming/2020/08/23/Stress-Testing.html)

### Preview 👀
![preview](preview.png)

### Prequirements
- [Python](https://www.python.org/)
- [Colorama](https://pypi.org/project/colorama/) and [Subprocess](https://docs.python.org/3/library/subprocess.html) python package
- Compiler for your language (C, C++, Java or Python)

### How to use ? 🤔
- Create files inside `Files` according to your language and add them in `hack.py`
```
no_users = 2
files = [ # first file expected output
    './Files/correct.cpp',
    './Files/wrong1.cpp',
]
```
- Generate testcase in `testcase.cpp` file
- Update `./Files/correct.cpp` file
- Update `./Files/wrong1.cpp` file
- Modify `hack.py` file according to number of users and files
- Run `python hack.py`
- After getting wrong answer chekout `wa.txt` (contains input, actual output and correct output) file and `in.txt` (current input) file

### Bye
- Testcase generator is written in `c++`, you can also use other language but make sure to modify `hack.py` accordingly.
- Give a star⭐️ & Follow ;)
