//
//  WorkoutDetail.swift
//  LiftLog
//
//  Created by Alex Wei on 6/7/24.
//

import SwiftUI

struct WorkoutDetail: View {
    @Binding var workout: Workout
    @State private var isShowingSheet = false

    var body: some View {
        NavigationStack {
            DatePicker("Change workout date", selection: $workout.date)
                .labelsHidden()
            // List each exercise in the workout
            WorkoutExerciseList(workout: $workout)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    EditButton()
                }
                ToolbarItem(placement: .bottomBar) {
                    Button("Add Exercise", systemImage: "plus.circle.fill") {
                        isShowingSheet.toggle()
                    }
                }
            }
            .sheet(isPresented: $isShowingSheet) {
                AddExerciseToWorkoutView { selectedExercise in
                    if let selectedExercise = selectedExercise {
                        workout.newExercise(exercise: selectedExercise)
                    }
                    isShowingSheet = false
                }
            }
            .navigationTitle($workout.name)
            .navigationBarTitleDisplayMode(.inline)
        }

    }
}

#Preview {
    struct Preview: View {
        @State var workout  = Workout(
            exercises: [
                WorkoutExercise(exercise: Exercise(name: "Test"))
            ]
        )
        
        var body: some View {
            WorkoutDetail(workout: $workout)
        }
    }

    return Preview()
}
