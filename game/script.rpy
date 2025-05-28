label start:
    $ renpy.block_rollback()
    scene bg roomA

    show screen inventory_button
    # show screen debug_info
    show screen hand_screen
    # show screen debug_inventory

    "이곳은 어디지?"

    "여기서 탈출해야만 해!"

    window hide
    show screen key
    show screen keyhole_button
    
    jump room1
    # $ renpy.pause(hard=True)

label room1:
    scene bg roomA

    hide screen branch
    hide screen wood_key
    hide screen front_to_1
    hide screen back_to_2
    show screen back_to_2
    show screen inventory_button
    hide screen front_to_6
    
    if room1_fire_key_visible != True:
        hide screen fire_key
    else:
        show screen fire_key

    if room1_branch_visible != True:
        hide screen branch_fire
    else:
        show screen branch_fire

    $ current_room = 1
    if current_item_in_hand == "branch_fire":
        if branch_move != 0:
            hide screen fire_key
            python:
                branch_move_count()
        else:
            python:
                branch_move_count()
            hide screen fire_key
            "나무가 모두 타버렸다. 바스러져서 재가 되어버렸다."
            if room1_fire_key_visible != True:
                hide screen fire_key
            else:
                show screen fire_key
            python:
                remove_from_inventory(items["branch"])
                current_item_in_hand = "ash"
                item_counts["ash"] += 1


    if room1_fire_key_visible != True:
        hide screen fire_key
    else:
        show screen fire_key

    if items["default_key"] not in inventory and It[0] == 0 and It[11] == 0:
        show screen key
    else:
        hide screen key
    show screen keyhole_button

    $ renpy.pause(hard=True)



label door_room1:
    scene bg used_key_roomA

    hide screen key
    hide screen keyhole_button
    hide screen keyhole_button2
    hide screen back_to_2
    hide screen popup
    hide screen inventory_button

    $ current_room = 0

    window show
    if current_item_in_hand != "default_key":
        "열쇠를 넣으면 문이 열릴 것 같다"
        window hide
        jump room1
    else:
            menu use_key:
                "들고 있는 열쇠를 넣으면 문이 열릴 것 같다. 넣어볼까?"
                "넣어본다.":
                    window hide
                    jump open_room1
                "넣지 않는다.":
                    window hide
                    jump room1
                

label open_room1:
    scene bg used_key_roomA

    window show
    hide screen keyhole_button
    hide screen hand_screen

    show used_key at Position(xpos=780, ypos=555, xanchor='center', yanchor='center') with dissolve
    "열쇠가 들어갔다."

    "돌려보니 문이 열린다."

    $ room1_open = 1

    window hide
    jump room2

label room2:
    scene bg room2

    hide screen keyhole_button
    hide screen back_to_2
    hide screen front_to_2
    hide screen back_to_4
    hide screen room3_door
    hide screen wall_water
    hide screen glass_key
    hide screen key
    
    show screen inventory_button
    show screen hand_screen
    show screen keyhole_button2
    show screen front_to_1
    show screen back_to_3
    if room2_branch_visible != True:
        hide screen branch_fire
    else:
        show screen branch_fire

    
    $ current_room = 2
    if current_item_in_hand == "branch_fire":
        if branch_move != 0:
            hide screen fire_key
            python:
                branch_move_count()
            "나무가 불이 타고 있다. 머지 않아 다 타버릴 것 같다."
        else:
            python:
                branch_move_count()
            hide screen fire_key
            "나무가 모두 타버렸다. 바스러져서 재가 되어버렸다."
            if room2_fire_key_visible != True:
                hide screen fire_key
            else:
                show screen fire_key
            python:
                remove_from_inventory(items["branch"])
                current_item_in_hand = "ash"
                item_counts["ash"] += 1

    if current_item_in_hand != "branch_fire":
        if room1_branch_visible != True and room2_branch_visible != True and room3_branch_visible != True and room4_branch_visible != True and room5_branch_visible != True and room6_branch_visible != True and room7_branch_visible != True:
                if It[2] == 0 and It[7] == 0:
                    show screen branch
                elif It[8] == 1 and It[2] == 0:
                    show screen branch

    if It[1] == 0 and room2_open == 0:
        show screen wood_key

    if room2_fire_key_visible != True:
        hide screen fire_key
    else:
        show screen fire_key


    

    $ renpy.pause(hard=True)


