TINY_WAIT = 1
SMALL_WAIT = 3
MEDIUM_WAIT = 5
BIG_WAIT = 10
SECURITY_WAIT = 15
BATTLE_FINISH_DETECT = 12
BATTLE_NONE_DETECT_TIME = 90

BATTLE_END_SIGNAL_MAX_EXECUTE_TIME = 15

# 关键动作的偏移
FLAGS_START_BATTLE_BIAS = (50, 25)
FLAGS_ENSURE_TEAM_INFO_BIAS = (25, 50)

# 正方形偏移
FLAGS_CLICK_BIAS_TINY = (3, 3)
FLAGS_CLICK_BIAS_SMALL = (5, 5)
FLAGS_CLICK_BIAS_MEDIUM = (10, 10)
FLAGS_CLICK_BIAS_BIG = (15, 15)
FLAGS_CLICK_BIAS_HUGE = (30, 30)

# 拖动偏移
# 用于左右拖动的偏移，也就是偏移初始坐标点
FLAGS_SWIPE_BIAS_TO_LEFT = ((1, 1), (1, 1))
FLAGS_SWIPE_BIAS_TO_RIGHT = ((1, 1), (1, 1))
