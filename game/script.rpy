init -2:
    $ qm_togle = False
    $ renpy.block_rollback()
init python:
    config.console = True
    mtime = 1.5 
    moveinleft = MoveTransition(mtime, enter=_moveleft)
    moveinright = MoveTransition(mtime, enter=_moveright)
    moveoutleft = MoveTransition(mtime, leave=_moveleft)
    moveoutright = MoveTransition(mtime, leave=_moveright)

#Курсоры
define config.mouse = {}
define config.mouse['one'] = [ ('gui/cursors/cursorglav1.png', 0, 0) ]
define config.mouse['two'] = [ ('gui/cursors/cursorglav2.png', 0, 0) ]
define config.mouse['three'] = [ ('gui/cursors/cursorglav3.png', 0, 0) ]
define config.mouse['pica'] = [ ('gui/cursors/pica.png', 0, 0) ]

# Определение персонажей игры.
define kara = Character('Кара', color="#c8ffc8")
define oda = Character('[odaname]', color="#c8ffc8")
define nvll = Character(None, kind = nvl)

define kerol = Character('Кэрол', color="#e005d9")
define chel1 = Character('Неизвестный 1', color="#17587e")
define chel2 = Character('Неизвестный 2', color="#17587e")
define child = Character('Мальчик', color="#17587e")
define pri = Character('Священник', color="#b5bcc0")
define krisa = Character('Крысолов', color="#382b7a")
define doc = Character('Чумной доктор', color="#700956")
define guard = Character('Стражник', color="#17587e")
define inq = Character('Инквизитор', color="#066c1c")
define voron = Character('Ворон', color="#ac0e26")
define order = Character('Торговец', color="#17587e")
define chel3 = Character('Неизвестный голос', color="#17587e")
define red = Character('Рыжий преступник', color="#d2691e")
define band = Character('Бандит 1', color="#32068f")
define band2 = Character('Бандит 2', color="#32068f")
#Музыка
define audio.musica = "music/Variant 2.mp3"
define audio.end_music = "music/End_Tailer.mp3"
define audio.sad_music = "music/Shadow of the Castle.mp3"
define audio.sad2_music = "music/Whispers of the Past.mp3"
define audio.epic_music = "music/Epic Escape.mp3"
define audio.epic2_music = "music/On the Run.mp3"
define audio.church1 = "music/church1.mp3"
define audio.church2 = "music/church2.mp3"

#Звуки
define audio.rinok = "sound/rinok.mp3"
define audio.guard_sound = "sound/guard.mp3"
define audio.vaza = "sound/vaza.mp3"
define audio.voron = "sound/voron.mp3"
define audio.ydar_inq = "sound/ydar_inq.mp3"

transform zoomin300:
        zoom 1.0 
        linear 5 zoom  2.0  xpos 717 ypos 577
init:
    #Сцены
    image logo = "images/guui/logo.png"
    image day1 = "images/scene/bg DayOne.png"
    image kh = "images/character/kara_happy.png"
    image kc = "images/character/kara_cute.png"
    image znaxr =  "images/scene/house_snax.png"
    image day1 = "images/scene/DayOne.png"
    image day2 = "images/scene/DayTwo.png"
    image day3 = "images/scene/DayThree.png"
    image day4 = "images/scene/DayFour.png"
    image st = "images/scene/street.png"
    image rt = "images/scene/rinok.png"
    image rtvo = "images/scene/rinok_voron.png"
    image st2 = "images/scene/street2.png"
    image st4 = "images/scene/street3.png"
    image st5 = "images/scene/street1_end.png"
    image ch = "images/scene/church_start.png"
    image st3 = "images/scene/street1.png"
    image game_over = "images/scene/game_over.png"
    image door = "images/scene/door.png"
    image door2 = "images/scene/door2.png"
    image podval = "images/scene/room_krisa.png"
    image store =  "images/scene/storeday3.png"
    image store1 =  "images/scene/storeday3_idle_idle.png"
    image twohome = "images/scene/two_home_krisa.png"
    image roomgg = "images/scene/bg roomgg.png"
    image run_house ="images/scene/run_house.png"
    image happy_end = "images/scene/happy_end.png"
    image box = "images/scene/street2_box.png"
    #Конечные экраны
    image end1 = "images/scene/end1.png"
    image end2 = "images/scene/end2.png"
    image end3 = "images/scene/end3.png"
    image end4 = "images/scene/end4.png"

