import re

class Puzzle001:
    def __init__(self):
        self.part1_description = open("descriptions/day1/description_part1", "r").read()
        self.part2_description = open("descriptions/day1/description_part2", "r").read()
        self.part1_path = "data/day1/input_part1"
        self.part2_path = "data/day1/input_part2"

    def _get_records(self, path):
        # Returns an array with calibration records

        records = None
        with open(path, "r") as input:
            records = input.readlines()
        return records

    def _get_calibration_value(self, record: list):
        # Given an array of char characters, return the first and last numbers in it concatenated

        if len(record) == 0: 
            return -1

        first, last = None, None
        for i in range(len(record)):

            if not first and record[i].isnumeric():
                first = record[i]
            if not last and record[(len(record)-1)-i].isnumeric():
                last = record[(len(record)-1)-i]
            
            # Found the first and last numbers
            if (first and last):
                return int(first+last)
    
    def _get_calibration_value_numerals(self, input: str):
        
        numbers_ordinals = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }

        first, first_index = None, 99999 
        last, last_index = None, 0
        for num in numbers_ordinals.keys():
            indexes = [i.start() for i in re.finditer(num, input)]
            if len(indexes) > 0:
                if min(indexes) <= first_index:
                    first = numbers_ordinals[num]
                    first_index = min(indexes)
                if max(indexes) >= last_index:
                    last = numbers_ordinals[num]
                    last_index = max(indexes)

        if first and last:
            return int(first+last)
        
        print("Invalid sequence")
        return -1
    
    def _get_calibration_num_sum(self, numerals: bool):
        
        result = 0
        records = self._get_records(self.part1_path)

        for record in records:

            calibration_number = self._get_calibration_value([c for c in record]) if not numerals else self._get_calibration_value_numerals(record)
            if calibration_number <0:
                print(f"Invalid input:\n{record}")
                return -1 
            result += calibration_number

        return result

    
    def part1(self):
        # Given an array of char characters, return the first and last numbers in it concatenated.
        calibration_sum = self._get_calibration_num_sum(numerals=False)
        print(f"Part 1 result: {calibration_sum}")
        return calibration_sum
        

    def part2(self):
        # Given an array of char characters, return the first and last numbers in it concatenated.
        # There might be ordinal numbers
        calibration_sum = self._get_calibration_num_sum(numerals=True)
        print(f"Part 2 result: {calibration_sum}")
        return calibration_sum

        
        

puzzle001 = Puzzle001()
puzzle001.part1()
puzzle001.part2()