label door_room2:
    scene bg room2_close

    hide screen wood_key
    hide screen keyhole_button
    hide screen keyhole_button2
    hide screen branch
    hide screen front_to_1
    hide screen back_to_3
    hide screen inventory_button
    $ current_room = 0

    window show
    if current_item_in_hand != "wood_key":
        "열쇠를 넣으면 문이 열릴 것 같다"
        window hide
        jump room2
    else:
            menu use_wood_key:
                "들고 있는 열쇠를 넣으면 문이 열릴 것 같다. 넣어볼까?"
                "넣어본다.":
                    window hide
                    jump open_room2
                "넣지 않는다.":
                    window hide
                    jump room2

    $ renpy.pause(hard=True)

label open_room2:
    scene bg room2_close

    window show
    hide screen keyhole_button2
    hide screen hand_screen
    show use_wood_key at Position(xpos=600, ypos=550, xanchor='center', yanchor='center') with dissolve
    "열쇠가 들어갔다."

    "돌려보니 문이 열린다."

    $ room2_open = 1
    window hide
    
    jump enter_room3

label enter_room3:
    python:
        remove_from_inventory(items["wood_key"])
        current_item_in_hand = "default_hand"
        It[1] = 0
    
    scene bg room3
    
    "나무 열쇠가 부서져서 더 이상 사용할 수 없다."

    hide screen keyhole_button2
    hide screen back
    hide screen wall_closeup
    hide screen front_to_1
    hide screen back_to_2
    hide screen back_to_3
    show screen hand_screen
    show screen wall_water

label room3:
    scene bg room3
    show screen inventory_button
    hide screen keyhole_button2
    hide screen back
    hide screen wall_closeup
    hide screen front_to_1
    hide screen back_to_2
    hide screen back_to_3
    hide screen branch
    hide screen front_to_3
    hide screen back_to_5
    hide screen wall_fire
    hide screen keyhole_button3
    hide screen keyhole_button4
    hide screen fire_close
    hide screen key
    show screen front_to_2
    show screen back_to_4
    show screen room3_door
    show screen wall_water
    show screen wall_water
    if room3_branch_visible != True:
        hide screen branch_fire
    else:
        show screen branch_fire

    $ current_room = 3
    if current_item_in_hand == "branch_fire":
        hide screen fire_key
        hide screen branch_fire
        if branch_move != 0:
            python:
                branch_move_count()
        else:
            python:
                branch_move_count()
            hide screen fire_key
            "나무가 모두 타버렸다. 바스러져서 재가 되어버렸다."
            if room3_fire_key_visible != True:
                hide screen fire_key
            else:
                show screen fire_key
            python:
                remove_from_inventory(items["branch"])
                current_item_in_hand = "ash"
                item_counts["ash"] += 1

    if items["glass_key"] not in inventory and items["water_key"] not in inventory and items["freeze_key"] not in inventory and It[3] == 0:
        if current_item_in_hand != "freeze_key" and current_item_in_hand != "water_key":
            show screen glass_key

    if room3_fire_key_visible != True:
        hide screen fire_key
    else:
        show screen fire_key

    $ renpy.pause(hard=True)


label wall_closeup:
    scene bg wall

    $ current_room = 0

    hide screen glass_key
    hide screen wall_water
    hide screen room3_door
    hide screen front_to_2
    hide screen back_to_4
    hide screen fire_key
    hide screen back_to_7
    hide screen back_to_6
    show screen back
    show screen hand_screen
    show screen wall_closeup

    $ renpy.pause(hard=True)

label wall_hold:
    scene bg wallaa
    hide screen wall_closeup
    hide screen keyhole_button

    if current_item_in_hand == "glass_key":
        menu use_glass:
            "저 수상한 액체를 담아볼까?"
            "담는다.":
                jump hold_water
            "담지 않는다.":
                jump wall_closeup
    elif current_item_in_hand == "pet":
        menu use_pet:
            "저 수상한 액체를 담아볼까?"
            "담는다.":
                jump hold_water_pet
            "담지 않는다.":
                jump wall_closeup
    else:
        "벽애서 액체가 흐르고 있다. 손에 닿지 않게 조심하자."
        jump wall_closeup

    $ renpy.pause(hard=True)