screen room:
    imagemap:
        idle 'images/scene/roomgg_idle.jpg'
        hover 'images/scene/room_gg_Hover.png'
        hotspot(383, 173, 158, 232) action Jump('window')
        hotspot(837, 170, 159, 235) action Jump('window')
        hotspot(554,340, 281, 242) action Jump('kamin')
        hotspot(591,30, 52, 79) action Jump('light_maker')
        hotspot(1006, 244, 71, 53) action Jump('books')
        hotspot(233, 158, 114, 65) action Jump('books')
        hotspot(970, 426, 309, 234) action Jump('beds')
        hotspot(2, 379, 352, 278) action Jump('beds')
        hotspot(1172, 663, 68, 42) action Jump('prod1')
label splashscreen:
    scene logo with dissolve
    pause 3.0
    return
label start:
    play music musica
    scene black with fade
    show text "Добро пожаловать в мир разрухи и чумы"
    pause 1.0
    scene day1 with dissolve
    pause 1.0
    scene bg roomgg with fade
    pause 0.2
    $ qm_togle = True
    $ odaname = renpy.input("Ваше имя, главный герой?", length = 12).strip() or "Ода"
    "Очередное утро очередного дня выживания в этом городе. Сделав все свои утренние дела, я жду когда проснется Кара."
label rop:
    "Надо бы осмотреть комнату"
    jump room_osmotr
label prod1:
    "Стоило об этом подумать, как она проснулась."
    show karanew
    oda "Доброе утро, Кара."
    kara "Доброе утро."
    oda "Как ты себя чувствуешь? Кэрол не надо звать?"
    hide karanew
    show kara_happy1 at right
    kara "Нет-нет, все хорошо. Благодаря Кэрол, я все еще чувствую себя отлично."
    oda "Отлично. Я пойду прогуляюсь. Будь аккуратнее, и, если что, сразу иди к Кэрол."
    kara "Да-да, я знаю. Береги себя."
    hide kara_happy1
    "Вот и все. Пора снова идти в город и искать средства к существованию. Хотя, лучше заскочу перед этим к Кэрол."
    jump znazarka 
    with dissolve
label room_osmotr:
    call screen room
label window:
    scene bg roomgg with fade
    oda "Из окон в нашей комнате открывается прекрасный вид на стену соседнего дома."
    jump room_osmotr
label kamin:
    scene bg roomgg with fade
    oda "Оранжевое пламя, вырывающееся из камина, напоминает о жертвах инквизиции."
    jump room_osmotr
label light_maker:
    scene bg roomgg with fade
    oda "Эта лампа всегда горит, но я даже не знаю, как Кара поджигает ее."
    jump room_osmotr
label books:
    scene bg roomgg with fade
    oda "У нас есть куча книг. Эх… Если бы я умел читать."
    jump room_osmotr
label beds:
    scene bg roomgg with fade
    oda "Кровати по отдельности, а могла бы быть одна."
    jump room_osmotr
label znazarka:
    scene znaxr
    "Кэрол – знахарка, живущая по соседству. Лучшая женщина в этом мире. Благодаря ей, я могу видеть Кару каждое утро."
    oda "Доброе утро."
    show kerol1
    kerol "Здравствуй, [odaname]. Чего-то хотел?"
    oda "Да нет. Всего лишь решил проведать вас."
    hide kerol1
    show kerol1_ryka
    kerol "Проведал? А теперь убирайся, нечего мне тут клиентов распугивать."
    oda "Ха-ха, если бы они еще были живы."
    kerol "Побойся Бога, паршивец."
    oda "Извините-извините, можете сказать что-нибудь по поводу Кары?"
    hide kerol1_ryka
    show kerol1_yxmilka
    kerol "Да-да, все в порядке. В ближайшее время осложнений не ожидается. Можешь не беспокоиться, пока твоя голубка жить будет."
    oda "Еще раз спасибо вам, мисс Кэрол."
    kerol "Да-да, принимаю твою благодарность, а теперь хватит меня бесить и кыш отсюда."
    oda "Прощайте, мисс Кэрол, надеюсь вы будете так же доброжелательны в следующий раз."
    hide kerol1
    jump street 
    with fade

