//
//  SetRow.swift
//  LiftLog
//
//  Created by Alex Wei on 6/11/24.
//

import SwiftUI

struct SetRow: View {
    @Binding var set: ExerciseSet
    let effortType: EffortType

    var body: some View {
        HStack {
            TextField("Weight", value: $set.weight, format: .number)
                .keyboardType(.decimalPad)
                .textFieldStyle(.roundedBorder)
            switch effortType {
            case .reps:
                TextField("Reps", value: $set.reps, format: .number)
                    .keyboardType(.numberPad)
                    .textFieldStyle(.roundedBorder)
            case .time:
                TextField("Time", value: $set.reps, format: .number)
                    .keyboardType(.decimalPad)
                    .textFieldStyle(.roundedBorder)
            }
        }
    }
}

#Preview {
    struct Preview: View {
        @State var set = ExerciseSet()
        
        var body: some View {
            SetRow(set: $set, effortType: .reps)
        }
    }
    
    return Preview()
}
