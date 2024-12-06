def explain():
    while life>0:
        if not explain:
            clue++;
            info++;
            life--;
    if life==0 or clue==0 or info==0:
        print("Can not explain")
