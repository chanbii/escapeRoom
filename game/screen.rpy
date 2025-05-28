##### 디버그용 스크린 #####
screen debug_info():
    text "room1_open: [room1_open]" ypos 0
    text "room2_open: [room2_open]" ypos 30
    text "room3_open: [room3_open]" ypos 60
    text "room4_open: [room4_open]" ypos 90
    text "room5_open: [room5_open]" ypos 120
    text "current_room: [current_room]" ypos 150
    text "splash: [splash]" ypos 180
    text "current hand: [current_item_in_hand]" ypos 210
    text "Item: [It]" ypos 240
    text "1: [room1_fire_key_visible]" ypos 270
    text "2: [room2_fire_key_visible]" ypos 300
    text "3: [room3_fire_key_visible]" ypos 330
    text "4: [room4_fire_key_visible]" ypos 360
    text "5: [room5_fire_key_visible]" ypos 390
    text "move: [move]" ypos 420
    text "count: [branch_move]" ypos 450
    text "current_room: [current_room]" ypos 480
    text "item_counts: [item_counts['ash']]" ypos 510

screen debug_inventory():
    frame:
        xsize 500
        ysize 200
        vbox:
            text "디버그 - 인벤토리 내용:"
            for item in inventory:
                text item["name"]

##### 손 스크린 #####

screen hand_screen():
    zorder 50
    if current_item_in_hand and current_item_in_hand != "default_hand": #만약 현재 손에 든 물건이 none이 아니면서 디폴트 핸드가 아닌 경우
        add items[current_item_in_hand]["hand_image"] pos items[current_item_in_hand]["pos"] # 딕셔너리 키에 접근해 값을 가져온다.
    else:
        add "hand/default_hand.png" pos (200, 688)



##### 방 이동 버튼 #####
screen front_to_1:
    vbox:
        align (0.85, 0.05)
        hbox:
            textbutton "이전 방으로":
                action Jump("room1")

screen front_to_2:
    vbox:
        align (0.85, 0.05)
        hbox:
            textbutton "이전 방으로":
                if room2_open == 1:
                    action Jump("room2")
                else:
                    action None

screen front_to_3:
    vbox:
        align (0.85, 0.05)
        hbox:
            textbutton "이전 방으로":
                if room3_open == 1:
                    action Jump("room3")
                else:
                    action None

screen front_to_4:
    vbox:
        align (0.85, 0.05)
        hbox:
            textbutton "이전 방으로":
                if room4_open == 1:
                    action Jump("room4")
                else:
                    action None

screen front_to_5:
    vbox:
        align (0.85, 0.05)
        hbox:
            textbutton "이전 방으로":
                if room5_open == 1:
                    action Jump("room5")
                else:
                    action None

screen front_to_6:
    vbox:
        align (0.85, 0.05)
        hbox:
            textbutton "이전 방으로":
                if room6_open == 1:
                    action Jump("room6")
                else:
                    action None

screen back_to_2:
    vbox:
        align (0.95, 0.05)
        hbox:
            textbutton "다음 방으로":
                if room1_open == 1:
                    action Jump("room2")
                else:
                    action None

screen back_to_3:
    vbox:
        align (0.95, 0.05)
        hbox:
            textbutton "다음 방으로":
                if room2_open == 1:
                    action Jump("room3")
                else:
                    action None

screen back_to_4:
    vbox:
        align (0.95, 0.05)
        hbox:
            textbutton "다음 방으로":
                if room3_open == 1:
                    action Jump("room4")
                else:
                    action None

screen back_to_5:
    vbox:
        align (0.95, 0.05)
        hbox:
            textbutton "다음 방으로":
                if room4_open == 1:
                    action Jump("room5")
                else:
                    action None

screen back_to_6:
    vbox:
        align (0.95, 0.05)
        hbox:
            textbutton "다음 방으로":
                if room5_open == 1:
                    action Jump("room6")
                else:
                    action None

screen back_to_7:
    vbox:
        align (0.95, 0.05)
        hbox:
            textbutton "다음 방으로":
                if room6_open == 1:
                    action Jump("room7")
                else:
                    action None

