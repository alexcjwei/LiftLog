//
//  CreateExerciseView.swift
//  LiftLog
//
//  Created by Alex Wei on 6/10/24.
//

import SwiftUI

struct CreateExerciseView: View {
    @Environment(ExerciseStore.self) private var exerciseStore
    @Environment(\.dismiss) var dismiss
    @State private var exercise = Exercise(name: "", isCustom: true)
    
    private var searchResults: [Exercise] {
        let searchText = exercise.name
        if searchText.isEmpty {
            return []
        } else {
            return exerciseStore.exercises.filter { $0.name.contains(searchText) }
        }
    }
    
    var body: some View {
        NavigationStack {
            VStack {
                Form {
                    TextField("Name", text: $exercise.name)
                        .textInputAutocapitalization(.words)
                    Button("Create") {
                        exerciseStore.addExercise(exercise: exercise)
                        dismiss()
                    }
                    .disabled(exercise.name.isEmpty)
                }
                List {
                    ForEach(searchResults) { result in
                        Text(result.name)
                    }
                }
            }
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Cancel", role: .cancel) {
                        dismiss()
                    }
                    .foregroundStyle(.red)
                }
            }
        }
        .navigationTitle("Create Exercise")
    }
}

#Preview {
    var exerciseStore = ExerciseStore()
    return CreateExerciseView()
        .environment(exerciseStore)
}
