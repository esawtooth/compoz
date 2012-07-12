class FreqOutOfBoundsException(Exception):
    def __init__(self, freq):
        self.freq = freq
    def __str__(self):
            return repr(self.freq)

class InvalidTuningException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "Invalid Tuning"

class Tuning:
    """Base class describing a tuning"""
    
    """
       This is a map of all frequencies used in this tuning.
       It looks like notation => frequency (float)
    """
    __freq_map = {}
    __zero_freq = 0

    """
       Hardcoded here in Hz. TODO: Figure out a way to make this
       configurable
    """
    __HEARING_MIN = 20.0
    __HEARING_MAX = 20000.0
    __enable_hearing_limits_check = True

    """
       This function needs to do some validation of the freq map
       freq_map: map of tuning frequencies. Assume zero_freq is min freq
    """
    def __init__(self, freq_map, enable_hearing_limits_check = True):
        self.__freq_map = freq_map
        self.__enable_hearing_limits_check = enable_hearing_limits_check

        if (len(self.__freq_map) <= 1):
            raise InvalidTuningException

        # Check if all freq are sane
        for note in self.__freq_map:
            if not (self.__freq_map[note] > 0):
                raise FreqOutOfBoundsException(self.__freq_map[note])

        # Check if all freq values are wihin hearing range
        if self.__enable_hearing_limits_check is True:
            for note in self.__freq_map:
                if not ((self.__freq_map[note] >= self.__HEARING_MIN) and
(self.__freq_map[note] <= self.__HEARING_MAX)):
                    raise FreqOutOfBoundsException(self.__freq_map[note])
    
        # Calculate zero_freq
        self.__zero_freq = min(self.__freq_map.items(), key=lambda x:x[1])[0]
    
    def __str__(self):
        return "Zero freq:" + str(self.__freq_map[self.__zero_freq])

    def getTuningOrder(self):
        return len(__freq_map)

# Just for sanity testing. Get rid ASAP
if __name__ == "__main__":
    print Tuning({"a":440,"b":568})
