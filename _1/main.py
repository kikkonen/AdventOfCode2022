from calories import CaloriesCounter

if __name__ == "__main__":
    calories_counter = CaloriesCounter()
    top_elves = calories_counter.get_top_n_elves_with_most_calories(3)
    print(top_elves)
    print(sum([elf.calories for elf in top_elves]))
