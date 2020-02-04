import gym
import numpy as np

if __name__ == '__main__':
    # game environement 생성
    env = gym.make('CartPole-v1')

    # 게임 환경 초기화
    obs = env.reset()
    # 초기 화면 출력
    env.render()
    print(obs)

    # 최대 반복 회수
    max_steps = 1000
    # for문 반복할 때마다 action 값이 0 또는 1을 랜덤하게 반복하도록
    # done 값이 True 이면 for loop를 종료하도록
    # 몇 step만에 종료되었는지 출력
    steps = 0

    print('---------------------')
    for t in range(max_steps):
        action = np.random.randint(0, 2)  # 게임 액션 설정
        obs, reward, done, info = env.step(action)

        env.render()  # 게임 환경 화면 출력
        print(obs)
        print(f'reward: {reward}, done: {done}, info: {info}')
        steps = t
        if done:
            break
    print('Num of loop:', steps+1)
    env.close()
