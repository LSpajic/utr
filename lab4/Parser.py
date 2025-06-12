# recursive descent parser for the grammar:
# S → aAB | bBA
# A → bC | a
# B → ccSbc | ϵ
# C → AA


def parse_S(input_string, index):
   pass
def parse_A(input_string, index):
   pass
def parse_B(input_string, index):
   pass
def parse_C(input_string, index):
   pass
def parse(input_string):
   index = 0
   index = parse_S(input_string, index)
   if index == len(input_string) :
      return True
   else:
      return False

def main():
   input_string = input()
   input_string += '$'  
   parsed = parse(input_string)
   if parsed:
      print("DA")
   else:
      print("NE")



if __name__ == "__main__":
   main()