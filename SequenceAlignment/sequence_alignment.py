def sequence_alignment(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    gap_penalty = -2
    match_penalty = 1
    mismatch_penalty = -2

    decision_matrix = [[' ' for _ in range(m + 1)] for _ in range(n + 1)]
    score_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            deletion = score_matrix[i - 1][j] + gap_penalty
            insertion = score_matrix[i][j - 1] + gap_penalty
            match_score = score_matrix[i - 1][j - 1] + (match_penalty if seq1[i - 1] == seq2[j - 1] else mismatch_penalty)

            max_score = max(match_score, deletion, insertion)
            score_matrix[i][j] = max_score

            if max_score == insertion:
                decision_matrix[i][j] = 'I'
            elif max_score == match_score:
                decision_matrix[i][j] = 'M'
            else:
                decision_matrix[i][j] = 'D'


    end_seq = 0
    max_score = float('-inf')
    for j in range(m, 0, -1):
        if score_matrix[n][j] > max_score:
            max_score = score_matrix[n][j]
            end_seq = j

    align1, align2 = '', ''
    i, j = n, end_seq

    while j > 0:
        if decision_matrix[i][j] == 'M':
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif decision_matrix[i][j] == 'D':
            align1 = seq1[i - 1] + align1
            align2 = '-' + align2
            i -= 1
        elif decision_matrix[i][j] == 'I':
            align1 = '-' + align1
            align2 = seq2[j - 1] + align2
            j -= 1


    print(max_score)
    print(align1)
    print(align2)

seq1 = input()
seq2 = input()
sequence_alignment(seq1, seq2)
