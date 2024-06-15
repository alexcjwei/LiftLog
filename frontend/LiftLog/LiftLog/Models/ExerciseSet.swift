//
//  ExerciseSet.swift
//  LiftLog
//
//  Created by Alex Wei on 6/8/24.
//

import Foundation

struct ExerciseSet: Identifiable, Codable {
    private(set) var id = UUID()

    var reps: Int?
    var weight: Float?
    var time: Float?
    
    var inProgress: Bool {
        return weight != nil || reps != nil || time != nil
    }
    
    var detail: String {
        var components = [String]()
        if let weight = weight {
            components.append("\(weight)")
        }
        if let reps = reps {
            components.append("x \(reps) reps")
        }
        if let time = time {
            components.append("x \(time) sec")
        }

        return components.joined(separator: " ")
    }
}
