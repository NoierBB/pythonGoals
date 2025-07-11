points = {}
visible = 0

def createNewItem():
    keyOf = input("Введите название цели: ")
    valueOf = input("Дайте описание цели: ")
    points.update({keyOf: valueOf})

while visible !="3":

    print(" 1 Добавить цель\n",          
          "2 Посмотреть цели\n",
          "3 Выйти\n")
    
    visible = input(":::")  

    if(visible == "1"):
        createNewItem()
    elif(visible == "2"):
       for key, value in points.items():
            print(f"{key}: {value}") 
    elif(visible == "3"):
        break
    else:
        print("Нет такой команды")


