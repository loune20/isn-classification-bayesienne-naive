Formule 1 : 
$$
P(ComPos \cap word1) = {freq\_word1 + prob\_pos - freq\_word1\_in\_pos}
$$

Formule 2 :
$$
P(word1|ComPos) = {P(ComPos \cap word1)\over prob\_pos} = pos\_score1
$$

Formule 3 : 
$$
P(ComPos|word1,word2,word3) = {pos\_score1*pos\_score2*pos\_score3 \over freq\_word1*freq\_word2*freq\_word3}
$$