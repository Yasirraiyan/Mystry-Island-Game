questions = 
[ 
    "What is the capital of France?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the largest planet in our solar system?", 
    "What is the chemical symbol for water?", 
    "Who painted the Mona Lisa?" 
]
answers 
=
[
    "Paris", "William Shakespeare", "Jupiter", "H2O", "Leonardo da Vinci"
]
map_array 
=
[
    "Jungle", "Cave", "River", "Old Home", "Jungle", "River", "Cave", "River", "Jungle"
    ]
characters = 
[ 
    { "name": "Hero", "powers":
        ["Strength", "Agility", "Flight"], 
        "things": ["Sword", "Shield", "Potion"]
        }, 
        { 
            "name": "Wizard", "powers": 
                [
                    "Magic", "Teleportation", "Invisibility"
                    ],
                    "things": 
                        ["Wand", "Spell Book", "Crystal Ball"] 
            
        },
        { 
            "name": "Rogue", "powers":
                ["Stealth", "Speed", "Lockpicking"],
                "things": ["Dagger", "Lockpick", "Cloak"] 
            
        },
        { 
            "name": "Healer", "powers":
                ["Healing", "Revival", "Protection"],
                "things": 
                    [
                        "Healing Staff", "Herbs", "Amulet"
                        ] 
        } 
        ]
        mission=5;
        quest=False;
        area=False;
        solve=False;
        chance=5;
        life=5;
        score=0;
        allsuccess=False;
        cross=False;
        power=False;
        thing=False;
        controlmechanism=False;
        clue=0;
        info=0;
        explain=False;
        competition=False;
        challange=False;
        lock=False;
        unlock=False;
        skill=0;
        items = ["Pocket", "Diagram", "Magnifying Glass", "Torch"]    
        equipment = ["Pocket", "Diagram", "Magnifying Glass", "Torch"]
      def controlmechanism1()  :
          while :
              life>0 and chance>0:
                  if not solve and
                      characters in characters and question in questions and answer in answer and equipment in equipment :
                          solve=True;
                          chance--;
                          life--;
                          score1=score+5;
                          quest=True
                          area=True
                          solve=True
                          skill1=skill+10;
                          mission--
                          
        def cross1(mission,quest,area,solve)   :
            if not mission and not quest and not area and not solve:
                print("Cross mission1 successfully.Go next step.")
                return (mission,quest,area,solve)
                 if life==0 or chance==0:
                else:
                    print("Not success.Fail")
        def controlmechanism2()  :
          while :
              life>0 and chance>0:
                  if not solve and
                      characters in characters and question in questions and answer in answer and equipment in equipment :
                          solve=True;
                          chance-=2;
                          life-=2;
                          score2=score+10;
                          quest=True
                          area=True
                          solve=True
                          skill2=skill+20;
                          mission--;
                          
        def cross2(mission,quest,area,solve)   :
            if not mission and not quest and not area and not solve:
                print("Cross mission2 successfully.Go next step.")
                return (mission,quest,area,solve)
                 if life==0 or chance==0:
                else:
                    print("Not success.Fail")
                    def controlmechanism1()  :
          while :
              life>0 and chance>0:
                  if not solve and
                      characters in characters and question in questions and answer in answer and equipment in equipment :
                          solve=True;
                          chance-=3;
                          life-=3;
                          score3=score+15;
                          cross=True
                          quest=True
                          area=True
                          solve=True
                          skill3=skill+30;
                          mission--
                          
        def cross3(mission,quest,area,solve)   :
            if not mission and not quest and not area and not solve:
                print("Cross mission3 successfully.Go next step.")
                return (mission,quest,area,solve)
               if life==0 or chance==0:
                    print("Not success.Fail")
                    def controlmechanism1()  :
          while :
              life>0 and chance>0:
                  if not solve and
                      characters in characters and question in questions and answer in answer and equipment in equipment :
                          solve=True;
                          chance--;
                          life--;
                          score4=score+20;
                          quest=True
                          area=True
                          solve=True
                          skill4=skill+40;
                          mission--
                          
        def cross4(mission,quest,area,solve)   :
            if not mission and not quest and not area and not solve:
                print("Cross mission3 successfully.Go next step.")
                return (mission,quest,area,solve)
                 if life==0 or chance==0:
                    print("Not success.Fail")
                    def controlmechanism1()  :
          while :
              life>0 and chance>0:
                  if not solve and
                      characters in characters and question in questions and answer in answer and equipment in equipment :
                          solve=True;
                          chance--;
                          life--;
                          score5=score+25;
                          quest=True
                          area=True
                          solve=True
                          skill5=skill+50;
                          mission--;
                def cross5(mission,quest,area,solve)   :
            if not mission and not quest and not area and not solve:
                print("Cross mission3 successfully.Go next step.")
                return (mission,quest,area,solve)
                 if life==0 or chance==0:
                    print("Not success.Fail")
                    def controlmechanism1()  :
          while :
              life>0 and chance>0:
                  if not solve and
                      characters in characters and question in questions and answer in answer and equipment in equipment :
                          solve=True;
                          chance--;
                          life--;
                          score5=score+25;
                          quest=True
                          area=True
                          solve=True
                          skill6=skill+60;
                          mission--

