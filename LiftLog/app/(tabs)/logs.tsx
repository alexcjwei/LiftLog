import { ThemedText } from '@/components/ThemedText';
import SimpleView from '@/components/BaseView';
import { useState } from 'react';
import { Link } from 'expo-router';
import { LogRow } from '@/components/logs/LogRow';

const dummyLogs = [
  {
    id: '1',
    name: 'Upper Body',
    date: '2024-09-14',
    type: 'upper',
    notes: 'good workout',
  },
  {
    id: '2',
    name: 'Lower Body',
    date: '2024-09-13',
    type: 'lower',
    notes: '',
  },
];

export default function LogScreen() {
  const [logs, setLogs] = useState(dummyLogs);

  return (
    <SimpleView>
      <ThemedText type='title'>Log</ThemedText>
      <Link href='/logs/new'>
        <ThemedText type='link'>Log New Workout</ThemedText>
      </Link>
      {logs.map((log) => (
        <Link key={log.id} href={`/logs/${log.id}`}>
          <LogRow {...log} />
        </Link>
      ))}
    </SimpleView>
  );
}
