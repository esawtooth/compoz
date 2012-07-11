class FreqOutOfBoundsException(Exception):
    def __init__(self, freq):
        self.freq = freq
    def __str__(self):
            return repr(self.freq)

class Tuning:
    """Base class describing a tuning"""
    
    """
       This is a map of all frequencies used in this tuning.
       It looks like notation => frequency (float)
       The first frequency is expected to be "zero"
    """
    __freq_map = {}

    """
       Hardcoded here in Hz. TODO: Figure out a way to sanitize this
    """
    __HEARING_MIN = 20.0
    __HEARING_MAX = 20000.0
    __enable_hearing_limits_check = True

    """
       This function needs to do some validation of the freq map
    """
    def __init__(self, freq_map, enable_hearing_limits_check = True):
        self.__freq_map = number_freq
        self.__enable_hearing_limits_check = enable_hearing_limits_check
        # Check if all freq are sane
        for note in self.__freq_map:
            if not (self.__freq_map[note] > 0):
                raise FreqOutOfBoundsException(self.__freq_map[note])

        # Check if all freq values are wihin hearing range
        if __enable_hearing_limits_check is True:
            for note in self.__freq_map:
                if not ((self.__freq_map[note] >= self.__HEARING_MIN) and
(self.__freq_map[note] <= self.__HEARING_MAX)):
                    raise FreqOutOfBoundsException(self.__freq_map[note])
