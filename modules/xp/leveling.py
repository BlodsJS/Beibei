import bisect


class LevelHandler:
    rates = {range(1, 26): 20, range(26, 51): 20, range(51, 101): 35}

    ordened_intervals = sorted(
        [(r.start, r.stop, v) for r, v in rates.items()], key=lambda x: x[0]
    )
    initial = [interval[0] for interval in ordened_intervals]
    final = [interval[1] for interval in ordened_intervals]
    values = [interval[2] for interval in ordened_intervals]

    @classmethod
    def get_rate(cls, level):

        idx = bisect.bisect_right(cls.initial, level) - 1

        if idx >= 0 and level < cls.final[idx]:
            return cls.values[idx]

        return 100

    @classmethod
    def required_xp(cls, level):

        rate = cls.get_rate(level)

        return (level**2) * rate + 100