label street:
    scene st2 with dissolve
    nvll"""Что ж, можно и поискать чего-нибудь. Надеюсь и сегодня
    найдется работка для дешевой рабочей силы, в виде только вступившего во 
    взрослую жизнь парня. Потому что, заработанного ранее хватит только на месяц. """
    nvll"*Столкнулся с кем-то*"
    play sound "sound/ydar_inq.mp3"
    oda "Ой, извините."
    nvll"Не думал, что врежусь в кого-то. "
    nvll"В ответ мне лишь хмыкнули, и он пошел дальше. "
    nvll"""А, инквизитор. По его указке на прошлой неделе сожгли 3 рыжих. Со слов инквизиции, 
    это потому что они распространяли заразу. По ним конечно было видно, что болезнь их не обошла стороной, 
    но в последнее время сжигают лишь рыжих и… «ведьм». Видимо у инквизитора рыжий цвет вызывает плохие воспоминание, 
    иначе не объяснишь."""
    nvl clear
    jump magaz
    with fade
label magaz:
    scene rt with dissolve
    pause 0.3
    play sound rinok
    "Придя на рынок, точнее на то, что от него осталось, я послушал всякие слухи. Надеюсь, работка мне найдется."
    show chel1 at left
    chel1 "Слышал, вчера у соседа дочь из окна выпала?"
    show chel2 at right
    chel2 "Да ты что?"
    "..."
    pause 0.5
    with fade
    show chel1 at left
    chel1 "Помни Авраам ныл, что крыса его за ногу укусила. Ну вот, в последнее время он из церкви не выходит"
    show chel2 at right
    chel2 "Да его ничего не спасет уже."
    "..."
    pause 0.5
    with fade
    chel1 "Не знаешь за сколько стражников на воротах подкупить можно?"
    chel2 "Если б знал, ноги б моей тут не было."
    "..."
    pause 0.5
    with fade
    hide chel1
    hide chel2
    oda "Сегодня я без работы. Ладно, пройдусь по улицам, может кто-то не очень внимательный сегодня останется без части своего товара."
    "Если бы меня учили не воровать в детстве, а счету, то может быть я сейчас не искал работу, а торговал бы крадеными ботинками. "
    "Хотя, кто мог бы меня такому научить. Ни отец, ни матушка считать не умели."
    "Или может, лучше бы отдали меня в церковь, сейчас бы хоть не искал способы выжить в этом городе."
    "Кстати об этом. Не заметил, как уже оказался перед вратами церкви. Может зайти?"
    stop sound
    stop music
    jump church
label church:
    play music church1
    scene ch with dissolve 
    pause 0.1
    pri "Здравствуй, сын мой."
    oda "Здравствуйте, святой отец."
    pri "..."
    oda "..."
    "Какое-то неловкое молчание."
    scene bg church
    pause 0.5
    show priest
    oda "Отец, вы новый пастор?"
    pri "Да"
    "..."
    "..."
    "Зря я сюда пришел. А еще он отвернулся от меня."
    pri "Вижу, сомнения терзают твой разум. Чтобы найти ответы, позволь сердцу провести тебя к ним."
    "Мёд какого растения оказывает такой эффект?"
    oda "Отец, моя дорогая Кара заразилась чумой. Она все еще хорошо себя чувствует, но я боюсь, что это ненадолго."
    pri "Не волнуйся, сын мой. Мы все должны переживать трудные времена. Верь в Божью милость, и он направит тебя по правильному пути."
    oda "Святой отец. Я готов на все, лишь бы Кара была жива."
    "В ответ священник все дальше пялился на крест, будто бы он даст ответ."
    pri "Готов на все? Знаешь ли ты значение этих слов?"
    oda "Что?"
    show priest at right
    pri "Сегодня Бог более милостив. Во времена основании столицы, когда алхимия была в своем расцвете, первый основатель храма в этом городе познал секреты медицины."
    pri "В ту ночь, небо озарилось нескончаемым потом огненных шаров. Приняв это за признание его познаний, он записал открытие в свою книгу, которую так и назвал – «Книга Огненных Звёзд»."
    oda "Красивая история…"
    pri "Панацея – лекарство от всех болезней. Единственный рецепт, который записан в легендарном манускрипте."
    "Как по щелчку, я понял, что нужно, чтобы спасти Кару."
    oda "А где же находится его книга?"
    pri "Давно утеряна."
    oda "Н-но…"
    pri "Позволь Богу вести себя, и тогда ты найдешь ответ на свой вопрос. Прощай, сын мой."
    hide priest with moveoutright
    "Секунду промедления стоило мне того, что он уже скрылся во внутренней двери. Позволь Богу вести себя? Хорошо."
    stop music
    jump street2
