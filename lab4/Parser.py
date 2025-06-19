##################################################
# Parser rekurzivnog spusta za gramatiku:        #
# S → aAB   | bBA                                #
# A → bC    | a                                  #
# B → ccSbc | ϵ                                  #
# C → AA                                         #
##################################################

simbol = ''
input_string = ''
index = 0
result = ''
false_result = ''

def next_symbol():
    global simbol
    if index < len(input_string):
        simbol = input_string[index]
    else:
        simbol = '$'

def parse_S():
    global index, result
    result += 'S'
    original_index = index
    original_result = result

    if index < len(input_string) and input_string[index] == 'a':
        index += 1
        next_symbol()
        if parse_A() and parse_B():
            return True
        index = original_index
        result = original_result
        next_symbol()

    if index < len(input_string) and input_string[index] == 'b':
        index += 1
        next_symbol()
        if parse_B() and parse_A():
            return True
        index = original_index
        result = original_result
        next_symbol()

    return False

def parse_A():
    global index, result
    result += 'A'
    original_index = index
    original_result = result

    if index < len(input_string) and input_string[index] == 'b':
        index += 1
        next_symbol()
        if parse_C():
            return True
        index = original_index
        result = original_result
        next_symbol()

    if index < len(input_string) and input_string[index] == 'a':
        index += 1
        next_symbol()
        return True

    return False

def parse_B():
    global index, result
    result += 'B'
    original_index = index
    original_result = result

    if (
        index + 1 < len(input_string)
        and input_string[index] == 'c'
        and input_string[index + 1] == 'c'
    ):
        index += 2
        next_symbol()
        if parse_S():
            if index < len(input_string) and input_string[index] == 'b':
                index += 1
                next_symbol()
                if index < len(input_string) and input_string[index] == 'c':
                    index += 1
                    next_symbol()
                    return True
        index = original_index
        next_symbol()

    return True

def parse_C():
    global index, result
    result += 'C'
    original_index = index
    original_result = result

    if parse_A() and parse_A():
        return True

    index = original_index
    next_symbol()
    return False

def parse():
    global index
    index = 0
    next_symbol()
    if parse_S() and simbol == '$':
        return True
    return False

def main():
    global input_string, result
    input_string = input().strip() + '$'
    result = ''
    if parse():
        print(result)
        print("DA")
    else:
        print(result)
        print("NE")

if __name__ == "__main__":
    main()
