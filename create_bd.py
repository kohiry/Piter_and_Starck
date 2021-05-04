import sqlite3
# -*- coding: utf8 -*-

db = sqlite3.connect('game.db')
sql = db.cursor()

sql.execute("""
    CREATE TABLE IF NOT EXISTS spider (
    text_1 TEXT,
    text_2 TEXT,
    text_3 TEXT,
    text_4 TEXT,
    text_5 TEXT,
    text_6 TEXT,
    text_7 TEXT,
    text_8 TEXT,
    text_9 TEXT,
    text_10 TEXT,
    text_11 TEXT,
    text_12 TEXT,
    text_13 TEXT,
    text_14 TEXT,
    text_15 TEXT,
    text_16 TEXT,
    text_17 TEXT,
    text_18 TEXT,
    text_19 TEXT,
    text_20 TEXT,
    text_21 TEXT,
    text_22 TEXT,
    text_23 TEXT,
    text_24 TEXT,
    text_25 TEXT,
    text_26 TEXT,
    text_27 TEXT,
    text_28 TEXT,
    text_29 TEXT,
    text_30 TEXT,
    text_31 TEXT,
    text_32 TEXT,
    text_33 TEXT,
    text_34 TEXT,
    text_35 TEXT,
    text_2_end TEXT,
    text_6_end TEXT,
    text_8_end TEXT,
    text_13_end TEXT,
    text_24_end TEXT
    )
""")

db.commit()
sql.execute("""
    CREATE TABLE IF NOT EXISTS monster (
    text_1 TEXT,
    text_2 TEXT,
    text_3 TEXT,
    text_4 TEXT,
    text_5 TEXT,
    text_6 TEXT,
    text_end_1 TEXT,
    text_end_2 TEXT,
    text_end_3 TEXT
    )""")

db.commit()
sql.execute("""
    CREATE TABLE IF NOT EXISTS TreeOfBarries (
    text_1 TEXT
    )""")

db.commit()
sql.execute("""
    CREATE TABLE IF NOT EXISTS FirstPhraseInDange (
    text_1 TEXT
    )""")

db.commit()
sql.execute("""
    CREATE TABLE IF NOT EXISTS FirstCutscene (
    text_1 TEXT
    )""")

db.commit()
sql.execute("""
    CREATE TABLE IF NOT EXISTS Hedgehog (
    text_1 TEXT,
    text_2 TEXT,
    text_3 TEXT,
    text_4 TEXT,
    text_5 TEXT,
    text_6 TEXT,
    text_7 TEXT
    )
""")
db.commit()

# заолнение БД данными по Пауку
SPIDER_TEXT_1 = '''
П,1 - Эй дружок! Я Человек-паук, дружелюбный сосед, залез сюда к вам с мирными намерениями забрать своего папоч- друга, не поможешь мне его найти?;Г,14 - /Злое бурчание/;П,1 - Судя по всему нет...
'''
SPIDER_TEXT_2 = '''
П,2 - Что это у тебя там... Яд?! Как негостеприимно!
'''
SPIDER_TEXT_3 = '''
П,1 - Мы с тобой одной крови - ты и я... Нет? А в мультике сработало... Кинематограф лжёт.
'''
SPIDER_TEXT_4 = '''
П,1 - Хей, мы же братишки-паучишки, так может ты отдашь мне Тони?;Г,14 - /злобное шипение/;П,1 - Ясно, кто-то тут приемный.
'''
SPIDER_TEXT_5 = '''
П,9 - Это потому что у меня всего 2 ноги?! Что с вами не так, гребаные бодишеймеры!
'''
SPIDER_TEXT_6 = '''
П,1 - Мне вот интересно. Ты гриб, которого укусил паук, или паук, которого укусил гриб?
'''
SPIDER_TEXT_7 = '''
П,1 - А у тебя ножки, или ложноножки?;Г,14 - /злобное шипение/;П,1 - Что ж, я пытался завязать наш разговор.
'''
SPIDER_TEXT_8 = '''
П,1 - Без обид, но я обязан отблагодарить вселенную за то, что после укуса не стал таким же красавцем, как ты.;
'''
SPIDER_TEXT_9 = '''
П,1 - Это птица? Это самолет? ЭТО ПИЗДЮЛИ!
'''
SPIDER_TEXT_10 = '''
П,1 - Кажется, мне понадобится тапок побольше.
'''
SPIDER_TEXT_11 = '''
П,1 - Хей! Парень, завязывай с этим! Хотя постой, я сам завяжу.
'''
SPIDER_TEXT_12 = '''
Г,14 - /Шипение/;П,6 - Оу, спасибо, это так мило!;Г,14 - /повторное шипение/;П,9 - А. Так это был не комплимент.
'''
SPIDER_TEXT_13 = '''
П,1 - Эти ваши пауки и двух слов связать не могут!
'''
SPIDER_TEXT_14 = '''
П,1 - Снова привет! Как делишки?;Г,14 - /агрессивное шипение/;П,4 - И почему я продолжаю притворяться, что понимаю вас...
'''
SPIDER_TEXT_15 = '''
П,1 - А если ты меня укусишь, я стану двойным человеком-пауком? Человеком-пауком-пауком? Челоуком-пауком?;П,1 - А если ты меня укусишь, я стану двойным человеком-пауком? Человеком-пауком-пауком? Челоуком-пауком?
'''
SPIDER_TEXT_16 = '''
П,1 - Каждый раз говорить «инопланетный грибной паук» как-то муторно, давай я буду называть вас... Кевинами?;Г,14 - /шипение/;П,1 - Тебя не спрашивали, Кевин!
'''
SPIDER_TEXT_17 = '''
П,1 - Ни у кого тут нет спрея от жуков?;Г,14 - /шипение/;П,1 - Прости, от арахнидов.
'''

