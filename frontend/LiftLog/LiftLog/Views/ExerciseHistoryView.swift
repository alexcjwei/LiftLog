//
//  ExerciseHistoryView.swift
//  LiftLog
//
//  Created by Alex Wei on 6/14/24.
//

import SwiftUI

struct ExerciseHistoryView: View {
    @Environment(WorkoutStore.self) private var workoutStore;
    let exercise: Exercise

    var body: some View {
        NavigationStack {
            List {
                ForEach(workoutStore.getExerciseHistory(exercise: exercise), id: \.workout.id) { item in
                    Section(header: Text(item.workout.date.formatted())) {
                        ForEach(item.exercises) { exercise in
                            ForEach(exercise.sets) {
                                Text($0.detail)
                            }
                        }
                    }
                }
            }
            .navigationTitle("\(exercise.name) History")
        }
    }
}

#Preview {
    ExerciseHistoryView(exercise: Exercise(id: "bench-press", name: "Bench Press", isCustom: false))
        .environment(WorkoutStore())
}
