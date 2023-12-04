class Puzzle004:
    def __init__(self):
        # self.part1_description = open("descriptions/day4/description_part1", "r").read()
        # self.part2_description = open("descriptions/day4/description_part2", "r").read()
        self.part1_path = "data/day4/input_part1"
        self.part2_path = "data/day4/input_part2"
        
        self.scratchcards_stock = {}

    def _get_scratchcards(self, path:str):
        lines = None
        with open(path) as f:
            lines = f.read().splitlines()
        return lines
    
    def _init_scratchcards_dict(self, n: int):
        scratchcards = {}
        for i in range(1,n+1):
            scratchcards[f"{i}"] = 1
        return scratchcards

    def _check_scratchcard(self, scratchcard: str):
        scratchcard = scratchcard.split(": ")[1]
        winning_numbers, my_numbers = scratchcard.split(" | ")

        winning_numbers = set([i for i in winning_numbers.split(" ")])
        my_numbers = [i for i in my_numbers.split(" ") if i!=""]

        matches = 0
        for num in my_numbers:
            if num in winning_numbers:
                matches += 1

        points = 2**(matches-1) if matches>0 else 0

        return points

    def part1(self): 
        scratchcards = self._get_scratchcards(self.part1_path)

        total_points = 0
        for scratchcard in scratchcards:
            total_points += self._check_scratchcard(scratchcard)
        
        print(f"Part 1 result: {total_points}")


    def _update_scratchcard_copies(self, scratchcard: str):
        card_id, scratchcard = scratchcard.split(": ")
        card_id = card_id.split(" ")
        card_id = [i for i in card_id if i!=""][1]
        winning_numbers, my_numbers = scratchcard.split(" | ")

        factor = self.scratchcards_stock[f"{card_id}"]

        winning_numbers = set([i for i in winning_numbers.split(" ")])
        my_numbers = [i for i in my_numbers.split(" ") if i!=""]

        matches = 0
        for num in my_numbers:
            if num in winning_numbers:
                matches += 1

        for i in range(int(card_id)+1, (int(card_id)+matches)+1):
            self.scratchcards_stock[f"{i}"] += 1*factor

    
    def part2(self):
        scratchcards = self._get_scratchcards(self.part2_path)
        self.scratchcards_stock = self._init_scratchcards_dict(len(scratchcards))

        for scratchcard in scratchcards:
            self._update_scratchcard_copies(scratchcard)

        result = 0
        for key in self.scratchcards_stock.keys():
            result += self.scratchcards_stock[key]
        print(f"Part 2 result: {result}")

puzzle004 = Puzzle004()
puzzle004.part1()
puzzle004.part2()