import pandas as pd

dataset = pd.read_csv('nb_test.csv',sep='\t')
print(dataset)

# 외출할 확률: p(go_out)
p_go_out = 5/10

# 집에 머물러 있을 확률: P(stay_home)
p_stay_home = 5/10  # P(stay_home) = 1 - P(go_out)

# 외출했을 때 날씨가 맑을 확률: P(sunny|go_out)
p_sunny_when_go_out = 4/5
# 외출했을 때 날씨가 맑을 확률: P(sunny|go_out)
p_rainy_when_go_out = 1/5

# 외출했을 때 자동차가 정상일 경우: P(working|go_out)
p_working_when_go_out = 4/5