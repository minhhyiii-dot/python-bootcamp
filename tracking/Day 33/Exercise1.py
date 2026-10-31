def record_game(score, player, new_score):
    score.append(new_score)
    player["games_played"] += 1


score = [80, 90]
player = {"name": "MinhYi", "games_played": 2}
new_score = 95

record_game(score, player, new_score)

print(score)
print(player)