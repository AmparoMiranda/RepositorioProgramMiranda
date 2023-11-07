from FuncionesMutantes import*

dna = [ "AAAAAA",
        "TATATA",
        "ACAGTG",
        "CGATCG",
        "GTCGTA",
        "ATGCTG"
    ]
print("Caso de prueba HORIZONTAL: ")
print(  "AAAAAA",
        "TATATA",
        "ACAGTG",
        "CGATCG",
        "GTCGTA",
        "ATGCTG"
    )
result = is_mutant(dna)
if(result):
    print("👽  El ADN ingresado pertenece a un MUTANTE  👽")

# dna =  ["ATGCGA",
#         "AGCCTA",
#         "ACAGTG",
#         "AGATCG",
#         "ATCGTA",
#         "ATGCTG"
#     ]
# print("Caso de prueba VERTICAL: ")
# print(  "ATGCGA",
#         "AGCCTA",
#         "ACAGTG",
#         "AGATCG",
#         "ATCGTA",
#         "ATGCTG"
#     )
# result = is_mutant(dna)
# if(result):
#     print("👽  El ADN ingresado pertenece a un MUTANTE  👽")

# dna = [ "ATGCGA",
#         "GACCTA",
#         "TCAGTG",
#         "TGGACG",
#         "GTCGAT",
#         "CTGCTA"
#     ]
# print("Caso de prueba DIAGONAL: ")
# print(  "ATGCGA",
#         "GACCTA",
#         "TCAGTG",
#         "TGGACG",
#         "GTCGAT",
#         "CTGCTA"
#     )
# result = is_mutant(dna)
# if(result):
#     print("👽  El ADN ingresado pertenece a un MUTANTE  👽")





