birds = {"red-tailed hawk": ""
         ,"killdeer": "",
         "snowy plover": "",
         "western gull": ""}
def count_birds(birds):
 bird_count = {}
 for bird in birds:
     if bird_count:
         bird_count[bird] += 1
     elif:#why invalid syntax error
          bird_count[x] = exit
     else:
         bird_count[bird] = 1
return bird_count
def display_bird_count(bird_count):
    birds =list(bird_count.keys())
    for bird in birds:
        count = bird_count[bird]
        print(bird,  ,count)

def main():
    print("Bird Counter program")
    print("Enter 'x' to exit")

   bird_count = count_birds(birds)
   display_bird_count(bird_count)

if__name__ == "__main__:
    main()