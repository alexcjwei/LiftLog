//
//  ContentView.swift
//  LiftLog
//
//  Created by Alex Wei on 6/7/24.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            WorkoutsView()
                .tabItem { Label("Workouts", systemImage: "figure.strengthtraining.traditional") }
            ExercisesView()
                .tabItem { Label("Exercises", systemImage: "dumbbell") }
        }
    }
}

#Preview {
    ContentView()
}