label hold_water_pet:
    scene bg wallaa
    hide screen hand_screen
    hide screen inventory_button

    show bg black with dissolve

    "물을 담았다."

    show full_pet at center with dissolve

    "물이 담긴 페트병을 획득했다."

    python:
        remove_from_inventory(items["pet"])
        current_item_in_hand = "full_pet"
        It[10] = 1
        It[9] = 0

    jump wall_closeup

label pour_water:
    if current_room == 1:
        scene bg room1
    elif current_room == 2:
        scene bg room2
    elif current_room == 3:
        scene bg room3
    elif current_room == 4:
        scene bg room4
    elif current_room == 5:
        scene bg room5
    elif current_room == 6:
        scene bg room6
    else:
        scene bg black


    hide screen front_to_3
    hide screen back_to_5
    hide screen wall_fire
    hide screen back3
    hide screen cooler_close
    hide screen keyhole_button3
    hide screen room3_door
    hide screen wall_water
    hide screen front_to_5
    hide screen back_to_7
    hide screen sentence_sharp
    hide screen sentence
    hide screen keyhole_side
    hide screen pet
    hide screen hand_screen
    hide screen front_to_4
    hide screen back_to_6
    hide screen cooler
    hide screen front_to_2
    hide screen back_to_4
    hide screen room3_door
    hide screen wall_water
    hide screen branch
    hide screen wood_key
    hide screen front_to_1
    hide screen back_to_2
    hide screen keyhole_button
    hide screen back_to_2
    hide screen front_to_2
    hide screen back_to_4
    hide screen room3_door
    hide screen wall_water
    hide screen glass_key
    hide screen wall_closeup
    hide screen keyhole_button4
    hide screen keyhole_button2
    hide screen inventory_button
    hide screen fire_key
    hide screen branch_fire

    show bg black with dissolve

    "페트병에 든 정체불명의 액체를 손에 닿지 않게 열쇠에 뿌렸다."

    window hide
    $ water = 0
    # $ renpy.pause(hard=True)
    show bg beige with dissolve
    window show
    show rusty_key at center

    "열쇠 끝 부분이 녹슬었다. 시간이 많이 흐른 열쇠처럼 되었다."

    python:
        It[0] = 0
        It[11] = 1
    window hide

    jump expression "room" + str(current_room)


label hold_water:
    scene bg wallaa
    hide screen hand_screen
    hide screen inventory_button

    show bg black with dissolve

    "물을 담았다."

    show glass_key_water at center with dissolve

    "물이 담긴 열쇠를 획득했다."

    python:
        remove_from_inventory(items["glass_key"])
        It[3] = 0
        It[5] = 1
        current_item_in_hand = "water_key"

    jump wall_closeup

label door_room3:
    scene bg room3_close
    hide screen front_to_2
    hide screen back_to_4
    hide screen inventory_button

    menu open_room3:
                "문이 잠겨있지 않다. 문을 열어볼까?"
                "열어본다.":
                    window hide
                    "문이 열렸다."
                    $ room3_open = 1
                    jump room4
                "열지 않는다.":
                    window hide
                    jump room3

label room4:
    scene bg room4

    hide screen front_to_2
    hide screen back_to_4
    hide screen wall_water
    hide screen glass_key
    hide screen room3_door
    hide screen front_to_4
    hide screen cooler
    hide screen keyhole_button_freeze
    hide screen back2
    hide screen fire_close
    hide screen key

    show screen inventory_button
    show screen front_to_3
    show screen back_to_5
    show screen wall_fire
    show screen keyhole_button3
    hide screen cooler
        
    if room4_branch_visible != True:
        hide screen branch_fire
    else:
        show screen branch_fire
    $ current_room = 4
    if current_item_in_hand == "branch_fire":
        hide screen fire_key
        if branch_move != 0:
            python:
                branch_move_count()
        else:
            python:
                branch_move_count()
            hide screen fire_key
            "나무가 모두 타버렸다. 바스러져서 재가 되어버렸다."
            if room4_fire_key_visible != True:
                hide screen fire_key
            else:
                show screen fire_key
            python:
                remove_from_inventory(items["branch"])
                current_item_in_hand = "ash"
                item_counts["ash"] += 1


    if room4_fire_key_visible != True:
        hide screen fire_key
    else:
        show screen fire_key
    if room4_open == 0 and It[4] == 0:
        show screen fire_key
    $ renpy.pause(hard=True)

