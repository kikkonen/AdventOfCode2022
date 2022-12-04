from missplaced import MisplacedFinder
from common import CommonItemFinder

if __name__ == '__main__':
    misplaced_finder = MisplacedFinder()
    print(misplaced_finder.get_sum_of_prios_of_all_non_unique_items())
    common_item_finder = CommonItemFinder(group_size=3)
    print(common_item_finder.get_sum_of_prios_of_common_items_per_group())