import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import SimpleView from '@/components/BaseView';
import { useState } from 'react';
import { BasicStatRow } from '@/components/profile/BasicStatRow';
import { StyleSheet, View } from 'react-native';
import ThemedSettingsButton from '@/components/profile/ThemedSettingsButton';

export default function ProfileScreen() {
  const [name, setName] = useState('Alex Wei');
  const [workoutsTracked, setWorkoutsTracked] = useState(300);
  const [consecutive, setConsecutive] = useState(10);
  const [consecutiveUnits, setConsecutiveUnits] = useState('weeks');

  return (
    <SimpleView>
      <ThemedSettingsButton />
      <View style={styles.title}>
        <ThemedText type='title'>{name}</ThemedText>
      </View>
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

const styles = StyleSheet.create({
  title: {
    alignItems: 'center',
  },
});
