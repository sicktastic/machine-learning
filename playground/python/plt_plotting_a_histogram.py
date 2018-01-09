import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

_ = plt.hist(df_swing['dem_share'], bins=20)

_ = plt.xlabel('percent of vote for Obama')

_ = plt.ylabel('number of countrires')

plt.show()
