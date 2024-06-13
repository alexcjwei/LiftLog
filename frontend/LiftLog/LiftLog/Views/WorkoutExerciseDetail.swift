//
//  WorkoutExerciseDetail.swift
//  LiftLog
//
//  Created by Alex Wei on 6/7/24.
//

import SwiftUI

struct WorkoutExerciseDetail: View {
    @Binding var exercise: WorkoutExercise

    var body: some View {
        NavigationStack {
            Form {
                HStack {
                    Text("Weight")
                    Spacer()
                    Text("Reps")
                    Spacer()
                }
                List {
                    ForEach($exercise.sets) {$myset in
                        SetRow(set: $myset)
                    }
                    .onDelete(perform: delete)
                    .onMove(perform: move)
                }
                Button {
                    exercise.sets.append(ExerciseSet())
                } label: {
                    Label("Add set", systemImage: "plus")
                }
            }
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    EditButton()
                }
            }
            .navigationTitle(exercise.exercise.name)
            .navigationBarTitleDisplayMode(.inline)
        }
    }
    
    func move(from source: IndexSet, to destination: Int) {
        exercise.sets.move(fromOffsets: source, toOffset: destination)
    }
    
    func delete(offsets: IndexSet) {
        exercise.sets.remove(atOffsets: offsets)
    }
}

#Preview {
    struct Preview: View {
        @State var exercise = WorkoutExercise(exercise: Exercise(name: "Bench Press"))
        var body: some View {
            WorkoutExerciseDetail(exercise: $exercise)
        }
    }

    return Preview()
}
