//
//  WorkoutsView.swift
//  LiftLog
//
//  Created by Alex Wei on 6/7/24.
//

import SwiftUI

struct WorkoutsView: View {
    @State private var viewModel = ViewModel()
    
    var body: some View {
        NavigationStack {
            List {
                // Links to each workout
                ForEach($viewModel.workoutStore.workouts) {$workout in
                    NavigationLink {
                        WorkoutDetail(workout: $workout)
                    } label: {
                        Text("\(workout.name) - \(workout.date.formatted())")
                    }
                    // Make a copy of the workout
                    .swipeActions(edge: .leading) {
                        Button {
                            viewModel.workoutStore.addWorkout(workout: workout.copy())
                        } label: {
                            Label("Copy", systemImage: "doc.on.doc.fill")
                        }
                        .tint(.indigo)
                    }
                }
                .onDelete(perform: viewModel.workoutStore.deleteWorkout)
                .onMove(perform: viewModel.workoutStore.moveWorkout)
            }
            .toolbar {
                // Add new workout button
                ToolbarItem(placement: .bottomBar) {
                    Button {
                        viewModel.workoutStore.newWorkout()
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

extension WorkoutsView {
    class ViewModel {
        var workoutStore = WorkoutStore()
    }
}

#Preview {
    WorkoutsView()
}
