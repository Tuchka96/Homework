#<span>5&nbsp;128&nbsp;P</span>
prize = input()
prize = prize.replace("<span>", "")
prize = prize.replace("</span>", "")
prize = prize.replace("&nbsp;", "")
prize = prize.replace("P", "")
print(prize)