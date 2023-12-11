# Define characters with their respective images
define jack = Character('Джек:', image='jack', color="#c8ffc8")
define john = Character('Джон', image='john')
define killian = Character('Киллиан', image='killian', color="#c8c8ff")
define steven = Character('Стивен', image='steven')


# Define the expressions
image john natural = "characters/john_natural.png"
image john smiling = "characters/john_smiling.png"
image killian natural = "characters/killian_natural.png"
image killian smiling = "characters/killian_smiling.png"
# Define the expressions
image jack normal = "characters/jack.png"
image killian natural = "characters/killian_natural.png"
image killian happy = "characters/killian_happy.png"
# Define the expressions
image steven = "characters/steven.png"

# Define the transform for Killian to be smaller
transform john1:
    zoom 0.7  # This scales the image to 20% of its original size
    xalign 0.8  # This centers the image horizontally on the screen
    yalign 1.0  # This aligns the image to the bottom of the screen

# Define transforms for characters
transform small_left:
    zoom 0.4  # Scale the image down to 70% of its original size
    xalign 0.1  # Align the image to the left of the screen
    yalign 1.0  # Align the image to the bottom of the screen

transform small_right:
    zoom 0.4  # Scale the image down to 70% of its original size
    xalign 0.9  # Align the image to the right of the screen
    yalign 1.0  # Align the image to the bottom of the screen

    # Define transforms for characters
transform small_center:
    zoom 0.3  # Scale the image down to 70% of its original size
    xalign 0.3  # Center the image horizontally
    yalign 1.0  # Align the image to the bottom of the screen

transform small_center1:
    zoom 0.7  # Scale the image down to 70% of its original size
    xalign 0.3  # Center the image horizontally
    yalign 1.0  # Align the image to the bottom of the screen

transform small_right1:
    zoom 0.3  # Scale the image down to 70% of its original size
    xalign 0.8  # Align the image to the right of the screen
    yalign 1.0  # Align the image to the bottom of the screen

    # Define transforms for characters
transform small_left2:
    zoom 0.3  # Scale the image down to 70% of its original size
    xalign 0.1  # Align the image to the left of the screen
    yalign 1.0  # Align the image to the bottom of the screen

# Define the backgrounds
image cafe background1 = "locations/сцена_1_1.png"

# Start of the game script
label start:
    scene cafe background1 with fade
    show killian natural at small_center with fade
    show john natural at john1 with fade
    show killian natural at small_center with fade

    john "Привет, Киллиан, Мы так давно не виделись, рассказывай как твои дела?"
    killian "Привет, Джон. Да все супер! Закончил в УрФу радиофак, и теперь настроен работать."

    # Continue with the dialogue
    john "И чем ты хочешь заняться?"
    killian "Думаю заняться разработкой игр. Всегда увлекался ими. А теперь хочу сам создавать игры, чтобы другие начали увлекаться моими."

    john "Звучит интересно, и с чего ты начнешь свой путь?"
    killian "Ну думаю устроиться в небольшую компанию сначала, там параллельно учиться гейм разработке, ну а дальше просто очень стараться и все думаю получится."

    john "Ну я в тебя верю, приятель! Обязательно сыграю в твою игру. А кстати, на каком языке ты хочешь писать игры?"

    # Here you can insert a menu choice if you want the player to choose the language
    menu:
        "Python":
            $ programming_language = "Python"
            killian "Думаю на Python."

        "C#":
            $ programming_language = "C#"
            killian "Думаю на C#."

    john "О, слышал это хороший язык для игр."
    killian "Я тоже так думаю."

    # Conclude the scene
    killian "Ладно, встретимся еще. А я побежал на встречу с наставником из небольшой компании по разработке приложений."
    john "Удачи!"

    # Hide characters as the scene ends
    hide john
    hide killian
    with fade

# Define the backgrounds
image office_exterior2 = "locations/сцена2.png"

# The second scene starts here
label scene_2:
    scene office_exterior2 with fade
    show jack normal at small_right1 with fade
    show killian natural at small_center with fade
    
    jack "Ну что, Киллиан, добро пожаловать к нам, хоть и в небольшую, но амбициозную компанию по разработке приложений!"
    
    killian "Спасибо, Джек. И что мне предстоит сделать?"
    
    jack "В первый день устроим тебе экскурсию, введем в курс дела, а потом уже будешь решать задачи, показывать свои знания! Мы знаем, что ты нацелен на разработку игр и найдем тебе подходящее дело."
    
    killian "Отлично, буду рад начать работать."
    
    jack "Также мы предоставляем несколько курсов для улучшения навыков по разработке игр или дизайну игр, но о них расскажу позже."
    
    killian "Было бы отлично записаться на такой курс."
    
    jack "Ну у тебя будет еще возможность! Увидимся завтра, удачи тебе, Киллиан."
    
    killian "Спасибо, Джек."
    
    # Hide characters as the scene ends
    hide jack
    hide killian
    with fade
    

