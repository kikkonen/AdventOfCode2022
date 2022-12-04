from find import OverlapFinder

if __name__ == '__main__':
    finder = OverlapFinder()
    print(finder.get_number_of_pairs_that_fully_overlap())
    print(finder.get_number_pairs_that_overlap())