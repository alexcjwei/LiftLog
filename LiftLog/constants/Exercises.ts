interface Exercise {
  id: string;
  name: string;
  type: string;
}

export const Exercises: Exercise[] = [
  { id: '1', name: 'Squat', type: 'leg' },
  { id: '2', name: 'Bench Press', type: 'chest' },
  { id: '3', name: 'Deadlift', type: 'leg' },
  { id: '4', name: 'Pull Up', type: 'back' },
  { id: '5', name: 'Bicep Curl', type: 'arm' },
  { id: '6', name: 'Tricep Pushdown', type: 'arm' },
  { id: '7', name: 'Shoulder Press', type: 'shoulder' },
  { id: '8', name: 'Lunges', type: 'leg' },
  { id: '9', name: 'Plank', type: 'core' },
  { id: '10', name: 'Row', type: 'back' },
];
