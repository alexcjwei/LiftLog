//
//  CreateExerciseView.swift
//  LiftLog
//
//  Created by Alex Wei on 6/10/24.
//

import SwiftUI

struct CreateExerciseView: View {
    private let viewModel = ViewModel()

    @Environment(\.dismiss) var dismiss
    @State private var exercise = Exercise(name: "", isCustom: true)
    
    private var searchResults: [Exercise] {
        let searchText = exercise.name
        if searchText.isEmpty {
            return []
        } else {
            return viewModel.exerciseStore.exercises.filter { $0.name.contains(searchText) }
        }
    }
    
    var body: some View {
        NavigationStack {
            VStack {
                Form {
                    TextField("Name", text: $exercise.name)
                        .textInputAutocapitalization(.words)
                    Button("Create") {
                        viewModel.exerciseStore.addNewExercise(exercise: exercise)
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

extension CreateExerciseView {
    class ViewModel {
        var exerciseStore = ExerciseStore()
    }
}

#Preview {
    CreateExerciseView()
}
