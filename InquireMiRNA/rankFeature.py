def rank(n_mirna, rank_list) -> dict:
    mirna_rank = {}
    for i in range(len(rank_list)):
        mirna_rank[n_mirna[i]] = rank_list[i]

    return mirna_rank
