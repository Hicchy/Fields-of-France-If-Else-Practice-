print('''                                                                                                  
                                                     _..----.._                                   
                                                    ]_.--._____[                                  
                                                  ___|'--'__..|--._                               
                              __               """    ;            :                              
                            ()_ """"---...__.'""!":  /    ___       :                             
                               """---...__\]..__] | /    [ 0 ]      :                             
                                          """!--./ /      """        :                            
                                   __  ...._____;""'.__________..--..:_                           
                                  /  !"''''''!''''''''''|''''/' ' ' ' \"--..__  __..              
                                 /  /.--.    |          |  .'          \' ' '.""--.{'.            
             _...__            >=7 //.-.:    |          |.'             \ ._.__  ' '""'.          
          .-' /    """"----..../ "">==7-.....:______    |                \| |  "";.;-"> \         
          """";           __.."   .--"/"""""----...."""""----.....H_______\_!....'----""""]       
        _..---|._ __..--""       _!.-=_.            """""""""""""""                   ;"""        
       /   .-";-.'--...___     ." .-""; ';""-""-...^..__...-v.^___,  ,__v.__..--^"--""-v.^v,      
      ;   ;   |'.         """-/ ./;  ;   ;\P.        ;   ;        """"____;  ;.--""""// '""<,     
      ;   ;   | 1            ;  ;  '.: .'  ;<   ___.-'._.'------""""""____'..'.--""";;'  o ';     
      '.   \__:/__           ;  ;--""()_   ;'  /___ .-" ____---""""""" __.._ __._   '>.,  ,/;     
        \   \    /"""<--...__;  '_.-'/; ""; ;.'.'  "-..'    "-.      /"/    `__. '.   "---";      
         '.  'v ; ;     ;;    \  \ .'  \ ; ////    _.-" "-._   ;    : ;   .-'__ '. ;   .^".'      
           '.  '; '.   .'/     '. `-.__.' /;;;   .o__.---.__o. ;    : ;   '"";;""' ;v^" .^        
             '-. '-.___.'<__v.^,v'.  '-.-' ;|:   '    :      ` ;v^v^'.'.    .;'.__/_..-'          
                '-...__.___...---""'-.   '-'.;\     'WW\     .'_____..>."^"-""""""""    fsc       
                                      '--..__ '"._..'  '"-;;"""                                   
                                             """---'""""""                                        
                                                                                                  ''')
print("Welcome to Arras.")
print("Your mission is to survive. \n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

q1 = input("""
You are the driver of an R35 of a French Armoured Platoon. The Battle of Arras is upon you. 
In the fields before you German armour can be seen. 
Your tank commander orders you to move forward. While going forward you see an friendly soldier wounded in front of you. Do you 'stop' or do you 'drive'? 
""")
q2 = input("""
You stop your tank and turn slightly to avoid running over the soldier. While doing so you've exposed your weak side armour. 
A German shell hits and penetrates the turret where the commander is. Your ears ring loudly and you look back to see your commander. 
His lifeless body sits on the seat. Realising the situation you're in, you either 'reverse' the tank or you 'bail' out. \n
""" )
q3 = input("""
Before the German tank can pump another round into your tank, you quickly point your front armour to it. 
It fires and the shell bounces. Having no way to fight back, you start reversing slowly. 
While reversing you see a massive bomb crater. It can provide cover for you for now but looks hard to get out of. 
You either decide to 'use' or 'ignore'.
""")

q1Lower = q1.lower()
q2Lower = q2.lower()
q3Lower = q3.lower()

if q1Lower == "drive":
  print ("You have ran over a fellow soldier, game over." )
elif q1Lower == "stop":
  print (q2)
  if q2Lower == "bail":
    print ("""
    You open the hatch and start getting out. Before you can lift yourself off the tank completely, advancing German infantry draw their guns on you. You surrender, game over. """)
  elif q2Lower == "reverse":
    print (q3Lower)
    if q3Lower == "use":
      print ("""
       You reverse into the crater, collecting yourself. You decide it's time to move after artillery shells start falling around you.
       You back up towards the edge of the crater but the tracks lose grip and you slide back into the middle.
       Shortly after, German infatry surrounds you and you surrender. Game over.
       """)
    elif q3Lower == "ignore":
      print ("""
      You decide the crater is a dead end and maneuver around it. 
      Despite the chaos of the battle, your sanity and your tank's frontal armour holds.
      You keep reversing until your tank slides down a hill, sheltering you from incoming fire.
      At which point you bail out and run towards friendly positions. You survived, for now.
      """)