##### room1 #####
screen keyhole_button:
    imagebutton:
        idle "click/keyhole_button.png" 
        pos (960, 310)
        if room1_open == 1:
            action Jump("room2")
        else: 
            action Jump("door_room1")

screen key:
    imagebutton:
        idle "item/dropped_key.png"
        pos (1281, 793)
        action [SetVariable("inventory", inventory + [items["default_key"]]), Function(update_It, It, 0), Hide("key")]

##### room2 #####
screen keyhole_button2:
    imagebutton:
        idle "click/keyhole_button.png" 
        pos (960, 310)
        if room2_open:
            action Jump("room3")
        else:
            action Jump("door_room2")

screen wood_key:
    imagebutton:
        idle "item/wood_key.png"
        pos (1212, 793)
        action [SetVariable("inventory", inventory + [items["wood_key"]]), Function(update_It, It, 1), Hide("wood_key")]

screen branch:
    imagebutton:
        idle "item/branch.png"
        pos (612, 789)
        action [SetVariable("inventory", inventory + [items["branch"]]), SetVariable("branch_move", 3),Function(update_It, It, 2), Hide("branch")]

##### room3 #####
screen wall_water:
    zorder -1
    imagebutton:
        idle "click/wall_water.png"
        pos (138, 318)
        action Jump("wall_closeup")

screen back:
    frame:
        vbox:
            xsize 100
            ysize 70
            align (0.5, 0.5)
            button:
                text "<-" align (0.5, 0.5)
                action Jump("room3")
        align (0.05, 0.05)

screen wall_closeup:
    imagebutton:
        idle "click/wall_closeup.png"
        pos (755, 110)
        action Jump("wall_hold")

screen glass_key:
    imagebutton:
        idle "item/glass_key.png"
        pos (612, 789)
        action [SetVariable("inventory", inventory + [items["glass_key"]]), Function(update_It, It, 3), Hide("glass_key")]

screen room3_door:
    zorder -5
    imagebutton:
        idle "click/room3_door.png"
        pos (705, 37)
        if room3_open == 1:
            action Jump("room4")
        else:
            action [Hide("glass_key"), Hide("wall_water"), Hide("room3_door"), Jump("door_room3")]

##### room4 #####
screen wall_fire:
    zorder -2
    imagebutton:
        idle "click/fire.png"
        pos (145, 80)
        action Jump("fire_closeup")

screen fire_close:
    zorder -7
    imagebutton:
        idle "click/fire_close.png"
        pos (506, -325)
        action Jump("fire_use")

screen back2:
    frame:
        vbox:
            xsize 100
            ysize 70
            align (0.5, 0.5)
            button:
                text "<-" align (0.5, 0.5)
                action Jump("room4")
        align (0.05, 0.05)

screen keyhole_button3:
    imagebutton:
        idle "click/keyhole_button.png" 
        pos (960, 310)
        if room4_open == 1:
            action Jump("room5")
        else:
            action Jump("door_room4")

screen fire_key:
    imagebutton:
        idle "item/fire_key.png"
        pos (1212, 600)
        action [
        If(current_item_in_hand == "branch_fire" and current_room == 1, [SetVariable("room1_branch_visible", True), Show("branch_fire")]),
        If(current_item_in_hand == "branch_fire" and current_room == 2, [SetVariable("room2_branch_visible", True), Show("branch_fire")]),
        If(current_item_in_hand == "branch_fire" and current_room == 3, [SetVariable("room3_branch_visible", True), Show("branch_fire")]),
        If(current_item_in_hand == "branch_fire" and current_room == 4, [SetVariable("room4_branch_visible", True), Show("branch_fire")]),
        If(current_item_in_hand == "branch_fire" and current_room == 5, [SetVariable("room5_branch_visible", True), Show("branch_fire")]),
        If(current_item_in_hand == "branch_fire" and current_room == 6, [SetVariable("room6_branch_visible", True), Show("branch_fire")]),
        If(current_item_in_hand == "branch_fire" and current_room == 7, [SetVariable("room7_branch_visible", True), Show("branch_fire")]),
        Function(select_item, "fire_key"), SetVariable("current_item_in_hand", "fire_key"), Hide("fire_key"), Function(update_It, It, 4),
        SetVariable("room1_fire_key_visible", False),
        SetVariable("room2_fire_key_visible", False),
        SetVariable("room3_fire_key_visible", False),
        SetVariable("room4_fire_key_visible", False),
        SetVariable("room5_fire_key_visible", False),
        SetVariable("room6_fire_key_visible", False),
        SetVariable("room7_fire_key_visible", False)]

