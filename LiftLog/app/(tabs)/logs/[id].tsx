import SimpleView from '@/components/BaseView';
import { ThemedText } from '@/components/ThemedText';
import { useLocalSearchParams } from 'expo-router';

export default function Page() {
  const { id } = useLocalSearchParams();
  return (
    <SimpleView>
      <ThemedText type='title'>Workout {id}</ThemedText>
    </SimpleView>
  );
}