label fire_closeup:
    scene bg room4_wall
    hide screen keyhole_button3
    hide screen branch
    hide screen wall_fire
    hide screen fire_key
    hide screen front_to_3
    hide screen back_to_5
    hide screen back_to_6
    hide screen back_to_7
    hide screen keyhole_button4
    show screen back2
    show screen fire_close
    show screen hand_screen

    $ current_room = 0

    python:
        fire_key_visible = False

    if fire_key_visible == False: 
        hide screen fire_key

    $ renpy.pause(hard=True)

label fire_use:
    scene bg room4_wall_2
    hide screen fire_close

    if current_item_in_hand != "branch":
        "불이 활활 타오르고 있다. 무언가에 불을 붙일 수 있을까?"
        jump fire_closeup
    else: 
        menu use_fire:
            "나뭇가지에 불을 붙일까?"
            "붙인다.":
                jump fire_branch
            "붙이지 않는다.":
                jump fire_closeup

    $ renpy.pause(hard=True)

label fire_branch: 
    scene bg room4_wall_2

    hide screen hand_screen
    hide screen fire_close
    hide screen inventory_button
    hide screen back2
    show bg black with dissolve

    "나뭇가지에 불을 붙였다"

    show branch_fire at center with dissolve

    "불 붙은 나뭇가지를 획득했다."

    python:
        remove_from_inventory(items["branch"])
        It[7] = 1
        It[2] = 0
        current_item_in_hand = "branch_fire"

    jump fire_closeup


label door_room4:
    scene bg room4_close

    hide screen fire_key
    hide screen keyhole_button3
    hide screen branch
    hide screen wall_fire
    hide screen branch_fire
    hide screen front_to_3
    hide screen back_to_5
    hide screen inventory_button

    $ current_room = 0

    window show
    if current_item_in_hand != "fire_key":
        "열쇠를 넣으면 문이 열릴 것 같다"
        window hide
        jump room4
    else:
            menu use_fire_key:
                "들고 있는 열쇠를 넣으면 문이 열릴 것 같다. 넣어볼까?"
                "넣어본다.":
                    window hide
                    jump open_room4
                "넣지 않는다.":
                    window hide
                    jump room4

    $ renpy.pause(hard=True)
    
label open_room4:
    scene bg room4_close

    window show
    hide screen keyhole_button3
    hide screen hand_screen

    show used_key at Position(xpos=780, ypos=555, xanchor='center', yanchor='center') with dissolve
    "열쇠가 들어갔다."

    "돌려보니 문이 열린다."

    $ room4_open = 1

    window hide
    
    jump room5

label room5:
    scene bg room5

    hide screen front_to_3
    hide screen back_to_5
    hide screen wall_fire
    hide screen back3
    hide screen cooler_close
    hide screen keyhole_button3
    hide screen room3_door
    hide screen wall_water
    hide screen front_to_5
    hide screen back_to_7
    hide screen sentence_sharp
    hide screen sentence
    hide screen keyhole_side
    hide screen pet
    hide screen key

    show screen inventory_button
    show screen hand_screen
    show screen front_to_4
    show screen back_to_6
    show screen cooler
    if melt_keyhole == 0:
        show screen keyhole_button_freeze
    else:
        show screen keyhole_button4

    if room5_fire_key_visible != True:
        hide screen fire_key
    else:
        show screen fire_key

    if room5_branch_visible != True:
        hide screen branch_fire
    else:
        show screen branch_fire
    $ current_room = 5
    if current_item_in_hand == "branch_fire":
        hide screen fire_key
        if branch_move != 0:
            python:
                branch_move_count()
        else:
            python:
                branch_move_count()
            hide screen fire_key
            "나무가 모두 타버렸다. 바스러져서 재가 되어버렸다."
            if room5_fire_key_visible != True:
                hide screen fire_key
            else:
                show screen fire_key
            python:
                remove_from_inventory(items["branch"])
                current_item_in_hand = "ash"
                item_counts["ash"] += 1

    if room5_fire_key_visible != True:
        hide screen fire_key
    else:
        show screen fire_key

    $ renpy.pause(hard=True)

