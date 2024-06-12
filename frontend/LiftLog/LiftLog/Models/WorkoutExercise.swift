//
//  WorkoutExercise.swift
//  LiftLog
//
//  Created by Alex Wei on 6/8/24.
//

import Foundation

struct WorkoutExercise: Identifiable, Codable {
    private(set) var id: UUID = UUID()
    var exercise: Exercise
    var sets: [Set] = []
    
    var inProgress: Bool {
        for set in sets {
            if set.inProgress {
                return true
            }
        }
        return false
    }
}
