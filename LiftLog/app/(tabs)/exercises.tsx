import { ThemedText } from '@/components/ThemedText';
import SimpleView from '@/components/BaseView';
import { useEffect, useState, useMemo } from 'react';
import { ThemedTextInput } from '@/components/ThemedTextInput';
import exercisesJson from '@/constants/exercises.json';
import { ScrollView } from 'react-native';

// TODO add search bar and filter exercises by search
// TODO add filter popup modal to filter for type of exercise
// TODO add favorite star next to each exercise
export default function ExercisesScreen() {
  const [exercises, setExercises] = useState(exercisesJson.exercises);
  const [search, setSearch] = useState('');

  const filteredExercises = useMemo(() => {
    return exercises.filter((exercise) =>
      exercise.name.toLowerCase().includes(search.toLowerCase())
    );
  }, [exercises, search]);

  return (
    <SimpleView>
      <ThemedText type='title'>Exercises</ThemedText>
      <ThemedTextInput
        placeholder='Search exercises'
        value={search}
        onChangeText={setSearch}
      />
      <ScrollView>
        {filteredExercises.map((exercise) => (
          <ThemedText key={exercise.id}>{exercise.name}</ThemedText>
        ))}
      </ScrollView>
    </SimpleView>
  );
}
