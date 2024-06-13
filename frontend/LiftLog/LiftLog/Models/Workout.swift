//
//  Workout.swift
//  LiftLog
//
//  Created by Alex Wei on 6/7/24.
//

import Foundation

struct Workout: Identifiable, Codable {
    private(set) var id = UUID()
    var createdAt: Date = Date()
    var date: Date = Date()
    var name: String = "New Workout"

    var exercises: [WorkoutExercise] = []
    
    mutating func newExercise(exercise: Exercise) {
        exercises.append(WorkoutExercise(exercise: exercise))
    }
    
    mutating func deleteExercise(at offsets: IndexSet) {
        exercises.remove(atOffsets: offsets)
    }
    
    mutating func moveExercise (from source: IndexSet, to destination: Int) {
        exercises.move(fromOffsets: source, toOffset: destination)
    }
    
    func copy() -> Workout {
        let newExercises = exercises.map { WorkoutExercise(exercise: $0.exercise)}
        return Workout(exercises: newExercises)
    }
    
}


let sampleWorkouts: [Workout] = [
    Workout(exercises: [
        WorkoutExercise(exercise: sampleExercises[0], sets: [
            ExerciseSet(reps: 15, weight: 95),
            ExerciseSet(reps: 14, weight: 95),
            ExerciseSet(reps: 12, weight: 95),
        ]),
        WorkoutExercise(exercise: sampleExercises[1], sets: [
            ExerciseSet(reps: 15, weight: 95),
            ExerciseSet(reps: 15, weight: 95),
            ExerciseSet(reps: 15, weight: 95),
        ]),
        WorkoutExercise(exercise: sampleExercises[4], sets: [
            ExerciseSet(duration: .seconds(30)),
            ExerciseSet(duration: .seconds(30)),
        ])
    ]),
]
