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
        repeat {
            evaluatePopulation()
            reproducePopulation()
        } while shouldContinueRunning()
    }
    
    private func createInitialPopulation() {
        for _ in 0..<populationDescriptor.size {
            population.append(createChromosome())
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
    
    private func evaluatePopulation() {
        let scores = population.map(evaluate(chromosome:))
    }
    
    private func evaluate(chromosome: Chromosome) -> Int {
        var score = 0
        score += 10
        return score
    }
    
    private func reproducePopulation() {
    }
    
    private func shouldContinueRunning() -> Bool {
        false
    }
    
    private func showPopulation() {
        population.forEach { chromosome in
            print(chromosome)
        }
    }
}
