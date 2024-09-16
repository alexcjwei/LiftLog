import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import SimpleView from '@/components/BaseView';
import { useState } from 'react';
import { BasicStatRow } from '@/components/profile/BasicStatRow';

export default function ProfileScreen() {
  const [name, setName] = useState('Alex Wei');
  const [workoutsTracked, setWorkoutsTracked] = useState(300);
  const [consecutive, setConsecutive] = useState(10);
  const [consecutiveUnits, setConsecutiveUnits] = useState('weeks');

  return (
    <SimpleView>
      <ThemedText type='title'>{name}</ThemedText>
      <ThemedText type='subtitle'>Stats</ThemedText>
      <ThemedView>
        <BasicStatRow
          title={`${workoutsTracked} workouts`}
          subtitle='Workouts Logged'
        />
        <BasicStatRow
          title={`${consecutive} ${consecutiveUnits}`}
          subtitle='Workout streak'
        />
      </ThemedView>
    </SimpleView>
  );
}
