import Foundation

public struct Chromosome: CustomStringConvertible {
    public let analysts: [Int]
    
    public var description: String {
        analysts.map { identifier in
            String(format: "%02d", identifier)
        }.joined(separator: ", ")
    }
    
    public init(analysts: [Int]) {
        self.analysts = analysts
    }
}
