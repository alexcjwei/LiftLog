//
//  ExercisesView.swift
//  LiftLog
//
//  Created by Alex Wei on 6/7/24.
//

import SwiftUI

struct ExercisesView: View {
    @Environment(ExerciseStore.self) private var exerciseStore
    @State private var searchText = ""
    @State private var isShowingMyExercises = false
    @State private var isShowingDefaultExercises = false
    
    private func showHide(_ isShowing: Bool) -> String {
        return isShowing ? "Hide" : "Show"
    }
    
    private func showHideSystemImage(_ isShowing: Bool) -> String {
        return isShowing ? "eye.slash" : "eye"
    }

    private var searchResults: [Exercise] {
        if searchText.isEmpty {
            return exerciseStore.exercises
        } else {
            return exerciseStore.exercises.filter { $0.name.contains(searchText) }
        }
    }
    
    private var filteredSearchResults: [Exercise] {
        if isShowingMyExercises && isShowingDefaultExercises {
            return searchResults
        } else if isShowingMyExercises {
            return searchResults.filter { $0.isCustom }
        } else if isShowingDefaultExercises {
            return searchResults.filter { !$0.isCustom }
        } else {
            return []
        }
    }
    
    var body: some View {
        NavigationStack {
            List {
                ForEach(filteredSearchResults) { exercise in
                    Text(exercise.name)
                }
            }
            .navigationTitle("Exercises")
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Menu {
                        Button {
                            isShowingMyExercises.toggle()
                        } label: {
                            Label("\(showHide(isShowingMyExercises)) my exercises",
                            systemImage: showHideSystemImage(isShowingMyExercises))
                        }
                        Button {
                            isShowingDefaultExercises.toggle()
                        } label: {
                            Label("\(showHide(isShowingDefaultExercises)) default exercises",
                            systemImage: showHideSystemImage(isShowingDefaultExercises))
                        }
                    } label: {
                        Label("Fitler", systemImage: "line.3.horizontal.decrease")
                    }
                }
            }
        }
        .searchable(text: $searchText, prompt: "Search for exercise")
    }
}

#Preview {
    var exerciseStore = ExerciseStore()
    return ExercisesView().environment(exerciseStore)
}
