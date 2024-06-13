//
//  WorkoutExerciseList.swift
//  LiftLog
//
//  Created by Alex Wei on 6/11/24.
//

import SwiftUI

struct WorkoutExerciseList: View {
    @Binding var workout: Workout
    
    var body: some View {
        List {
            ForEach($workout.exercises) {$exercise in
                WorkoutExerciseRow(exercise: $exercise)
            }
            .onDelete(perform: { indexSet in
                workout.deleteExercise(at: indexSet)
            })
            .onMove(perform: { indices, newOffset in
                workout.moveExercise(from: indices, to: newOffset)
            })
        }    }
}

#Preview {
    struct Preview: View {
        @State private var workout = Workout()
        
        var body: some View {
            WorkoutExerciseList(workout: $workout)
        }
    }
    
    return Preview()
}
