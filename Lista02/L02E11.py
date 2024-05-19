"""
11. Faça o programa que leia o resultado de alinhamento entre duas sequências
com BLAST e retorne a identidade (em porcentagem). Dica: copie a tabela abaixo e
cole em um arquivo chamado “resultado.txt”; leia o arquivo manualmente e
identifique qual linha armazena o valor de identidade; depois crie um programa que
leia e imprima na tela apenas esse valor.
Query= sp|P52407|E13B_HEVBR Glucan endo-1,3-beta-glucosidase, basic
vacuolar isoform OS=Hevea brasiliensis OX=3981 GN=HGN1 PE=1 SV=2
Length=374
Subject= sp|Q9SE50|BGL18_ARATH Beta-D-glucopyranosyl abscisate
beta-glucosidase OS=Arabidopsis thaliana OX=3702 GN=BGLU18 PE=1 SV=2
Length=528
Score = 25.0 bits (53), Expect = 0.005, Method: Compositional matrix adjust.
Identities = 26/126 (21%), Positives = 51/126 (40%), Gaps = 18/126 (14%)
Query 233 FTSPSVVVWDGQR--GYK---NLFDATLDALYSALE------RASGGSLEVVVSESGWPS 281
+T+ S+V WD + GYK F+ LD L + + G EV+++E+G+
Sbjct 368 WTTDSLVDWDSKSVDGYKIGSKPFNGKLDVYSKGLRYLLKYIKDNYGDPEVIIAENGYGE 427
Query 282 AGA-------FAATFDNGRTYLSNLIQHVKGGTPKRPNRAIETYLFAMFDENKKQPEVEK 334
F N + Y+ + + K +++++ D + Q +
Sbjct 428 DLGEKHNDVNFGTQDHNRKYYIQRHLLSMHDAICKDKVNVTGYFVWSLMDNFEWQDGYKA 487
Query 335 HFGLFF 340
FGL++
Sbjct 488 RFGLYY 493
"""