from random import randrange
import subprocess as sp

class Rather:
    a = ""
    b = ""
    def __init__(self, a, b):
        self.a=a
        self.b=b

sp.call('cls',shell=True)
prompt = "Welcome to a game of Would You Rather! "
print (prompt)

rather = []
rather.append(Rather("have a velcro beard", "have bamboo hair"))
rather.append(Rather("only exist every other day for the rest of your life", "only live 20 more years"))
rather.append(Rather("win $100,000 but have to spend it in five minutes", "win $50,000 and spend it whenever you want"))
rather.append(Rather("be a master of origami", "be a master of feng shui"))
rather.append(Rather("be unable to tell the difference between puppies and sandpaper", "be unable to tell the difference between lamps and bananas"))
rather.append(Rather("speak only in song", "move only by breakdancing"))
rather.append(Rather("have your office chair replaced with a unicycle", "have your office chair be replaced with a block of ice"))
rather.append(Rather("get caught in an avalanche of croutons", "get caught in an avalanche of koosh balls"))
rather.append(Rather("have whitehead zits that turn into pearls over months", "have caviar eye crust"))
rather.append(Rather("have a unibrow", "have a uni-nostril"))
rather.append(Rather("name your kids after famous robots", "name your kids after Starbucks cup sizes and coffee terms"))
rather.append(Rather("look 3/4 your age", "look 4/5 your weight"))
rather.append(Rather("be able to summon eagles", "be able to summon back-up singers"))
rather.append(Rather("share a bed with a porcupine", "share a bed with a skunk"))
rather.append(Rather("have to always drive half the speed limit", "have to always drive twice the speed limit"))
rather.append(Rather("eat a bar of soap", "swallow the hair wad found collected in a public shower drain"))
rather.append(Rather("get a huge back tattoo of the periodic table", "get a huge back tattoo of your parents"))
rather.append(Rather("take a road trip with Ben Franklin and Elvis", "take a road trip with Napoleon and Lil Wayne"))
rather.append(Rather("lose 5 IQ points if you also lost 20 pounds", "stay the same IQ and weight"))
rather.append(Rather("eat a maggot encrusted sushi roll", "eat bloodworms Bolognese"))
rather.append(Rather("have an automatic Instagram pic of you posted every 10 seconds", "have an automatic facebook status post every 10 seconds"))
rather.append(Rather("have a trained ferret that fetches your personals", "have a trained caterpillar that crawls to any spot you need itched"))
rather.append(Rather("have your belly button double as an electrical outlet","have your belly button double as a gumball dispenser"))
rather.append(Rather("have the neck of a 90 year old", "have the feet of a 90 year old"))
rather.append(Rather("have your mouth always close when you throw up", "have your nose and mouth seal up when you sneeze"))
rather.append(Rather("always feel like you are wealking against a 40mph wind", "feel like you are walking on ice"))

answers = []
index = 0
while len(rather) > 0:
    question_number = randrange(len(rather))
    print ("\nWould you rather \n  (a)" + rather[question_number].a + " or \n  (b)" + rather[question_number].b + "\n")
    answer = input("choose a or b: ")
    while answer != "a" and answer != "b":
        answer = input("answer " + answer + " is not valid.  Please answer a or b: ")
    if answer == "a":
        answers.append(rather[question_number].a + " than " + rather[question_number].b)
    else:
        answers.append(rather[question_number].b + " than " + rather[question_number].a)
    rather.remove(rather[question_number])

print("You would rather: ")
for answer in answers:
    print(answer)