SPIDER_TEXT_18 = """
П,1 - Вселенная подарила мне шанс отомстить паукам за тот укус! Подставляй лапки, буду делать кусь.
"""

SPIDER_TEXT_19 = """
П,1 - Пещерка у вас, чуваки, просто космос! У кого заказывали этот внеземной дизайн?
"""

#КОМИК МОМНТ НА 20 ДИАЛОГЕ
SPIDER_TEXT_20 = """
П,1 - Не так страшно увидеть паука, как потерять его из виду. Верно, приятель?;П,2 - ... Приятель?...
"""

SPIDER_TEXT_21 = """
П,1 - Быть дружелюбным соседом Человеком-пауком означает помогать всем, кто нуждается в помощи, именно поэто-;Г,14 - /злое шипение/;П,1 - Эй, не перебивай! Так вот… Я помогаю каждому, кто нуж-;Г,14 - /очень злое шипение/;П,1 - Я пытаюсь, окей? Знаешь как сложно быть примером для подражания?;Г,14 - /шипение/;П,9 - Что? Ты назвал меня нытиком? Я изливаю тебе душу, а ты так поступаешь со мной? Кевин, ты слишком грубый, поучился бы у своих братьев. Они хотябы не пытаются меня унизить. Они просто хотят меня съесть.
"""

SPIDER_TEXT_22 = """
П,1 - Стой, паук, я твой отец!;Г,14 - /злобное шипение/;П,1 - Ну хоть классику ты знаешь.
"""

SPIDER_TEXT_23 = """
П,1 - Тётя Мэй явно будет не в восторге, если я приведу вас в качестве своих родственников на ее свадьбу с Хэппи.
"""

SPIDER_TEXT_24 = """
П,6 - А ты как вижу любишь грубости.
"""

SPIDER_TEXT_25 = """
П,6 - Как насчет небольшой практики в шибари?
"""

SPIDER_TEXT_26 = """
П,1 - Хей, приятель, ты правда любишь грибной дождь?;Г,14 - /злое бурчание/;П,1 - Что ж, споры никогда не были моим коньком.
"""

SPIDER_TEXT_27 = """
Г,14 - /злое бурчание/;П,1 - На твоём месте я бы сходил к логопеду.
"""

