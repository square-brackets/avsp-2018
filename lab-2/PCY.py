import sys
import time
from itertools import combinations

def count_items(bucket_count):
    # start_time = time.time()
    item_count = {}
    bucket_items = []
    for bucket in range(bucket_count):
        bucket_items_line = sys.stdin.readline()
        bucket_items.append([])
        for item in bucket_items_line.split(' '):
            item_int = int(item)
            item_count[item_int] = item_count.get(item_int, 0) + 1
            bucket_items[bucket].append(item_int)
    # print('[COUNT_ITEMS]: ', time.time() - start_time)
    return item_count, bucket_items

def create_itemsets(buckets_items, itemset_count, item_count, threshold):
    # start_time = time.time()
    itemsets = [0] * itemset_count;
    for bucket_items in buckets_items:
        for itemA, itemB in combinations(bucket_items, 2):
            if item_count[itemA] >= threshold and item_count[itemB] >= threshold:
                k = (itemA * len(item_count) + itemB) % itemset_count
                itemsets[k] += 1;
    # print('[CREATE_ITEMSETS]: ', time.time() - start_time)
    return itemsets


if __name__ == '__main__':
    bucket_count = int(sys.stdin.readline())
    s = float(sys.stdin.readline())
    itemset_count = int(sys.stdin.readline())

    threshold = int(s * bucket_count)
    item_count, buckets_items = count_items(bucket_count)
    itemsets = create_itemsets(buckets_items, itemset_count, item_count, threshold)

    # start_time = time.time()
    pairs = {}
    for bucket_items in buckets_items:
        for itemA, itemB in combinations(bucket_items, 2):
            if item_count[itemA] >= threshold and item_count[itemB] >= threshold:
                k = (itemA * len(item_count) + itemB) % itemset_count
                if (itemsets[k] >= threshold):
                    pairs[(itemA, itemB)] = pairs.get((itemA, itemB), 0) + 1

    # print('[COUNT_PAIRS]: ', time.time() - start_time)

    print(len(list(filter(lambda x: x > 0, itemsets))))
    print(len(pairs))
    for s in sorted(pairs, key=pairs.get, reverse=True):
        print(pairs[s])
