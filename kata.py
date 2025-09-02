def parse_int(string):
    number_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40,
        "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000, "million": 1_000_000
    }
    


    parsed_string_list = string.replace("-", " ").replace(" and ", " ").split() # Returns a list.
    
    accumulator = 0
    total = 0
    
    print(parsed_string_list)

parse_int('eight hundred eighty-eight thousand eight hundred and eighty-eight')