label door_room5_freeze:
    scene bg room5_close_freeze

    hide screen keyhole_button_freeze
    hide screen cooler
    hide screen fire_key
    hide screen branch_fire
    hide screen front_to_4
    hide screen back_to_6
    hide screen inventory_button

    if current_item_in_hand != "branch_fire":
        "열쇠 구멍이 얼어있다."
        "녹일 수 있는 방법이 있을까?"
    else:
        "나뭇 가지의 불로 녹일 수 있을 것 같다. 녹여볼까?"
        menu use_branch_fire:
            "녹인다.":
                window hide
                $ melt_keyhole = 1
                jump room5_melt
            "그만둔다.":
                window hide
                jump room5

    jump room5

    $ renpy.pause(hard=True)

label room5_melt:
    scene bg room5_close_freeze
    hide screen hand_screen

    show bg black with dissolve

    "열쇠 구멍을 녹였다."

    jump room5

label door_room5:
    scene bg room5_close

    hide screen keyhole_button4
    hide screen cooler
    hide screen fire_key
    hide screen branch_fire
    hide screen front_to_4
    hide screen back_to_6

    hide screen inventory_button

    if current_item_in_hand != "freeze_key":
        "열쇠를 넣으면 문이 열릴 것 같다"
        window hide
        jump room5
    else:
            menu use_freeze_key:
                "들고 있는 열쇠를 넣으면 문이 열릴 것 같다. 넣어볼까?"
                "넣어본다.":
                    window hide
                    jump open_room5
                "넣지 않는다.":
                    window hide
                    jump room5

    $ renpy.pause(hard=True)

label cooler_closeup:
    scene bg room4_cooler

    hide screen glass_key
    hide screen wall_water
    hide screen cooler
    hide screen room3_door
    hide screen back_to_5
    hide screen front_to_4
    hide screen keyhole_button_freeze
    hide screen fire_key
    hide screen back_to_6
    hide screen keyhole_button4
    hide screen branch_fire
    show screen hand_screen
    show screen back3
    show screen cooler_close

    $ current_room = 0

    $ renpy.pause(hard=True)

label water_freeze:
    scene bg room4_cooler

    hide screen cooler_close
    hide screen keyhole_button_freeze
    hide screen inventory_button
    hide screen back3

    if current_item_in_hand != "water_key":
        "냉각기이다. 무언가를 얼릴 수 있을 것 같다"
        jump cooler_closeup
    else:
        menu key_freeze:
            "이 물이 담긴 열쇠를 얼려볼까?"
            "얼린다.":
                jump freeze
            "얼리지 않는다.":
                jump cooler_closeup

    $ renpy.pause(hard=True)

label freeze:
    scene bg room4_cooler
    hide screen hand_screen
    hide screen inventory_button

    show bg black with dissolve

    "열쇠를 얼렸다."

    show glass_key_freeze at center with dissolve

    "얼린 열쇠를 획득했다."

    python:
        remove_from_inventory(items["water_key"])
        remove_from_inventory(items["glass_key"])
        It[3] = 0
        It[5] = 0
        It[6] = 1
        current_item_in_hand = "freeze_key"

    jump cooler_closeup

label open_room5:
    scene bg room5_close

    window show
    hide screen keyhole_button4
    hide screen hand_screen
    hide screen branch_fire
    hide screen inventory_button
    show use_freeze_key at Position(xpos=650, ypos=550, xanchor='center', yanchor='center') with dissolve
    "열쇠가 들어갔다."

    "돌려보니 문이 열린다."

    $ room5_open = 1
    window hide
    
    jump room6

