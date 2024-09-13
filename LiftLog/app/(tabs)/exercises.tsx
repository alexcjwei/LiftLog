import { ThemedText } from '@/components/ThemedText';
import SimpleView from '@/components/BaseView';
import { useEffect, useState } from 'react';
import { ThemedTextInput } from '@/components/ThemedTextInput';
import { Exercises } from '@/constants/Exercises';

// TODO add search bar and filter exercises by search
// TODO add filter popup modal to filter for type of exercise
// TODO add favorite star next to each exercise
export default function ExercisesScreen() {
  const [exercises, setExercises] = useState(Exercises);
  const [search, setSearch] = useState('');

  return (
    <SimpleView>
      <ThemedText type='title'>Exercises</ThemedText>
      <ThemedTextInput
        placeholder='Search exercises'
        value={search}
        onChangeText={setSearch}
      />
      {exercises
        .filter((exercise) =>
          exercise.name.toLowerCase().includes(search.toLowerCase())
        )
        .map((exercise) => (
          <ThemedText key={exercise.id}>{exercise.name}</ThemedText>
        ))}
    </SimpleView>
  );
}