##### room5 #####
screen cooler:
    zorder -3
    imagebutton:
        idle "click/cooler.png"
        pos (145, 80)
        action Jump("cooler_closeup")

screen keyhole_button_freeze:
    imagebutton:
        idle "click/keyhole_button_freeze.png" 
        pos (960, 310)
        action Jump("door_room5_freeze")

screen keyhole_button4:
    imagebutton:
        idle "click/keyhole_button.png" 
        pos (960, 310)
        if room5_open == 1:
            action Jump("room6")
        else:
            action Jump("door_room5")

screen back3:
    frame:
        vbox:
            xsize 100
            ysize 70
            align (0.5, 0.5)
            button:
                text "<-" align (0.5, 0.5)
                action [Jump("room5")]
        align (0.05, 0.05)

screen cooler_close:
    zorder -6
    imagebutton:
        idle "click/cooler_close.png"
        pos (417, 35)
        if current_item_in_hand != "water_key":
            action Show("popup")
        else:
            action Jump("water_freeze")

screen branch_fire:
    imagebutton:
        idle "item/branch_fire.png"
        pos (1000, 800)
        action [
        If(current_item_in_hand == "fire_key" and current_room == 1, [SetVariable("room1_fire_key_visible", True), Show("fire_key")]),
        If(current_item_in_hand == "fire_key" and current_room == 2, [SetVariable("room2_fire_key_visible", True), Show("fire_key")]),
        If(current_item_in_hand == "fire_key" and current_room == 3, [SetVariable("room3_fire_key_visible", True), Show("fire_key")]),
        If(current_item_in_hand == "fire_key" and current_room == 4, [SetVariable("room4_fire_key_visible", True), Show("fire_key")]),
        If(current_item_in_hand == "fire_key" and current_room == 5, [SetVariable("room5_fire_key_visible", True), Show("fire_key")]),
        If(current_item_in_hand == "fire_key" and current_room == 6, [SetVariable("room6_fire_key_visible", True), Show("fire_key")]),
        If(current_item_in_hand == "fire_key" and current_room == 7, [SetVariable("room7_fire_key_visible", True), Show("fire_key")]),
        SetVariable("current_item_in_hand", "branch_fire"), Hide("branch_fire"), Function(update_It, It, 7),
        Function(select_item, "branch_fire"),
        SetVariable("room1_branch_visible", False),
        SetVariable("room2_branch_visible", False),
        SetVariable("room3_branch_visible", False),
        SetVariable("room4_branch_visible", False),
        SetVariable("room5_branch_visible", False),
        SetVariable("room6_branch_visible", False),
        SetVariable("room7_branch_visible", False),
        SetVariable("move", current_room)]

##### room6 #####
screen keyhole_side:
    imagebutton:
        idle "click/keyhole_side.png" 
        pos (1570, 397)
        if room6_open == 0:
            action Jump("door_room6")
        else:
            action Jump("room7")

screen sentence:
    imagebutton:
        idle "click/sentence.png" 
        pos (739, 210)
        action Jump("sentence_room6")

screen back4:
    frame:
        vbox:
            xsize 100
            ysize 70
            align (0.5, 0.5)
            button:
                text "<-" align (0.5, 0.5)
                action Jump("room6")
        align (0.05, 0.05)

screen sentence_sharp:
    imagebutton:
        idle "click/sentence_sharp.png" 
        pos (739, 210)

screen pet:
    zorder -1
    imagebutton:
        idle "item/dropped_pet.png"
        pos (612, 789)
        action [SetVariable("inventory", inventory + [items["pet"]]), Function(update_It, It, 9), Hide("pet")]

