//
//  ExercisesView.swift
//  LiftLog
//
//  Created by Alex Wei on 6/7/24.
//

import SwiftUI

struct ExercisesView: View {
    let viewModel = ViewModel()
    
    var body: some View {
        List {
            ForEach(viewModel.exerciseStore.exercises) { exercise in
                Text(exercise.name)
            }
        }
    }
}

extension ExercisesView {
    class ViewModel {
        var exerciseStore = ExerciseStore()
    }
}

#Preview {
    ExercisesView()
}
