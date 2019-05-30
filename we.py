import os

running = True

os.system('taskkill /f /im mpv.exe')

while running:
    print("")
    print("Введите название файла или команду, для списка всех доступных команд введите 'help':")
    file = input()

    if file == "Выход":
        running = False
        os.system('taskkill /f /im mpv.exe')
        print("Выход успешно выполнен")
    elif file == "Выключить":
        os.system('taskkill /f /im mpv.exe')
        continue
    elif file == "help":
        print("Спиок всех доступных команд:")
        print("Выход - выйти из программы и выключить обои")
        print("Выключить - выключить обои")
    elif file == "":
        continue
    else:
        exists = os.path.isfile('wallpapers/{0}.mp4'.format(file))

        if exists:
            id = 'wp id > id.txt'
            os.system(id)

            wpId = open('id.txt')
            wpId = wpId.read()

            cmd = 'wp run mpv --wid={0} wallpapers/{1}.mp4 --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio'.format(wpId, file)

            os.system(cmd)
            continue
        else:
            print("Файл {0}.mp4 не существует".format(file))
            continue