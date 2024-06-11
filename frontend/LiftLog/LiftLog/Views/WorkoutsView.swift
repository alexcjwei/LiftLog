//
//  WorkoutsView.swift
//  LiftLog
//
//  Created by Alex Wei on 6/7/24.
//

import SwiftUI

struct WorkoutsView: View {
    @Environment(WorkoutStore.self) private var workoutStore
    
    var body: some View {
        @Bindable var workoutStore = workoutStore
        NavigationStack {
            List {
                // Links to each workout
                ForEach($workoutStore.workouts) {$workout in
                    NavigationLink {
                        WorkoutDetail(workout: $workout)
                    } label: {
                        Text("\(workout.name) - \(workout.date.formatted())")
                    }
                    // Make a copy of the workout
                    .swipeActions(edge: .leading) {
                        Button {
                            workoutStore.addWorkout(workout: workout.copy())
                        } label: {
                            Label("Copy", systemImage: "doc.on.doc.fill")
                        }
                        .tint(.indigo)
                    }
                }
                .onDelete(perform: workoutStore.deleteWorkout)
                .onMove(perform: workoutStore.moveWorkout)
            }
            .toolbar {
                // Add new workout button
                ToolbarItem(placement: .bottomBar) {
                    Button {
                        workoutStore.newWorkout()
                    } label: {
                        Label("New Workout", systemImage: "plus.circle.fill")
                            .labelStyle(.titleAndIcon)
                    }
                }
            }
            .toolbar {
                EditButton()
            }
            .navigationTitle("Workouts")
        }
    }
}

#Preview {
    var workoutStore = WorkoutStore()
    return WorkoutsView().environment(workoutStore)
}
