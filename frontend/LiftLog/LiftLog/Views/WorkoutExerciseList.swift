//
//  WorkoutExerciseList.swift
//  LiftLog
//
//  Created by Alex Wei on 6/11/24.
//

import SwiftUI

struct WorkoutExerciseList: View {
    @Binding var workout: Workout
    @State private var multiSelection = Set<UUID>()
    @State private var isShowingSheet = false

    var body: some View {
        NavigationStack{
            List(selection: $multiSelection) {
                ForEach($workout.exercises) {$exercise in
                    WorkoutExerciseRow(exercise: $exercise)
                }
                .onDelete(perform: { indexSet in
                    workout.deleteExercise(at: indexSet)
                })
                .onMove(perform: { indices, newOffset in
                    workout.moveExercise(from: indices, to: newOffset)
                })
            }
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    EditButton()
                }
                ToolbarItemGroup(placement: .bottomBar) {
                    Button("Add Exercise") {
                        isShowingSheet.toggle()
                    }
                    .buttonStyle(.borderedProminent)
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
        }
    }
}

#Preview {
    struct Preview: View {
        @State private var workout = sampleWorkouts[0]
        
        var body: some View {
            WorkoutExerciseList(workout: $workout)
        }
    }
    
    return Preview()
}
