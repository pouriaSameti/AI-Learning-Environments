import pygame
from environment import PygameInit, AngryBirds

if __name__ == "__main__":

    FPS = 2
    env = AngryBirds()
    screen, clock = PygameInit.initialization()
    state = env.reset()

    for _ in range(5):
        episode_reward = 0
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            env.render(screen)

            # extract action from policy
            action = 1
            next_state, probability, reward, done = env.step(action)
            episode_reward += reward

            if done:
                print(f"Episode finished with reward: {episode_reward}")
                state = env.reset()

            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()


