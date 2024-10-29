import random

team_hp = [random.random(), random.random(), random.random(), random.random(), random.random()]

sum, wsum = 0, 0
for i, hp in enumerate(team_hp):
    if i == 0:
        if hp > 0.8:
            w = 1.0
        else:
            w = 1.2
    elif i == 1:
        w = 1.1
    else:
        w = 1.0

    if hp <= 0.1:
        w *= 3.0
    elif hp <= 0.3:
        w *= 2.0
    elif hp <= 0.5:
        w *= 1.5

    wsum += w
    sum += hp * w

score = 100 * sum / wsum

print(f"tank: {team_hp[0]}")
print(f"self: {team_hp[1]}")
print(f"teammates: {team_hp[2:]}")
print(f"score: {score}")