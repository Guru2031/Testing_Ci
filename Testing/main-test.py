# Import the Add function, and assert that it works correctly.
import os

from main import Add
os.chdir(r'D:\PASCAL_INTERNAL\Sep20CI\Testing_Ci\Testing')
file = open('file.main-test')

def TestAdd():
        assert Add(2, 3) == 5
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()