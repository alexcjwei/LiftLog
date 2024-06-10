//
//  Exercise.swift
//  LiftLog
//
//  Created by Alex Wei on 6/8/24.
//

import Foundation

struct Exercise: Identifiable, Codable {
    private(set) var id: String = UUID().uuidString
    var name: String
    private(set) var isCustom = false
}

let sampleExercises: [Exercise] = [
    Exercise(name: "Barbell Back Squat"),
    Exercise(name: "Deadlift"),
    Exercise(name: "Bench Press"),
    Exercise(name: "Pull-up"),
    Exercise(name: "Overhead Standing Press"),
    Exercise(name: "Side Plank Hold"),
]
