import random
import plotly.express as px

dice_result = []
count = []

for r in range(0, 100):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_result.append(dice_1 + dice_2)
    count.append(r)

fig = px.bar(x = dice_result, y = count)
fig.show()

print(dice_result)
print(count)