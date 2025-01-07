# Домашнее задание по теме "Валидация данных"

Цель: научится писать необходимую валидацию для вводимых данных при помощи классов Path и Annotated.

Задача "Аннотация и валидация":

Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated:

'/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id, для которого необходимо написать следующую валидацию:

1. Должно быть целым числом

2. Ограничено по значению: больше или равно 1 и меньше либо равно 100.

3. Описание - 'Enter User ID'

4. Пример - '1' (можете подставить свой пример не противоречащий валидации)

'/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту, принимает аргументы username и age, для которых необходимо написать следующую валидацию:

1. username - строка, age - целое число.

2. username ограничение по длине: больше или равно 5 и меньше либо равно 20.

3. age ограничение по значению: больше или равно 18 и меньше либо равно 120.

4. Описания для username и age - 'Enter username' и 'Enter age' соответственно.

5. Примеры для username и age - 'UrbanUser' и '24' соответственно. (можете подставить свои примеры не противоречащие валидации).

Пример результата выполнения программы:

Ошибки валидации для маршрутов '/user/{user_id}' и '/user/{username}/{age}' :

![image](https://github.com/user-attachments/assets/eff23b12-b620-4d54-848e-15e22df405d5)

Как должен выглядеть Swagger:

![image](https://github.com/user-attachments/assets/907c7aef-5bb5-4021-b13f-c3ffc30a651d)
![image](https://github.com/user-attachments/assets/7c67e414-f2f6-49eb-9cb7-3ad60dd2abbf)

Примечания:

Если у вас не отображаются параметры Path, проверьте, сделали вы присвоение данных или подсказку типа.
Верно: username: Annotated[...].
Не верно: username = Annotated[...]
