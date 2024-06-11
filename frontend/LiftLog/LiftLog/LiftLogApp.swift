//
//  LiftLogApp.swift
//  LiftLog
//
//  Created by Alex Wei on 6/7/24.
//

import SwiftUI

@main
struct LiftLogApp: App {
    @State private var exerciseStore = ExerciseStore()
    @State private var workoutStore = WorkoutStore()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(exerciseStore)
                .environment(workoutStore)
        }
    }
}
