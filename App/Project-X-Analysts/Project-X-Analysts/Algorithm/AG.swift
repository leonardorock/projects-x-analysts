public class AG {
    let populationDescriptor: PopulationDescriptor
    let analystProvider: AnalystsProvider
    
    var population: [Chromosome] = []
    lazy var analysts: [Analyst] = analystProvider.analysts()
    
    public init(populationDescriptor: PopulationDescriptor, analystProvider: AnalystsProvider) {
        self.populationDescriptor = populationDescriptor
        self.analystProvider = analystProvider
    }
    
    public func run() {
        createInitialPopulation()
    }
    
    private func createInitialPopulation() {
        for _ in 0..<populationDescriptor.size {
            population.append(createChromosome())
        }
        population.forEach { chromosome in
            print(chromosome)
        }
    }
    
    private func createChromosome() -> Chromosome {
        var seed = analysts
        var identifiers: [Int] = []
        for _ in 0..<populationDescriptor.chromosomeWidth where !seed.isEmpty {
            let analyst = seed.randomElement()!
            identifiers.append(analyst.identifier)
            seed.removeAll(where: { $0.identifier == analyst.identifier })
        }
        return Chromosome(analysts: identifiers)
    }
}
