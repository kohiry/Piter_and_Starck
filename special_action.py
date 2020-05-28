import starter_obj


def AI():
    for i in starter_obj.enemys:
        i.AI(starter_obj.hero)

def spider_check(screen):  # паучье чутьё
    around = 200
    max_len = 500
    for enemy in starter_obj.enemys:
        if max_len >= abs(enemy.xy[0] - starter_obj.hero.xy[0]) >= around:
            starter_obj.hero.check(screen)
            break



if __name__ == "__main__":
    print('Буду активировать ИИ')
