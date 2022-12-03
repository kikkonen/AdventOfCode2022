from simulate import MatchSimulatorPartOne, MatchSimulatorPartTwo

if __name__ == "__main__":
    simulator_one = MatchSimulatorPartOne()
    simulator_two = MatchSimulatorPartTwo()
    final_score_one = simulator_one.simulate()
    final_score_two = simulator_two.simulate()
    print(final_score_one)
    print(final_score_two)