# Continuing from the previous definitions, now we set up the third scene.

# Define the backgrounds
image office_interior3 = "locations/cцена_3.png"

# Scene 3 starts here
label scene_3:
    scene office_interior3 with fade
    show killian natural at small_center with fade
    
    # Killian's thoughts
    killian "Что-то волнительно начинать работу в офисе… Но он такой маленький и спокойный, что думаю я вольюсь быстро. Эта компания по разработке приложений хоть и маленькая, но надеюсь поможет мне начать карьеру. А дальше уже перейду в саму разработку игр."
    
    # Jack enters the scene
    show jack normal at small_right1 with fade
    jack "О, Киллиан, здравствуй. Как твой настрой?"
    
    killian "Настроен на успех!"
    jack "Это отлично. Идем, покажу тебе твое место."
    
    # The show and hide commands can be used with a 'with' statement to apply transitions
    hide killian
    hide jack
    show killian happy at small_center1 with fade
    show jack normal at small_right1 with fade
    
    # Jack showing Killian around
    jack "Вот один из этих столов твой."
    killian "Выглядит неплохо."
    
    # Jack gives Killian a task
    jack "Отлично, справился, Киллиан. Теперь введу тебя в курс дела. Тебе нужно будет приходить в офис и выполнять по 2-3 задачи в день. За это ты будешь получать бонусы, а за них можешь получить наши курсы."
    
    # Killian reacts
    killian "Да! А когда я смогу получить курсы?"
    
    # Jack explains the points system
    jack "Смотри, за день ты сможешь получить максимум 20 баллов, а 10 баллов, если не останешься на час дольше. Первый курс доступен с 30 баллов."
    
    # Killian confirms understanding
    killian "Все понял!"
    
    # Jack gives more tasks
    jack "Даю тебе еще пару задач и на время отойду."
    
    # Time skip to evening decision
    # You can use a menu here for the choice to stay or leave
    menu:
        "Остаться на час":
            $ points = 20
            killian "Решу остаться и поработать еще час."
            # Additional narrative or tasks can go here
        
        "Уйти домой":
            $ points = 10
            killian "Пожалуй, я пойду домой и отдохну. Сегодня был продуктивный день."

    # Hide characters and transition out
    hide killian
    hide jack
    with fade
    
    # Transition to the next scene or label
    # jump scene_4 or call scene_4 (if you have scene_4 as a separate label)

# Scene 4 code starts here

# Define the backgrounds
image office_interior4 = "locations/сцена4_4.png"

label scene_4:
    scene office_interior4 with fade
    show killian happy at small_center1 with fade
    show jack normal at small_right1 with fade
    
    # Week later Killian comes to the office
    killian "Спустя неделю упорной работы, я прошёл стажировку и теперь официально работаю."
    jack "Привет, Киллиан! Рад видеть тебя. Как прошла твоя стажировка?"
    killian "Привет, Джек! Стажировка прошла отлично. Я многому научился и получил ценный опыт."
    
    jack "Это замечательно! Теперь ты готов браться за серьёзные дела. Какие у тебя планы на будущее?"
    killian "Я хочу развиваться в своей профессии и стать ещё более опытным специалистом."
    
    jack "Отлично, Киллиан. Я уверен, что у тебя всё получится. Давай обсудим твои первые задачи на новой должности."
    
    # Career path choice
    menu:
        "Разработчик":
            scene office_interior4
            show killian happy at small_center1
            show jack normal at small_right1
            $ career_path = "Разработчик"
            jack "Твоё первое задание - это написать код для простой 2D-игры, где игрок управляет движущимся объектом (например, космическим кораблем), и цель игры - собрать все звёзды на уровне, избегая астероидов. Постарайся выполнить как можно скорее."
            killian "Будет сделано."
            
            # Killian works on the task
            # Evening choice
            menu:
                "Остаться подольше":
                    scene office_interior4
                    show killian happy at small_center1
                    show jack normal at small_right1
                    $ points += 10
                    killian "Я решил остаться и продолжить работу над разработкой."
                "Уйти":
                    scene office_interior4
                    show killian happy at small_center1
                    show jack normal at small_right1
                    $ points += 5
                    killian "Лучше уйду домой и продолжу завтра."

        "Аниматор":
            scene office_interior4
            show killian happy at small_center1
            show jack normal at small_right1
            $ career_path = "Аниматор"
            jack "Твоё первое задание - это создать анимацию прыгающего мяча и сделать анимацию движения кошки."
            killian "Будет сделано."
            
            # Killian works on the task
            # Evening choice
            menu:
                "Остаться подольше":
                    scene office_interior4
                    show killian happy at small_center1
                    show jack normal at small_right1
                    $ points += 10
                    killian "Я решил остаться и продолжить работу над анимацией."
                "Уйти":
                    scene office_interior4
                    show killian happy at small_center1
                    show jack normal at small_right1
                    $ points += 5
                    killian "Лучше уйду домой и продолжу завтра."

    # Transition to next scene or end the day
    hide killian
    hide jack
    with fade
    # jump next_scene or return

