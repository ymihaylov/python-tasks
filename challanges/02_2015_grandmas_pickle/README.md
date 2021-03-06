Баба прави туршия. От оная де и викат "царска". В една от 18-те "оригинални" рецепти участват следните съставки:
- камби
- карфиол
- моркови
- целина

Баба има 4 купчинки от горните съставки и неизвестен брой буркани. Бурканите са бездънни и безкрайни, поемат всичко що баба реши да натика в тях.

Баба обаче иска да пръсне съставките по специален начин и за това прави следното:

- взима 1 камбa (ако е възможно)
- 2 карфиола (ако / колкото е възможно)
- 4 моркова (ако / колкото е възможно)
- 3 целини (ако / колкото е възможно)
и цикли така последователно през бурканите. В случай, че някоя от съставките свърши - продължава по познатата схема с останалите продукти и така докато продуктите свършат си цикли през бездънните буркани.

Напишете функция:
```
def jars_content(jars, bell_peppers, cauliflowers, carrots, celeries):
    ....
```

На която се подават само стойности от тип int отговарящи съответно на броя буркани / камби / карфиол / моркови и целина и връща списък от итератори, които отговарят на съответното съдържание в бурканите.

Итераторите трябва да връщат стринговете 'bell_pepper', 'cauliflower', 'carrot', 'celery' за съответните неща, които "вадим" от буркана с next. Подредбата вътре в тях няма значение, важно е броя да е коректен.

Пример:

```
jars = jars_content(jars=3, bell_peppers=1, cauliflowers=3, carrots=5, celeries=2)

type(jars)  # => <class 'list'>
jars[0]  #=> <generator object ....>
first_jar = list(jars[0])
second_jar = list(jars[1])
third_jar = list(jars[2])
first_jar.count('bell_pepper')  # 1
first_jar.count('cauliflower')  # 2
first_jar.count('celery')  # 2
second_jar.count('cauliflower')  # 1
second_jar.count('celery')  # 0
len(third_jar)  # 0
```

Третия буркан по схемата на баба остава празен, дано се усети и не го свари.