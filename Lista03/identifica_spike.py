from Bio import SeqIO

# Função para identificar o gene Spike em um genoma
def identificar_gene_spike(genoma_file):
    for record in SeqIO.parse(genoma_file, "fasta"):
        # Suponha que a proteína Spike seja conhecida como "S" na anotação do genoma
        for feature in record.features:
            if feature.type == "gene" and "S" in feature.qualifiers.get("gene", []):
                return feature.qualifiers["gene"], feature.location
    return "Gene Spike não encontrado no genoma.",0

# Nome do arquivo contendo o genoma
genoma_file = "proteina.fasta"

# Chamar a função para identificar o gene Spike
gene_spike, localizacao = identificar_gene_spike(genoma_file)

# Exibir resultados
if gene_spike != "Gene Spike não encontrado no genoma.":
    print("Gene Spike encontrado:")
    print("Nome do gene:", gene_spike)
    print("Localização no genoma:", localizacao)
else:
    print(gene_spike)