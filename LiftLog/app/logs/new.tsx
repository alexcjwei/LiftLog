import SimpleView from '@/components/BaseView';
import { ThemedText } from '@/components/ThemedText';
import { useLocalSearchParams } from 'expo-router';

export default function Page() {
  return (
    <SimpleView>
      <ThemedText type='title'>New Workout</ThemedText>
    </SimpleView>
  );
}