label street2:
    play music musica
    scene st2 with dissolve
    """Позволяя Богу вести себя, я прогуливаюсь по улицам нашего города. 
    Мало кого можно встретить, но на улице не прям уж запустение. Хотя счастливым тут никого не встретишь – у каждого кто-нибудь 
    болен чумой."""
    oda "Сэр, извините, кажется это ваше."
    show docktor with moveinright
    doc "A?"
    oda "Говорю вам, сэр, кажется вы обронили записку, в которой указан способ найти манускрипт «Книга Огненных Звёзд». Или хотите сказать, что это не ваше?"
    doc "A, ну..."
    oda "О, извините, кажется это не ваше, а мое. Даст Бог – свидимся."
    hide docktor with moveoutleft
label street3:
    scene st3 with fade
    pause 0.2
    "Не успел я ничего осознать, как он уже скрылся в темном переулке. Странно конечно, что при свете дня переулок такой темный."
    "И у него есть метод добыть легендарный манускрипт. Точнее, это все с его слов. Но откуда он о нем знает? И откуда знает, что это мне нужно? Как он меня нашел?"
    "Столько вопросов, и ни одного ответа."
    "Можно, конечно, побежать за ним, но бегать по темным переулкам – такая себе затея."
    "Ладно, делать нечего, а домой идти рано, стоит еще прогуляться."
    with dissolve
    scene rt with fade
    show child at left
    child "Aй"
    chel2 "Паршивец мелкий!"
    "Как же мальчик громко кричит. Ему прилетело за то, что он попытался украсть хлеб у торговца"
    "Что бы мне сделать?"
    menu:
        "Отвлечь торговца":
            jump choise_otvlek
        "У меня есть дела поважнее":
            jump exit_hel
        "У него не получилось, так получится у меня":
            jump ykral
label choise_otvlek:
    $ menu_flag = False
    scene rt with dissolve
    play music sad2_music
    "Этот торговец же убьет его!"
    "Я хватаю камень и бросаю его в лицо продавца."
    show chel2 at center
    chel2 "Ублюдок"
    "Оу, он в ярости. И вроде отстал от мальчика."
    oda "И что ты мне сделаешь?!"
    "Не думал, что во мне столько смелости."
    "Торговец подбегает ко мне и… "
    "Я не чувствую челюсть."
    "Как-то резко в глазах потемнело…"
    scene game_over with fade
    stop music
    pause 3.0
    return

label ykral:
    $ menu_flag = True
    scene rt with fade
    "Бедный мальчик, сегодня явно не твой день"
    "Ну что ж, торговец, сегодня ты продашь на одну булку хлеба меньше."
    "Надеюсь никто не заметил, как я спрятал хлеб."
    menu:
        "Вот и мой обед":
            jump my_lunch
        "Вот и обед для Кары":
            jump lunch_for_kara

label lunch_for_kara:
    $ menu_flag = True
    scene st3 with dissolve
    "Ай да я, ай да добытчик. Пойду домой, отдам Каре поесть."
    scene bg roomgg with fade
    oda "Кара! Я принес поесть"
    show karanew at center
    kara "О, Ода. С возвращением. Это нам?"
    oda "Нет, это тебе. Я уже поел"
    hide karanew
    show kara_happy1 at right
    kara "Да-да, по тебе видно какой ты сытый. Присаживайся, покушаем вместе. Обед уже готов."
    oda "Тебя не обманешь."
    kara "Конечно, сколько я тебя уже знаю."
    oda "Хорошо-хорошо, давай есть."
    hide kara_happy1
    "Таким образом мы с ней разделили трапезу. В процессе которой завязался диалог о моем дне. Про манускрипт я пока рассказывать не стал."
    oda "Ну вот, пообщался с пастором, и он наставил меня следовать своему сердцу, чтобы найти то, что я ищу."
    show karanew at center
    kara "И что же ты нашел?"
    oda "Как видишь, сердце привело меня снова к тебе."
    hide karanew
    show kara_cute1 at center
    kara "Льстец."
    oda "Просто правда."
    kara "Ешь давай."
    oda "Хорошо-хорошо."
    hide kara_cute1
    "Так и дальше прошел наш обед. Запоздалый немного, но сегодня мы хорошо поели."
    "Решив, что день еще в самом разгаре, я решил все-таки еще раз пройтись, может быть случится еще что-нибудь интересного."
    oda "Кара, я ушел!"
    kara "Хорошо."
    scene st2 with dissolve
    "Прогуливаюсь по улочкам столицы. Ничего нового, как будто город вообще не меняется. Хотя людей, конечно меньше, не устану это подмечать."
    "Но есть еще смельчаки, которым болезнь нипочем, снуют туда-сюда"
    "Интересно, а часто ли инквизитор гуляет по улицам города, чтобы отловить… «ведьм»… Хотя наверняка у инквизиции и своих дел полно."
    show inq at right
    oda "Здравствуйте! Колдунов и ведьм не видели?!"
    inq "Э-э… Нет?"
    oda "Как жаль. Всего вам доброго."
    hide inq
    "Откуда он взялся? У него других дел нет? Опять же, одни вопросы, и ни одного ответа."
    "Хотя вот и ответ на мой прошлый вопрос. Видимо других дел у него нет, раз он гуляет тут и ищет кого бы сжечь на костре."
    "..."
    "Больше ничего интересного не произошло. Даже никого не грабили посреди бела дня"
    "Думаю, уже пора домой."
    scene bg roomgg with fade
    "Уже поздно, и Кара спит."
    "Завалившись на кровать я и уснул."
    jump day2ykral_obed_kara
    return

