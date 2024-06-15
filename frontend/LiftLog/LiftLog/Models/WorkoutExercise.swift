//
//  WorkoutExercise.swift
//  LiftLog
//
//  Created by Alex Wei on 6/8/24.
//

import Foundation

enum EffortType: String, CaseIterable, Codable {
    case reps = "Repetitions"
    case time = "Time"
}

struct WorkoutExercise: Identifiable, Codable {
    private(set) var id: UUID = UUID()
    var exercise: Exercise
    var sets: [ExerciseSet] = []
    var note: String = ""
    var effortType: EffortType = .reps

    var inProgress: Bool {
        for set in sets {
            if set.inProgress {
                return true
            }
        }
        return false
    }
}
