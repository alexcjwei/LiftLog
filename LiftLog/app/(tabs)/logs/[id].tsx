import SimpleView from '@/components/BaseView';
import { ThemedText } from '@/components/ThemedText';
import { useLocalSearchParams } from 'expo-router';

export default function Page() {
  const { id } = useLocalSearchParams();
  return (
    <SimpleView>
      <ThemedText type='title'>Workout {id}</ThemedText>
      {/* TODO title input */}
      {/* TODO date time input */}
      {/* TODO exercise list */}
      {/*   TODO exercise card */}
      {/*     TODO attatch note button */}
      {/*     TODO set row (weight, reps, time) */}
      {/*     TODO add set button */}
      {/* TODO add exercise button */}
    </SimpleView>
  );
}
