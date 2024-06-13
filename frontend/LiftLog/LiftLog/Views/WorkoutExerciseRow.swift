//
//  WorkoutExerciseRow.swift
//  LiftLog
//
//  Created by Alex Wei on 6/12/24.
//

import SwiftUI

struct WorkoutExerciseRow: View {
    @Binding var exercise: WorkoutExercise
    
    var body: some View {
        NavigationLink {
            WorkoutExerciseDetail(exercise: $exercise)
        } label: {
            HStack {
                Text(exercise.exercise.name)
                if exercise.inProgress {
                    Spacer()
                    Image(systemName: "checkmark")
                }
            }

        }
    }
}

#Preview {
    struct Preview: View {
        @State private var exercise = WorkoutExercise(exercise: Exercise(name: "Bench Press"), sets: [Set(reps: 10)])
        
        var body: some View {
            WorkoutExerciseRow(exercise: $exercise)
        }
    }
    
    return Preview()
}
