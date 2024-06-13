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
    var unit: String?
    var duration: Duration?
    
    var inProgress: Bool {
        return weight != nil || reps != nil || duration != nil
    }
}
