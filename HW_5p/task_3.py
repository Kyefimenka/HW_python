# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком



def get_corteges(languages: list[str]):
    cortege = list(zip(numbers, map(lambda x: x.upper(), languages)))
    return cortege

def get_filtred_cortege(corteges: list[tuple[int, str]]):
    sum_points = list(map(lambda c: sum(map(ord, list(c[1]))), corteges))
    extended_corteges = list(zip(sum_points, corteges))
    filtered_corteges = list(filter(lambda c: c[0] % c[1][0] == 0, extended_corteges))
    filtered_corteges = list(map(lambda c: (c[0],c[1][1] ), filtered_corteges))
    return (sum(map(lambda c: c[0], filtered_corteges)), filtered_corteges)

languages = ['Python', 'Java', 'PHP', 'Swift', 'Go', 'C#']
numbers = list(range(1, len(languages)+ 1))
print(get_corteges(languages))
corteges = get_corteges(languages)
print(get_filtred_cortege(corteges))
