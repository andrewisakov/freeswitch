def encode(data):
    if isinstance(data, (datetime.datetime)):
        data = datetime.datetime.strftime(data, '%Y-%m-%d %H:%M:%S')
    return data


def decode(data):
    _result = {}
    for k, v in data.items():
        try:
            _result[k] = datetime.datetime.strptime(v, '%Y-%m-%d %H:%M:%S')
        except Exception as e:
            _result[k] = v
    return _result
