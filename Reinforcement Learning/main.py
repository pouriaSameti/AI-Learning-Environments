import numpy as np
import pygame
from environment import UnknownAngryBirds, PygameInit


if __name__ == "__main__":

    env = UnknownAngryBirds()
    screen, clock = PygameInit.initialization()
    FPS = 4

    episode_reward = []
    for _ in range(5):

        running = True
        total_reward = 0
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            env.render(screen)

            # random policy
            action = np.random.choice([0, 1, 2, 3])
            next_state, reward, pig_state, done = env.step(action)
            print(pig_state)
            state = next_state
            total_reward += reward

            if done:
                print(f"Episode finished with reward: {total_reward}")
                state = env.reset()
                episode_reward.append(total_reward)
                total_reward = 0
                running = False

            pygame.display.flip()
            clock.tick(FPS)

    print(f'MEAN REWARD: {sum(episode_reward)/len(episode_reward)}')

    pygame.quit()
