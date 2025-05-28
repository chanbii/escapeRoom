init:
    ##### 캐릭터 설정 #####
    define abel=Character("아벨", color="#FF3B3B")
    define nar=Character(None, kind=nvl)

    ##### 캐릭터 이미지 #####
    image abel_stand = "character/abel.png"

    ##### 배경 이미지 #####
    image bg roomA = "bg/roomA.png"
    image bg roomB = "bg/roomB.png"
    image bg used_key_roomA = "bg/used_key_roomA.png"
    image bg roomaa = "bg/roomaa.png"
    image bg roombb = "bg/roombb.png"
    image bg usekey = "bg/usekey.png"
    image bg wall = "bg/wall.png"
    image bg wallaa = "bg/wallaa.png"
    image bg room2 = "bg/room2.png"
    image bg room2_close = "bg/room2_close.png"
    image bg room3 = "bg/room3.png"
    image bg room3_close = "bg/room3_close.png"
    image bg room4 = "bg/room4.png"
    image bg room4_close = "bg/room4_close.png"
    image bg room5 = "bg/room5.png"
    image bg room5_close = "bg/room5_close.png"
    image bg room5_close_freeze = "bg/room5_close_freeze.png"
    image bg room4_cooler = "bg/room4_cooler.png"
    image bg room4_wall = "bg/room4_wall.png"
    image bg room4_wall_2 = "bg/room4_wall_2.png"
    image bg room6 = "bg/room6.png"
    image bg room6_close = "bg/room6_close.png"
    image bg room6_door_close = "bg/room6_door.png"
    image bg room6_sharp = "bg/room6_sharp.png"
    image bg room6_close_sharp = "bg/room6_close_sharp.png"
    image bg black = Solid("#000")
    image bg white = Solid("#fff")
    image bg beige = Solid("#caa")

    ##### 아이템 이미지 #####
    image used_key = "hand/used_key.png"
    image full_pet:
        im.FactorScale("item/full_pet.png", 2)
        yalign 0.5
    image rusty_key:
        im.FactorScale("item/rusty_key.png", 2)
        yalign 0.5
    image glass_key_water:
        im.FactorScale("item/glass_key_water.png", 2)
        yalign 0.5
    image glass_key_freeze:
        im.FactorScale("item/glass_key_freeze.png", 2)
        yalign 0.5
    image branch_fire:
        im.FactorScale("item/branch_fire.png", 2)
        yalign 0.5


    ##### 변수 설정 #####
    default inventory = []
    default It = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    default room1_open = 0
    default room2_open = 0
    default room3_open = 0
    default room4_open = 0
    default room5_open = 0
    default room6_open = 0
    default room7_open = 0
    default fire_key_visible = True
    default room1_fire_key_visible = False
    default room2_fire_key_visible = False
    default room3_fire_key_visible = False
    default room4_fire_key_visible = False
    default room5_fire_key_visible = False
    default room6_fire_key_visible = False
    default room7_fire_key_visible = False
    default room1_branch_visible = False
    default room2_branch_visible = False
    default room3_branch_visible = False
    default room4_branch_visible = False
    default room5_branch_visible = False
    default room6_branch_visible = False
    default room7_branch_visible = False
    default melt_keyhole = 0
    default water = 0
    default branch_move = 3
    default move = 4
    default splash = 0
    define center = Position(xalign = 0.5, yalign = 0.3)
    default screen_block = False

    ##### 아이템 정의 #####
    default items = {
        "default_key": {"di": "default_key", "name": "열쇠", "image": "item/dropped_key.png", "explain": "이상하게 생긴 열쇠다. 손잡이 쪽이 살짝 녹슬어 있다.", "hand_image": "hand/key_hand.png", "pos": (200, 530)},
        "wood_key": {"di": "wood_key", "name": "나무 열쇠", "image": "item/wood_key.png", "explain": "나무로 된 열쇠이다. 금방 부러질 것 같다.", "hand_image": "hand/wood_key_hand.png", "pos": (200, 530)},
        "branch": {"di": "branch", "name": "나뭇가지", "image": "item/branch.png", "explain": "나뭇가지이다. 태울 수 있을 것 같다.", "hand_image": "hand/branch_hand.png", "pos": (200, 457)},
        "glass_key": {"di": "glass_key", "name": "유리 열쇠", "image": "item/glass_key.png", "explain": "유리로 된 열쇠이다. 안에 무언가를 넣을 수 있을 것 같다.", "hand_image": "hand/glass_key_hand.png", "pos": (200, 510)},
        "fire_key": {"di": "fire_key", "name": "불타는 열쇠", "image": "item/fire_key.png", "explain": "불타는 열쇠이다. 바로 문을 여는 데에 사용해야할 것 같다.", "hand_image": "hand/fire_key_hand.png", "pos": (200, 163)},
        "water_key": {"di": "water_key", "name": "물이 담긴 유리 열쇠", "image": "item/glass_key_water.png", "explain": "유리 열쇠에 물을 담았다.", "hand_image": "hand/glass_key_water_hand.png", "pos": (200, 510)},
        "freeze_key": {"di": "freeze_key", "name": "얼린 열쇠", "image": "item/glass_key_freeze.png", "explain": "유리 열쇠를 꽝꽝 얼렸다.", "hand_image": "hand/freeze_key_hand.png", "pos": (200, 510)},
        "branch_fire": {"di": "branch_fire", "name": "불 타는 나뭇가지", "image": "item/branch_fire.png", "explain": "나뭇가지에 불을 붙였다. 재가 나오고 있다", "hand_image": "hand/branch_fire_hand.png", "pos": (200, 510)},
        "ash": {"di": "ash", "name": "재", "image": "item/ash.png", "explain": "나무가 모두 다 타버렸다. 바스러져서 재가 되었다.", "hand_image": "hand/ash_hand.png", "pos": (200, 300)},
        "pet": {"di": "pet", "name": "빈 페트병", "image": "item/dropped_pet.png", "explain": "빈 페트병이다. 액체를 담을 수 있을 것 같다", "hand_image": "hand/pet_hand.png", "pos": (200, 435)},
        "full_pet": {"di": "full_pet", "name": "액체가 든 페트병", "image": "item/full_pet.png", "explain": "이상한 액체가 가득 담겼다.", "hand_image": "hand/full_pet_hand.png", "pos": (170, 459)},
        "rusty_key": {"di": "rusty_key", "name": "녹슨 열쇠", "image": "item/rusty_key.png", "explain": "이상한 액체로 인해 끝부분이 녹슬었다.", "hand_image": "hand/rusty_key_hand.png", "pos": (200, 530)}   
    }

    default item_counts = {"ash": 0}

    ##### 현재 손에 든 아이템을 저장하는 변수 #####
    default current_item_in_hand = "default_hand"

    ##### 일기장 정의 #####
    default diary_pages = [
        {"date": "24-07-28", "contents": "알 수 없는 곳에 떨어졌다.\n열쇠로 문을 열려고 하니 열렸다. \n\n 다음 방으로 갔다. 수상한 액체와 열쇠를 결합하니, 문이 열렸다.\n 다음 방에는 침대가 놓여있었다. 수상했지만 알 수 없는 피로감에 누웠다."},
        {"date": "24-07-29", "contents": "이상하게 개운하다."}
    ]
    default current_page = 0 #현재 페이지 인덱스

    ##### 방 정의 #####
    default current_room = 1  # 시작 방 설정

    ##### 함수 정의 #####
    python:
        import renpy.store as store

        # 인벤토리에서 아이템 이미지 띄우기
        def show_item_screen(item):
            renpy.show_screen("item_screen", item=item)

        # 인벤토리에서 아이템 지우기
        def remove_from_inventory(item):
            if item in inventory:
                store.inventory.remove(item)

        # 인벤토리에 아이템 추가하기
        def add_to_inventory(item):
            store.inventory.append(item)

        # 아이템 획득 상태
        def update_It(It, index):
            new_status = It[:]
            new_status[index] = 1
            store.It = new_status

        # # 인벤토리에서 아이템 손에 든다 선택할 시, 손에 든 아이템 이미지 변경을 위한 함수
        # def select_item(item_key):
        #     global It
        #     global current_item_in_hand
        #     global inventory
        #     current_item_in_hand = item_key  # item_key는 'key', 'wood_key' 등이어야 함
        #     remove_from_inventory(items[item_key])
    
        #     for i, (key, item) in enumerate(items.items()):
        #         if It[i] == 1 and key != item_key and key != "fire_key" and key != "branch_fire":
        #             if key == "ash" and item_counts.get("ash", 0) > 0:
        #                 for _ in range(item_counts["ash"]):  # item_counts["ash"] 값만큼 반복
        #                     inventory.append(items["ash"])  # 중복 추가 허용
        #         else:
        #             add_to_inventory(item)
        #         if key != "ash":  # `ash` 외에는 반복 종료
        #             break

        #     renpy.restart_interaction()
        def select_item(item_key):
            global It
            global current_item_in_hand
            global inventory
            current_item_in_hand = item_key  # item_key는 'key', 'wood_key' 등이어야 함
            remove_from_inventory(items[item_key])

            for i, (key, item) in enumerate(items.items()):
                if It[i] == 1 and key != item_key and key != "fire_key" and key != "branch_fire":
                    # ash를 여러 개 추가
                    if key == "ash" and item_counts.get("ash", 0) > 0:
                        for _ in range(item_counts["ash"]):  # item_counts["ash"] 값만큼 반복
                            inventory.append(items["ash"])  # 중복 추가 허용
                        item_counts["ash"] -= 1
                    # 그 외 아이템은 한 번만 추가
                    elif item not in inventory and key != "ash":
                        add_to_inventory(item)
                        break  # ash가 아닌 다른 아이템은 반복 종료

            renpy.restart_interaction()


      
        def show_fire_key_if_visible():
            if current_room == 1 and room1_fire_key_visible:
                renpy.show_screen("fire_key")
            elif current_room == 2 and room2_fire_key_visible:
                renpy.show_screen("fire_key")
            elif current_room == 3 and room3_fire_key_visible:
                renpy.show_screen("fire_key")
            elif current_room == 4 and room4_fire_key_visible:
                renpy.show_screen("fire_key")
            elif current_room == 5 and room5_fire_key_visible:
                renpy.show_screen("fire_key")
            elif current_room == 6 and room6_fire_key_visible:
                renpy.show_screen("fire_key")

        def show_branch_if_visible():
            if current_room == 1 and room1_branch_visible:
                renpy.show_screen("branch_fire")
            elif current_room == 2 and room2_branch_visible:
                renpy.show_screen("branch_fire")
            elif current_room == 3 and room3_branch_visible:
                renpy.show_screen("branch_fire")
            elif current_room == 4 and room4_branch_visible:
                renpy.show_screen("branch_fire")
            elif current_room == 5 and room5_branch_visible:
                renpy.show_screen("branch_fire")
            elif current_room == 6 and room6_branch_visible:
                renpy.show_screen("branch_fire")

        # 불 타는 나뭇가지 이동 횟수
        def branch_move_count():
            global current_item_in_hand
            global current_room
            global branch_move
            global move
            global It

            if branch_move == 0:
                It[8] = 1
                It[7] = 0
                branch_move = 3
                return

            if current_item_in_hand == "branch_fire":
                if move != current_room:
                    if(current_room != 0 or move != 0):
                        branch_move = branch_move - 1
                        renpy.say(None, "나무가 불이 타고 있다. 머지 않아 다 타버릴 것 같다.")
                    move = current_room


        # 사용 버튼 클릭 시 어떤 동작을 할 것인가
        def handle_button_click(item, items):
            global current_item_in_hand
            if item == items["default_key"]:
                renpy.show_screen("popup")
            elif item == items["wood_key"]:
                renpy.show_screen("popup")
            elif item == items["full_pet"]:
                if current_item_in_hand == "default_key":
                    remove_from_inventory(items["default_key"])
                    remove_from_inventory(items["full_pet"])
                    add_to_inventory(items["pet"])
                    renpy.hide_screen("item_screen")
                    renpy.hide_screen("inventory_screen")
                    current_item_in_hand = "rusty_key"
                    It[11] = 1
                    It[10] = 0
                    It[9] = 1
                    renpy.call("pour_water")
                else:
                    renpy.show_screen("popup")
            else:
                renpy.show_screen("popup")
    

        # 일기장 페이지 넘기는 함수
        def next_page():
            global current_page
            if current_page < len(diary_pages) - 1:
                if current_page + 2 > len(diary_pages) - 1:
                    renpy.hide_screen("diary_read")
                    renpy.jump("ending")
                current_page += 2

        def previous_page():
            global current_page
            if current_page > 0:
                current_page -= 2


    ##### 트랜스폼 정의 #####
    transform reduce_size1:
        zoom 0.45
    transform reduce_size2:
        zoom 0.25

    transform fit_to_frame(width, height):
        size(width, height)
        fit "contain"
       
