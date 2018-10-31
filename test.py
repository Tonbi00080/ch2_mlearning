def _range(_min, args=None):
    _max, _step = None, None
    if args:
        if not isinstance(args, int):
            _max, _step = map(int, args.split(','))
        else:
            _max = args
    #filterの第一引数noneだと第二引数そのまま入る
    args = filter(None, (_min,_max,_step))
    return range(*args)

print(range(3))
