//
//  WorkoutDetail.swift
//  LiftLog
//
//  Created by Alex Wei on 6/7/24.
//

import SwiftUI

struct WorkoutDetail: View {
    @Binding var workout: Workout

    var body: some View {
        NavigationStack {
            DatePicker("Change workout date", selection: $workout.date)
                .labelsHidden()
            // List each exercise in the workout
            WorkoutExerciseList(workout: $workout)
            .navigationTitle($workout.name)
            .navigationBarTitleDisplayMode(.inline)
        }

    }
}

#Preview {
    struct Preview: View {
        @State var workout = sampleWorkouts[0]
        
        var body: some View {
            WorkoutDetail(workout: $workout)
        }
    }

    return Preview()
}
