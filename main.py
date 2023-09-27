import os

def EnterNumbers():
    usersArray = []
    for i in range(7):
        number = input(f"Enter a number #{i + 1}: ")
        usersArray.append(number)
    return usersArray

def writeInFile(usersArray):
    with open('file.txt', 'w') as file:
        i = 1
        for item in usersArray:
            file.write(f"{str(item)}")
            if i < 7: file.write(",")
            i += 1
    print("Запись чисел в файл прошла успешно!")

def readNumbers():
    with open("file.txt", 'r') as file:
        data = file.read().split(',')
        return data

def printNumbers(usersArray):
        data = "Вывод чисел с файла:"
        i = 1
        for item in usersArray:
            data += f" {str(item)}"
            if i < 7: data += ","
            i += 1
        print(data)

def sumOfNumbers(usersArray):
    sum = 0
    for item in usersArray:
            sum += int(item)
    print(f"Сумма всех чисел: {str(sum)}")

def sumOfOnlyEvenNumbers(usersArray):
    sumEven = 0
    for item in usersArray:
        if int(item) % 2 == 0:
            sumEven += int(item)
    print(f"Сумма только четных чисел: {str(sumEven)}")

def makeDirectoryOfNumbers(usersArray):
    if not os.path.exists("NUMBERS"):
        os.mkdir("NUMBERS")
    os.chdir("NUMBERS")
    for item in usersArray:
        nameOfFile = str(item) + ".txt"
        with open(nameOfFile, 'w') as file:
            file.write(str(item))
    print("Создание директории с файлами чисел прошло успешно!")

def removeBigFiles(nameOfDirectory = os.path.abspath("NUMBERS")):
    os.chdir(nameOfDirectory)
    files = os.listdir(os.getcwd())
    for item in files:
        pathToItem = os.path.abspath(item)
        fileSize = os.path.getsize(pathToItem)
        if 4 < fileSize:
            os.remove(pathToItem)
            print(f"!Файл '{pathToItem}' был удален из-за привышения размера (4 байта)!")

#==================================MAIN==================================
if __name__ == "__main__":
    # Завдання №1
    array = EnterNumbers()
    writeInFile(array)
    # Завдання №2
    array = readNumbers()
    printNumbers(array)
    sumOfNumbers(array)
    # Завдання №3
    sumOfOnlyEvenNumbers(array)
    # Завдання №4
    makeDirectoryOfNumbers(array)
    # Завдання №5(6)
    removeBigFiles()