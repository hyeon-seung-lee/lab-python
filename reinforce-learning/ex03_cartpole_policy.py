import gym
import random
import numpy as np


def random_policy():
    """ 0 또는 1을 무작위로 생성해서 리턴"""
    return random.randint(0, 1)

def basic_policy(observation):
    """관측치(observation) 중에서 막대가 기울어진 각도에 따라서
    각도 > 0 이면 +1
    각도 < 0 이면 -1 을 return
    obs: [x, v, theta(각도), w각속도]
    """
    angle =observation[2]
    if angle>0:
        action = 1
    else:
        action = 0
    return action

if __name__ == '__main__':
    env = gym.make("CartPole-v1")  # 환경(env) 생성
    max_episodes = 100

    # episode = 막대가 넘어지기 전까지(done == false)
    max_steps = 1000  # 에피소드 하나에서 최대 반복 회수

    total_rewards = []  # 에피소드가 끝날 때마다 rewards를 보상할 리스트
    for episode in range(max_episodes):  # 게임 실행 회수만큼 반복
        print(f' == Episode  #{episode+1} ==')
        obs = env.reset()  # 게임 환경(env) 초기화
        episode_rewards = 0  # 에피소드 하나에서 얻은 보상점수
        for step in range(max_steps):  # 각 에피소드마다 최대 회수만큼 반복
            env.render()  # 게임 화면 출력(렌더링)
            action = basic_policy(obs)
            obs, reward, done, info = env.step(action)  # 게임 상태 변경
            episode_rewards += reward  # 해당 에피소드의 보상을 더함
            if done:
                print(f'Episode finished after {step + 1} steps')
                break
        total_rewards.append(episode_rewards)
    env.close()
    # 보상(점수)들의 리스트의 평균, 표준편차, 최댓값, 최솟값
    print(f'mean: {np.mean(total_rewards)}')
    print(f'std: {np.std(total_rewards)}')
    print(f'max: {np.max(total_rewards)}')
    print(f'min: {np.min(total_rewards)}')

