import os
import time

print("Running", os.path.basename(__file__))


def run(limit=1e6):
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
