from multiprocessing import Pool
from multiprocessing.pool import ApplyResult
import time
from functools import partial

def square(number):
    """计算一个数的平方"""
    print(f"计算 {number} 的平方")
    time.sleep(1)  # 模拟耗时操作
    if number % 10 == 9:
        raise Exception("sssssssssss")
    # return number * number

def task_error(pool, number, error):
    print(f"Work {number} exist with error: {error}")
    pool.terminate()

if __name__ == "__main__":
    # 创建任务并等待完成
    results: dict[str, ApplyResult] = {}
    pool = Pool(3)
    for work in range(100):
        error_cb = partial(task_error, pool, work)
        result = pool.apply_async(square, args=(work, ), error_callback=error_cb)
        results[work] = result
    # 检查任务结果
    pool.close()
    pool.join()
    # print("xxxxxxxxxxxxxxxxxx")
    # time.sleep(100)
    for number, result in results.items():
        try:
            if not result.ready():
                succ = False
            else:
                result.get()
        except Exception as e:
            print(f"任务{number}执行异常: {str(e)}")
            succ = False