label room6:
    scene bg room6

    hide screen front_to_4
    hide screen back_to_6
    hide screen room6_sentence
    hide screen cooler
    hide screen hand_screen
    hide screen keyhole_button4
    hide screen diary
    hide screen wall_closeup
    hide screen back3
    hide screen cooler_close
    hide screen key
    hide screen keyhole_button
    hide screen keyhole_button2
    hide screen keyhole_button3

    show screen inventory_button
    show screen front_to_5
    show screen back_to_7
    if splash:
        hide screen sentence
        show screen sentence_sharp
    else:
        show screen sentence
    show screen hand_screen
    show screen keyhole_side

    if It[9] == 0 and It[10] == 0:
        show screen pet

    if room6_fire_key_visible != True:
        hide screen fire_key
    else:
        show screen fire_key
    if room6_branch_visible != True:
        hide screen branch_fire
    else:
        show screen branch_fire
    $ current_room = 6
    if current_item_in_hand == "branch_fire":
        hide screen fire_key
        if branch_move != 0:
            python:
                branch_move_count()
        else:
            python:
                branch_move_count()
            hide screen fire_key
            "나무가 모두 타버렸다. 바스러져서 재가 되어버렸다."
            if room6_fire_key_visible != True:
                hide screen fire_key
            else:
                show screen fire_key
            python:
                remove_from_inventory(items["branch"])
                current_item_in_hand = "ash"
                item_counts["ash"] += 1

    if room6_fire_key_visible != True:
        hide screen fire_key
    else:
        show screen fire_key
    $ renpy.pause(hard=True)

label sentence_room6:
    scene bg room6_close

    hide screen hand_screen
    hide screen pet
    hide screen sentence
    hide screen sentence_sharp
    hide screen keyhole_side
    hide screen front_to_5
    hide screen back_to_7
    hide screen inventory_button
    hide screen fire_key

    if current_item_in_hand != "ash":
        "뭔가 스크래치가 나 있다. 뭔가를 뿌리면 선명하게 보일 것 같다."
        jump room6
    else:
        "뭔가 스크래치가 나 있다. 뭔가를 뿌리면 선명하게 보일 것 같다."
        "이 재를 뿌려볼까?"
        menu use_ash:
            "그래":
                python:
                    item_counts["ash"] -= 1
                jump splash_ash
            "아니":
                jump room6

label sentence_room6_sharp:
    scene bg room6_close_sharp

    hide screen hand_screen
    hide screen pet
    hide screen sentence
    hide screen sentence_sharp
    hide screen keyhole_side
    hide screen front_to_5
    hide screen back_to_7
    hide screen inventory_button
    hide screen back3
    hide screen fire_key

    show screen room6_sentence

    
    $ renpy.pause(hard=True)

label door_room6:
    scene bg room6_door_close

    hide screen pet
    hide screen sentence
    hide screen sentence_sharp
    hide screen keyhole_side
    hide screen front_to_5
    hide screen back_to_7
    hide screen inventory_button
    hide screen fire_key

    if current_item_in_hand != "rusty_key":
        "열쇠를 넣으면 문이 열릴 것 같다"
        window hide
        jump room6
    else:
            menu use_rusty_key:
                "들고 있는 열쇠를 넣으면 문이 열릴 것 같다. 넣어볼까?"
                "넣어본다.":
                    window hide
                    jump open_room6
                "넣지 않는다.":
                    window hide
                    jump room6

    $ renpy.pause(hard=True)

label open_room6:
    scene bg room6_door_close
    hide screen hand_screen
    hide screen inventory_button

    window show
    show used_key at Position(xpos=780, ypos=555, xanchor='center', yanchor='center') with dissolve
    "열쇠가 들어갔다."

    "돌려보니 문이 열린다."

    $ room6_open = 1
    window hide
    
    jump room7


    $ renpy.pause(hard=True)


label splash_ash:
    scene bg room6_close
    hide screen back3

    hide screen inventory_button

    show bg black with dissolve

    "재를 뿌렸다."

    $ splash = 1

    jump sentence_room6_sharp

    
label room7:
    scene bg roomA

    hide screen branch
    hide screen wood_key
    hide screen front_to_5
    hide screen back_to_7
    hide screen keyhole_side
    hide screen sentence_sharp
    hide screen key
    hide screen keyhole_button
    show screen front_to_6
    show screen inventory_button
    if room7_fire_key_visible != True:
        hide screen fire_key
    else:
        show screen fire_key
    $ current_room = 7
    show screen diary

    $ renpy.pause(hard=True)

label ending:
    scene bg roomA

    hide screen diary
    hide screen hand_screen
    hide screen front_to_7
    hide screen front_to_6
    hide screen inventory_button

    "끊임없는 루프 속에서 조금씩 달라지는 점들을 찾아내야한다."

    "나는 탈출하지 못했지만, 너는 할 수 있을 것이다."

    show bg black with dissolve

    $ renpy.pause(1.0)

    $ renpy.quit()







        











 


