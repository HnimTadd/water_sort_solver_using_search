from termcolor import colored
Color = {
    '0': "  ",
    '1': colored("██", "red"),
    '2': colored("██", "white"),
    '3': colored("██", "green"),
    '4': colored("██", "blue"),
    '5': colored("██", "magenta"),
    '6': colored("██", "cyan"),
    '7': colored("██", "grey")
}


class Tube:
    color = []
    volume = 0

    def __init__(self, color_tube, tube_volume) -> None:
        """class represent water tube in watersort game

        Args:
            color_tube (list[int]): list of color code
            tube_volume (int): volume of tube
        """
        self.color = color_tube
        self.volume = tube_volume

    def get_current_volume(self):
        return len(self.color)

    def get_remain_volume(self):
        return self.volume - self.get_current_volume()

    def get_volume(self):
        return self.volume

    def get_last_color_volume(self):
        if self.get_last_color_code() != 0:
            i = self.get_current_volume() - 1
            res = 1
            while i > 0 and self.color[i] == self.color[i - 1]:
                res += 1
                i -= 1
            return res
        return 0

    # Get last color code, if there is no last color, return 0
    def get_last_color_code(self):
        if self.get_current_volume() != 0:
            return self.color[-1]
        else:
            return 0

    def get_copy(self):
        return Tube(self.color[:], self.volume)

    # def get_validate

    def is_goal(self):
        """check if tube contains only one color water, or no water at all.
        Returns:
            Bool: True if tube is goal. 
        """
        if 0 < self.get_remain_volume() < self.get_volume():
            return False
        for i in range(self.get_current_volume() - 1):
            if self.color[i] != self.color[i + 1]:
                return False
        return True

    def __eq__(self, tube):
        if self.get_volume() != tube.get_volume():
            return False
        if self.get_remain_volume() != tube.get_remain_volume():
            return False
        for i in range(self.get_current_volume()):
            if self.color[i] != tube.color[i]:
                return False
        return True

    # def get_cost(self):
    #     res = 0
    #     for i in range(self.get_current_volume() - 1):
    #         if self.color[i] != self.color[i+1]:
    #             res += (i+1)
    #         else:
    #             res -= self.get_volume() - i - 1
    #     return res

    def get_cost(self):
        """tube.get_cost: get cost of tube, calculate by sum all color block with different color code

        Returns:
            int: number of all color block with different color code
        """        
        res = 0
        for i in range(self.get_current_volume() - 1):
            if self.color[i] != self.color[i + 1]:
                res += 1
            else:
                res -= 1
        return res

    def get_full_tube(self):
        c_tube = self.color[:]
        n = self.get_remain_volume()
        while n > 0:
            c_tube.append(0)
            n -= 1
        return c_tube

    def __str__(self):
        c_tube = self.get_full_tube()
        return "Tube: [" + ",".join([str(i) for i in c_tube]) + "]"

    # def print_tube(self):
    #     print(self.get_full_tube())

    def print_info(self):
        print("Tube volume: " + str(self.get_volume()))
        print("Tube remain volume: " + str(self.get_remain_volume()))
        x = ""
        print(self.color)
        tubes = self.get_full_tube()
        for i in tubes:
            x = "|" + Color[str(i)] + "|" + "\n" + x
        print(x)
        # print("\n".join([Color[str(i)]] for i in self.color))

    def poor(self, color_code, volume):
        if self.get_current_volume() == 0 and volume > 0:
            while self.get_remain_volume() > 0 and volume > 0:
                volume -= 1
                self.color.append(color_code)
            return self
        elif color_code == self.get_last_color_code():
            if volume > 0:
                while self.get_remain_volume() > 0 and volume > 0:
                    volume -= 1
                    self.color.append(color_code)
                return self
            else:
                while self.get_current_volume() > 0 > volume:
                    volume += 1
                    self.color.pop()
                return self
        else:
            return self

    def poor_to(self, tube, volume):
        self_color_code = self.get_last_color_code()
        poor_in_volume = volume
        poor_out_volume = - volume
        self.poor(self_color_code, poor_out_volume)
        tube.poor(self_color_code, poor_in_volume)

    def check_can_poor(self, tube):
        if (tube.get_remain_volume() == 0
                or self.get_remain_volume() == tube.get_volume()
                or self.get_remain_volume() == self.get_volume()):
            return False, None
        color_code = tube.get_last_color_code()
        self_color_code = self.get_last_color_code()
        if color_code == 0 or color_code == self_color_code:
            volume = self.get_last_color_volume()
            poor_in_volume = volume
            if volume > tube.get_remain_volume():
                poor_in_volume = tube.get_remain_volume()
            return True, poor_in_volume
        return False, None
