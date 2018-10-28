import sys
import math

buckets = []
bucket_timestamps = []

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    max_bucket_size_potention = int(math.log(n, 2) + 1)
    bucket_sizes = [2**x for x in range(max_bucket_size_potention)]

    for line in sys.stdin.read().splitlines():
        if line.startswith('q'):
            k = int(line.split(' ')[1])

            isFirst = True
            total = 0

            for i in range(len(bucket_timestamps)):
                if bucket_timestamps[i] < k:
                    factor = 1
                    if isFirst:
                        isFirst = False
                        factor = 0.5

                    total += buckets[i] * factor

            print(int(total))
        else:
            for bit in line:
                bucket_timestamps = [bucket_timestamp + 1 for bucket_timestamp in bucket_timestamps]

                if len(bucket_timestamps) > 0 and bucket_timestamps[0] >= n:
                    bucket_timestamps.pop(0)
                    buckets.pop(0)

                if bit == '1':
                    buckets.append(1)
                    bucket_timestamps.append(0)

                    for bucket_size in bucket_sizes:
                        if buckets.count(bucket_size) == 3:
                            [first_bucket_index, second_bucket_index, _] = [k for k, bucket in enumerate(buckets) if bucket == bucket_size]
                            buckets[second_bucket_index] = bucket_size * 2

                            buckets.pop(first_bucket_index)
                            bucket_timestamps.pop(first_bucket_index)
