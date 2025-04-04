from collections import deque


def create_rankings(prefs):
    n = len(prefs)
    ranking = [[0] * n for _ in range(n)]  # Ranking[w, m]
    for w in range(n):
        for pref, m in enumerate(prefs[w]):
            ranking[w][m] = pref
    return ranking


def gale_shapley(men_prefs, women_prefs):
    """
    Gale-Shapley Algorithm

    Suggested implementation from "Algorithm Design - Jon Kleinberg & Éva Tardos":

    1. Identify a free man.
        - Free man will be kept in a linked list:
            - Delete m if he gets engaged
            - If some other man m' becomes free, insert at the front of the list
    2. A man should be able to identify the highest ranking woman he has not yet proposed.
        - Array Next that indicates for each man m the position of the next woman he will propose on his list.
        Next[m] <- Next[m] + 1; after proposal.
    3. For a woman w, we need to decide if w is currently engaged, and if so, identify her partner.
        - Array Current to identify the man m' that w is engaged.
        Current[w] <- Null when she is not engaged.
    4. For a woman w and two men m and m', we need to be able to decide, at runtime, which of the men is preferred by w.
        - Array Ranking n x n containing the rank of man m in the sorted order of w's preferences.
        To decide which of m or m' is preferred by w, Ranking[w, m] and Ranking[w, m'] are compared.
    """

    n = len(men_prefs)

    free_men = deque(range(n))  # Free man

    next_proposal = [0] * n  # Next woman to propose
    current = [None] * n  # None = not engaged

    ranking = create_rankings(women_prefs)

    while free_men:
        # Select a free man
        m = free_men.popleft()

        # Check next proposal of m
        w = men_prefs[m][next_proposal[m]]
        next_proposal[m] = next_proposal[m] + 1

        # Check if w is engaged
        engaged = current[w]
        if engaged is not None:  # if engaged
            # change engagement if the rank of the man that is
            # engaged to w is smaller than the free man proposing
            if ranking[w][engaged] < ranking[w][m]:
                current[w] = m
                free_men.append(engaged)  # engaged man is now free again
            else:
                free_men.append(m)  # stays free
        else:  # since w was alone, she engages with m
            current[w] = m

    return current


if __name__ == '__main__':
    import random
    import statistics
    
    random.seed(42)
    
    n = 1000
    women_prefs = [random.sample(range(n), n) for _ in range(n)]
    men_prefs = [random.sample(range(n), n) for _ in range(n)]
    
    matches = gale_shapley(men_prefs=men_prefs, women_prefs=women_prefs)
    
    # See if the algorithm is better for men or for women
    ranking_men = create_rankings(men_prefs)
    ranking_women = create_rankings(women_prefs)
    
    scores_men = [0] * n
    scores_women = [0] * n
    for w, m in enumerate(matches):
        scores_men[m] = ranking_men[m][w]
        scores_women[w] = ranking_women[w][m]
        # print(f'Match (m, w): {(m, w)} - Index in ranking: ({ranking_men[m][w]}, {ranking_women[w][m]})')
    
    print(f'Men score median: {statistics.median(scores_men)}; Women: {statistics.median(scores_women)} -- (closer to 0 is better)')
    print(f'Men score mean: {statistics.mean(scores_men)}; Women: {statistics.mean(scores_women)} -- (closer to 0 is better)')
