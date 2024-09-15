import { StyleSheet } from 'react-native';
import { useMemo } from 'react';
import { ThemedText } from '../ThemedText';
import { ThemedView } from '../ThemedView';

export function LogRow({
  name,
  type,
  date,
}: {
  name: string;
  type: string;
  date: string;
}) {
  const avatar = useMemo(() => {
    switch (type) {
      case 'upper':
        return '💪';
      case 'lower':
        return '🦵';
      case 'fullbody':
        return '🏋️';
      case 'cardio':
        return '🏃‍♂️';
      default:
        return '🤔';
    }
  }, [type]);

  return (
    <ThemedView style={styles.container}>
      <ThemedText style={styles.avatar}>{avatar}</ThemedText>
      <ThemedView>
        <ThemedText style={styles.name}>{name}</ThemedText>
        <ThemedText style={styles.date}>{date}</ThemedText>
      </ThemedView>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 16,
  },
  avatar: {
    width: 40,
    height: 40,
    marginRight: 16,
  },
  name: {
    fontWeight: 'bold',
    marginBottom: 4,
  },
  date: {
    color: 'gray',
  },
});
