
class example(object):
    def __init__(self, color = ""):
        mem_color = "stop:0 rgba(95, 95, 95, 255), stop:1 rgba(76, 76, 76, 255));"
        net_color = "stop:0 rgba(156, 202, 248, 255), stop:1 rgba(137, 183, 229, 255));"
        if color == "9cf":
            mem_color = "stop:0 rgba(156, 202, 248, 255), stop:1 rgba(137, 183, 229, 255));"
            net_color = "stop:0 rgba(156, 202, 248, 255), stop:1 rgba(137, 183, 229, 255));"
        if color == "lightgrey":
            mem_color = "stop:0 rgba(161, 161, 161, 255), stop:1 rgba(143, 143, 143, 255));"
            net_color = "stop:0 rgba(161, 161, 161, 255), stop:1 rgba(143, 143, 143, 255));"
        if color == "grey":
            mem_color = "stop:0 rgba(95, 95, 95, 255), stop:1 rgba(76, 76, 76, 255));"
            net_color = "stop:0 rgba(95, 95, 95, 255), stop:1 rgba(76, 76, 76, 255));"
        if color == "ff69b4":
            mem_color = "stop:0 rgba(248, 113, 180, 255), stop:1 rgba(230, 95, 162, 255));"
            net_color = "stop:0 rgba(248, 113, 180, 255), stop:1 rgba(230, 95, 162, 255));"

        self.mem_lable = "color:white;background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, "+mem_color+"border-bottom-left-radius:4px;border-top-left-radius:4px"
        self.net_lable = "color:white;background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, "+net_color+"border-bottom-right-radius:4px;border-top-right-radius:4px"
        
