class AnalogicMap:
    """
       create_map = AnalogicMap()
       print(create_map.create_map(x, 0, 64300, 0, 100))
    """
    def __init__(self, return_float=False):
        self._return_float = return_float

    def create_map(
        self,
        x,
        in_min,
        in_max,
        out_min,
        out_max
    ):
        
        _value_map = (
            (x-in_min)*(out_max-out_min)/(in_max - in_min)+out_min
        )
        return _value_map if self._return_float else int(_value_map)

def hex_to_rgb(value):
        _value = value.strip().replace('#', '')
        _rgb = len(_value)
        if _rgb != 6:
            raise ValueError(f'The hex color #{value} is not valid')
        return tuple(int(_value[i:i+_rgb//3], 16) for i in range(0, _rgb, _rgb//3))
