//
//  main.swift
//  Project-X-Analysts
//
//  Created by Leonardo Oliveira on 23/09/20.
//

import Foundation

let analystProvider = CSVAnalystProvider(fileAt: "/Users/leonardooliveira/Developer/projects-x-analysts/Dataset/analyst-dataset.csv")
let populationDescriptor = PopulationDescriptor(size: 20, chromosomeWidth: 9)
let ag = AG(populationDescriptor: populationDescriptor, analystProvider: analystProvider)
ag.run()

