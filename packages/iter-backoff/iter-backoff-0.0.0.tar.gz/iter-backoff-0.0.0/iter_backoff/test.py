# ループによる指数バックオフ [iter_backoff]
# 【動作確認 / 使用例】

import sys
import ezpip
import random
iter_backoff = ezpip.load_develop("iter_backoff", "../", develop_flag = True)

# ループによる指数バックオフ [iter_backoff]
for _ in iter_backoff(s0 = 0.5, r = 2, n = 4):
	if random.random() < 1/4:
		print("成功！")
		break
	else:
		print("失敗！")
