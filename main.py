from coincidence2 import Schedule, CSVFileInput, TXTFileInput
import sys


def main():

    data = TXTFileInput()

    data.process_input(sys.argv[1])

    results = Schedule.get_coincidences()

    for i in results:
        print(i, results[i])


if __name__ == '__main__':
    main()