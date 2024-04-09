from pyvirtualdisplay import Display
import gym
import matplotlib.pyplot as plt


# display = Display(visible=False, size=(1400, 900))
# _ = display.start()


env = gym.make("CartPole-v1")
env.reset()
print(env)
print(env.render('rgb_array'))
img = plt.imshow(env.render('rgb_array'))
print(img)
