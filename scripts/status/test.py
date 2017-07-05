import datetime
def clk():
    today = datetime.datetime.today()
    cal = today.strftime('%m/%d')
    clk = today.strftime('%I:%M')
    return clk

clk = clk()
print(clk)
