import Foundation

public struct CSVAnalystProvider: AnalystsProvider {
    let path: String
    
    public init(fileAt path: String) {
        self.path = path
    }
    
    public func analysts() -> [Analyst] {
        guard let csvStringContent = try? String(contentsOfFile: path, encoding: .utf8) else {
            return []
        }
        let lines = csvStringContent.components(separatedBy: "\n")
        return lines.compactMap(analyst(for:))
    }
    
    private func analyst(for line: String) -> Analyst? {
        let fields = line.components(separatedBy: ",")
        guard let id = Int(fields[0]), let velocity = Int(fields[1]) else {
            return nil
        }
        return Analyst(identifier: id, velocity: velocity)
    }
}
