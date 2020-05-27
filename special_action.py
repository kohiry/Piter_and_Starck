import starter_obj


def AI():
    for i in starter_obj.enemys:
        i.AI(starter_obj.hero)


if __name__ == "__main__":
    print('Буду активировать ИИ')
