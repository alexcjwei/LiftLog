//
//  ExerciseStore.swift
//  LiftLog
//
//  Created by Alex Wei on 6/9/24.
//

import Foundation


@Observable
class ExerciseStore {
    let EXERCISES_KEY = "Exercises"
    let predefinedExercises = Bundle.main.decode("exercises.json")
    var userExercises = [Exercise]() {
        didSet {
            saveExercises()
        }
    }
    
    var exercises: [Exercise] {
        return predefinedExercises + userExercises
    }
    
    init() {
        decodeExercises()
    }
    
    func saveExercises() {
        if let encoded = try? JSONEncoder().encode(userExercises) {
            UserDefaults.standard.setValue(encoded, forKey: EXERCISES_KEY)
        }
    }
    
    func decodeExercises() {
        if let savedExercises = UserDefaults.standard.data(forKey: EXERCISES_KEY) {
            if let decodedExercises = try? JSONDecoder().decode([Exercise].self, from: savedExercises) {
                userExercises = decodedExercises
                return
            }
        }
        
        userExercises = []
    }
    
    func addNewExercise(exercise: Exercise) {
        userExercises.insert(exercise, at: 0)
    }
}