SPIDER_TEXT_28 = """
П,1 - Если я скажу, что боюсь пауков , ты мне поверишь?
"""
#СНОВА ИСЧЕЗНОВЕНИЕ
SPIDER_TEXT_29 = "Я считаю до трех, и ты просто исчезаешь с моего пути, окей? Раз, два, три...;П,2 - Чувак, я передумал, вернись пожалуйста!"
SPIDER_TEXT_30 = "П,1 - /Попытки напеть песню про Человека Паука/;Г,14 - /шипение/;П,1 - Дружок, ты не попадаешь в ноты."
SPIDER_TEXT_31 = "П,1 - Хочешь шутку?;Г,14 - /шипение/;П,1 - Короче, заходят как-то в бар...;Г,14 - /злобное шипение/;П,1 - Да ладно тебе, это же классика!"
SPIDER_TEXT_32 = "П,1 - Эй приятель!;Г,14 - /паучьи звуки/;П,1 - /подражание на паучьи звуки/;Г,14 - ?????"
SPIDER_TEXT_33 = "П,1 - Тут так холодно из-за того что это подземная пещера? Или из-за твоего сердца?"
SPIDER_TEXT_34 = "П,1 - Эй, такси! До мистера Старка не подвезешь?;Г,14 - /шипение/;П,1 - Отвратный у вас тут сервис."
SPIDER_TEXT_35 = "П,1 - Знаешь что? А давай на этот раз ты пошутишь! А то все, я, да я...;Г,14 - /шипение/;П,1 - Не стесняйся!;Г,14 - /шипение/;П,1 - Ммм, тебе стоит попрактиковаться. Но попытка засчитана."



SPIDER_TEXT_13_END = 'П,1 - Ничего себе, как тебя скрутило!'
SPIDER_TEXT_2_END = "П,1 - Передохни пока, грубиян. "
SPIDER_TEXT_6_END = "П,1 - Не волнуйся, оно растворится через пару часов."
SPIDER_TEXT_8_END = "П,1 - Знаешь, тебе бы пора перестать себя так накручивать."
SPIDER_TEXT_24_END = "П,1 - Не поймал, не поймал, свой обед ты проебал."

SPIDER_TEXT = [SPIDER_TEXT_1, SPIDER_TEXT_2, SPIDER_TEXT_3,
               SPIDER_TEXT_4, SPIDER_TEXT_5, SPIDER_TEXT_6,
               SPIDER_TEXT_7, SPIDER_TEXT_8, SPIDER_TEXT_9, SPIDER_TEXT_10,
               SPIDER_TEXT_11, SPIDER_TEXT_12, SPIDER_TEXT_13, SPIDER_TEXT_14,
               SPIDER_TEXT_15, SPIDER_TEXT_16, SPIDER_TEXT_17,
               SPIDER_TEXT_18, SPIDER_TEXT_19, SPIDER_TEXT_20, SPIDER_TEXT_21,
               SPIDER_TEXT_22, SPIDER_TEXT_23, SPIDER_TEXT_24, SPIDER_TEXT_25,
               SPIDER_TEXT_26, SPIDER_TEXT_27, SPIDER_TEXT_28, SPIDER_TEXT_29, SPIDER_TEXT_30, SPIDER_TEXT_31,
               SPIDER_TEXT_32, SPIDER_TEXT_33, SPIDER_TEXT_34, SPIDER_TEXT_35,
               SPIDER_TEXT_2_END, SPIDER_TEXT_6_END, SPIDER_TEXT_8_END, SPIDER_TEXT_13_END, SPIDER_TEXT_24_END]
sql.execute('SELECT * FROM spider')
quantity = ['?' for i in range(40)]
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO spider VALUES ({', '.join(quantity)})", (tuple(SPIDER_TEXT)))
    db.commit()
else:
    print('Уже записывали паука.')

# заолнение БД данными по Тентаклям
MONSTER_TEXT_1 = '''
П,3 - Ну привет... Что-то длинное и вихляющее... Растение? Животное? От чего-то у меня сейчас чутье завопило пониже спины...
'''

MONSTER_TEXT_2 = '''
П,3 - Я все еще не хочу знакомиться с тобой ближе чем на 3 метра.
'''

MONSTER_TEXT_3 = '''
П,1 - Дайте мне подключение к интернету, мини-холодильник и небольшой диван, и я бы с удовольствием обосновался в соседней яме.
'''

MONSTER_TEXT_4 = '''
П,1 - Лови, приятель! Только давай без руко-зачеркнуто-щупальцеприкладства.
'''

MONSTER_TEXT_5 = '''
П,1 - Лови вкусняшку. Эх сейчас бы пиццы... У вас тут случайно нет подземной доставки?
'''

MONSTER_TEXT_6 = '''
П,1 - Твоё любимое, без сахара, соли, и с критическим содержанием фтора.
'''

MONSTER_TEXT_END_1 = """
П,2 - ЕБ ТВОЮ МААА…
"""

MONSTER_TEXT_END_2 = """
П,2 - ЕБАНЫЙ РОООО…
"""