# Scene 5 code starts here
# Define the backgrounds
# Scene 5 starts here
image office_interior5 = "locations/cцена_5.png"

# Scene 5 starts here
label scene_5:
    # A month later, the outcome depends on previous choices of the player.
    if points >= 30:
        # Player gets a promotion
        scene office_interior5 with fade
        show jack normal at small_right1 with fade
        show killian natural at small_left2 with fade

        jack "Привет, Киллиан. Можешь зайти ко мне в кабинет?"
        killian "Конечно, Джек. Что случилось?"
        jack "Присаживайся. У меня есть к тебе предложение. Как ты смотришь на повышение?"
        killian "Повышение? Я даже не знаю, что сказать. Это очень неожиданно."
        jack "Послушай, Киллиан, ты один из самых ответственных новых сотрудников в нашей компании. Ты всегда стараешься выполнить свою работу на все 100%%, и я это ценю. И я думаю, что ты заслуживаешь повышения."
        killian "Спасибо, Джек, мне очень приятно это слышать. Но я не уверен, что готов к повышению. Я только недавно освоился на своей текущей должности."
        jack "Я понимаю твои опасения. Но ты не бойся, повышение не будет означать, что тебе придется делать что-то новое или незнакомое. Ты будешь заниматься тем же, чем и сейчас, но с большей ответственностью и зарплатой."
        killian "Ну, если так, то я согласен. Мне кажется, это будет хорошим опытом для меня."
        jack "Отлично! Я рад, что мы смогли договориться."

        $ points += 20  # Player gains points for the promotion

    else:
        # Player needs to work harder
        scene office_interior5 with fade
        show jack normal at small_right1 with fade
        show killian natural at small_left2 with fade
        
        jack "Здравствуй, Киллиан! У меня к тебе серьезный разговор."
        killian "Да, что случилось?"
        jack "Мне кажется, что ты недостаточно усердно работаешь в последнее время."
        killian "Но, я стараюсь изо всех сил!"
        jack "Я думал, что повышу тебя, но теперь я вижу, что тебе нужно еще поработать."
        killian "И сколько мне нужно работать?"
        jack "Еще одну неделю. Если ты покажешь хорошие результаты, то я повышу тебя. Но если нет, то придется подождать еще некоторое время."
        killian "Хорошо. Я постараюсь сделать все возможное."
        jack "Вот и отлично. Удачи тебе, Киллиан!"
        $ points -= 10  # Player loses points if they didn't work hard enough