def mapcrossarea():
    if map in map_array:
        if map==area and not cross:
            print("Cross the area successfully.")
            else:
                print("Not success!")
def mapcrossforest():
    if map in map_array:
        if map==forest and not cross:
            print("Cross the forest successfully.")
            else:
                print("Not success!")
def mapcrosscave():
    if map in map_array:
        if map==cave and not cross:
            print("Cross the cave successfully.")
            else:
                print("Not success!")
def mapcrossriver():
    if map in map_array:
        if map==river and not cross:
            print("Cross the river successfully.")
            else:
                print("Not success!")
def mapcrossoldhouse():
    if map in map_array:
        if map==cave and not cross:
            print("Cross the old house successfully.")
            else:
                print("Not success!")
def character(character):
    if character in character and not power and not thing:
        print("Solve")
        else:
            print("Not solve")
def mission():
    while mission>0:
        if life>0 and not area and not quest and not cross:
            print("Welcome new area")
            score+=5;
        if life==0 
        print("Dead");
        else:
            print("Pass mission successfully!");
       def win():
           finalscore=score1+score2+score3+score4+score5;
           if not allsuccess:
               print(f"You win! Your final score is:{finalscore}")
def checkitem():
    if item in item:
    print("Valid item")
    else:
        print("Invalid item!")
def checkequipment():
    if equipment in equipment:
    print("Valid equipment!")
    else:
        print("Invalid equipment!")
    def solvepuzzle():
        if not controlmechanism:
            print("Puzzle solve successfully!")
        else:
            print("Fail!")
def explain():
    while life>0:
        if not explain:
            clue++;
            info++;
            life--;
    if life==0 or clue==0 or info==0:
        print("Can not explain")
    def nextlevel():
        if not compitition and not challange:
            lock=True;
            unlock=False;
            print("Next level unlocked")
        else:
            print("Can't unlock next level")
    def end():
        if life==0 or chance==0:
            print("Game end!")
    def finalscore():
        Finalscore=score1+score2+score3+score4+score5;
        return Finalscore;
        print(f"Your final score is:{Finalscore}");
        
          def finalskill():
        Finalskill=skill1+skill2+skill3+skill4+skill5;
def final_skill(skill1, skill2, skill3, skill4, skill5):
    # Calculate Final Skill Score
    final_score = skill1 + skill2 + skill3 + skill4 + skill5
    
    # Categorize Final Score
    if final_score >= 90:
        category = "Excellent"
    elif final_score >= 70:
        category = "Very Good"
    elif final_score >= 50:
        category = "Good"
    elif final_score >= 30:
        category = "Average"
    else:
        category = "Needs Improvement"
    
    print(f"Your final skill score is: {final_score}")
    print(f"Your skill category is: {category}")
    
    return final_score, category

# Example usage
skill1, skill2, skill3, skill4, skill5 = 20, 15, 10, 8, 12
final_score, category = final_skill(skill1, skill2, skill3, skill4, skill5)

        return Finalscore;
        print(f"Your final skill is:{Finalskill}");
        
