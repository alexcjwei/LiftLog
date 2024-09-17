import { ThemedText } from '@/components/ThemedText';
import SimpleView from '@/components/BaseView';
import { router } from 'expo-router';
import { Button } from 'react-native';
import { useState } from 'react';
import { Link } from 'expo-router';
import { LogRow } from '@/components/logs/LogRow';
import { ScrollView } from 'react-native';

var idCounter = 3;
const dummyLogs = [
  {
    id: 1,
    name: 'Upper Body',
    date: '2024-09-14',
    type: 'upper',
    notes: 'good workout',
  },
  {
    id: 2,
    name: 'Lower Body',
    date: '2024-09-13',
    type: 'lower',
    notes: '',
  },
];

export default function LogScreen() {
  const [logs, setLogs] = useState(dummyLogs);

  const handleNewWorkoutPress = () => {
    const newLog = {
      id: idCounter++,
      name: 'Upper Body',
      date: '2024-09-14',
      type: 'upper',
      notes: 'good workout',
    };
    setLogs([newLog, ...logs]);
    router.push(`/logs/${newLog.id}`);
  };

  return (
    <SimpleView>
      <ThemedText type='title'>Log</ThemedText>
      <Button title='Log New Workout' onPress={handleNewWorkoutPress} />
      <ScrollView>
        {logs.map((log) => (
          <Link key={log.id} href={`/logs/${log.id}`}>
            <LogRow {...log} />
          </Link>
        ))}
      </ScrollView>
    </SimpleView>
  );
}
