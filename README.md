# Stress Testing using Python

[What is stress testing ?](https://ali-ibrahim137.github.io/competitive/programming/2020/08/23/Stress-Testing.html)

### Preview 👀
![preview](preview.png)

### Prequirements
- [Python](https://www.python.org/)
- [Colorama](https://pypi.org/project/colorama/) and [Subprocess](https://docs.python.org/3/library/subprocess.html) python package
- compiler for your language (C, C++, Java or Python)

### How to use ? 🤔
- create files inside `Files` according to your language and add them in `hack.py`
```
no_users = 2
files = [ # first file expected output
    './Files/correct.cpp',
    './Files/wrong1.cpp',
]
```
- generate testcase in `testcase.cpp` file
- update correct file in Files folder
- update wrong file in Files folder
- modify `hack.py` file according to number of user and files
- run `python hack.py`
- after getting wrong answer chekout `wa.txt` file and `in.txt` file

### Bye
- testcase generator is written in c++, you can also use other language but make sure to modify `hack.py` accordingly.
```c++
if(enjoy 🙃) {
    giveStar(⭐️);
    Follow();
}
```
