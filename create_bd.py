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
    text_2_end TEXT,
    text_6_end TEXT,
    text_8_end TEXT,
    text_13_end TEXT
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
    text_5 TEXT
    )
""")
db.commit()

# заолнение БД данными по Пауку
SPIDER_TEXT_1 = '''
П - Эй дружок! Я Человек-паук, дружелюбный сосед, залез сюда к вам с мирными намерениями забрать своего папоч- друга, не поможешь мне его найти?;Г - /Злое бурчание/;П - Судя по всему нет...
'''
SPIDER_TEXT_2 = '''
П - Что это у тебя там... Яд?! Как негостеприимно!
'''
SPIDER_TEXT_3 = '''
П - Мы с тобой одной крови - ты и я... Нет? А в мультике сработало... Кинематограф лжёт.
'''
SPIDER_TEXT_4 = '''
П - Хей, мы же братишки-паучишки, так может ты отдашь мне Тони?;Г - /злобное шипение/;П - Ясно, кто-то тут приемный.
'''
SPIDER_TEXT_5 = '''
П - Это потому что у меня всего 2 ноги?! Что с вами не так, гребаные бодишеймеры!
'''
SPIDER_TEXT_6 = '''
П - Мне вот интересно. Ты гриб, которого укусил паук, или паук, которого укусил гриб?
'''
SPIDER_TEXT_7 = '''
П - Без обид, но я обязан отблагодарить вселенную за то, что после укуса не стал таким же красавцем, как ты.
'''
SPIDER_TEXT_8 = '''
П - А у тебя ножки, или ложноножки?;Г - /злобное шипение/;П - Что ж, я пытался завязать наш разговор.
'''
SPIDER_TEXT_9 = '''
П - Это птица? Это самолет? ЭТО ПИЗДЮЛИ!
'''
SPIDER_TEXT_10 = '''
П - Кажется, мне понадобится тапок побольше.
'''
SPIDER_TEXT_11 = '''
П - Хей! Парень, завязывай с этим! Хотя постой, я сам завяжу.
'''
SPIDER_TEXT_12 = '''
Г - /Шипение/;П - Оу, спасибо, это так мило!;Г - /повторное шипение/;П - А. Так это был не комплимент.
'''
SPIDER_TEXT_13 = '''
П - Эти ваши пауки и двух слов связать не могут!
'''
SPIDER_TEXT_14 = '''
П - Снова привет! Как делишки?;Г - /агрессивное шипение/;П - И почему я продолжаю притворяться, что понимаю вас...
'''
SPIDER_TEXT_15 = '''
П - А если ты меня укусишь, я стану двойным человеком-пауком? Человеком-пауком-пауком? Челоуком-пауком?;П - Нет, стой где стоишь, я передумал проверять!
'''
SPIDER_TEXT_16 = '''
П - Каждый раз говорить «инопланетный грибной паук» как-то муторно, давай я буду называть вас... Кевинами?;Г - /шипение/;П - Тебя не спрашивали, Кевин!
'''
SPIDER_TEXT_17 = '''
П - Ни у кого тут нет спрея от жуков?;Г - /шипение/;П - Прости, от арахнидов.
'''
SPIDER_TEXT_13_END = '''
П - Ничего себе, как тебя скрутило! (после)
'''
SPIDER_TEXT_2_END = """
Передохни пока, грубиян. (после)
"""
SPIDER_TEXT_6_END = """
Не волнуйся, оно растворится через пару часов. (после)
"""
SPIDER_TEXT_8_END = """
Знаешь, тебе бы пора перестать себя так накручивать. (после)
"""

SPIDER_TEXT = [SPIDER_TEXT_1, SPIDER_TEXT_2, SPIDER_TEXT_3,
               SPIDER_TEXT_4, SPIDER_TEXT_5, SPIDER_TEXT_6,
               SPIDER_TEXT_7, SPIDER_TEXT_8, SPIDER_TEXT_9, SPIDER_TEXT_10,
               SPIDER_TEXT_11, SPIDER_TEXT_12, SPIDER_TEXT_13, SPIDER_TEXT_14,
               SPIDER_TEXT_15, SPIDER_TEXT_16, SPIDER_TEXT_17,
               SPIDER_TEXT_2_END, SPIDER_TEXT_6_END, SPIDER_TEXT_8_END, SPIDER_TEXT_13_END]
sql.execute('SELECT * FROM spider')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO spider VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (SPIDER_TEXT))
    db.commit()
else:
    print('Уже записывали паука.')

# заолнение БД данными по Тентаклям
MONSTER_TEXT_1 = '''
П - Ну привет... Что-то длинное и вихляющее... Растение? Животное? От чего-то у меня сейчас чутье завопило пониже спины...
'''

MONSTER_TEXT_2 = '''
П - Я все еще не хочу знакомиться с тобой ближе чем на 3 метра.
'''

MONSTER_TEXT_3 = '''
П - Дайте мне подключение к интернету, мини-холодильник и небольшой диван, и я бы с удовольствием обосновался в соседней яме.
'''

MONSTER_TEXT_4 = '''
П - Лови, приятель! Только давай без руко-зачеркнуто-щупальцеприкладства. (кидает ягоду)
'''

MONSTER_TEXT_5 = '''
П - Лови вкусняшку. Эх сейчас бы пиццы... У вас тут случайно нет подземной доставки? (кидает ягоду)
'''

MONSTER_TEXT_6 = '''
П - Твоё любимое, без сахара, соли, и с критическим содержанием фтора. (кидает ягоду)
'''

MONSTER_TEXT_END_1 = """
ЕБ ТВОЮ МААА....(проигрыш, обнуление)
"""

MONSTER_TEXT_END_2 = """
П - ЕБАНЫЙ РОООО… (проигрыш, обнуление)
"""

MONSTER_TEXT_END_3 = """
П - ДРАТЬ МЕНЯ В УХО ТОЛЬКО НЕ СНОВА…  (проигрыш, обнуление)
"""

MONSTER_TEXT = [MONSTER_TEXT_1, MONSTER_TEXT_2, MONSTER_TEXT_3, MONSTER_TEXT_4,
                MONSTER_TEXT_5, MONSTER_TEXT_6, MONSTER_TEXT_END_1, MONSTER_TEXT_END_2, MONSTER_TEXT_END_3]
sql.execute('SELECT * FROM monster')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO monster VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (MONSTER_TEXT))
    db.commit()
else:
    print('Уже записывали тентакли.')

# заолнение БД данными по ежу
HENDEHOG_TEXT_1 = "Что-то мне подсказывает, что лучше не приземляться на эту штуковину..."
HENDEHOG_TEXT_END_1 = 'Я чувствую уколы совести за то, что упустил мистера Старка. Ай! Или не совести. (укол) '
HENDEHOG_TEXT_END_2 = 'Ау-ау-ау! Колкости в сторону, сударь! (укол)'
HENDEHOG_TEXT_END_3 = 'Да кто тут раскидал эти штуки?! (укол) *смех розовой чайки неподалёку*'
HENDEHOG_TEXT_END_4 = 'В следующий раз я прилечу сюда с лопатой и садовыми ножницами! (укол)'

HENDEHOG_TEXT = [HENDEHOG_TEXT_1, HENDEHOG_TEXT_END_1, HENDEHOG_TEXT_END_2, HENDEHOG_TEXT_END_3,
                HENDEHOG_TEXT_END_4]
sql.execute('SELECT * FROM Hedgehog')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO Hedgehog VALUES (?, ?, ?, ?, ?)', (HENDEHOG_TEXT))
    db.commit()
else:
    print('Уже записывали ежа.')

# заолнение БД данными по ежу
FirstCutscene_TEXT_1 = u"""
ЖДавай, Паучок, только здесь мы не смотрели, тут точно должны быть эти ягоды. Если мы не притащим их здоровяку, в сыворотку покрошат уже нас. Погнали, путешествие на 5 минут, зашли и вышли.;П – Вы как будто в спальню меня зовете, а не в пещеру, ха-ха-ха :D;Ж – Нос клоунский сними, юморист. Давай-ка посерьезнее и пошли.;П – Ну не знаю, мистер Старк, эта пещера выглядит зловеще...;П - Стоп, вы слышали это? \оглядывается\ Может поищем ягоды в каком-нибудь другом месте..? Вы не подумайте, я не за себя, за вас беспокоюсь!;П- ...мистер Старк? \Старк исчез\\
"""


FirstCutscene_TEXT = [FirstCutscene_TEXT_1]
sql.execute('SELECT * FROM FirstCutscene')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO FirstCutscene VALUES (?)', (FirstCutscene_TEXT))
    db.commit()
else:
    print('Уже записывали Первую катсцену.')

FirstPhraseInDange_TEXT_1 = u"П- Так. Только без паники!; П- Мы не на Титанике.; П- А в гребаном космосе... на чужой, заселенной и вероятнее всего враждебной планете...; П- Слава Таносу у меня с собой достаточно картриджей с паутиной.; П- И Брюс дал небольшую справку об обитающих здесь существах... по объему больше напоминающую список покупок ...; П- Ладно, Питер, яйца в кулак... Я уже бегу, Мистер Старк!"

FirstPhraseInDange_TEXT = [FirstPhraseInDange_TEXT_1]
sql.execute('SELECT * FROM FirstPhraseInDange')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO FirstPhraseInDange VALUES (?)', (FirstPhraseInDange_TEXT))
    db.commit()
else:
    print('Уже записывали вступительную речь.')
