# Math Quiz Game by Dohyun Kim

number_1 = int(random(0, 100))
number_2 = int(random(0, 100))
score = 0
mark = score / 20 * 100
answer = number_1 + number_2
button_size = 200
button_x = 400
button_y = 450
page = 1
time_speed = 1.5
time_limit = 0
question = 0

def setup():
    size(800, 650)

def draw():
    background(255)
    # Start button
    fill(255, 0, 0)
    ellipse(button_x, button_y, button_size, button_size)
    # Title
    fill(0)
    textSize(75)
    text("Math Quiz Game", 100, 200)
    text("Start", 315, 475)
    textSize(25)
    text("By. Dohyun Kim", 575, 600)
    if page == 2:
        global time_limit, time_speed, number_1, number_2, score
        fill(255)
        rect(0, 0, 800, 650)
        fill(0)
        textSize(75)
        text(str(number_1) + "+" + str(number_2) + "= ?", 200, 200)
        textSize(40)
        text("Score: " + str(score) + "/10", 550, 50)
        fill(255)
        rect(200, 400, 400, 50)
        fill(100)
        rect(200, 400, time_limit, 50)
        time_limit += time_speed
        global question
        #player_answer = input("Your answer is:")
        fill(0)
        textSize(50)
        #text(str(player_answer), 300, 600)
        if time_limit >= 400:
            time_limit = 0
            fill(0)
            text("Time over", 200, 500)
            number_1 = int(random(0, 100))
            number_2 = int(random(0, 100))
            question += 1
        """
        elif player_answer == answer:
            fill(0)
            text("Correct", 200, 500)
            score += 1
            question += 1
            number_1 = int(random(0, 100))
            number_2 = int(random(0, 100))
        """

        if question >= 10:
            fill(255)
            rect(0, 0, 800, 650)
            fill(0)
            textSize(75)
            text("Your Mark is", 170, 200)
            text(str(int(score) / 10 * 100) + "%", 320, 400)

# def keyTyped():


def mouseClicked():
    global button_size, button_x, button_y, page
    radius = button_size / 2.0
    distance_x = abs(mouseX - button_x)
    distance_y = abs(mouseY - button_y)
    hypotenuse = sqrt(distance_x ** 2 + distance_y ** 2)
    if hypotenuse <= radius:
        page += 1
