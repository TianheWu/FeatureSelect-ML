def func_buildDict(x, count=0) -> dict:
    # miRNA -> No. string -> int
    mirna_n = {}
    # No. -> miRNA int -> string
    n_mirna = {}

    for i in x:
        mirna_n[i] = count
        n_mirna[count] = i
        count += 1

    return mirna_n, n_mirna





