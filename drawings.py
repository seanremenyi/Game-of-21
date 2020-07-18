import cards_and_deck

###Display the board, drawings for possible hand sizes with coressponding cards
###Display total
def cards_display_in_game(uh, ch, users_display, dealers_display = "yes"):
    dealers_total_is = dealers_display
    users_total_is = users_display
    if dealers_display == "yes":
###Dealers hidden card during play
        hd="  "
        dealers_total_is = f"{cards_and_deck.value(ch[1])} and ???"
###Dealers cards shown after play    
    else:
        hd=ch[0]
        total= 0
        count =0
        while count < len(ch):
            total += cards_and_deck.value(ch[count])
            count+=1
        dealers_total_is = total

    if len(uh)==2 and len(ch) == 2:
        print(f"""
 ____     ____
|    |   |    |
| {hd} |   | {ch[1]} |   
|____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____
|    |   |    |
| {uh[0]} |   | {uh[1]} |   
|____|   |____|                    """)
    elif len(uh)==3 and len(ch) == 2:
        print(f"""
 ____     ____
|    |   |    |
| {hd} |   | {ch[1]} |   
|____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____
|    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   
|____|   |____|   |____|                    """)
    elif len(uh)==4 and len(ch) == 2:
        print(f"""
 ____     ____
|    |   |    |
| {hd} |   | {ch[1]} |   
|____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   
|____|   |____|   |____|   |____|                 """)
    elif len(uh)==5 and len(ch) == 2:
        print(f"""
 ____     ____
|    |   |    |
| {hd} |   | {ch[1]} |   
|____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   
|____|   |____|   |____|   |____|   |____|                 """)
    elif len(uh)==6 and len(ch) == 2:
        print(f"""
 ____     ____
|    |   |    |
| {hd} |   | {ch[1]} |   
|____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   | {uh[5]} |   
|____|   |____|   |____|   |____|   |____|   |____|              """)

    elif len(uh)==7 and len(ch) == 2:
        print(f"""
 ____     ____
|    |   |    |
| {hd} |   | {ch[1]} |   
|____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   | {uh[5]} |   | {uh[6]} |   
|____|   |____|   |____|   |____|   |____|   |____|   |____|              """)

################################################
    elif len(uh)==2 and len(ch) == 3:
        print(f"""
 ____     ____     ____
|    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   
|____|   |____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____
|    |   |    |
| {uh[0]} |   | {uh[1]} |   
|____|   |____|                    """)
    elif len(uh)==3 and len(ch) == 3:
        print(f"""
 ____     ____     ____
|    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   
|____|   |____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____
|    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   
|____|   |____|   |____|                    """)
    elif len(uh)==4 and len(ch) == 3:
        print(f"""
 ____     ____     ____
|    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   
|____|   |____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   
|____|   |____|   |____|   |____|                 """)
    elif len(uh)==5 and len(ch) == 3:
        print(f"""
 ____     ____     ____
|    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   
|____|   |____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   
|____|   |____|   |____|   |____|   |____|                 """)
    elif len(uh)==6 and len(ch) == 3:
        print(f"""
 ____     ____     ____
|    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   
|____|   |____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   | {uh[5]} |   
|____|   |____|   |____|   |____|   |____|   |____|              """)

    elif len(uh)==7 and len(ch) == 3:
        print(f"""
 ____     ____     ____
|    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   
|____|   |____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   | {uh[5]} |   | {uh[6]} |   
|____|   |____|   |____|   |____|   |____|   |____|   |____|              """)
################################################
    elif len(uh)==2 and len(ch) == 4:
        print(f"""
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   
|____|   |____|   |____|   |____|       

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____
|    |   |    |
| {uh[0]} |   | {uh[1]} |   
|____|   |____|                    """)
    elif len(uh)==3 and len(ch) == 4:
        print(f"""
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   
|____|   |____|   |____|   |____|             

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____
|    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   
|____|   |____|   |____|                    """)
    elif len(uh)==4 and len(ch) == 4:
        print(f"""
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   
|____|   |____|   |____|   |____|             

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   
|____|   |____|   |____|   |____|                 """)
    elif len(uh)==5 and len(ch) == 4:
        print(f"""
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   
|____|   |____|   |____|   |____|            

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   
|____|   |____|   |____|   |____|   |____|                 """)
    elif len(uh)==6 and len(ch) == 4:
        print(f"""
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   
|____|   |____|   |____|   |____|            

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   | {uh[5]} |   
|____|   |____|   |____|   |____|   |____|   |____|              """)

    elif len(uh)==7 and len(ch) == 4:
        print(f"""
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   
|____|   |____|   |____|   |____|             

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   | {uh[5]} |   | {uh[6]} |   
|____|   |____|   |____|   |____|   |____|   |____|   |____|              """)

