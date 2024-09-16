import { StyleSheet } from 'react-native';
import { ThemedText } from '../ThemedText';
import { ThemedView } from '../ThemedView';

export function BasicStatRow({
  title,
  subtitle,
}: {
  title: string;
  subtitle: string;
}) {
  return (
    <ThemedView style={styles.container}>
      <ThemedText type='subtitle'>{title}</ThemedText>
      <ThemedText type='defaultSemiBold'>{subtitle}</ThemedText>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'column',
    alignItems: 'flex-start',
    padding: 16,
  },
});
