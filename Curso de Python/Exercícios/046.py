import emoji
from time import sleep
print("Prepare-se para a contagem de 10 segundos")
sleep(3)
for contador in range(10, -1, -1):
    print(contador)
    sleep(1)
print("\033[31mBUUUUUUMMMMMM!!!!!\033[m", end = '')
print(emoji.emojize(":collision: "*3))
