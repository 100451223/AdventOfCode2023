import re

class Puzzle002:
    def __init__(self, red: int, blue: int, green: int):
        self.part1_description = open("descriptions/day2/description_part1", "r").read()
        self.part2_description = open("descriptions/day2/description_part2", "r").read()
        self.part1_path = "data/day2/input_part1"
        self.part2_path = "data/day2/input_part2"

        self.colors_amount = {
            "red": red,
            "blue": blue,
            "green": green
        }

    def _get_games(self, path):
        # Returns an array with calibration records

        games = None
        with open(path, "r") as input:
            games = input.read().splitlines() 
        return games

    def _read_game(self, game: str):

        game = game.split(": ")
        gameID = game[0].split(" ")[1]
        showings = game[1].split("; ")

        for showing in showings:
            colors = {"red": 0, "blue": 0, "green": 0}
            showing = showing.split(", ")
            for evidence in showing:
                evidence = evidence.split(" ")
                colors[evidence[1]] = int(evidence[0])
            
            if colors["red"]>self.colors_amount["red"] or colors["blue"]>self.colors_amount["blue"] or colors["green"]>self.colors_amount["green"]:
                return -1
            
        # print(f"Game {gameID} is valid")
        return int(gameID)
    
    def part1(self):

        result = 0
        games = self._get_games(self.part1_path)
        for game in games:
            game_result = self._read_game(game)
            if game_result<0:
                continue
            result += game_result
        print(f"Part 1 result: {result}")
        return result
    
    def _get_game_power(self, game: str):
        
        game = game.split(": ")
        gameID = game[0].split(" ")[1]
        showings = game[1].split("; ")

        colors = {"red": 0, "blue": 0, "green": 0}
        for showing in showings:
            showing = showing.split(", ")
            for evidence in showing:
                evidence = evidence.split(" ")
                colors[evidence[1]] = max(colors[evidence[1]], int(evidence[0]))
            
        return colors["red"]*colors["blue"]*colors["green"]
            
    def part2(self):
        result = 0
        games = self._get_games(self.part2_path)
        for game in games:
            result += self._get_game_power(game)
        
        print(f"Part 2 result: {result}")
        return result

    
puzzle002 = Puzzle002(red=12, blue=14, green=13)
puzzle002.part1()
puzzle002.part2()