MONSTER_TEXT_END_3 = """
П,2 - ДРАТЬ МЕНЯ В УХО ТОЛЬКО НЕ СНОВА…
"""

MONSTER_TEXT = [MONSTER_TEXT_1, MONSTER_TEXT_2, MONSTER_TEXT_3, MONSTER_TEXT_4,
                MONSTER_TEXT_5, MONSTER_TEXT_6, MONSTER_TEXT_END_1, MONSTER_TEXT_END_2, MONSTER_TEXT_END_3]
sql.execute('SELECT * FROM monster')
quantity = ['?' for i in range(9)]
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO monster VALUES ({', '.join(quantity)})", (MONSTER_TEXT))
    db.commit()
else:
    print('Уже записывали тентакли.')

# заолнение БД данными по ежу
HENDEHOG_TEXT_1 = "П,1 - Что-то мне подсказывает, что лучше не приземляться на эту штуковину..."
HENDEHOG_TEXT_END_1 = 'П,1 - Я чувствую уколы совести за то, что упустил мистера Старка. Ай! Или не совести. (укол) '
HENDEHOG_TEXT_END_2 = 'П,1 - Ау-ау-ау! Колкости в сторону, сударь! (укол)'
HENDEHOG_TEXT_END_3 = 'П,1 - Колись, куда подевали мистера Старка?! (укол)'
HENDEHOG_TEXT_END_4 = 'П,1 - Хочешь прикол? \молчание ежа\ И я не хочу. (укол)'
HENDEHOG_TEXT_END_5 = 'П,1 - Да кто тут раскидал эти штуки?! (укол)'
HENDEHOG_TEXT_END_6 = 'П,7,8 - В следующий раз я прилечу сюда с лопатой и садовыми ножницами! (укол)'

HENDEHOG_TEXT = [HENDEHOG_TEXT_1, HENDEHOG_TEXT_END_1, HENDEHOG_TEXT_END_2, HENDEHOG_TEXT_END_3,
                HENDEHOG_TEXT_END_4, HENDEHOG_TEXT_END_5, HENDEHOG_TEXT_END_6]
sql.execute('SELECT * FROM Hedgehog')

quantity = ['?' for i in range(7)]
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO Hedgehog VALUES ({', '.join(quantity)})", (HENDEHOG_TEXT))
    db.commit()
else:
    print('Уже записывали ежа.')

# заолнение БД данными по ежу
FirstCutscene_TEXT_1 = " Ж,10 – Давай, Паучок, только здесь мы не смотрели, тут точно должны быть эти ягоды. Если мы не притащим их здоровяку, в сыворотку покрошат уже нас.;Ж,10 – Погнали, путешествие на 5 минут, зашли и вышли.;П,6 – Вы как будто в спальню меня зовете, а не в пещеру, ха-ха-ха :D;Ж,10 – Нос клоунский сними, юморист. Давай-ка посерьезнее и пошли.;П,1 – Ну не знаю, мистер Старк, эта пещера выглядит зловеще...;П,2 -  Стоп, вы слышали это?;П,1 – Может поищем ягоды в каком-нибудь другом месте..? Вы не подумайте, я не за себя, за вас беспокоюсь!;П,1 – ...Мистер Старк?;П,1 – Мистер Старк!"


FirstCutscene_TEXT = [FirstCutscene_TEXT_1]
sql.execute('SELECT * FROM FirstCutscene')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO FirstCutscene VALUES (?)', (FirstCutscene_TEXT))
    db.commit()
else:
    print('Уже записывали Первую катсцену.')

FirstPhraseInDange_TEXT_1 = u"П,1 - Так. Только без паники!;П,1 - Мы не на Титанике.;П,3 - А в гребаном космосе... на чужой, заселенной и вероятнее всего враждебной планете...;П,1 - Слава Таносу у меня с собой достаточно картриджей с паутиной.;П,1 - И Брюс дал небольшую справку об обитающих здесь существах... по объему больше напоминающую список покупок...;П,1 - Ладно, Питер, яйца в кулак... Я уже бегу, Мистер Старк!"

FirstPhraseInDange_TEXT = [FirstPhraseInDange_TEXT_1]
sql.execute('SELECT * FROM FirstPhraseInDange')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO FirstPhraseInDange VALUES (?)', (FirstPhraseInDange_TEXT))
    db.commit()
else:
    print('Уже записывали вступительную речь.')
