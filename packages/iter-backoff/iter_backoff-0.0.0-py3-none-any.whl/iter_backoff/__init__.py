# ループによる指数バックオフ [iter_backoff]

import sys
import time

# ループによる指数バックオフ [iter_backoff]
def iter_backoff_func(
	s0,	# 初回待機時間 (秒単位)
	r,	# 待機時間の延伸倍率
	n	# 最大試行回数
):
	yield 0
	wait_t = s0
	for idx in range(1, n):
		time.sleep(wait_t)
		wait_t *= r
		yield idx

# モジュールを関数と同一視
sys.modules[__name__] = iter_backoff_func
