public struct Analyst: CustomStringConvertible {
    public let identifier: Int
    public let velocity: Int
    
    public var description: String {
        "Analyst: \(identifier), velocity: \(velocity)"
    }
    
    public init(identifier: Int, velocity: Int) {
        self.identifier = identifier
        self.velocity = velocity
    }
}
