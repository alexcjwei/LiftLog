//
//  WorkoutStore.swift
//  LiftLog
//
//  Created by Alex Wei on 6/9/24.
//

import Foundation


@Observable
class WorkoutStore {
    let WORKOUTS_KEY = "Workouts"

    var workouts = [Workout]() {
        didSet {
            saveWorkouts()
        }
    }
    
    init() {
        decodeWorkouts()
    }
    
    func saveWorkouts() {
        if let encoded = try? JSONEncoder().encode(workouts) {
            UserDefaults.standard.setValue(encoded, forKey: WORKOUTS_KEY)
        }
    }
    
    func decodeWorkouts() {
        if let savedWorkouts = UserDefaults.standard.data(forKey: WORKOUTS_KEY) {
            if let decodedWorkouts = try? JSONDecoder().decode([Workout].self, from: savedWorkouts) {
                workouts = decodedWorkouts
                return
            }
        }
        
        workouts = []
    }
    
    
    func newWorkout() {
        workouts.insert(Workout(), at: 0)
    }
    
    func addWorkout(workout: Workout) {
        workouts.insert(workout, at: 0)
    }
    
    func deleteWorkout(at offsets: IndexSet) {
        workouts.remove(atOffsets: offsets)
    }
    
    func moveWorkout(from source: IndexSet, to destination: Int) {
        workouts.move(fromOffsets: source, toOffset: destination)
    }
    
    func getExerciseHistory(exercise: Exercise) -> [(workout: Workout, exercises: [WorkoutExercise])] {
        let exerciseHistory: [(workout: Workout, exercises: [WorkoutExercise])] = workouts.reduce(into: []) { accum, workout in
            let filteredWorkoutExercises = workout.exercises.filter { $0.exercise.id == exercise.id }
            if !filteredWorkoutExercises.isEmpty {
                accum.append((workout: workout, exercises: filteredWorkoutExercises))
            }
        }
        return exerciseHistory
    }
}