screen room6_sentence:
    imagebutton:
        idle "click/door6_sentence.png" 
        pos (582, 53)
        action Jump("room6")
    
##### room7 #####
screen diary:
    imagebutton:
        idle "item/diary.png"
        pos (565, 828)
        action Show("diary_read")

screen diary_read():
    zorder 1006
    add "click/diary_closeup.png"
    frame:
        vbox:
            xsize 100
            ysize 100
            button:
                text "닫기" align (0.5, 0.5)
                action [Hide("diary_read"), Jump("ending")]
                align (0.8, 0.1)
        align (1.0, 0.0)
    frame:
        xsize 858
        ysize 852
        # (122, 145, 858, 852)
        pos (122, 145)
        # background Solid("#caa")
        
        text "[diary_pages[current_page]['date']]" size 30 color "#000" align (0.05, 0.05)
        xpadding 50
        vbox:
            xsize 600
            ysize 600
            spacing 30
            text "[diary_pages[current_page]['contents']]" size 35 color "#000"
            align (0.0, 0.8)

        hbox:
            if current_page > 0:
                textbutton "<-" action Function(previous_page)
                align (0.0, 1.0)
    frame:
        xsize 858
        ysize 852
        pos (978, 145)
        # background Solid("#cdd")
        # (978, 145, 860, 857)

        text "[diary_pages[current_page + 1]['date']]" size 30 color "#000" align (0.05, 0.05)
        xpadding 50
        vbox:
            xsize 600
            ysize 600
            spacing 30
            text "[diary_pages[current_page + 1]['contents']]" size 35 color "#000"
            align (0.0, 0.8)
        
        hbox:
            if current_page < len(diary_pages) - 1:
                textbutton "->" action Function(next_page)
                align (1.0, 1.0)

    



##### inventory #####

screen inventory_button:
    frame:
        vbox: 
            xsize 30
            ysize 20
            button:
                text "가방" 
                action ShowTransient("inventory_screen")

        align (1.0, 0.0)

screen inventory_item(item):  # item_key 추가
    frame:
        background "#fff"
        xsize 185
        ysize 165
        if item["image"] == "item/ash.png":
            add item["image"] at reduce_size2 align (0.5, 0.5) 
        else:
            add item["image"] at reduce_size1 align (0.5, 0.5) 
        button:
            action Function(show_item_screen, item)  # item_key 전달

screen inventory_screen():
    modal True
    zorder 100
    frame: 
        hbox:
            xsize 700
            ysize 100
            text "가방" align (0.5, 0.5)
        align (0.4, 0.1)
    
    frame:
        vbox:
            xsize 100
            ysize 100
            button:
                text "닫기" align (0.5, 0.5)
                action [Hide("inventory_screen"), Hide("item_screen"), Hide("popup")]
                align (0.5, 0.5)
        align (0.75, 0.1)
    frame:
        background "#111"
        vbox:
            xsize 1004
            ysize 704
        align (0.5, 0.7)

    frame:
        background "#caa"
        hbox:
            xsize 1000
            ysize 700
            if not inventory:
                text "아무것도 없다." align (0.5, 0.5)
            else:
                grid 5 4:
                    for i in range(20):
                        if i < len(inventory):
                            frame:
                                background Solid("#999")
                                xsize 195
                                ysize 170
                                xalign 0.5
                                yalign 0.5
                                use inventory_item(inventory[i]) # inventory의 현재 아이템에 대한 key 전달
                        else:
                            frame:
                                background Solid("#caa")
                                xsize 195
                                ysize 170
                                xalign 0.5
                                yalign 0.5
        align (0.5, 0.7)



##### 팝업 #####

screen popup:
    zorder 1004
    frame:
        text "어떻게 사용하면 좋을까? 다른 아이템이랑 조합해볼 수도 있을까?" align (0.5, 0.5)
        xsize 700
        ysize 100
        align (0.5, 0.5)
    
    button:
        action Hide("popup")