# Check if the player stayed longer previously and adjust the narrative accordingly
if points >= 30:
    # Player gets a promotion
    jack "Привет, Киллиан, как твой первый день в новой должности?"
    killian "Все отлично, спасибо за возможность. Я очень рад быть частью вашей команды."
    jack "Это здорово! Я уверен, что ты справишься с новыми обязанностями. Но помни, что теперь у тебя больше ответственности. Теперь тебе нужно работать в команде."
    killian "Конечно, я понимаю. Я готов к новым вызовам."
    jack "Отлично! Скоро к тебе придется Тимлид команды."
    killian "Понял."

    # Branching based on the career path chosen by the player
    if career_path == "Разработчик":
        # Developer path
        hide jack
        show steven normal at small_right1 with fade
        steven "Привет, Киллиан. Я тимлид команды в этом отделе. Слышал, ты хорошо проявил себя в должности Разработчика. Я готов тебе выдать задачи."
        steven "Попробуй разработать код для головоломки, где игрок должен управлять различными объектами (например, кубами), чтобы решать задачи и преодолевать препятствия на своем пути. Головоломки должны становиться все сложнее по мере прохождения игры. В любой момент ты сможешь советоваться с командой по сюжету и персонажам."
        killian "Я все понял."
        # Placeholder for the work animation
        # show killian working at laptop with code on the screen

    elif career_path == "Аниматор":
        # Animator path
        hide jack
        show jack normal at small_right1 with fade
        steven "Привет, Киллиан. Я тимлид команды в этом отделе. Слышал, ты хорошо проявил себя в должности Аниматора. Я готов тебе выдать задачи. Создай анимацию персонажа, который прыгает и бегает, а затем сделай анимацию кошки, которая играет с клубком ниток."
        killian "Я все понял."
        # Placeholder for the animation work

    # Evening choice to stay longer or leave
    menu:
        "Остаться подольше":
            $ points += 20
            killian "Решу остаться и поработать еще час."
            # Additional narrative or tasks can go here
        
        "Уйти домой":
            $ points += 10
            killian "Пожалуй, я пойду домой и отдохну. Сегодня был продуктивный день."

    # Transition to next scene or end the day
    hide killian
    hide steven
    with fade
# The scene continues based on the player's choices

# Week later after choosing to stay longer or leave
image office_interior6 = "locations/сцена_5_3.png"

label week_later:
    if points >= 40:
        # Successful promotion and work
        scene office_interior5 with fade
        show killian happy at small_center1 with fade
        show jack normal at small_right1 with fade
        killian "Работа в команде была сложной, но интересной. Я столкнулся с различными проблемами и задачами, которые требовали от меня творческого подхода и умения работать в условиях ограниченного времени."
        killian "Однако, благодаря своему опыту и упорству, я смог успешно справиться со всеми задачами и достичь поставленных целей."
        jack "Киллиан, я слышал, что ты закончил проект в команде по разработке новой игры. Как тебе этот опыт?"
        killian "Мне очень нравится работать в команде. Это позволяет мне учиться у других и развивать свои навыки."
        jack "Рад слышать, что ты наслаждаешься этим опытом. Продолжай двигаться в том же духе и не забывай, что командная работа - это ключ к успеху."
        
        # Evening at home without a choice to stay or leave
        $ points -= 5  # Deduct points for the evening
        killian "Рабочий день в этот раз прошел без выбора оставаться или нет. Я устал."
        
        # Killian at home
        scene office_interior6 with fade
        show killian natural at small_left2 with fade
        killian "Я не могу найти время на отдых и начал чувствовать усталость. Я стал делать ошибки и потерял концентрацию. Не знаю, как я дальше продолжу эту работу…"
        # Phone call from John
        play sound "audio/mobile.wav"
        killian "Джон? Давно тебя не слышал. Ты уже работаешь?"
        john "Киллиан, ты как всегда вовремя. Я только задумался о том, что не справляюсь с этим всем и не знаю хочу ли уже заниматься этим делом."
        john "Киллиан, тебе срочно нужно что-то менять. Начни планировать свое время и расставлять приоритеты. Уделяй больше времени отдыху и занятиям, которые тебе нравятся."
        killian "Хорошо. Я попробую это все."
        john "Звони в любое время. Я верю, что все наладится."
        # End of phone call
        killian "Может, Джон и прав. Нужно последовать его советам. Пойду попробую написать план на завтрашний день и включить туда перерыв на отдых."

# A month after the promotion or the additional week of hard work
label a_month_later:
    scene office_interior4 with fade
    show killian natural at small_left2 with fade
    show jack normal at small_right1 with fade
    if points >= 30:
        # If Killian got a promotion
        jack "Киллиан, я слышал, что ты закончил проект в команде по разработке новой игры. Как тебе этот опыт?"
        killian "Мне очень нравится работать в команде. Это позволяет мне учиться у других и развивать свои навыки."
        jack "Рад слышать, что ты наслаждаешься этим опытом. Продолжай двигаться в том же духе и не забывай, что командная работа - это ключ к успеху."
    else:
        # If Killian needs to work harder
        jack "Киллиан, я рассчитывал на твою усердную работу, но кажется, тебе нужно еще немного времени, чтобы доказать, что ты готов к повышению."
        killian "Я понимаю, Джек. Я постараюсь не подвести."
        jack "У тебя все получится, я в тебя верю. Просто помни, что от тебя зависят и другие члены команды."
        killian "Спасибо за вашу поддержку."

    # Fade out and transition to the next part of the story
    hide killian
    hide steven
    with fade
# End of Scene 5