label my_lunch:
    $ menu_flag = False
    scene st3 with dissolve
    "Разворачиваюсь и иду в другую сторону, где можно будет спокойно поесть."
    "День еще не закончился, заскочу к Кэрол."
    scene znaxr with fade
    oda "И снова здравствуйте."
    "Хм? Никого? Подожду ее тут."
    "..."
    "Скууууучно. Где же она там?"
    "..."
    "Я сразу обратил внимание на звук открывающейся двери."
    show kerol1_yxmilka
    kerol "О, [odaname]. Хотел чего-то?"
    oda "Наконец-то я вас дождался. Да, я хотел вам кое-что рассказать"
    kerol "Я вся внимание."
    oda "Слышали что-нибудь про «Книгу Огненных Звёзд»?"
    hide kerol1_yxmilka
    show kerol1_ryka
    kerol "Хм… Книга Огненных Звёзд говоришь?.. О, ну, впервые слышу. А сам-то откуда узнал?"
    oda "От нового пастора."
    kerol "Ты больше их слушай, много всего интересного расскажут."
    oda "Но ладно бы это был он один, еще какой-то странный мужчина весь в черном и с вороном на плече, он тоже знает про эту книгу."
    kerol "Чумной доктор-то? Это уже поубедительнее."
    oda "Так вот, пастор сказал, что в этом манускрипте содержится секрет создания панацеи – лекарства от всех болезней."
    kerol "Даже так? А мертвых к жизни оно случайно возвращать не может? "
    oda "Сомневаюсь. Но даже если и не лечит от всех болезней, как думаете, Каре эта панацея жизнь облегчить сможет?"
    kerol "Кто знает. Но может в записях моих предков есть что-нибудь об этой книжке. Я поищу, может узнаю что-то."
    oda "Спасибо большое. Век не забуду."
    hide kerol1_ryka
    show kerol1
    kerol "Да-да, принимаю твою благодарность."
    oda "Еще раз спасибо, я тогда уже пойду."
    kerol "Хорошо, прощай."
    oda "Увидимся."
    scene st3 with fade
    "И с этими словами я вышел из магазина."
    "Даже не знал, что я так долго прождал, уже ночь."
    "Пойду уже поскорее домой."
    scene bg roomgg with dissolve
    "Дом, родимый дом. Кара уже спит"
    "С такими словами я завалился на кровать и уснул."
    jump day2ykral_obed
    return

