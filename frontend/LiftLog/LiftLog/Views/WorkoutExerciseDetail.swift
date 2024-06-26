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
            VStack {
                Form {
                    List {
                        ForEach($exercise.sets) {$myset in
                            SetRow(set: $myset, effortType: exercise.effortType)
                        }
                        .onDelete(perform: delete)
                        .onMove(perform: move)
                    }
                    Button {
                        exercise.sets.append(ExerciseSet())
                    } label: {
                        Label("Add set", systemImage: "plus")
                    }
                    Picker("Effort Type", selection: $exercise.effortType) {
                        ForEach(EffortType.allCases, id: \.self) {
                            Text($0.rawValue)
                        }
                    }
                    .pickerStyle(.segmented)
                    TextField("Note", text: $exercise.note, axis: .vertical)
                        .lineLimit(5...10)
                }
                NavigationLink {
                    ExerciseHistoryView(exercise: exercise.exercise)
                } label: {
                    Text("See \(exercise.exercise.name) History")
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
