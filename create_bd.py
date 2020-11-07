import sqlite3

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
    text_2_end TEXT,
    text_6_end TEXT,
    text_8_end TEXT
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
    text_end TEXT
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
Эй дружок! Я Человек-паук, дружелюбный сосед, залез сюда к вам с мирными намерениями забрать своего -папочку- друга, не поможешь мне его найти?;/Злое бурчание/;Судя по всему нет...
'''
SPIDER_TEXT_2 = '''
Что это у тебя там... Яд?! Как негостеприимно!
'''
SPIDER_TEXT_3 = '''
Ты и я: одной крови!... Нет? А в мультике сработало... Кинематограф нам лжёт.
'''
SPIDER_TEXT_4 = '''
Хей, мы же братишки-паучишки, так может ты отдашь мне Тони?;/злобное шипение/;Ясно, кто-то тут приемный.
'''
SPIDER_TEXT_5 = '''
Это потому что у меня всего 2 ноги?! Что с вами не так, гребаные бодишеймеры!
'''
SPIDER_TEXT_6 = '''
Кто-то сейчас будет ласково закутан в одеялко... из паутины!
'''
SPIDER_TEXT_7 = '''
- Без обид, но я обязан отблагодарить вселенную за то, что после укуса не стал таким же красавцем, как ты.
'''
SPIDER_TEXT_8 = '''
Это птица? Это самолет? Это пиздюли!
'''
SPIDER_TEXT_9 = '''
Оу, мне кажется, понадобится тапок побольше.;
'''
SPIDER_TEXT_10 = '''
*Получил немного по жопе*;Хей! Парень, завязывай с этим! Хотя, я сам завяжу.;*Стреляет паутиной*
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
               SPIDER_TEXT_2_END, SPIDER_TEXT_6_END, SPIDER_TEXT_8_END]
sql.execute('SELECT * FROM spider')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO spider VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (SPIDER_TEXT))
    db.commit()
else:
    print('Уже записывали паука.')

# заолнение БД данными по Тентаклям
MONSTER_TEXT_1 = '''
Ну привет... Что-то длинное и вихляющее... Растение? Животное? От чего-то у меня сейчас чутье завопило пониже спины...
'''

MONSTER_TEXT_2 = '''
Держи, это должно тебе понравится... только не ешь меня... или что ты там собирался делать... бррр (кидает ягоду)
'''

MONSTER_TEXT_3 = '''
Лови вкусняшку. Эх сейчас бы пиццы... У вас тут случайно нет подземной доставки? (кидает ягоду)
'''

MONSTER_TEXT_4 = '''
Твоё любимое, без сахара, соли, и с критическим содержанием фтора. (кидает ягоду)
'''

MONSTER_TEXT_5 = '''
Твоё любимое, без сахара, соли, и с критическим содержанием фтора. (кидает ягоду)
'''

MONSTER_TEXT_END = """
ЕБ ТВОЮ МААА....(проигрыш, обнуление)
"""

MONSTER_TEXT = [MONSTER_TEXT_1, MONSTER_TEXT_2, MONSTER_TEXT_3, MONSTER_TEXT_4,
                MONSTER_TEXT_5, MONSTER_TEXT_END]
sql.execute('SELECT * FROM monster')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO monster VALUES (?, ?, ?, ?, ?, ?)', (MONSTER_TEXT))
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
FirstPhraseInDange_TEXT_1 = r"""
- Давай, паучок, только здесь мы еще не смотрели, тут точно должны быть эти ягоды, наша зеленая принцесса не простит мне если я не принесу их для его исследований. Погнали, путешествие на 5 минут, зашли и вышли.;- Ну не знаю, мистер Старк, эта пещера выглядит довольно зловеще... Вы слышали стрекотание? \оглядывается\ Может мы поищем эти ягоды на каких-то других, более дружелюбного вида... Мистер Старк??? \Старк исчез\
"""


FirstPhraseInDange_TEXT = [FirstPhraseInDange_TEXT_1]
sql.execute('SELECT * FROM FirstPhraseInDange')
if sql.fetchone() is None:
    sql.execute(f'INSERT INTO FirstPhraseInDange VALUES (?)', (FirstPhraseInDange_TEXT))
    db.commit()
else:
    print('Уже записывали Первую катсцену.')