screen popup_unusable(item):
    zorder 1005
    modal True
    frame:
        text "불타는 물체를 가방에 넣을 수 없어, 다른 물건을 들 수 없다. 버릴까?" align (0.1, 0.1)
        xsize 700
        ysize 400
        align (0.5, 0.5)
        vbox:
            spacing 10
            align (0.5, 0.7)
            textbutton "그래" action [
                If(current_room == 0, Show("popup_drop")),
                If(current_room != 0, [
                    SetVariable("current_item_in_hand", item["di"]),
                    Hide("popup_unusable"),
                    Hide("item_screen"),
                    Function(select_item, item["di"]),
                    If(current_room == 1, SetVariable("room1_fire_key_visible", True)),
                    If(current_room == 2, SetVariable("room2_fire_key_visible", True)),
                    If(current_room == 3, SetVariable("room3_fire_key_visible", True)),
                    If(current_room == 4, SetVariable("room4_fire_key_visible", True)),
                    If(current_room == 5, SetVariable("room5_fire_key_visible", True)),
                    If(current_room == 6, SetVariable("room6_fire_key_visible", True)),
                    Function(show_fire_key_if_visible)
                ])
            ]
            textbutton "아니" action Hide("popup_unusable")


screen popup_unusable2(item):
    zorder 1005
    modal True
    frame:
        text "불타는 물체를 가방에 넣을 수 없어, 다른 물건을 들 수 없다. 버릴까?" align (0.1, 0.1)
        xsize 700
        ysize 400
        align (0.5, 0.5)
        vbox:
            spacing 10
            align (0.5, 0.7)
            textbutton "그래" action [
                If(current_room == 0, Show("popup_drop")),
                If(current_room != 0, [
                    SetVariable("current_item_in_hand", item["di"]),
                    Hide("popup_unusable2"),
                    Hide("item_screen"),
                    Function(select_item, item["di"]),
                    If(current_room == 1, SetVariable("room1_branch_visible", True)),
                    If(current_room == 2, SetVariable("room2_branch_visible", True)),
                    If(current_room == 3, SetVariable("room3_branch_visible", True)),
                    If(current_room == 4, SetVariable("room4_branch_visible", True)),
                    If(current_room == 5, SetVariable("room5_branch_visible", True)),
                    If(current_room == 6, SetVariable("room6_branch_visible", True)),
                    Function(show_branch_if_visible)
                ])
            ]
            textbutton "아니" action Hide("popup_unusable")


screen popup_drop:
    zorder 1005
    frame:
        text "방으로 가서 버리자." align (0.5, 0.5)
        xsize 700
        ysize 100
        align (0.5, 0.5)
    button:
        action [Hide("popup_drop"), Hide("popup_unusable"), Hide("popup_unusable2")]

##### 아이템 #####

screen item_screen(item):
    zorder 1001
    modal True
    frame:
        xsize 1000
        ysize 700
        align (0.5, 0.7)
        background Solid("#caa")
        frame:
            xsize 300
            ysize 300
            vbox:
                align (0.5, 0.5)
                add item["image"] at fit_to_frame(270, 270)
            align (0.2, 0.2)

        frame:
            xsize 350
            ysize 100
            vbox:
                align (0.5, 0.5)
                button:
                    text "손에 든다" align (0.5, 0.5)
                    if current_item_in_hand == "fire_key":
                        action Show("popup_unusable", item=item)
                    elif current_item_in_hand == "branch_fire":
                        action Show("popup_unusable2", item=item)
                    else:
                        action [
                            Function(select_item, item["di"]),  # item_key 전달
                            Hide("item_screen")
                        ]
            align (0.8, 0.15)

        frame:
            xsize 350
            ysize 100
            vbox:
                align (0.5, 0.5)
                button:
                    text "사용한다" align (0.5, 0.5)
                    action Function(handle_button_click, item, items)
            align (0.8, 0.3)

        frame:
            xsize 350
            ysize 100
            vbox:
                align (0.5, 0.5)
                button:
                    text "아무것도 하지 않는다" align (0.5, 0.5)
                    action Hide("item_screen")
            align (0.8, 0.45)

        frame:
            vbox:
                xsize 800
                ysize 200
                text str(item["explain"])
            xpadding 10
            align (0.5, 0.9)




