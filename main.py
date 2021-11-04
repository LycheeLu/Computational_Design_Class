# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ != '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def results_too_big(result):
    print(f'{result} is too big')

def results_too_small(result):
    print(f'{result} is too small')

def positive_results(result):
    print(f'{result} is appropriate')

result = 15
#this is just a test
if result > 10:
    results_too_big(result)
elif result == 10:
    positive_results(result)
else: results_too_small(result)

