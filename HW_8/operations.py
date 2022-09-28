header = ['ID', 'FirstName', 'LastName', 'tel1', 'tel2']


def convert_list_to_dics(data: list[list[str]]) -> list[dict[str, str]]:
    return list(map(lambda row: dict(zip(header, row)), data))

def convert_dics_to_list(data: list[dict[str, str]]) -> list[list[str]]:
    return list(map(lambda dic: list(dic.values()), data))