label exit_hel:
    $ menu_flag = False
    scene st3 with fade
    nvll "Бедный мальчик. Вот что бывает, когда лезешь на кого не следует."
    nvll "Но мне не следует здесь задерживаться. Да и не собираюсь я тут оставаться."
    nvll "Эх, детям приходиться красть еду у бешеных торговцев, чтобы выжить, а эти барыги готовы убить за любую копейку."
    nvll "Ну стража в любом случае его скрутит и покажет, почему нельзя совершать акты насилия прямо посреди улицы."
    nvll "Хоть в чем-то эти странные придурки полезные."
    nvl clear
    scene door with dissolve
    "Кстати о странном. Передо мной вполне необычная дверь. Необычного в ней то, что заперта она с помощью веревки. Слишком странно"
    "Изнутри так не запереться… Интересно, если там сейчас никого, то, значит, можно оттуда что-нибудь позаимствовать."
    "Как удобно, что я взял с собой нож."
    "И… Раз… Дверь открылась. За дверью тут лестница, ведущая куда-то вниз. О, кто-то забыл потушить свет, прежде чем уйти. Мне же лучше."
    "По-быстрому закрываю за собой дверь и спускаюсь вниз."
    scene room_krisa with dissolve
    "И это сплошное разочарование. Свечка на комоде позволяет видеть, что кроме комода, тут есть кровать. Собственно, на этом все."
    "Можно было и догадаться, что человек, запирающий дверь веревкой, не самый богатый. Но тут прям вообще нечем поживиться."
    krisa "Нравится, что видишь?"
    "Откуда?!"
    "Удар об этот кусок камня, который тут, вроде бы, вместо кровати, не назвать мягким приземлением. Да в этой ситуации вообще мало приятного."
    "Поза человека и его положение создают интересную игру света, из-за чего его лица не видно. Только зубы отсвечивают и все."
    show krisa_zlo
    krisa "Ну что ж, мальчишка. Папка с мамкой не научили не шариться по чужим подвалам, а? Может стоит им рассказать, что их чадо бегает где попало?"
    oda "Можешь прыгнуть на нож, чтобы поскорее сообщить им эти вести."
    krisa "Какой у тебя острый язык. Не боишься, что отрежут?"
    oda "Не особо."
    krisa "Какой смелый… И, что мне с тобой такого сделать, чтобы тебя не видеть?"
    hide krisa_zlo
    show krisa
    oda "Можешь меня отпустить."
    krisa "Почему я должен тебя отпускать?"
    oda "Чтобы меня не видеть. Что за глупые вопросы?"
    hide krisa
    show krisa_ydivlen
    krisa "Да, точно, извини, что-то не подумал."
    krisa "Хорошо, я прощаю тебя. Ну, я пошел."
    oda "Ага, давай."
    hide krisa_ydivlen
    "Быстро встав, я уже почувствовал ступеньку под ногой, но не тут-то было. Меня снова кинули на этот кусок камня."
    show krisa_zlo
    krisa "Ты или тупой, или очень смелый. Но мне как-то без разницы. Слушай внимательно, мне нужно, чтобы ты кое-что для меня сделал. Ты согласен?"
    oda "Нет."
    "Видимо, этот ответ неправильный. А доказательство моих слов – кинжал в стене рядом с моим ухом."
    oda "Н-ну, поговорим о моей оплате?"
    hide krisa_zlo
    show krisa_xitriy
    krisa "Как насчет того, что я сохраню тебе жизнь, а? Достаточная плата за твои услуги?"
    "Выбора особо нет, конечно."
    oda "Сойдет."
    krisa "Вот и договорились, а теперь кыш отсюда. Завтра я найду тебя."
    hide krisa_xitriy
    scene st with fade
    "Ну вот и наконец-то отпустили меня."
    "Быстрым шагом ухожу отсюда, хватит на сегодня приключений."
    jump scene_6_room_gg

label scene_6_room_gg:
    scene bg roomgg with dissolve
    oda "Я вернулся."
    show karanew at right
    kara "С возвращением. Как на улице?"
    oda "Как будто из церкви сбежали особо опасные душевнобольные."
    kara "С чего же ты так решил?"
    oda "Сначала новый пастор, как будто сам себе на уме. Потом какой-то укутанный во все черное с вороном на плече, уже это говорит о его душевном состоянии."
    oda "Ну и напоследок какой-то лысый, раскидывающийся ножами."
    "Стоило мне закончить, как Кара принялась меня осматривать."
    kara "Тебя не задело?"
    oda "Как видишь, жив и цел."
    hide karanew
    show kara_happy1
    kara "Слава богу."
    oda "Ага. А ты как? Все хорошо?"
    hide kara_happy1
    show karanew
    kara "Кэрол сказала, что со мной в ближайшее время ничего не случится."
    "Надеюсь это правда."
    kara "Кстати, ты так и не сказал, как ты встретился со всеми этими странными людьми."
    "Рассказ и обсуждение этих странных личностей затянулся у нас до ночи." 
    jump day2_exit_hell
    
    return     
