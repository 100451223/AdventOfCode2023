class Puzzle003:
    def __init__(self):
        self.part1_description = open("descriptions/day3/description_part1", "r").read()
        self.part2_description = open("descriptions/day3/description_part2", "r").read()
        self.part1_path = "data/day3/input_part1"
        self.part2_path = "data/day3/input_part2"

    def _parse_input(self, path):
        lines = None
        with open(path) as f:
            lines = f.read().splitlines()
        return lines

    def part1(self):
        schematic = self._parse_input(self.part1_path)

        rows = len(schematic)
        cols = len(schematic[0])

        parts = []
        for i in range(rows):
            current_num = ""
            is_part = False
            
            for j in range(cols):
                current_character = schematic[i][j]
                if current_character.isdigit():
                    # Accumulate digits until a dot or a symbol is found
                    current_num += current_character

                    # Check surrounding items (only if we don't still know wether it is a part or not)
                    if not is_part:
                        for n in range(i-1, (i+1)+1):
                            for m in range(j-1, (j+1)+1):
                                if n>=0 and n<rows and m>=0 and m<cols and not (n==i and m==j):
                                    if not schematic[n][m].isdigit() and not schematic[n][m] == ".":
                                        # is part because there is a number
                                        is_part = True
                else: 
                    # A non-digit character is found
                    if is_part:
                        parts.append(int(current_num))
                        is_part = False
                    current_num = ""
                
                if (not current_character.isdigit() or j==cols-1) and is_part:
                    # The schematic line ends with a number
                    parts.append(int(current_num))
                    current_num = ""
                    is_part = False

        result = sum(parts)
        print(f"Part 1 result: {result}")
        return result
    

    def part2(self):
        schematic = self._parse_input(self.part2_path)
        
        rows = len(schematic)
        cols = len(schematic[0])

        gear_systems = {}
        for i in range(rows):
            current_num = ""
            current_gear = ""
            is_part = False
            
            for j in range(cols):
                current_character = schematic[i][j]
                if current_character.isdigit():
                    # Accumulate digits until a dot or a symbol is found
                    current_num += current_character

                    # Check surrounding items (only if we don't still know wether it is a part of a gear system or not)
                    if not is_part:
                        for n in range(i-1, (i+1)+1):
                            for m in range(j-1, (j+1)+1):
                                if n>=0 and n<rows and m>=0 and m<cols and not (n==i and m==j):
                                    if schematic[n][m] == "*":
                                        # is part of a gear system
                                        is_part = True
                                        current_gear = f"gear_{n}_{m}"
                else: 
                    # A non-digit character is found
                    if is_part:
                        if not current_gear in gear_systems:
                            gear_systems[current_gear] = [int(current_num)]
                        else:
                            gear_systems[current_gear].append(int(current_num))
                        is_part = False
                    current_num = ""
                    current_gear = ""
                
                if (not current_character.isdigit() or j==cols-1) and is_part:
                    # The schematic line ends with a number
                    if not current_gear in gear_systems:
                        gear_systems[current_gear] = [int(current_num)]
                    else:
                        gear_systems[current_gear].append(int(current_num))
                    is_part = False
                    current_num = ""
                    current_gear = ""

        result = 0
        for gear in gear_systems.keys():
            # Add up only the gear systems of length 2
            if len(gear_systems[gear]) == 2:
                result += gear_systems[gear][0]*gear_systems[gear][1]
        
        print(f"Part 2 result: {result}")
        return result

                                            
                    
puzzle003 = Puzzle003()
puzzle003.part1()
puzzle003.part2()