################################################
    elif len(uh)==2 and len(ch) == 5:
        print(f"""
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   
|____|   |____|   |____|   |____|   |____|    

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____
|    |   |    |
| {uh[0]} |   | {uh[1]} |   
|____|   |____|                    """)
    elif len(uh)==3 and len(ch) == 5:
        print(f"""
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   
|____|   |____|   |____|   |____|   |____|            

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____
|    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   
|____|   |____|   |____|                    """)
    elif len(uh)==4 and len(ch) == 5:
        print(f"""
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   
|____|   |____|   |____|   |____|   |____|           

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   
|____|   |____|   |____|   |____|                 """)
    elif len(uh)==5 and len(ch) == 5:
        print(f"""
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   
|____|   |____|   |____|   |____|   |____|           

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   
|____|   |____|   |____|   |____|   |____|                 """)
    elif len(uh)==6 and len(ch) == 5:
        print(f"""
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   
|____|   |____|   |____|   |____|   |____|         

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   | {uh[5]} |   
|____|   |____|   |____|   |____|   |____|   |____|              """)

    elif len(uh)==7 and len(ch) == 5:
        print(f"""
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   
|____|   |____|   |____|   |____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   | {uh[5]} |   | {uh[6]} |   
|____|   |____|   |____|   |____|   |____|   |____|   |____|              """)

################################################
    elif len(uh)==2 and len(ch) == 6:
        print(f"""
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   | {ch[5]} |   
|____|   |____|   |____|   |____|   |____|   |____| 

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____
|    |   |    |
| {uh[0]} |   | {uh[1]} |   
|____|   |____|                    """)
    elif len(uh)==3 and len(ch) == 6:
        print(f"""
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   | {ch[5]} |   
|____|   |____|   |____|   |____|   |____|   |____|            

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____
|    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   
|____|   |____|   |____|                    """)
    elif len(uh)==4 and len(ch) == 6:
        print(f"""
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   | {ch[5]} |   
|____|   |____|   |____|   |____|   |____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____
|    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   
|____|   |____|   |____|   |____|                 """)
    elif len(uh)==5 and len(ch) == 6:
        print(f"""
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   | {ch[5]} |   
|____|   |____|   |____|   |____|   |____|   |____|         

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   
|____|   |____|   |____|   |____|   |____|                 """)
    elif len(uh)==6 and len(ch) == 6:
        print(f"""
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   | {ch[5]} |   
|____|   |____|   |____|   |____|   |____|   |____|          

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   | {uh[5]} |   
|____|   |____|   |____|   |____|   |____|   |____|              """)

    elif len(uh)==7 and len(ch) == 6:
        print(f"""
 ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |
| {hd} |   | {ch[1]} |   | {ch[2]} |   | {ch[3]} |   | {ch[4]} |   | {ch[5]} |   
|____|   |____|   |____|   |____|   |____|   |____|         

Dealers Hand:                Dealers Total = {dealers_total_is}

Your Hand:                   Your Total = {users_total_is}
 ____     ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |   |    |
| {uh[0]} |   | {uh[1]} |   | {uh[2]} |   | {uh[3]} |   | {uh[4]} |   | {uh[5]} |   | {uh[6]} |   
|____|   |____|   |____|   |____|   |____|   |____|   |____|              """)
    return ""


