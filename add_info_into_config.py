def main(text):
    with open('config.txt', 'w') as f:
        f.write(text)


if __name__ == '__main__':
    main('test')
