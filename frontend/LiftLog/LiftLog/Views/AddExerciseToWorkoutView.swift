//
//  AddExerciseToWorkoutView.swift
//  LiftLog
//
//  Created by Alex Wei on 6/8/24.
//

import SwiftUI

struct AddExerciseToWorkoutView: View {
    @Environment(ExerciseStore.self) private var exerciseStore
    @State private var searchText = ""
    @State private var selectedFilterOption: FilterOptions = .all
    @State private var isShowingCreateExerciseSheet = false

    enum FilterOptions: String, CaseIterable {
        case all = "All"
        case preset = "Presets"
        case mine = "Mine"
    }

    private var searchResults: [Exercise] {
        if searchText.isEmpty {
            return filterResults
        } else {
            return filterResults.filter { $0.name.contains(searchText) }
        }
    }
    
    private var filterResults: [Exercise] {
        switch selectedFilterOption {
        case .all:
            return exerciseStore.exercises
        case .preset:
            return exerciseStore.predefinedExercises
        case .mine:
            return exerciseStore.userExercises
        }
    }
    
    var onSelect: (Exercise?) -> Void
    
    var body: some View {
        NavigationStack {
            Picker("Filter exercises", selection: $selectedFilterOption) {
                ForEach(FilterOptions.allCases, id:\.self) { option in
                    Text(option.rawValue)
                }
            }
            .pickerStyle(.segmented)
            .padding(.horizontal)
            List {
                ForEach(searchResults) { result in
                    Button {
                        onSelect(result)
                    } label: {
                        Text(result.name)
                    }
                }
                if selectedFilterOption == .mine {
                    Button {
                        isShowingCreateExerciseSheet = true
                    } label: {
                        Label("Create new exercise", systemImage: "plus.circle.fill")
                    }
                }
            }
            .navigationTitle("Exercises")
            .sheet(isPresented: $isShowingCreateExerciseSheet) {
                CreateExerciseView()
            }
        }
        .searchable(text: $searchText, prompt:"Search for exercise")
    }
}

#Preview {
    var exerciseStore = ExerciseStore()
    return AddExerciseToWorkoutView { selectedItem in
        if let selectedItem = selectedItem {
            print(selectedItem.name)
        }
    }
    .environment(exerciseStore)
}
