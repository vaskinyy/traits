from itertools import chain, combinations
from traits_web_prototype.TraitsEvaluator.Trait import Trait

__author__ = 'yuriy.vaskin'

class ExtendedPunnetSquare:
    def __init__(self, trait=None):
        if not trait:
            trait = Trait()

        self.fathers_genes = []
        self.mothers_genes = []
        self.trait = trait
        self.genotype_operator = GenotypeOperator()
        self.build_by_trait_map()

    def get_genotype_frequency(self, genotype):
        size = len(self.fathers_genes) * len(self.mothers_genes)
        if size == 0:
            return 0
        count = 0
        for p_trait in self.fathers_genes:
            for m_trait in self.mothers_genes:
                if self.genotype_operator.cross_genotypes(p_trait,m_trait) == genotype:
                    count += 1
        return count / float(size)

    def get_possible_genotypes(self):
        result = []
        for p_trait in self.fathers_genes:
            for m_trait in self.mothers_genes:
                genotype = self.genotype_operator.cross_genotypes(p_trait,m_trait)
                if genotype not in result:
                    result.append(genotype)
        return result

    def get_traits_probability_map(self):
        result = {}
        for trait in self.trait.trait_map:
            freq = 0
            for g in self.trait.trait_map[trait]:
                freq += self.trait.get_phenotype_probs(g, trait) * self.get_genotype_frequency(g)
            result[trait] = freq
        return result

    def set_trait(self, trait):
        self.trait = trait
        self.build_by_trait_map()

    def build_by_trait_map(self):
        alleles = self.genotype_operator.get_allele_variations(list(chain.from_iterable(self.trait.trait_map.values())))
        self.fathers_genes = [a for a in alleles]
        self.mothers_genes = [a for a in alleles]

    def reduce_by_fathers_traits(self, traits):
        self.fathers_genes = self.reduce_genotype_by_traits(traits, self.fathers_genes)

    def reduce_by_mothers_traits(self, traits):
        self.mothers_genes = self.reduce_genotype_by_traits(traits, self.mothers_genes)

    def reduce_genotype_by_traits(self, traits, genotype):
        if not any(p in self.trait.trait_map for p in traits):
            associated_genotypes = list(chain.from_iterable(self.trait.trait_map.values()))
        else:
            associated_genotypes = list(chain.from_iterable([self.trait.trait_map[p] for p in traits if p in self.trait.trait_map]))

        possible_genotypes = self.genotype_operator.get_allele_variations(associated_genotypes)

        return [g for g in genotype if g in possible_genotypes]

    def __repr__(self):
        result = ''
        for m_trait in self.mothers_genes:
            for p_trait in self.fathers_genes:
                result += self.genotype_operator.cross_genotypes(p_trait,m_trait)
                result += '\t'
            result += '\n'
        return result



GENE_SEPARATOR = ','

class GenotypeOperator:
    def get_lexicographic_string(self, s):
        return ''.join(sorted(s, lambda x,y: cmp(x.lower(), y.lower()) or cmp(x,y)))

    def cross_genotypes(self, genotype1, genotype2):
        #multigene
        if (GENE_SEPARATOR in genotype1) and (GENE_SEPARATOR in genotype2):
            result = ''
            for (g1, g2) in zip(genotype1.split(GENE_SEPARATOR), genotype2.split(GENE_SEPARATOR)):
                if result != '':
                    result += GENE_SEPARATOR
                result += self.get_lexicographic_string(g1 + g2)
            return result

        return self.get_lexicographic_string(genotype1 + genotype2)

    def get_allele_variations(self, genotypes):
        gene_sets = []
        for gt in genotypes:
            full_alleles = gt.split(GENE_SEPARATOR)

            while len(gene_sets) < len(full_alleles):
                gene_sets.append([])

            for i in range(0, len(full_alleles)):
                gene_set = gene_sets[i]
                for a in list(full_alleles[i]):
                    if a not in gene_set:
                        gene_set.append(a)
                gene_sets[i] = sorted(gene_set, lambda x,y: cmp(x.lower(), y.lower()) or cmp(x,y))
        allele_variations = []
        for c in combinations(list(chain.from_iterable(gene_sets)), len(gene_sets)):
            skip = False
            for i in range(0, len(gene_sets)):
                if c[i] not in gene_sets[i]:
                    skip = True
                    break
            allele_variation = ','.join(c)
            if allele_variation in allele_variations:
                skip = True
            if skip:
                continue
            allele_variations.append(','.join(c))
        return allele_variations
